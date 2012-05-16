#-----------------------------------------------------------------------------
# Name:        DlgInterv.py
#
#
# RCS-ID:      $Id: DlgInterv.py $
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
#Boa:Dialog:DlgInterv

import wx
import module2
from dlgpersona import PersonaDlg
from DLGTaxTree import getTaxonomyTree

def create(parent):
    return DlgInterv(parent)

[wxID_DLGINTERV, wxID_DLGINTERVBTNASIGNAR, wxID_DLGINTERVBTNCANCELAR, 
 wxID_DLGINTERVBTNPARTEINT, wxID_DLGINTERVBTNTIPOINT, 
 wxID_DLGINTERVCONTEXTHELPBUTTON1, wxID_DLGINTERVSTATICPARTEINT, 
 wxID_DLGINTERVSTATICTEXT1, wxID_DLGINTERVSTATICTEXT2, 
 wxID_DLGINTERVSTATICTIPOINT, 
] = [wx.NewId() for _init_ctrls in range(10)]

class DlgInterv(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DLGINTERV, name='DlgInterv',
              parent=prnt, pos=wx.Point(86, 111), size=wx.Size(546, 340),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Agregar intervenci\xf3n')
        self.SetClientSize(wx.Size(530, 304))
        self.SetBackgroundColour(wx.Colour(222, 254, 203))

        self.btnParteInt = wx.Button(id=wxID_DLGINTERVBTNPARTEINT, label='+',
              name='btnParteInt', parent=self, pos=wx.Point(120, 80),
              size=wx.Size(24, 23), style=0)
        self.btnParteInt.Bind(wx.EVT_BUTTON, self.OnBtnParteIntButton,
              id=wxID_DLGINTERVBTNPARTEINT)

        self.btnTipoInt = wx.Button(id=wxID_DLGINTERVBTNTIPOINT, label='+',
              name='btnTipoInt', parent=self, pos=wx.Point(120, 136),
              size=wx.Size(24, 23), style=0)
        self.btnTipoInt.Bind(wx.EVT_BUTTON, self.OnBtnTipoIntButton,
              id=wxID_DLGINTERVBTNTIPOINT)

        self.btnAsignar = wx.Button(id=wxID_DLGINTERVBTNASIGNAR,
              label='Seleccionar', name='btnAsignar', parent=self,
              pos=wx.Point(144, 264), size=wx.Size(75, 23), style=0)
        self.btnAsignar.Bind(wx.EVT_BUTTON, self.OnBtnAsignarButton,
              id=wxID_DLGINTERVBTNASIGNAR)

        self.btnCancelar = wx.Button(id=wxID_DLGINTERVBTNCANCELAR,
              label='Cancelar', name='btnCancelar', parent=self,
              pos=wx.Point(296, 264), size=wx.Size(75, 23), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_DLGINTERVBTNCANCELAR)

        self.staticText1 = wx.StaticText(id=wxID_DLGINTERVSTATICTEXT1,
              label=u'Tipo de intervenci\xf3n', name='staticText1', parent=self,
              pos=wx.Point(16, 144), size=wx.Size(97, 32), style=0)

        self.staticText2 = wx.StaticText(id=wxID_DLGINTERVSTATICTEXT2,
              label='Qui\xe9n inicia o realiza esta intervenci\xf3n',
              name='staticText2', parent=self, pos=wx.Point(16, 80),
              size=wx.Size(96, 48), style=0)

        self.staticParteInt = wx.StaticText(id=wxID_DLGINTERVSTATICPARTEINT,
              label='  ', name='staticParteInt', parent=self, pos=wx.Point(160,
              88), size=wx.Size(6, 13), style=0)

        self.staticTipoInt = wx.StaticText(id=wxID_DLGINTERVSTATICTIPOINT,
              label='  ', name='staticTipoInt', parent=self, pos=wx.Point(168,
              144), size=wx.Size(6, 13), style=0)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self,
              pos=wx.Point(504, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.persona=None
        self.tipo=None
        self.retcode = None
        module2.LlenaAyuda(self, u'DlgInterv')
        self.btnAsignar.Enable(False)


    def OnBtnParteIntButton(self, event):
        self.persona = PersonaDlg(self, help=u'PersonaDlgAltaInter')
        if self.persona:
            self.staticParteInt.SetLabel( self.persona.Descriptor())
            if self.tipo:
                self.btnAsignar.Enable()
        event.Skip()

    def OnBtnTipoIntButton(self, event):
        self.tipo = getTaxonomyTree(self, u"T20", u"Tipo de intervenci\xf3n", help=u'getTaxAltaInterTipoInt')
        if self.tipo:
            self.staticTipoInt.SetLabel( self.tipo.descripcion)
            if self.persona:
                self.btnAsignar.Enable()

        event.Skip()

    def OnBtnAsignarButton(self, event):
        self.retcode= True
        self.EndModal(wx.ID_OK)
        event.Skip()

    def OnBtnCancelarButton(self, event):
        self.EndModal(wx.ID_CANCEL)
        event.Skip()
def DialogIntervencion(prnt):
    dlg = create(prnt)
    
    
    dlg.ShowModal()
    P = dlg.persona
    T = dlg.tipo
    if dlg.retcode:
        
        return P, T
    else:
        if module2.status.personaReciente:
            module2.BorraPersona(module2.status.personaReciente)
        return None, None
    


if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = create(None)
    try:
        dlg.ShowModal()
    finally:
        dlg.Destroy()
    app.MainLoop()
