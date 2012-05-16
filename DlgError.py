#-----------------------------------------------------------------------------
# Name:        DlgError.py
#
#
# RCS-ID:      $Id: DlgError.py $
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
#Boa:Dialog:Dialog2

import wx

def create(parent):
    return Dialog2(parent)

[wxID_DIALOG2, wxID_DIALOG2BUTTON1, wxID_DIALOG2CONTEXTHELPBUTTON1, 
 wxID_DIALOG2MSG, 
] = [wx.NewId() for _init_ctrls in range(4)]

class Dialog2(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG2, name='', parent=prnt,
              pos=wx.Point(93, 147), size=wx.Size(400, 269),
              style=wx.DEFAULT_DIALOG_STYLE, title='Alerta')
        self.SetClientSize(wx.Size(392, 242))
        self.SetBackgroundColour(wx.Colour(255, 187, 119))

        self.button1 = wx.Button(id=wxID_DIALOG2BUTTON1, label='Aceptar',
              name='button1', parent=self, pos=wx.Point(160, 200),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_DIALOG2BUTTON1)

        self.MSG = wx.TextCtrl(id=wxID_DIALOG2MSG, name='MSG', parent=self,
              pos=wx.Point(56, 48), size=wx.Size(280, 145),
              style=wx.TE_MULTILINE | wx.TE_CENTRE, value='')
        self.MSG.SetEditable(True)
        self.MSG.Center(wx.BOTH)
        self.MSG.SetAutoLayout(True)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self,
              pos=wx.Point(360, 16), size=wx.Size(20, 19),
              style=wx.BU_AUTODRAW)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        self.Close()
        event.Skip()
def MError(prnt, mensaje):
    dlg = Dialog2(prnt)
    
    dlg.MSG.AppendText(mensaje)
    dlg.ShowModal()
