#-----------------------------------------------------------------------------
# Name:        moduleRep4.py
#
#
# RCS-ID:      $Id: moduleRep4.py $
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
# genera cruces
from module2 import *
import module2
import codecs
import moduleRep2
import webbrowser
#from midataset import MiDataset
from sqlalchemy.sql import func
import operator

session = status.session

camposDef = moduleRep2.campos
renderObj = moduleRep2.renderObj

m={}
campo={}
entidad={}
y=[]
totalx={}
totaly={}
total = 0

def NoCero(i):
    if i:
        return str(i)
    return ''

def ReporteLineal(titulo=''):
#agrego columnas especificas
#cambia segun cada reporte

    MiDataset=MiDataset.add_entity(TesNode, id='PTipodelugar')
    MiDataset=MiDataset.add_entity(TesNode, id='PTipodeacto')
    filename = 'salida.htm'
    fileout = codecs.open(filename,'w','utf-8')
    fileout.write(moduleRep2.HTMLHeader(titulo=titulo))
    
    # reporte por columnas
    for i,j,k in MiDataset.all():
        fileout.write('<tr><td>%s</td><td>%s</td><td>%s</td></tr>'%(DesNotNull(i),DesNotNull(j),DesNotNull(k)))
    
    fileout.write('</table>')
    fileout.write(moduleRep2.HTMLFooter())
    fileout.close()
    webbrowser.open(filename)

#ojo codigo obsoleto
def procesaMatriz(vi,vj):
#        for o,vi,vj in MiDataset: #   .all():
        global id, m, campo, entidad, y, totalx, totaly, total
        
        i = renderObj(vi, campo[0], entidad[0],'RAW')
        j = renderObj(vj, campo[1], entidad[1],'RAW')
        total += 1
        
        if i not in m.keys():
            m[i]={}
            m[i][j]=1
            totalx[i]=1
        else:
            totalx[i] += 1
            if j not in m[i].keys():
                m[i][j]=1
            else:
                m[i][j] += 1
        if j not in totaly.keys():
            totaly[j] = 1
        else:
            totaly[j] += 1
        if j not in y:
            y.append(j)

# ojo, codigo obsoleto. reemplazado por generacruce2
def generaCruce(MiDataset, camposAincluir, titulo=''):
    #campos a incluir es una lista de 2-tuplas con entidad y campo de la entidad
    #MiDataset = Dataset
    
    Dataset={}
    Dataset[0]=MiDataset.order_by(Caso.id)
    Dataset[1]=MiDataset.order_by(Caso.id)
    global id, m, campo, entidad, y, totalx, totaly, total
    
    id={}
    m={}
    campo={}
    entidad={}
    y=[]
    totalx={}
    totaly={}
    total = 0
    
    for k in range(2):
        i = camposAincluir[k]
        miDef = camposDef[i[0]][i[1]]
        if len(miDef) > 2:
            entidad[k] = miDef[2]
            id[k] = miDef[3]
            campo[k] = miDef[4]
        else:
            entidad[k] = i[0]
            id[k]=''
            campo[k] = i[1]
        print entidad, id, campo
        print "agregando entidad ", entidad[k]
        #
        #Dataset[k] = Dataset[k].outerjoin(eval(entidad[k]))
        #Dataset[k] = Dataset[k].add_entity(eval(entidad[k]))
        if i[0] in Req.keys():
            Dataset[k] = Dataset[k].outerjoin(Req[i[0]])
        Dataset[k] = Dataset[k].outerjoin(eval(i[0]))
        Dataset[k] = Dataset[k].add_entity(eval(entidad[k]))
    

    filename = 'salida.htm'
    fileout = codecs.open(filename,'w','utf-8')
    fileout.write(moduleRep2.HTMLHeader(titulo=titulo, border=1))

    
    
    # reporte de cruzamiento
    #armado preliminar de la matriz

    y=[]
    totalx={}
    totaly={}
    total = 0
    #contabiliza las ocurrencias de los i,j en una matriz bidimensional m[i][j]
    #ademas construye una lista  con los posibles valores j, llamado y
    print "dataset:", MiDataset
    
    L={}
    R={}
    
    R0 = Dataset[0].all()
    R1 = Dataset[1].all()
    print '-----'
    print R0
    print '-----'
    print R1
    print '-----'
    L0 = len(R0)     
    
    objActual = None
    n = 0
    while n < L0:
        x1 = R0[n]
        if x1[0] != objActual:
            objActual = x1[0]
            lista = [o for o in R1 if o[0] == objActual]
        for y1 in lista:
            print x1[0], y1[0]
            procesaMatriz(x1[1],y1[1])
        n = n + 1
        
    #impresion de la matriz
    fileout.write('<tr><td></td>')
    
    
    for i in m.keys():
       fileout.write('<td>%s</td> ' % (i))
       
    fileout.write('<td>Total</td></tr>')
    for j in y:
       fileout.write('<tr><td>%s</td>'% (j) )
       for i in m.keys():
            fileout.write('<td>%i</td>'% (MatNotNull(m,i,j)))
       fileout.write('<td>%i</td>'% (totaly[j]))
       fileout.write('</tr>')
    
    fileout.write('<tr><td>%s</td>'% ('Total'))
    for i in m.keys():
       fileout.write('<td>%i</td> ' % (totalx[i]))
    fileout.write('<td>%i</td> ' % (total))
       
    fileout.write('</tr>')
    
    fileout.write(moduleRep2.HTMLFooter())
    fileout.close()
    #return filename
    webbrowser.open(filename)
    








def procesaMatriz2(n,vi,vj):
        "agrega el valor n (ocurrencias) a la matriz m segun coordenadas (vi, vj)"
        # vi , vj son IDs de alguna clase arbitraria
        global id, m, campo, entidad, y, totalx, totaly, total
        i = vi
        j = vj

        if i not in m.keys():
            m[i]={}
            totalx[i]=0
        if j not in m[i].keys():
            m[i][j]=0
        if j not in totaly.keys():
            totaly[j] = 0
        if j not in y:
            y.append(j)        
        
        totalx[i] += n
        totaly[j] += n
        total += n
        m[i][j] += n
        

def generaCruce2(MiDataset,  #serie de tripletas donde
                             #la columna 0 es el No de ocurrencias
                             # i,j son ID de las clases que se especifican en DI, DJ
                             # la columna 1 corresponde a la ID i
                             # la columna 2 corresponde a la ID j

                 DI, # la clase para obtener los titulos de la columna i
                 DJ, # la clase para obtener los titulos de la columna j
                 filename = 'salida.htm', 
                 titulo='', 
                 DIRaiz=None, 
                 DJRaiz=None, 
                 descriptorIsrt=Descriptor, 
                 descriptorJsrt=Descriptor, 
                 descriptorIprt=Descriptor, 
                 descriptorJprt=Descriptor, 
                 
                 TotalJIzq=False, 
                 PieDePagina='',
                 strTotal = 'Total', #titulo de columna 2 (de totales)
                 strTituloCol1='',   # titulo columna 1
                 OmitirColumnas=False,
                 strGranTotal='Total',
                 BlanquearCero=False
                 
                 ):
    
    global id, m, campo, entidad, y, totalx, totaly, total
    print >> status.log, titulo.encode("latin_1", 'replace')
    #print >> status.log, "MiDataset (contenido) ", MiDataset
    print >> status.log, "MiDataset (contenido) ", [(i[0], str(i[1])+'-'+module2.Descriptor(TesNode, i[1]), str(i[2])+'-'+module2.Descriptor(TesNode, i[2])) for i in MiDataset]
    
    
    MostrarColumnas = not OmitirColumnas
    
    # inicializar estas estructuras en cada llamada
    m={}
    campo={}
    entidad={}
    y=[]
    totalx={}
    totaly={}
    total = 0
    
    listaI=[]
    listaJ=[]
    n=0
    strTotal='<td>'+strTotal+'</td>'
    
    #para cada dato en el dataset, incremento una unidad en la matriz usando procesamatriz2
    for i in MiDataset:
        
        procesaMatriz2(i[0], i[1], i[2])
        if DJRaiz:
        # para incluir tambien los titulos de las taxonomias de nivel superior
            nodo = TesById(i[2])
            padre = None
            if nodo:
                 padre=nodo.parent
            while padre and padre.parent and padre != DJRaiz:
                
                procesaMatriz2(0, i[1], padre.id)
                padre = padre.parent
                
        
    
    #m = matriz resultante
    #listaM  lista de indices por columna.
    print >> status.log, "M ", m
    listaM=m.keys()
    
    # para cada id en I...
    Id_y_descriptor = []
    for i in listaM:
        Id_y_descriptor.append( (i,descriptorIsrt(DI,i)) )
    aux = sorted(Id_y_descriptor, key=operator.itemgetter(1))
    
    listaM = map(operator.itemgetter(0), aux)
    
    
    # ojo listaM.sort()    ## como sortear segun diferentes criterios
    
    #listaY = lista de indices por renglon
    listaY=y
    
    
    # para cada id en J...
    Id_y_descriptor = []
    for i in listaY:

        Id_y_descriptor.append( (i,descriptorJsrt(DJ,i)) )
    aux = sorted(Id_y_descriptor, key=operator.itemgetter(1))
    
    listaY = map(operator.itemgetter(0), aux)
    
    
    
    
    # ojo listaY.sort()   ## como sortear segun diferentes criterios
    fileout = codecs.open(filename,'w','utf-8')
    fileout.write(moduleRep2.HTMLHeader(titulo=titulo, border=1))

    
    
    # reporte de cruzamiento
    #armado preliminar de la matriz


    #contabiliza las ocurrencias de los i,j en una matriz bidimensional m[i][j]
    #ademas contruye una lista  con los posibles valores j, llamado y

    
    print "matriz m ",m        
    #impresion de la matriz
    fileout.write('<tr><td>%s</td>'%(strTituloCol1))
    #print totalx.keys()
    
    # impresion del encabezado de la matriz
    # para cada columna de la matriz....
    if  TotalJIzq:   
       fileout.write(strTotal)
    if MostrarColumnas:
        for i in listaM:
           fileout.write('<td>%s</td> ' % (descriptorIprt(DI, i))) ## cambiar i por descriptor
    if not TotalJIzq:   
       fileout.write(strTotal)
    fileout.write('</tr>')
        
    for j in listaY:
       descripcion = descriptorJprt(DJ, j)
       # indentacion
       if DJRaiz:
            prof = tesauroProfundidad(j, DJRaiz)
            #descripcion = prof * '&nbsp;&nbsp;&nbsp;' + descripcion 
            descripcion = prof * '<ul>' + descripcion + prof * '</ul>'
       fileout.write('<tr><td>%s</td>'% (descripcion) ) ## cambiar j por descriptor
       
       if TotalJIzq:
           fileout.write('<td>%i</td>'% (totaly[j]))
       if MostrarColumnas:
           for i in listaM:
                
                fileout.write('<td>%s</td>'% NoCero(MatNotNull(m,i,j)))
       if not TotalJIzq:
           fileout.write('<td>%i</td>'% (totaly[j]))
       fileout.write('</tr>')
    
    fileout.write('<tr><td>%s</td>'% (strGranTotal))
    if TotalJIzq:
        fileout.write('<td>%i</td> ' % (total))
    if MostrarColumnas:
        for i in listaM:
           fileout.write('<td>%i</td> ' % (totalx[i]))
    if not TotalJIzq:
        fileout.write('<td>%i</td> ' % (total))
       
    fileout.write('</tr>')
        
    fileout.write(moduleRep2.HTMLFooter(PieDePagina = PieDePagina))
    
    fileout.close()
    return filename
