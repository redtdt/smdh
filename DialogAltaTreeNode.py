#-----------------------------------------------------------------------------
# Name:        DialogAltaTreeNode.py
#
#
# RCS-ID:      $Id: DialogAltaTreeNode.py $
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
#Boa:Dialog:Dialog3

import wx

def create(parent):
    return Dialog3(parent)

[wxID_DIALOG3, wxID_DIALOG3BUTTON1, wxID_DIALOG3BUTTON2, 
 wxID_DIALOG3STATICTEXT1, wxID_DIALOG3STATICTEXT2, wxID_DIALOG3TEXTCTRL1, 
 wxID_DIALOG3TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Dialog3(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG3, name='', parent=prnt,
              pos=wx.Point(421, 289), size=wx.Size(400, 250),
              style=wx.DEFAULT_DIALOG_STYLE, title='Vocabularios')
        self.SetClientSize(wx.Size(392, 220))

        self.staticText1 = wx.StaticText(id=wxID_DIALOG3STATICTEXT1,
              label='Clave', name='staticText1', parent=self, pos=wx.Point(48,
              24), size=wx.Size(27, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_DIALOG3STATICTEXT2,
              label='Descripcion', name='staticText2', parent=self,
              pos=wx.Point(48, 80), size=wx.Size(54, 13), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG3TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(120, 24), size=wx.Size(100, 21),
              style=0, value='textCtrl1')

        self.textCtrl2 = wx.TextCtrl(id=wxID_DIALOG3TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(120, 80), size=wx.Size(240, 21),
              style=0, value='textCtrl2')



    def __init__(self, parent):
        self._init_ctrls(parent)
