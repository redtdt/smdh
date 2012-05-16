#-----------------------------------------------------------------------------
# Name:        DlgAltaActo.py
#
#
# RCS-ID:      $Id: DlgAltaActo.py $
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
#Boa:Dialog:AltaActo

import wx
import module2
from module2 import status, LlenaAyuda
from dlgpersona import DlgVictima, PersonaDlg
from DLGTaxTree import getTaxonomyTree

def create(parent):
    return AltaActo(parent)

[wxID_ALTAACTO, wxID_ALTAACTOACTOVDH, wxID_ALTAACTOACTOVICTIMA, 
 wxID_ALTAACTOBTNASIGNAR, wxID_ALTAACTOBTNCANCELAR, 
 wxID_ALTAACTOCONTEXTHELPBUTTON1, wxID_ALTAACTOSTATICTEXT1, 
 wxID_ALTAACTOSTATICTEXT2, wxID_ALTAACTOTXTVDH, wxID_ALTAACTOTXTVICTIMA, 
] = [wx.NewId() for _init_ctrls in range(10)]

class AltaActo(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_ALTAACTO, name='AltaActo', parent=prnt,
              pos=wx.Point(43, 58), size=wx.Size(644, 291),
              style=wx.DEFAULT_DIALOG_STYLE, title='Nuevo acto')
        self.SetClientSize(wx.Size(628, 255))
        self.SetBackgroundColour(wx.Colour(183, 219, 219))

        self.staticText1 = wx.StaticText(id=wxID_ALTAACTOSTATICTEXT1,
              label='V\xedctima', name='staticText1', parent=self,
              pos=wx.Point(48, 72), size=wx.Size(34, 13), style=0)

        self.ActoVictima = wx.Button(id=wxID_ALTAACTOACTOVICTIMA, label='+',
              name='ActoVictima', parent=self, pos=wx.Point(96, 64),
              size=wx.Size(24, 23), style=0)
        self.ActoVictima.Bind(wx.EVT_BUTTON, self.OnActoVictima,
              id=wxID_ALTAACTOACTOVICTIMA)

        self.txtVictima = wx.StaticText(id=wxID_ALTAACTOTXTVICTIMA,
              label='______________________', name='txtVictima', parent=self,
              pos=wx.Point(136, 72), size=wx.Size(472, 24),
              style=wx.ST_NO_AUTORESIZE)
        self.txtVictima.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))

        self.staticText2 = wx.StaticText(id=wxID_ALTAACTOSTATICTEXT2,
              label='Tipo de acto \no VDH', name='staticText2', parent=self,
              pos=wx.Point(24, 112), size=wx.Size(62, 26), style=0)

        self.ActoVdh = wx.Button(id=wxID_ALTAACTOACTOVDH, label='+',
              name='ActoVdh', parent=self, pos=wx.Point(96, 112),
              size=wx.Size(24, 23), style=0)
        self.ActoVdh.Bind(wx.EVT_BUTTON, self.OnActoVdh,
              id=wxID_ALTAACTOACTOVDH)

        self.txtVdh = wx.StaticText(id=wxID_ALTAACTOTXTVDH,
              label='______________________', name='txtVdh', parent=self,
              pos=wx.Point(136, 120), size=wx.Size(472, 56),
              style=wx.ST_NO_AUTORESIZE)
        self.txtVdh.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))

        self.btnAsignar = wx.Button(id=wxID_ALTAACTOBTNASIGNAR,
              label='Seleccionar', name='btnAsignar', parent=self,
              pos=wx.Point(32, 184), size=wx.Size(75, 23), style=0)
        self.btnAsignar.Enable(False)
        self.btnAsignar.Bind(wx.EVT_BUTTON, self.OnBtnAsignar,
              id=wxID_ALTAACTOBTNASIGNAR)

        self.btnCancelar = wx.Button(id=wxID_ALTAACTOBTNCANCELAR,
              label='Cancelar', name='btnCancelar', parent=self,
              pos=wx.Point(120, 184), size=wx.Size(75, 23), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelar,
              id=wxID_ALTAACTOBTNCANCELAR)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self,
              pos=wx.Point(600, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.pattern=None
        self.persona=None
        self.tipo=None
        self.retcode = None
        self.hayVictima = False
        self.hayVDH = False
        LlenaAyuda(self, u'DlgAltaActo')
    def OnActoVictima(self, event):
        self.persona = PersonaDlg(self, help=u'PersonaDlgVictima')
        if self.persona:
            self.txtVictima.SetLabel( self.persona.Descriptor())
            self.hayVictima = True
            if self.hayVictima and self.hayVDH:
                self.btnAsignar.Enable()
            
        event.Skip()

    def OnActoVdh(self, event):
        self.tipo = getTaxonomyTree(self,u'T04',"Tipo de acto",Pattern=self.pattern, help=u'getTaxonomyTreeTipoActo')
        if self.tipo:
            self.txtVdh.SetLabel( self.tipo.descripcion)
            self.hayVDH = True
            if self.hayVictima and self.hayVDH:
                self.btnAsignar.Enable()
        
        event.Skip()

    def OnBtnAsignar(self, event):
        self.retcode= True
        self.EndModal(wx.ID_OK) 
        event.Skip()

    def OnBtnCancelar(self, event):
        self.EndModal(wx.ID_CANCEL)
        event.Skip()
def NuevoActo(prnt, pattern):
    dlg = AltaActo(prnt)
    dlg.pattern=pattern
    LlenaAyuda(dlg, u'Victima')
    dlg.ShowModal()
    P = dlg.persona
    T = dlg.tipo
    if dlg.retcode:
        return P, T
    else:
        if module2.status.personaReciente:
            module2.BorraPersona(module2.status.personaReciente)
        return None, None 
