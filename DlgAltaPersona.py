#-----------------------------------------------------------------------------
# Name:        DlgAltaPersona.py
#
#
# RCS-ID:      $Id: DlgAltaPersona.py $
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
#Boa:Dialog:DlgAltaPersona

import wx
from module2 import MError, LlenaAyuda, LimpiaString

def create(parent):
    return DlgAltaPersona(parent)

[wxID_DLGALTAPERSONA, wxID_DLGALTAPERSONABTNASIGNAR, 
 wxID_DLGALTAPERSONABTNCANCELAR, wxID_DLGALTAPERSONACONTEXTHELPBUTTON1, 
 wxID_DLGALTAPERSONARADIOBOXINDIVIDUAL, 
 wxID_DLGALTAPERSONASTATICTEXTAPELLIDO_ORG, 
 wxID_DLGALTAPERSONASTATICTEXTNOMBREPERSONA, wxID_DLGALTAPERSONATXTAPELLIDO, 
 wxID_DLGALTAPERSONATXTNOMBREPERSONA, 
] = [wx.NewId() for _init_ctrls in range(9)]

class DlgAltaPersona(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DLGALTAPERSONA, name='DlgAltaPersona',
              parent=prnt, pos=wx.Point(184, 114), size=wx.Size(580, 279),
              style=wx.DEFAULT_DIALOG_STYLE, title='Datos de una persona')
        self.SetClientSize(wx.Size(564, 243))
        self.SetBackgroundColour(wx.Colour(27, 254, 225))
        self.Bind(wx.EVT_ACTIVATE, self.OnDlgAltaPersonaActivate)

        self.radioBoxIndividual = wx.RadioBox(choices=['Individual',
              'Colectiva' ], id=wxID_DLGALTAPERSONARADIOBOXINDIVIDUAL,
              label='Tipo', majorDimension=1, name='radioBoxIndividual',
              parent=self, pos=wx.Point(40, 8), size=wx.Size(152, 72),
              style=wx.RA_SPECIFY_COLS)
        self.radioBoxIndividual.Bind(wx.EVT_RADIOBOX, self.OnRadioBoxIndividual,
              id=wxID_DLGALTAPERSONARADIOBOXINDIVIDUAL)

        self.staticTextApellido_Org = wx.StaticText(id=wxID_DLGALTAPERSONASTATICTEXTAPELLIDO_ORG,
              label='Apellido(s)', name='staticTextApellido_Org', parent=self,
              pos=wx.Point(56, 144), size=wx.Size(50, 13), style=0)

        self.staticTextNombrePersona = wx.StaticText(id=wxID_DLGALTAPERSONASTATICTEXTNOMBREPERSONA,
              label='Nombre(s)', name='staticTextNombrePersona', parent=self,
              pos=wx.Point(56, 112), size=wx.Size(50, 13), style=0)

        self.TxtApellido = wx.TextCtrl(id=wxID_DLGALTAPERSONATXTAPELLIDO,
              name='TxtApellido', parent=self, pos=wx.Point(168, 136),
              size=wx.Size(312, 24), style=0, value='')
        self.TxtApellido.SetMaxLength(330)

        self.TxtNombrePersona = wx.TextCtrl(id=wxID_DLGALTAPERSONATXTNOMBREPERSONA,
              name='TxtNombrePersona', parent=self, pos=wx.Point(168, 104),
              size=wx.Size(312, 24), style=0, value='')
        self.TxtNombrePersona.SetMaxLength(330)

        self.btnAsignar = wx.Button(id=wxID_DLGALTAPERSONABTNASIGNAR,
              label='Seleccionar', name='btnAsignar', parent=self,
              pos=wx.Point(224, 208), size=wx.Size(75, 23), style=0)
        self.btnAsignar.Bind(wx.EVT_BUTTON, self.OnBtnAsignarButton,
              id=wxID_DLGALTAPERSONABTNASIGNAR)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self,
              pos=wx.Point(536, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)

        self.btnCancelar = wx.Button(id=wxID_DLGALTAPERSONABTNCANCELAR,
              label='Cancelar', name='btnCancelar', parent=self,
              pos=wx.Point(320, 208), size=wx.Size(75, 23), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_DLGALTAPERSONABTNCANCELAR)

    def __init__(self, parent):
        self._init_ctrls(parent)
        LlenaAyuda(self, u'AltaPersonaInd')
        LlenaAyuda(self, u'AltaPersona')
        self.res = False

    def OnRadioBoxIndividual(self, event):
        self.AjustaRadiobox()
        
    def AjustaRadiobox(self):
        i = self.radioBoxIndividual.GetSelection()
        if i == 0:
            SetRadioBoxIndividual(self, True)
            LlenaAyuda(self, u'AltaPersonaInd')
            
        else:
            SetRadioBoxIndividual(self, False) 
            LlenaAyuda(self, u'AltaPersonaCol')       
            


    def OnDlgAltaPersonaActivate(self, event):
        #SetRadioBoxIndividual(self, True)
        self.AjustaRadiobox()
        event.Skip()

    def OnBtnAsignarButton(self, event):
        self.res = True
        self.Close()
        event.Skip()

    def OnBtnCancelarButton(self, event):
        self.Close()
        event.Skip()
        
def SetRadioBoxIndividual(self, indiv):
    if indiv:
        self.staticTextApellido_Org.SetLabel( 'Apellido(s)')
        self.staticTextNombrePersona.SetLabel( 'Nombre(s)')

        
    else:
        self.staticTextApellido_Org.SetLabel( 'Nombre')
        self.staticTextNombrePersona.SetLabel( 'Sigla')
def DatosAltaPersona(prnt):
    dlg= DlgAltaPersona(prnt)
    dlg.ShowModal()
    nombre, apellido, indiv, res = dlg.TxtNombrePersona.GetValue(), dlg.TxtApellido.GetValue(), dlg.radioBoxIndividual.GetSelection(), dlg.res
    nombre = LimpiaString(nombre)
    apellido = LimpiaString(apellido)
    if indiv: indiv =0
    else: indiv =1
    if not apellido:

                if indiv == 1:
                    MError(prnt, "No se puede crear una persona individual sin apellido")
                else:
                    MError(prnt, "No se puede crear una persona colectiva sin nombre")
    dlg.Destroy()
    return nombre, apellido, indiv, res

