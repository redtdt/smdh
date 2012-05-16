#-----------------------------------------------------------------------------
# Name:        moduleRep3.py
#
#
# RCS-ID:      $Id: moduleRep3.py $
#
# Licence: Sistema de Monitoreo de Derechos Humanos, Compilacion de datos
#  Copyright (C) 2010, Asociacion Todos los Derechos para Todos, A.C.
#  Registro Publico de Derechos de Autor, Num. de Registro
#  03-2010-101210014200-01, Mexico.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see<http://www.gnu.org/licenses/>.
#
#-----------------------------------------------------------------------------


# codigo para ReporteAnalitico
from module2 import *
import moduleRep2
from midataset import GeneraQueryCaso

import codecs
import webbrowser


session = status.session

camposDef = moduleRep2.campos
renderObj = moduleRep2.renderObj
# renderObj(obj, campo, Clase, 'RAW')


delim = '|'

def IdNotNull(obj):
    if hasattr(obj, 'id'):
        return obj.id
    else:
        return 0



def valoresUnicos(dataset, campoOffset, campoLong):
    #print 'offset ', campoOffset, campoLong 
    
    lista = []
    if dataset:
        for registro in dataset:
            slice = [i for i in registro[campoOffset + 1:campoOffset + campoLong + 1] ]
            #print 'slice ', slice
            
            if slice not in lista:
                
                lista.append(slice)
    #lista.sort() ?? a ver como....
    
    return lista

def dumpdataset(datos):
    j=0
    limite=20
    print '----------------'
    print len(datos) , " registros"
    for i in datosListado:
        print i
        j += 1
        if j > limite: return
         
def filtroDataset(dataset, campo, valorList):
    l = len(valorList)
    
    lista = []
    for i in dataset:
        
        if [j for j in i[campo + 1:campo + l + 1]] == valorList:
            lista.append(i)
    
    return lista

def reporta(dataset, clasificadoresList, nivel, campos, fileout, numerar=False):
    if clasificadoresList:
        clasiList=clasificadoresList[0]
        TipoDeColumna = clasiList[0]
        clasiLong = clasiList[1]
        #clasiLong = len(clasiList) - 1
        
        if TipoDeColumna == 'D':
            vunicos=valoresUnicos(dataset, nivel, clasiLong)
            
            for valorList in vunicos:
                #print valor.descripcion.encode('utf-8')
                exprList = []
                for i in range(len(valorList)):
                    valor = valorList[i] # instancia de la entidad
                    expr = renderObj(valor, campos[nivel + i][1], campos[nivel + i][0],'RAW')
                    
                    #      render (objeto/instancia, campo de la tabla, tabla, formato de salida)
                    exprList.append(expr)
                #print [expr.encode('utf-8') for expr in exprList]
                encabezado(exprList, nivel, fileout, numerar=numerar)
                nuevodataset = filtroDataset(dataset, nivel, valorList)
                
                reporta(nuevodataset, clasificadoresList[clasiLong:], nivel + clasiLong, campos, fileout, numerar=numerar)
                sumario(valorList, nivel, fileout)
        if TipoDeColumna == 'S':
            exprList = []
            for i in range(clasiLong):
                vunicos=valoresUnicos(dataset, nivel + i, 1)
                total = len(vunicos)
                print total
                exprList.append(str(total))
            encabezado(exprList, nivel, fileout, numerar=numerar)
            print "totales ", exprList
            
    else:
        vaciado(dataset, fileout, campos, nivel, numerar=numerar)
def encabezado(exprList, nivel, fileout, numerar=False):
    expr=''
    status.num_renglon = status.num_renglon + 1
    if numerar:
                expr = "<td valign=top>%i</td><td>&nbsp;</td>"%status.num_renglon
                
    fileout.write('<tr>'+expr+'<td>' * nivel)
    for expr in exprList:
        fileout.write('<td valign=top>'+expr+'</td><td></td>')
    fileout.write('</td> <td></td>' * (nivel + 1 - len(exprList) ) +'</tr>')
    
def sumario(exprList, nivel, fileout):
    pass
        
        
        

def vaciado(dataset, fileout, campos, nivel, numerar=False):

    if nivel < len(campos):
        for r in dataset:
            status.num_renglon = status.num_renglon + 1
            renglon = ''
            fileout.write('<tr>')
            if numerar:
                expr = "<td>%i</td>"%status.num_renglon
                renglon = renglon + expr
            for Field in range(nivel, len(campos)):
                expr=''
                if r[Field + 1]:
                    expr =  renderObj(r[Field + 1], campos[Field][1],campos[Field][0],'RAW')
                if not expr:
                    expr=''
                renglon = renglon + expr
                print "renglon=",renglon
                
                    
                fileout.write('<td>' * nivel+'<td>'+expr+'</td><td></td>'+'</td>' * nivel)
            fileout.write('</tr>')
        
def ReporteAnalitico(MiDataset, camposAincluir, Formato, filename='salida.htm',  encabezado=None, titulo='', cols=[], numerar=False):

#entidades : los objetos necesarios para armar el query
# ejemplo : ['A','AA']  (Acto, Perpetradores, ver midataset)
#camposaincluir: campos incluyendo la entidad
#ejemplo: [('Acto','PTipodeacto'),('Acto','PTipodelugar'),('Acto','Descriptor')]
#Formato: Sumario 'S'(contar) o Detalle 'D'
#ejemplo: [['D',1],['D',2]['S',3]]



    
    print >>status.log, titulo.encode("latin_1", 'replace')
    status.num_renglon = 0
    
    # determinando caracteristicas de los campos a incluir
    campos=[]
    print camposAincluir
    
    for i in camposAincluir:
        
        if i[0] in camposDef.keys():
            if i[1] in camposDef[i[0]].keys():
                miDef = camposDef[i[0]][i[1]]
            else:
                print "i[0], i[1] ",i[0], i[1]
                print "camposDef[i[0]].keys() ", camposDef[i[0]].keys() 
                MError(None,  u"El t\xe9rmino %s no esta incluido en %s"%(i[1],i[0]) )
        else:
            MError(None,  u"El t\xe9rmino %s no esta incluido en camposDef"%(i[0]) )
        if len(miDef) > 2:
            entidad = miDef[2]
            id = miDef[3]
            campo = miDef[4]
        else:
            entidad = i[0]
            id=''
            campo = i[1]
        
        MiDataset = MiDataset.add_entity(eval(entidad))
        campos.append((entidad,campo))


    #print MiDataset
    
   
    datosListado = MiDataset.all()  
    #dumpdataset(datosListado)
    
    #listos para generar el reporte    

    #Formato = [['D',1],['D',2]]
    fileout = codecs.open(filename,'w','utf-8')
    fileout.write(moduleRep2.HTMLHeader(titulo=titulo, cols=cols))
    # generando el cuerpo del reporte
    reporta(datosListado, Formato, 0, campos, fileout, numerar=numerar)
    
    fileout.write(moduleRep2.HTMLFooter())
    fileout.close()
    return(filename)
    webbrowser.open(filename)

        

if __name__ == '__main__':
    #filename=ReporteAnalitico(['AB', 'EA'], [('Acto','PTipodeacto'), ('EventoTipificacion','derechosafectados')], [['D',1],['S',2]], filename='salida.htm', filtro=None)
    filename=ReporteAnalitico(['EA', 'GB'],[('EventoTipificacionDerechosAfectados','derechosafectados'),
                                            #('Localidad','strEstado'),
                                            ('TesEstado','descripcion'),
                                            ('Caso','fecha_inicio'),
                                            
                                            ('Caso','descripcion'),
                                            ('Caso','no_persona_afectadas')
                                            ],
                                            [['D',1],['D',1],['D',3]]
                                            )
                                            
    webbrowser.open(filename)
    pass # add a call to run your script here
