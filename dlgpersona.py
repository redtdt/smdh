#-----------------------------------------------------------------------------
# Name:        dlgpersona.py
#
#
# RCS-ID:      $Id: dlgpersona.py $
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
#Boa:Dialog:DlgVictima

import wx
import module2
from module2 import status, Persona, ExistePersona, MError, BorraPersona, LlenaAyuda, LimpiaString
from DlgAltaPersona import DlgAltaPersona

session = status.session

def create(parent):
    return DlgVictima(parent)

[wxID_DLGVICTIMA, wxID_DLGVICTIMAASIGNARPERSONA, wxID_DLGVICTIMABTNCANCELAR, 
 wxID_DLGVICTIMABUTTON1, wxID_DLGVICTIMACHKINVERTIR, 
 wxID_DLGVICTIMACONTEXTHELPBUTTON1, wxID_DLGVICTIMALISTBOXPERSONA, 
 wxID_DLGVICTIMAPERSONAISEARCH, wxID_DLGVICTIMARADIOBOXTIPOPERSONA, 
] = [wx.NewId() for _init_ctrls in range(9)]

class DlgVictima(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DLGVICTIMA, name='DlgVictima',
              parent=prnt, pos=wx.Point(319, 190), size=wx.Size(741, 507),
              style=wx.DEFAULT_DIALOG_STYLE, title='Seleccionar una persona')
        self.SetClientSize(wx.Size(725, 471))
        self.SetForegroundColour(wx.Colour(255, 255, 255))
        self.SetBackgroundColour(wx.Colour(128, 128, 64))
        self.Bind(wx.EVT_ACTIVATE, self.OnDialog2Activate)
        self.Bind(wx.EVT_CLOSE, self.OnDlgVictimaClose)

        self.listBoxPersona = wx.ListBox(choices=[],
              id=wxID_DLGVICTIMALISTBOXPERSONA, name='listBoxPersona',
              parent=self, pos=wx.Point(104, 48), size=wx.Size(528, 336),
              style=wx.HSCROLL)
        self.listBoxPersona.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnListBoxPersonaDclick, id=wxID_DLGVICTIMALISTBOXPERSONA)
        self.listBoxPersona.Bind(wx.EVT_LISTBOX, self.OnListBoxPersonaListbox,
              id=wxID_DLGVICTIMALISTBOXPERSONA)

        self.button1 = wx.Button(id=wxID_DLGVICTIMABUTTON1,
              label='Nueva persona', name='button1', parent=self,
              pos=wx.Point(320, 432), size=wx.Size(96, 23), style=0)
        self.button1.Show(False)
        self.button1.Bind(wx.EVT_BUTTON, self.OnBtnAltaPersona,
              id=wxID_DLGVICTIMABUTTON1)

        self.radioBoxTipoPersona = wx.RadioBox(choices=['Individual',
              'Colectiva', 'Todas'], id=wxID_DLGVICTIMARADIOBOXTIPOPERSONA,
              label='Mostrar', majorDimension=1, name='radioBoxTipoPersona',
              parent=self, pos=wx.Point(8, 16), size=wx.Size(88, 80),
              style=wx.RA_SPECIFY_COLS)
        self.radioBoxTipoPersona.SetSelection(2)
        self.radioBoxTipoPersona.Bind(wx.EVT_RADIOBOX,
              self.OnRadioBoxTipoPersona,
              id=wxID_DLGVICTIMARADIOBOXTIPOPERSONA)

        self.personaIsearch = wx.TextCtrl(id=wxID_DLGVICTIMAPERSONAISEARCH,
              name='personaIsearch', parent=self, pos=wx.Point(104, 24),
              size=wx.Size(528, 21), style=0, value='')
        self.personaIsearch.Bind(wx.EVT_TEXT, self.OnPersonaIsearchText,
              id=wxID_DLGVICTIMAPERSONAISEARCH)

        self.asignarPersona = wx.Button(id=wxID_DLGVICTIMAASIGNARPERSONA,
              label='Seleccionar', name='asignarPersona', parent=self,
              pos=wx.Point(152, 392), size=wx.Size(80, 23), style=0)
        self.asignarPersona.Bind(wx.EVT_BUTTON, self.OnAsignarPersonaButton,
              id=wxID_DLGVICTIMAASIGNARPERSONA)

        self.btnCancelar = wx.Button(id=wxID_DLGVICTIMABTNCANCELAR,
              label='Cancelar', name='btnCancelar', parent=self,
              pos=wx.Point(488, 392), size=wx.Size(75, 23), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_DLGVICTIMABTNCANCELAR)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self,
              pos=wx.Point(696, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)

        self.chkInvertir = wx.CheckBox(id=wxID_DLGVICTIMACHKINVERTIR,
              label='Invertir condici\xf3n', name='chkInvertir', parent=self,
              pos=wx.Point(104, 8), size=wx.Size(112, 13), style=0)
        self.chkInvertir.SetValue(False)

    def __init__(self, parent):
        self.excepto=None
        self._init_ctrls(parent)
        self.cancelar = True
        self.personaIsearch.SetFocus()
        
        
    GLBLi = None
    def OnBtnAltaPersona(self, event):
        
        status.personaReciente = None
        status.personaActual = Persona('','')
        s = self.radioBoxTipoPersona.GetStringSelection()
        dlg=DlgAltaPersona(self)
        if s == 'Colectiva':
            dlg.radioBoxIndividual.SetSelection(1)
        else:
            dlg.radioBoxIndividual.SetSelection(0)
        
        dlg.ShowModal()
        resultadoApellido = dlg.TxtApellido.GetValue()
        resultadoApellido = LimpiaString(resultadoApellido)
        if not(resultadoApellido):
            status.personaActual = None
            self.aplicaFiltro()
            if s == 'Colectiva':
                MError(self, "No se puede crear una persona colectiva sin nombre")
                    
            else:
                MError(self, "No se puede crear una persona sin apellido")
                    
            return
        status.personaActual.apellido = resultadoApellido
        status.personaActual.nombre   = dlg.TxtNombrePersona.GetValue()
        status.personaActual.nombre   = LimpiaString(status.personaActual.nombre)
        IndivChoice = dlg.radioBoxIndividual.GetStringSelection()
        if IndivChoice == 'Individual':
            status.personaActual.esindividual = 1
        else:
            status.personaActual.esindividual = 0
        if dlg.TxtApellido.GetValue() != '':
            if not ExistePersona(status.personaActual.nombre, status.personaActual.apellido, status.personaActual.esindividual == 1):
                
                
                session.add(status.personaActual)
                session.flush()
                
                self.GLBLi = status.personaActual
                status.personaReciente = status.personaActual
                
            else:
                MError(self, "Ya existe una persona con este nombre")
        status.personaActual = None   
        
        module2.LlenaPersonas(self.listBoxPersona)
        if status.personaReciente:
            s=status.personaReciente.Descriptor()
            self.listBoxPersona.SetStringSelection(s)
        
        #self.aplicaFiltro()
        dlg.Destroy()
        #self.EndModal(wx.ID_OK)
        
        event.Skip()

    def OnDialog2Activate(self, event):
        
        event.Skip()

    def OnListBoxPersonaDclick(self, event):
        #i = self.listBoxPersona.Selection
        #self.GLBLi = self.listBoxPersona.GetClientData(i)
        
        #self.EndModal(wx.ID_OK)
        event.Skip()
    def GetData(self):
        return self.GLBLi
        
#        return self.listBox1.GetClientData(i)

    def OnRadioBoxTipoPersona(self, event):
        
        self.aplicaFiltro()
        event.Skip()
    def aplicaFiltro(self):
        s= self.radioBoxTipoPersona.GetStringSelection()
        module2.LlenaPersonas(self.listBoxPersona, filtro=s)

    def OnListBoxPersonaListbox(self, event):
        event.Skip()

    def OnPersonaIsearchText(self, event):
        a = module2.Sortable(self.personaIsearch.GetValue(), trans=module2.transWildChar)
        module2.LlenaPersonas(self.listBoxPersona, filtro2=a)
        
        self.button1.Show(len(a) > 2)
        
            
        event.Skip()

    def OnAsignarPersonaButton(self, event):
        self.GLBLi = None
        i = self.listBoxPersona.Selection
        if i > -1:
            self.GLBLi = self.listBoxPersona.GetClientData(i)
        self.cancelar = False
        self.EndModal(wx.ID_OK)
        event.Skip()

    def OnBtnCancelarButton(self, event):
        BorraPersona(status.personaReciente)
        self.cancelar = True
        self.EndModal(wx.ID_CANCEL)
        event.Skip()

    def OnDlgVictimaClose(self, event):
        #self.cancelar = True
        event.Skip()
def PersonaDlg(self, help=None, excepto=None, search=False, invertir=False):
        dlg=DlgVictima(self)
        module2.LlenaPersonas(dlg.listBoxPersona, excepto=excepto)
        dlg.listBoxPersona.SetSelection(-1)
        LlenaAyuda(dlg, help)
        
        dlg.chkInvertir.Show(search)
        dlg.chkInvertir.SetValue(invertir)
        
            
            
        dlg.ShowModal()
        ret = dlg.GetReturnCode()
        if ret == wx.ID_OK:
            result =dlg.GetData()
        else:
            result =None
        dlg.Destroy()
        if search:
            return result, dlg.chkInvertir.GetValue(), dlg.cancelar
        return result
        
            
