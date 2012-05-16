#-----------------------------------------------------------------------------
# Name:        DlgTipoCond.py
#
#
# RCS-ID:      $Id: DlgTipoCond.py $
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
#Boa:Dialog:DlgTipoCond

import wx
from module2 import LlenaCtrl3, LlenaAyuda

def create(parent):
    return DlgTipoCond(parent)

[wxID_DLGTIPOCOND, wxID_DLGTIPOCONDBTNSELECCIONAR, wxID_DLGTIPOCONDCANCELAR, 
 wxID_DLGTIPOCONDCONTEXTHELPBUTTON1, wxID_DLGTIPOCONDCTRLCAMPO, 
] = [wx.NewId() for _init_ctrls in range(5)]

class DlgTipoCond(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DLGTIPOCOND, name='DlgTipoCond',
              parent=prnt, pos=wx.Point(322, 183), size=wx.Size(518, 507),
              style=wx.DEFAULT_DIALOG_STYLE, title='Condici\xf3n')
        self.SetClientSize(wx.Size(502, 471))
        self.SetBackgroundColour(wx.Colour(184, 225, 228))

        self.btnSeleccionar = wx.Button(id=wxID_DLGTIPOCONDBTNSELECCIONAR,
              label='Seleccionar', name='btnSeleccionar', parent=self,
              pos=wx.Point(416, 32), size=wx.Size(75, 23), style=0)
        self.btnSeleccionar.Enable(False)
        self.btnSeleccionar.Bind(wx.EVT_BUTTON, self.OnBtnSeleccionarButton,
              id=wxID_DLGTIPOCONDBTNSELECCIONAR)

        self.ctrlCampo = wx.ListBox(choices=[], id=wxID_DLGTIPOCONDCTRLCAMPO,
              name='ctrlCampo', parent=self, pos=wx.Point(32, 32),
              size=wx.Size(376, 424), style=0)
        self.ctrlCampo.Bind(wx.EVT_LEFT_DOWN, self.OnCtrlCampoLeftDown)
        self.ctrlCampo.Bind(wx.EVT_LISTBOX, self.OnCtrlCampoListbox,
              id=wxID_DLGTIPOCONDCTRLCAMPO)

        self.Cancelar = wx.Button(id=wxID_DLGTIPOCONDCANCELAR, label='Cancelar',
              name='Cancelar', parent=self, pos=wx.Point(416, 64),
              size=wx.Size(75, 23), style=0)
        self.Cancelar.Bind(wx.EVT_BUTTON, self.OnCancelarButton,
              id=wxID_DLGTIPOCONDCANCELAR)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self,
              pos=wx.Point(472, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.seleccion = None
    def OnCtrlCampoChoice(self, event):
        
        event.Skip()

    def OnBtnSeleccionarButton(self, event):
        
        self.seleccion = self.ctrlCampo.GetClientData(self.ctrlCampo.GetSelection())
        self.Close()
        event.Skip()

    def OnCtrlCampoLeftDown(self, event):
        event.Skip()

    def OnCtrlCampoListbox(self, event):
        self.btnSeleccionar.Enable()
        event.Skip()

    def OnCancelarButton(self, event):
        self.Close()
        event.Skip()
def Condicion(prnt, campos):
    dlg = DlgTipoCond(prnt)
    LlenaCtrl3(dlg.ctrlCampo, campos)
    LlenaAyuda(dlg, u"condicion")
    dlg.ShowModal()
    r = dlg.seleccion
    return r
    
    
