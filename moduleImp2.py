#-----------------------------------------------------------------------------
# Name:        moduleImp2.py
#
#
# RCS-ID:      $Id: moduleImp2.py $
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
from moduleImp1 import getElements, myNodeValue
import module2
from moduleFechas import camposFechasValidas


def myValue(nodo):
       
        valor=None
        if nodo.hasAttribute('REFID'):
            valor=nodo.getAttribute('REFID')
        else:
            if nodo.childNodes:
                
                
                exp = nodo.childNodes[0].nodeValue
                if exp:
                    valor = exp
        return valor

def validaFechas(nodo, EtipoI, EfechaI, EtipoF, EfechaF, tipodenodo, separador='\n'):
    listadeErrores=[]

    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i

    descriptor = nodo.getAttribute('descriptor')
    
    mensaje = ''
    llaves = childs.keys()
    for elemento in [EtipoI, EfechaI, EtipoF, EfechaF]:
        if elemento not in llaves:
            #error = u" - En "+tipodenodo+' "'+descriptor+u' La fecha de inicio o fin esta incompleta' # no hay elementos suficientes (cosa rara...)
            #listadeErrores.append(error + separador)
            return listadeErrores
            
    
    tipoI = myValue(childs[EtipoI])
    tipoF = myValue(childs[EtipoF])
    
    if tipoI == 'None': tipoI = None 
    if tipoF == 'None': tipoF = None 
    
    
    
    fechaI = myNodeValue(childs[EfechaI], 'Date')
    fechaF = myNodeValue(childs[EfechaF], 'Date')
    
    
    error = ''
    
    valido=camposFechasValidas(tipoI, fechaI, tipoF, fechaF, module2.status)
    
    if not valido:
                error = u" - En "+tipodenodo+' "'+descriptor+u'": La fecha final es anterior a la fecha inicial'
                print "fecha invalida ", tipoI, fechaI, tipoF, fechaF
        
    
    if error: listadeErrores.append(error + separador)
    return listadeErrores



def validaNodo(nodos, condiciones, tipodenodo, separador='\n'):
    #print "validando nodo"
    listadeErrores=[]
    for nodo in nodos:
        childs={}
        for i in nodo.childNodes:
            childs[i.nodeName]=i
        #for i in childs.keys():
        #    print i, childs[i]
        descriptor = nodo.getAttribute('descriptor')
        #descriptor = descriptor.encode( "latin-1", 'ignore' )
        for cond in condiciones:
            error = ''
            elemento, mensaje = cond
            miElemento = childs[elemento] if elemento in childs else None
            #miElemento = nodo.getElementsByTagName(elemento)
            #print miElemento
            contenido = None
            if miElemento:
                if elemento == 'loginfo':
                    if miElemento.childNodes:
                        contenido = True
                    
                
                else:
                    contenido = myValue(miElemento)
                    if not contenido:
                        error = u" - En "+tipodenodo+' "'+descriptor+u'":'+mensaje+u" ausente" # el elemento esta vacio
                
            else:
                error = u" - En "+tipodenodo+' "'+descriptor+u'":'+mensaje+u" ausente" #el elemento no esta presente
            if error: listadeErrores.append(error + separador)
    return listadeErrores

def validaCaso(nodo, separador='\n'):
    
    res = []
    caso = nodo
    res += validaNodo([caso],[
                              #['descripcion_narrativa',u'Descripci\xf3n narrativa'],
                              ['resumen_descripcion',u'Resumen de la descripci\xf3n'],
                              ['loginfo',u'Informaci\xf3n de creaci\xf3n/actualizaci\xf3n'],
                              
                              
                              ], 'caso')
    
    res += validaFechas(caso, 'tipo_fecha_inicio', 'fecha_inicio', 'tipo_fecha_final', 'fecha_final','caso')
    localidades = getElements(caso,'Localidades')
    res += validaNodo(localidades,[['loginfo',u'Informaci\xf3n de creacion/actualizaci\xf3n']],'localidad')
    
    intervenciones = getElements(caso, 'Intervenciones')
    res += validaNodo(intervenciones,[
                                       ['tesauro_id',u'Tipo de intervenci\xf3n'],
                                       ['Pinterviniente',u'Parte interviniente'],
                                       ['loginfo',u'Informaci\xf3n de creaci\xf3n/actualizaci\xf3n'],
                                     ],'intervencion')
    
    fuentes = getElements(caso, 'FuentesPersonales')
    res += validaNodo(fuentes,[
                                      ['PersonaFuente',u'Persona como fuente'],
                                      ['loginfo',u'Informaci\xf3n de creaci\xf3n/actualizaci\xf3n']
                                      ],'fuente personal')
                                      
                                      
    publicaciones = getElements(caso, 'Publicaciones')
    res += validaNodo(publicaciones,[
                                     ['titulo_de_parte',u'T\xedtulo'],
                                     ['loginfo',u'Informaci\xf3n de creaci\xf3n/actualizaci\xf3n'],
                                     ],'fuente documental')
    
    actos = getElements(caso, 'Actos')
    res += validaActos(actos)
    return res
def validaActos(actos):
    res = []
    for acto in actos:
        
        res += validaNodo([acto],[
                                  ['tipodeacto',u'Tipo de acto'],
                                  ['Victima',u'V\xedctima'],
                                  ['loginfo',u'Informaci\xf3n de creaci\xf3n/actualizaci\xf3n'],
                                  ],'acto')
        res += validaFechas(acto, 'tipofechainicio', 'fechainicio', 'tipofechafinal', 'fechafin','acto')
        perpetradores = getElements(acto, 'Perpetradores')
        res += validaNodo(perpetradores,[
                                          ['persona_id',u'Informaci\xf3n de perpetrador'],
                                          ['loginfo',u'Informaci\xf3n de creaci\xf3n/actualizaci\xf3n'],
                                          ],'involucramiento')
    return res                                      
                                  
        

