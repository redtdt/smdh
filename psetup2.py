#-----------------------------------------------------------------------------
# Name:        psetup2.py
#
#
# RCS-ID:      $Id: psetup2.py $
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
#
#
from distutils.core import setup
#
import py2exe
#
import sys
#
 
#
# no arguments
#
if len(sys.argv) == 1:
#
     sys.argv.append("py2exe")
#
 
#
# creates a standalone .exe file, no zip files
#
setup( options = {"py2exe": {"compressed": 1, "optimize": 2, "ascii": 1, "bundle_files": 1}},
#
                zipfile = None,
#
# replace myFile.py with your own code filename here ...
#
                windows = [{"script": 'psetup.py'}] )
