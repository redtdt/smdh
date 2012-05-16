#-----------------------------------------------------------------------------
# Name:        DlgInteger.py
#
#
# RCS-ID:      $Id: DlgInteger.py $
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
#Boa:Dialog:dlgInt

import wx

def create(parent):
    return dlgInt(parent)

[wxID_DLGINT, wxID_DLGINTBUTTON1, wxID_DLGINTSPINCTRL1, 
] = [wx.NewId() for _init_ctrls in range(3)]

class dlgInt(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DLGINT, name='dlgInt', parent=prnt,
              pos=wx.Point(514, 294), size=wx.Size(400, 250),
              style=wx.DEFAULT_DIALOG_STYLE, title='')
        self.SetClientSize(wx.Size(392, 223))

        self.spinCtrl1 = wx.SpinCtrl(id=wxID_DLGINTSPINCTRL1, initial=0,
              max=100, min=0, name='spinCtrl1', parent=self, pos=wx.Point(144,
              56), size=wx.Size(117, 21), style=wx.SP_ARROW_KEYS)

        self.button1 = wx.Button(id=wxID_DLGINTBUTTON1, label='OK',
              name='button1', parent=self, pos=wx.Point(160, 120),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_DLGINTBUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.res = 0

    def OnButton1Button(self, event):
        self.res = self.spinCtrl1.GetValue()
        self.Close()
        event.Skip()
def dlgInteger(prnt):
    dlg = dlgInt(prnt)
    dlg.ShowModal()
    res = dlg.res
    dlg.Destroy()
    
    return res
    
