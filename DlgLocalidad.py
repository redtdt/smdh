#-----------------------------------------------------------------------------
# Name:        DlgLocalidad.py
#
#
# RCS-ID:      $Id: DlgLocalidad.py $
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
#Boa:Dialog:DlgLocalidad

import wx
from module2 import LlenaCtrlCategoria, LlenaCtrl, LlenaCtrlTipificacion, LlenaCtrl2, Caso, Acto, status, TesNode, LlenaTree, Localidad
from module2 import LlenaCtrl3, getChoiceValueId, CtrlSelect, getChoiceValue
from module2 import MError, Borrar, LlenaCtrlChildren, nonEmpty, MyClientData, FlushInfo, LlenaAyuda, LlenaCtrlMunicipios
from DLGTaxTree import getTaxonomyTree
import module2
import cnf

session = status.session
provider = wx.SimpleHelpProvider()
wx.HelpProvider_Set(provider)

def create(parent):
    return DlgLocalidad(parent)

[wxID_DLGLOCALIDAD, wxID_DLGLOCALIDADBTNASIGNAR, wxID_DLGLOCALIDADBTNCANCELAR, 
 wxID_DLGLOCALIDADBTNPAIS, wxID_DLGLOCALIDADCONTEXTHELPBUTTON1, 
 wxID_DLGLOCALIDADESTADO, wxID_DLGLOCALIDADLOCALIDAD1, 
 wxID_DLGLOCALIDADMUNICIPIO, wxID_DLGLOCALIDADMUNISEARCH, 
 wxID_DLGLOCALIDADNOTAS_LOCALIDAD, wxID_DLGLOCALIDADNOTAS_MUNICIPIO, 
 wxID_DLGLOCALIDADPAIS, wxID_DLGLOCALIDADSTATICTEXT1, 
 wxID_DLGLOCALIDADSTATICTEXT2, wxID_DLGLOCALIDADSTATICTEXT3, 
 wxID_DLGLOCALIDADSTATICTEXT4, wxID_DLGLOCALIDADSTATICTEXT5, 
 wxID_DLGLOCALIDADSTATICTEXT6, wxID_DLGLOCALIDADSTATICTEXT7, 
 wxID_DLGLOCALIDADSTATICTEXT8, wxID_DLGLOCALIDADTEXTMUNICIPIO, 
] = [wx.NewId() for _init_ctrls in range(21)]

class DlgLocalidad(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DLGLOCALIDAD, name='DlgLocalidad',
              parent=prnt, pos=wx.Point(248, 109), size=wx.Size(814, 399),
              style=wx.DEFAULT_DIALOG_STYLE, title='Localizaci\xf3n')
        self.SetClientSize(wx.Size(798, 363))
        self.SetBackgroundColour(wx.Colour(175, 209, 208))
        self.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'Tahoma'))

        self.staticText1 = wx.StaticText(id=wxID_DLGLOCALIDADSTATICTEXT1,
              label='Pa\xeds', name='staticText1', parent=self, pos=wx.Point(40,
              52), size=wx.Size(32, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_DLGLOCALIDADSTATICTEXT2,
              label='Estado', name='staticText2', parent=self, pos=wx.Point(40,
              88), size=wx.Size(64, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_DLGLOCALIDADSTATICTEXT3,
              label='Municipio', name='staticText3', parent=self,
              pos=wx.Point(40, 128), size=wx.Size(56, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_DLGLOCALIDADSTATICTEXT4,
              label='Localidad', name='staticText4', parent=self,
              pos=wx.Point(40, 272), size=wx.Size(64, 13), style=0)

        self.Estado = wx.Choice(choices=[], id=wxID_DLGLOCALIDADESTADO,
              name='Estado', parent=self, pos=wx.Point(176, 88),
              size=wx.Size(240, 22), style=0)
        self.Estado.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Tahoma'))
        self.Estado.Bind(wx.EVT_CHOICE, self.OnEstadoChoice,
              id=wxID_DLGLOCALIDADESTADO)

        self.Localidad1 = wx.TextCtrl(id=wxID_DLGLOCALIDADLOCALIDAD1,
              name='Localidad1', parent=self, pos=wx.Point(176, 264),
              size=wx.Size(240, 21), style=0, value='')
        self.Localidad1.SetToolTipString('')
        self.Localidad1.SetMaxLength(120)
        self.Localidad1.Bind(wx.EVT_KILL_FOCUS, self.OnLocalidad1KillFocus)
        self.Localidad1.Bind(wx.EVT_TEXT, self.OnLocalidad1Text,
              id=wxID_DLGLOCALIDADLOCALIDAD1)

        self.Notas_municipio = wx.TextCtrl(id=wxID_DLGLOCALIDADNOTAS_MUNICIPIO,
              name='Notas_municipio', parent=self, pos=wx.Point(448, 144),
              size=wx.Size(240, 21), style=0, value='')
        self.Notas_municipio.SetToolTipString('')
        self.Notas_municipio.SetMaxLength(120)

        self.Notas_localidad = wx.TextCtrl(id=wxID_DLGLOCALIDADNOTAS_LOCALIDAD,
              name='Notas_localidad', parent=self, pos=wx.Point(448, 264),
              size=wx.Size(240, 21), style=0, value='')
        self.Notas_localidad.SetToolTipString('')
        self.Notas_localidad.SetMaxLength(120)

        self.staticText5 = wx.StaticText(id=wxID_DLGLOCALIDADSTATICTEXT5,
              label='- Notas -', name='staticText5', parent=self,
              pos=wx.Point(536, 128), size=wx.Size(48, 13), style=0)

        self.staticText6 = wx.StaticText(id=wxID_DLGLOCALIDADSTATICTEXT6,
              label='- Notas -', name='staticText6', parent=self,
              pos=wx.Point(536, 248), size=wx.Size(56, 13), style=0)

        self.btnPais = wx.Button(id=wxID_DLGLOCALIDADBTNPAIS, label='+',
              name='btnPais', parent=self, pos=wx.Point(80, 47),
              size=wx.Size(24, 23), style=0)
        self.btnPais.Bind(wx.EVT_BUTTON, self.OnBtnPais,
              id=wxID_DLGLOCALIDADBTNPAIS)

        self.Municipio = wx.ListBox(choices=[], id=wxID_DLGLOCALIDADMUNICIPIO,
              name='Municipio', parent=self, pos=wx.Point(176, 168),
              size=wx.Size(240, 80), style=0)
        self.Municipio.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnMunicipioListboxDclick, id=wxID_DLGLOCALIDADMUNICIPIO)

        self.MuniSearch = wx.TextCtrl(id=wxID_DLGLOCALIDADMUNISEARCH,
              name='MuniSearch', parent=self, pos=wx.Point(176, 144),
              size=wx.Size(240, 21), style=0, value='')
        self.MuniSearch.Bind(wx.EVT_TEXT, self.OnMuniSearchText,
              id=wxID_DLGLOCALIDADMUNISEARCH)

        self.Pais = wx.TextCtrl(id=wxID_DLGLOCALIDADPAIS, name='Pais',
              parent=self, pos=wx.Point(176, 48), size=wx.Size(240, 21),
              style=0, value='')
        self.Pais.SetEditable(False)

        self.staticText7 = wx.StaticText(id=wxID_DLGLOCALIDADSTATICTEXT7,
              label='(seleccionar)', name='staticText7', parent=self,
              pos=wx.Point(99, 168), size=wx.Size(69, 16), style=0)

        self.staticText8 = wx.StaticText(id=wxID_DLGLOCALIDADSTATICTEXT8,
              label='(buscar)', name='staticText8', parent=self,
              pos=wx.Point(120, 144), size=wx.Size(48, 13), style=0)

        self.textMunicipio = wx.TextCtrl(id=wxID_DLGLOCALIDADTEXTMUNICIPIO,
              name='textMunicipio', parent=self, pos=wx.Point(176, 120),
              size=wx.Size(240, 21), style=0, value='')
        self.textMunicipio.SetToolTipString('')
        self.textMunicipio.SetEditable(False)

        self.btnAsignar = wx.Button(id=wxID_DLGLOCALIDADBTNASIGNAR,
              label='Seleccionar', name='btnAsignar', parent=self,
              pos=wx.Point(240, 312), size=wx.Size(75, 23), style=0)
        self.btnAsignar.Bind(wx.EVT_BUTTON, self.OnBtnAsignarButton,
              id=wxID_DLGLOCALIDADBTNASIGNAR)

        self.btnCancelar = wx.Button(id=wxID_DLGLOCALIDADBTNCANCELAR,
              label='Cancelar', name='btnCancelar', parent=self,
              pos=wx.Point(448, 312), size=wx.Size(75, 23), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_DLGLOCALIDADBTNCANCELAR)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self,
              pos=wx.Point(768, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.retcode= False
        self.Edo = None
        LlenaAyuda(self, u'DlgLocalidad')
        if cnf.OSlinux:
            module2.choiceFix(self, __name__)

    def OnEstadoChoice(self, event):
        self.Edo = self.Estado.GetClientData(self.Estado.Selection)
        if self.Edo:
            LlenaCtrlMunicipios(self.Municipio, self.Edo)
        else:
            self.Municipio.Clear()
        
        event.Skip()

    def OnBtnPais(self, event):
        
        pais = getTaxonomyTree(self, u"T15", u"Pa\xeds")
        if pais:
           self.Pais.SetValue(pais.descripcion)
           self.ObjetoActual.Pais = pais
           
           mostrarEdo = pais.descripcion == status.localCountry
           AjustaLocalidadSegunPais(self, mostrarEdo)
        
        event.Skip()
    ObjetoActual = None

    def OnMunicipioKeyDown(self, event):
        
        event.Skip()

    def OnMuniSearchText(self, event):
        texto = self.MuniSearch.GetValue().capitalize()
        #print "texto 1", texto
        #texto = module2.Sortable(texto, trans=module2.transWildChar)
        #print "texto 2", texto
        Edo = self.Estado.GetClientData(self.Estado.Selection)
        if Edo:
            if texto:
                LlenaCtrlChildren(self.Municipio, Edo, orden="descripcion", expr=texto)
            else:
                LlenaCtrlMunicipios(self.Municipio, Edo)
        
        event.Skip()

    def OnMunicipioListboxDclick(self, event):
        d=MyClientData(event)
        if d:
             self.textMunicipio.SetLabel( d.descripcion)
             self.Notas_municipio.Enable()
        else:
             self.textMunicipio.SetLabel( '')
            # confirmar
             self.Notas_municipio.SetValue('')
             self.Notas_municipio.Enable(False)
             
             
        event.Skip()

    def OnBtnAsignarButton(self, event):
        self.retcode= True
        if not self.Localidad1.GetValue(): self.Notas_localidad.SetValue('')
        if self.Municipio.Selection < 1: self.Notas_municipio.SetValue('')
        
        self.Close()
        event.Skip()

    def OnBtnCancelarButton(self, event):
        self.retcode= False
        self.Close()
        
        event.Skip()

    def OnLocalidad1KillFocus(self, event):
        if self.Localidad1.GetValue():
            self.Notas_localidad.Enable(True)
        else:
            self.Notas_localidad.Enable(False)
            self.Notas_localidad.Clear()
            
            
        event.Skip()

    def OnLocalidad1Text(self, event):
        if self.Localidad1.GetValue():
            self.Notas_localidad.Enable(True)
        else:
            self.Notas_localidad.Enable(False)
            self.Notas_localidad.Clear()
        event.Skip()


def AjustaLocalidadSegunPais(self, toShow):
    
    ctrls = ['staticText2', 'Estado', 'staticText3', 'textMunicipio', 'staticText8', 'MuniSearch', 
             'staticText5', 'Notas_municipio', 'staticText7', 'Municipio']
    for ctrlName in ctrls:
        ctrl = getattr(self, ctrlName)
        ctrl.Show(toShow)
    
def LocalidadMaint(prnt, Loc, nuevo=False):
    
    dlg = DlgLocalidad(prnt)
    dlg.ObjetoActual  = Loc
    EdoSeleccionar = status.EdoDef if nuevo else Loc.Estado
    LlenaCtrlCategoria(dlg.Estado, u"T63", Tselected=EdoSeleccionar)
    MpoDefDescripcion = status.MpoDef.descripcion if status.MpoDef else None
    if Loc.Estado or MpoDefDescripcion:
       seleccionMunicipio = Loc.Municipio.descripcion if Loc.Municipio else MpoDefDescripcion
       LlenaCtrlMunicipios(dlg.Municipio, EdoSeleccionar, selected=seleccionMunicipio)
    if Loc.Municipio:
       dlg.textMunicipio.SetLabel( Loc.Municipio.descripcion)
       dlg.Notas_municipio.SetValue(nonEmpty(Loc.notas_municipio))
    else:
        dlg.Notas_municipio.Enable(False)
        if MpoDefDescripcion and nuevo:
            dlg.textMunicipio.SetLabel( MpoDefDescripcion)
            dlg.Notas_municipio.Enable()
       
    if Loc.Pais:   
        dlg.Pais.SetValue(Loc.Pais.descripcion)
        mostrarEdo = Loc.Pais.descripcion == status.localCountry
        AjustaLocalidadSegunPais(dlg, mostrarEdo)
    else:
        AjustaLocalidadSegunPais(dlg, False)
        
    dlg.Localidad1.SetValue(nonEmpty(Loc.localidad))
    if Loc.localidad:
        dlg.Notas_localidad.SetValue(nonEmpty(Loc.notas_localidad))
        dlg.Notas_localidad.Enable()
    else:
        dlg.Notas_localidad.Enable(False)
    
    dlg.Notas_municipio.SetValue(nonEmpty(Loc.notas_municipio))
    
    
    
    dlg.ShowModal()
    if dlg.retcode:
        paisLocal = Loc.Pais.descripcion == status.localCountry
        Loc.localidad = dlg.Localidad1.GetValue()
        Loc.notas_localidad = dlg.Notas_localidad.GetValue()

        if paisLocal:
            i = dlg.Municipio.Selection
            if dlg.Municipio.Selection > -1:
                Loc.Municipio = dlg.Municipio.GetClientData(dlg.Municipio.Selection)
            else:
                Loc.Municipio = None
            if dlg.Estado.Selection > -1:
                Loc.Estado = dlg.Estado.GetClientData(dlg.Estado.Selection)
                
            
            Loc.notas_municipio = dlg.Notas_municipio.GetValue()
        else:
            Loc.Municipio = None
            Loc.Estado = None
            
            Loc.notas_municipio = ''
            
            
            
        
        if Loc.localidad or Loc.Municipio or Loc.Pais:
            session.add(Loc)
            FlushInfo(id=100)
            #dlg.Destroy()
            return True
        else:
            MError(prnt, u"No se guard\xf3 informaci\xf3n")
            return False
    else:
        return False
            
        
    
      


