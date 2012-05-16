#-----------------------------------------------------------------------------
# Name:        PopError.py
#
#
# RCS-ID:      $Id: PopError.py $
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
#Boa:PopupWindow:PopupWindow1

import wx

def create(parent):
    return PopupWindow1(parent)

[wxID_POPUPWINDOW1, wxID_POPUPWINDOW1BUTTON1, wxID_POPUPWINDOW1MSG, 
] = [wx.NewId() for _init_ctrls in range(3)]

class PopupWindow1(wx.PopupWindow):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.PopupWindow.__init__(self, flags=wx.SIMPLE_BORDER, parent=prnt)
        self.SetSize(wx.Size(400, 204))
        self.Move(wx.Point(463, 260))
        self.SetAutoLayout(True)
        self.Center(wx.BOTH)

        self.button1 = wx.Button(id=wxID_POPUPWINDOW1BUTTON1, label='Aceptar',
              name='button1', parent=self, pos=wx.Point(168, 104),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_POPUPWINDOW1BUTTON1)

        self.MSG = wx.StaticText(id=wxID_POPUPWINDOW1MSG, label='', name='MSG',
              parent=self, pos=wx.Point(168, 32), size=wx.Size(0, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        self.Close(True)
        event.Skip()
