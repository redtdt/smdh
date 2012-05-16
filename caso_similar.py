#-----------------------------------------------------------------------------
# Name:        caso_similar.py
#
#
# RCS-ID:      $Id: caso_similar.py $
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
if __name__ == '__main__':
    import cnf
    cnf.user='admin'
    cnf.passwd='redtdt'

import module2
from module2 import session, Caso
Sc2 = None
descrip = None
busTips = None
busTemas = None
busLocalidadE,busLocalidadM  =  None, None

palabras_no_consideradas = ['a','ante','bajo','cabe','con','contra','de','desde','con','contra',
'de','desde','durante','en','entre','hacia','hasta','mediante','para','por',
'segun','sin','so','sobre','tras','y','o','abuso','caso','en','el','al','la','del','las','los','un','una',
'temor']

signos_de_puntuacion =  ['.',',',';',':','-']
def similaridad_descripcion(p1, p2):
    cuenta = 0
    for i in p1:
        if i in p2:
            cuenta += 1
    return cuenta
def similaridad_tipificacion(s1, s2):
    s= s1.intersection(s2)
    return len(s)

def similaridad_localidad(se1, sm1, se2, sm2):
    se=se1.intersection(se2)
    sm=sm1.intersection(sm2)
    return len(se)+len(sm)*2
    

def lista_descripcion(p):
    """ regresa una lista de palabras a considerar cuando se comparan dos descripciones de caso"""
    for s in signos_de_puntuacion:
        p = p.replace(s," ")
    p = p.replace('    ',' ')    
    p = p.replace('   ',' ')    
    p = p.replace('  ',' ')
    p = p.lower()
    p=p.split(' ')
    return [i for i in p if i not in palabras_no_consideradas]

def caso_sim(c1, c2):
    
    global Sc2, descrip, busTips, busTemas, busLocalidadE,busLocalidadM
    
    
    
    descrip1 = lista_descripcion(c1.descripcion)
    busTips1    = c1.setDerechosAfectados()
    busTemas1   = c1.setTemas()
    busLocalidadE1,busLocalidadM1  =  c1.setLocalidades()
    
    if c2 != Sc2:
        Sc2 = c2
        descrip = lista_descripcion(c2.descripcion)
        busTips    = c2.setDerechosAfectados()
        busTemas   = c2.setTemas()
        busLocalidadE,busLocalidadM  =  c2.setLocalidades()
    r1 = similaridad_descripcion(descrip, descrip1)
    r2 = similaridad_tipificacion(busTips,busTips1)
    r3 = similaridad_tipificacion(busTemas, busTemas1)
    r4 = similaridad_localidad(busLocalidadE,busLocalidadM, busLocalidadE1,busLocalidadM1)
    
    return r1 + r2 + r3 + r4
    
if __name__ == '__main__':
    caso_a_buscar = session.query(Caso)[10]
    casos = session.query(Caso).filter(Caso.id < 9999).all()
    for  caso_busqueda in casos:
      descrip = lista_descripcion(caso_busqueda.descripcion)
      busTips    = caso_busqueda.setDerechosAfectados()
      busTemas   = caso_busqueda.setTemas()
      busLocalidadE,busLocalidadM  =  caso_busqueda.setLocalidades()
    
    
      for c in casos:
        des = lista_descripcion(c.descripcion)
        tips = c.setDerechosAfectados()
        temas = c.setTemas()
        E,M  =  c.setLocalidades()
        res = similaridad_descripcion(descrip, des)
        if res > 0:
           print res, similaridad_tipificacion(busTips, tips), similaridad_tipificacion(busTemas, temas),\
           similaridad_localidad(busLocalidadE,busLocalidadM, E,M)
           
        
