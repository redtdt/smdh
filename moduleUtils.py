#-----------------------------------------------------------------------------
# Name:        moduleUtils.py
#
#
# RCS-ID:      $Id: moduleUtils.py $
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
def moveCtrl(obj, px=0, dx=0, py=0, dy=0):
    x,y=obj.GetPositionTuple()
    x += dx
    if px:
        x = px
    if py:
        y=py
    if dy:
        y += dy
    
    obj.Move((x,y))
    
def Mvs(value):
    if value:
        return value
    else:
        return ''
    
def getCheckBoxValue(ctrl):
    if ctrl.GetValue() == True:
        return 1
    else:
        return 0
    
def setCheckBoxValue(value):
    if value == 1:
        return True
    else:
        return False
        