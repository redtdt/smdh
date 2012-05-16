#-----------------------------------------------------------------------------
# Name:        dlggetpass.py
#
#
# RCS-ID:      $Id: dlggetpass.py $
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
#Boa:Dialog:GetDescrip

import wx

from module2 import LlenaAyuda

def create(parent):
    return GetDescrip(parent)

[wxID_GETDESCRIP, wxID_GETDESCRIPBTNCANCELAR, wxID_GETDESCRIPBUTTONREGRESAR, 
 wxID_GETDESCRIPCONTEXTHELPBUTTON1, wxID_GETDESCRIPSTATICTEXT1, 
 wxID_GETDESCRIPTEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(6)]

class GetDescrip(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_GETDESCRIP, name='GetDescrip',
              parent=prnt, pos=wx.Point(409, 307), size=wx.Size(691, 155),
              style=wx.DEFAULT_DIALOG_STYLE, title='Datos de seguridad')
        self.SetClientSize(wx.Size(675, 119))
        self.SetBackgroundColour(wx.Colour(194, 216, 218))
        self.SetToolTipString('')

        self.staticText1 = wx.StaticText(id=wxID_GETDESCRIPSTATICTEXT1,
              label='Contrase\xf1a', name='staticText1', parent=self,
              pos=wx.Point(120, 45), size=wx.Size(141, 13), style=0)
        self.staticText1.SetToolTipString('')

        self.textCtrl1 = wx.TextCtrl(id=wxID_GETDESCRIPTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(272, 40),
              size=wx.Size(168, 21), style=wx.TE_PASSWORD, value='')
        self.textCtrl1.Bind(wx.EVT_TEXT_ENTER, self.OnTextCtrlDescripENTER,
              id=wxID_GETDESCRIPTEXTCTRL1)

        self.buttonRegresar = wx.Button(id=wxID_GETDESCRIPBUTTONREGRESAR,
              label='Aceptar', name='buttonRegresar', parent=self,
              pos=wx.Point(248, 88), size=wx.Size(75, 23), style=0)
        self.buttonRegresar.Bind(wx.EVT_BUTTON, self.OnButtonRegresar,
              id=wxID_GETDESCRIPBUTTONREGRESAR)

        self.btnCancelar = wx.Button(id=wxID_GETDESCRIPBTNCANCELAR,
              label='Cancelar', name='btnCancelar', parent=self,
              pos=wx.Point(368, 88), size=wx.Size(75, 23), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_GETDESCRIPBTNCANCELAR)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self,
              pos=wx.Point(648, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTextCtrlDescripENTER(self, event):
        event.Skip()

    def OnButtonRegresar(self, event):
        self.Close()
        event.Skip()

    def OnBtnCancelarButton(self, event):
        self.textCtrl1.SetValue('')
        self.Close()
        event.Skip()
        
def MyPass(prnt, titulo=None, long=None, help=u''):
    dlg = GetDescrip(prnt)
    if titulo:
        dlg.staticText1.SetLabel( titulo)
        dlg.Title = titulo
    if long:
        dlg.textCtrl1.SetMaxLength(long)
    if help:
        LlenaAyuda(dlg, help)
    
    dlg.ShowModal()
    str = dlg.textCtrl1.GetValue()
    str = str.strip()
    dlg.Destroy()
    return str
    
    
