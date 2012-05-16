#-----------------------------------------------------------------------------
# Name:        configmodule.py
#
#
# RCS-ID:      $Id: configmodule.py $
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
VDefault={
          'T04':11258, # tipo de acto/vdh
          'T09':291,   #escolaridad
          'T14':11501, #idioma
          'T15':11610  #pais
          }
VOrden={'T01':"A",'T03':"C,C,A",'T04':"C,C,A", "T23":"C,A",
 "T41":"C", "T18":"C", "T26":"C", "T21":"C,C", "T46":"C", 
 "T62":"C", "T24":"C","T22":"C","T06":"C","T17":"C", "T42":"C"}

#def getDefault(valor):
#    if valor in VDefault.keys():
#        return VDefault[valor]
#    else:
#        return None
def getVOrden(valor):
    if valor in VOrden.keys():
        return VOrden[valor].split(',')
    else:
        return None