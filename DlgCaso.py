#-----------------------------------------------------------------------------
# Name:        DlgCaso.py
#
#
# RCS-ID:      $Id: DlgCaso.py $
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
#Boa:Dialog:DlgCaso

import wx
from module2 import LlenaCtrlCasos, MyClientData, status, LlenaAyuda
from DLGTaxTree import getTaxonomyTree

def create(parent):
    return DlgCaso(parent)

[wxID_DLGCASO, wxID_DLGCASOBTNCANCELAR, wxID_DLGCASOBTNSELECCIONAR, 
 wxID_DLGCASOBTNTIPORELCASO, wxID_DLGCASOCASOISEARCH, 
 wxID_DLGCASOCONTEXTHELPBUTTON1, wxID_DLGCASOFRCCASORELTIPO, 
 wxID_DLGCASOLISTBOXCASOS, wxID_DLGCASOSTATICCASO, wxID_DLGCASOSTATICTEXT1, 
 wxID_DLGCASOSTATICTEXT109, wxID_DLGCASOSTATICTEXT2, 
] = [wx.NewId() for _init_ctrls in range(12)]

elCaso = None
class DlgCaso(wx.Dialog):
    
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DLGCASO, name='DlgCaso', parent=prnt,
              pos=wx.Point(381, 70), size=wx.Size(428, 509),
              style=wx.DEFAULT_DIALOG_STYLE, title='Seleccionar caso')
        self.SetClientSize(wx.Size(420, 482))
        self.SetBackgroundColour(wx.Colour(187, 198, 188))
        self.Bind(wx.EVT_INIT_DIALOG, self.OnDlgCasoInitDialog)

        self.listBoxCasos = wx.ListBox(choices=[], id=wxID_DLGCASOLISTBOXCASOS,
              name='listBoxCasos', parent=self, pos=wx.Point(32, 160),
              size=wx.Size(344, 272), style=wx.HSCROLL)
        self.listBoxCasos.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnListBoxCasosListboxDclick, id=wxID_DLGCASOLISTBOXCASOS)
        self.listBoxCasos.Bind(wx.EVT_LISTBOX, self.OnListBoxCasosListbox,
              id=wxID_DLGCASOLISTBOXCASOS)

        self.casoIsearch = wx.TextCtrl(id=wxID_DLGCASOCASOISEARCH,
              name='casoIsearch', parent=self, pos=wx.Point(96, 128),
              size=wx.Size(280, 21), style=0, value='')
        self.casoIsearch.Bind(wx.EVT_TEXT, self.OnCasoIsearchText,
              id=wxID_DLGCASOCASOISEARCH)

        self.staticText1 = wx.StaticText(id=wxID_DLGCASOSTATICTEXT1,
              label='Buscar', name='staticText1', parent=self, pos=wx.Point(32,
              136), size=wx.Size(32, 13), style=0)

        self.btnSeleccionar = wx.Button(id=wxID_DLGCASOBTNSELECCIONAR,
              label='Establecer relaci\xf3n', name='btnSeleccionar',
              parent=self, pos=wx.Point(56, 448), size=wx.Size(107, 23),
              style=0)
        self.btnSeleccionar.Bind(wx.EVT_BUTTON, self.OnBtnSeleccionarButton,
              id=wxID_DLGCASOBTNSELECCIONAR)

        self.btnCancelar = wx.Button(id=wxID_DLGCASOBTNCANCELAR,
              label='Cancelar', name='btnCancelar', parent=self,
              pos=wx.Point(248, 448), size=wx.Size(75, 23), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_DLGCASOBTNCANCELAR)

        self.staticText109 = wx.StaticText(id=wxID_DLGCASOSTATICTEXT109,
              label='Se relaciona como', name='staticText109', parent=self,
              pos=wx.Point(32, 72), size=wx.Size(86, 13), style=0)

        self.btnTipoRelCaso = wx.Button(id=wxID_DLGCASOBTNTIPORELCASO,
              label='+', name='btnTipoRelCaso', parent=self, pos=wx.Point(128,
              64), size=wx.Size(24, 23), style=0)
        self.btnTipoRelCaso.Bind(wx.EVT_BUTTON, self.OnBtnTipoRelCasoButton,
              id=wxID_DLGCASOBTNTIPORELCASO)

        self.FRCCasoRelTipo = wx.StaticText(id=wxID_DLGCASOFRCCASORELTIPO,
              label='_________________', name='FRCCasoRelTipo', parent=self,
              pos=wx.Point(168, 72), size=wx.Size(200, 40),
              style=wx.ST_NO_AUTORESIZE)

        self.staticCaso = wx.StaticText(id=wxID_DLGCASOSTATICCASO,
              label='staticText2', name='staticCaso', parent=self,
              pos=wx.Point(32, 24), size=wx.Size(336, 40),
              style=wx.ST_NO_AUTORESIZE)

        self.staticText2 = wx.StaticText(id=wxID_DLGCASOSTATICTEXT2,
              label='Con el caso siguente:', name='staticText2', parent=self,
              pos=wx.Point(32, 104), size=wx.Size(103, 13), style=0)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self,
              pos=wx.Point(392, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)
        self.contextHelpButton1.SetBackgroundColour(wx.Colour(202, 192, 183))

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.Resultado=None
        self.ResultadoTipo=None
        self.NoMyself = False
        self.cancelar = True
        
    def OnDlgCasoInitDialog(self, event):
        LlenaCtrlCasos(self.listBoxCasos, NotMyself= self.NoMyself)
        self.staticCaso.SetLabel( "["+str(status.casoActual.id)+"] "+status.casoActual.descripcion)
        event.Skip()



    def OnCasoIsearchText(self, event):
        LlenaCtrlCasos(self.listBoxCasos, filtroIsearch=self.casoIsearch.GetValue(), NotMyself= self.NoMyself)
        event.Skip()

    def OnListBoxCasosListboxDclick(self, event):
        
        
        event.Skip()

    def OnBtnSeleccionarButton(self, event):
        
        self.Resultado = MyClientData(self.listBoxCasos)
        self.cancelar  = False
        self.Close()
        event.Skip()

    def OnBtnCancelarButton(self, event):
        self.Resultado = None
        
        self.Close()
        event.Skip()

    def OnBtnTipoRelCasoButton(self, event):
        self.ResultadoTipo = getTaxonomyTree(self, u"T22", "Tipo de relacion")
        if self.ResultadoTipo:
            self.FRCCasoRelTipo.SetLabel( self.ResultadoTipo.descripcion)
        event.Skip()

    def OnListBoxCasosListbox(self, event):
        event.Skip()
    
def GetCaso(prnt, NoMyself=False, SoloCaso=False):
    dlg = create(prnt)
    LlenaAyuda(dlg, u'DlgCaso')
    cancelar=True
    if SoloCaso:
        dlg.FRCCasoRelTipo.Show(False)
        dlg.btnTipoRelCaso.Show(False)
        dlg.staticText109.Show(False)
    
    dlg.NoMyself = NoMyself
    dlg.ShowModal()
    r, r2, cancelar = dlg.Resultado, dlg.ResultadoTipo, dlg.cancelar
    #dlg.Destroy()

    if SoloCaso:
        return r
    else:
        return r, r2, cancelar
    

if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = create(None)
    try:
        GetCaso(None)
    finally:
        dlg.Destroy()
    app.MainLoop()
