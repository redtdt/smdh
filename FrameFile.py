#-----------------------------------------------------------------------------
# Name:        FrameFile.py
#
#
# RCS-ID:      $Id: FrameFile.py $
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
#Boa:Frame:FrameFile

import wx
import wx.lib.filebrowsebutton

def create(parent):
    return FrameFile(parent)

[wxID_FRAMEFILE, wxID_FRAMEFILEFILEBROWSE, wxID_FRAMEFILEPANEL1, 
] = [wx.NewId() for _init_ctrls in range(3)]

class FrameFile(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEFILE, name='FrameFile',
              parent=prnt, pos=wx.Point(44, 56), size=wx.Size(396, 171),
              style=wx.DEFAULT_FRAME_STYLE, title='File')
        self.SetClientSize(wx.Size(380, 135))

        self.panel1 = wx.Panel(id=wxID_FRAME3PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(380, 135),
              style=wx.TAB_TRAVERSAL)

        self.fileBrowse = wx.lib.filebrowsebutton.FileBrowseButton(buttonText='Buscar',
              dialogTitle='Elija un archivo', fileMask='*.htm',
              id=wxID_FRAMEFILEFILEPICKERCTRL1, initialValue='',
              labelText='Reporte:', parent=self.panel1, pos=wx.Point(32, 24),
              size=wx.Size(296, 80), startDirectory='../archivos',
              style=wx.TAB_TRAVERSAL,
              toolTip='Escriba un nombre o escoja un archivo')

    def __init__(self, parent):
        self._init_ctrls(parent)
