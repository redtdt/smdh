#-----------------------------------------------------------------------------
# Name:        index-palabras.py
#
#
# RCS-ID:      $Id: index-palabras.py $
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
indice={}

def indexa(palabra):
    if palabra in indice.keys():
        indice[palabra] += 1
    else:
        indice[palabra] = 1

q=module2.session.query(Caso.descripcion, Caso.descripcion_narrativa)
for r in q.all():
    palabras = r[0].split(' ')
    for p in palabras:
        indexa(p)
    palabras = r[1].split(' ')
    for p in palabras:
        indexa(p)
l = [(indice[p],p) for p in indice.keys()]
for i in sorted(l):
    print i[0], i[1]


        
               
