#-----------------------------------------------------------------------------
# Name:        tdtdb.py
#
#
# RCS-ID:      $Id: App1.py $
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
#!/usr/bin/env python
#Boa:App:BoaApp



#enie  \xf1
#a   \xe1
#e   \xe9
#i   \xed
#o   \xf3
#u   \xfa

import wx
import sys

import Frame1
import logging
import os
import cnf

modules ={'Frame1': [1, 'Main frame of Application', u'Frame1.py'],
 u'FrameUtils': [0, '', u'FrameUtils.py'],
 u'configmodule': [0, '', u'configmodule.py']}

class BoaApp(wx.App):
    def OnInit(self):
        
        self.main = Frame1.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    os.umask(000)
    if not cnf.OSlinux:
        fsock = open('error.log', 'a')
        sys.stderr = fsock
    application = BoaApp(0)
    application.MainLoop()
    if not cnf.OSlinux:
        fsock.close()

if __name__ == '__main__':
    main()
