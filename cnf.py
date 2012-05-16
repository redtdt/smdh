#-----------------------------------------------------------------------------
# Name:        cnf.py
#
#
# RCS-ID:      $Id: cnf.py $
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
from ConfigParser import *
from os import name as NameOS
slash = '\\'
OSwin = True
OSlinux = False
if NameOS in ['posix']:
    slash = '/'
    OSwin = False
    OSlinux = True
    
db='redtdt'
host='localhost'


conf = ConfigParser()
nombre = 'config%ssmdh.ini'%slash
l=conf.read(nombre)
if l:
    entradas = conf.defaults().keys()
    
    if 'db' in entradas:
        db=conf.defaults()['db']
        db=db.lower()
    else:
        db='redtdt'
    if 'host' in entradas:
        host=conf.defaults()['host']
user = ''
passwd = ''
baseCentral = db in ["redtdtcentral","'redtdtcentral'"]
baseLocal   = not baseCentral
if host.strip() == '':
    host = 'localhost'
localhost = host in ['localhost', '127.0.0.1']
adminAccount = ['admin', 'vocab', 'postgres']
localCountry=u'M\xe9xico'
# criterio para versiones
# se avanza una letra con cada correccion de bugs
# se avanzan centesimas (del 00 al 99) cuando se agregar funcionalidades
# la version 2.00 esta prevista con la fase 2 (exportacion/importacion)
PRGversion = "2.40"
PRGdate = '12-ago-11'

