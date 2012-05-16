#-----------------------------------------------------------------------------
# Name:        persona_similar.py
#
#
# RCS-ID:      $Id: persona_similar.py $
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
from module2 import session, Persona
from  metaphone import dm
from caso_similar import palabras_no_consideradas

def similaridad(a,b):
    
    if a[0] == b[0]: return 4
    if a[0] == b[1] or \
           a[1] == b[0]: return 2
    if a[1] and b[1] and \
           a[1] == b[1]: return 1
    return 0

def palabras_sim(palabras1, palabras2):
    palabras1 = module2.Sortable(palabras1).encode('latin_1').split(' ')
    palabras2 = module2.Sortable(palabras2).encode('latin_1').split(' ')
    cuenta = 0
    #for j in range(min(len(palabras1),len(palabras2))):
    for j in range(len(palabras1)):
        if palabras1[j].lower() not in palabras_no_consideradas:
           for k in range(len(palabras2)):
               if palabras2[k].lower() not in palabras_no_consideradas:
                   cuenta +=  similaridad(dm(palabras1[j]), dm(palabras2[k]))
                   #print "comparando ", palabras1[j] , " con ", palabras2[k]
        
    return cuenta
    
def persona_sim(p1, p2):
    peso_apellido = 3
    peso_nombre   = 1
    peso_edo      = 1
    peso_mpo      = 1
    cuenta = 0
    apellidos1 = p1.apellido
    apellidos2 = p2.apellido

    nombre1    = p1.nombre
    nombre2    = p2.nombre

    cuenta = palabras_sim(apellidos1, apellidos2) * peso_apellido

    if cuenta:
        cuenta += palabras_sim(nombre1, nombre2) * peso_nombre
        if p1.estado_nac_u_origen:
            cuenta += (p1.estado_nac_u_origen == p2.estado_nac_u_origen ) * peso_edo
        if p1.mpio_nac_u_origen:
            cuenta += (p1.mpio_nac_u_origen == p2.mpio_nac_u_origen) * peso_mpo
        
    return cuenta


if __name__ == '__main__':    
    codigosab = {}
    buscar = session.query(Persona).filter(Persona.id == 1102033).first()
    
    
    print buscar.apellido, buscar.nombre, buscar.estado_nac_u_origen, buscar.mpio_nac_u_origen
    indx = 0
    
    lista = session.query(Persona).filter(Persona.id < 9999).all()
    
    for i in lista:
            cuenta = persona_sim(i, buscar)
            if cuenta:
                print cuenta, i.apellido, i.nombre, i.estado_nac_u_origen, i.mpio_nac_u_origen
