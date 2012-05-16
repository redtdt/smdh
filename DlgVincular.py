#-----------------------------------------------------------------------------
# Name:        DlgVincular.py
#
#
# RCS-ID:      $Id: DlgVincular.py $
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
#Boa:Dialog:Dialog1

import wx
from module2 import *
import module2
from DlgAltaPersona import DatosAltaPersona

session = status.session

TipoRelacion = 0

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BTNCANCELAR, wxID_DIALOG1BTNGUARDAR, 
 wxID_DIALOG1CONTEXTHELPBUTTON1, wxID_DIALOG1ISEARCH, 
 wxID_DIALOG1LISTBOXPERSONABROWSER, wxID_DIALOG1NUEVAPERSONA, 
 wxID_DIALOG1STATICBOX1, wxID_DIALOG1STATICPERSONA, 
 wxID_DIALOG1STATICPERSONA2, wxID_DIALOG1STATICTDESCRIPCION, 
 wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICTEXT2, wxID_DIALOG1TDB1, 
 wxID_DIALOG1TDB2, wxID_DIALOG1TEXTDESCRIPCION, wxID_DIALOG1TREECTRLVINCULOS, 
] = [wx.NewId() for _init_ctrls in range(17)]


class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(456, 44), size=wx.Size(722, 551),
              style=wx.DEFAULT_DIALOG_STYLE, title='Dato biogr\xe1fico')
        self.SetClientSize(wx.Size(706, 515))
        self.SetBackgroundColour(wx.Colour(205, 185, 180))
        self.Bind(wx.EVT_INIT_DIALOG, self.OnDialogInit)
        self.Bind(wx.EVT_CLOSE, self.OnDialog1Close)

        self.listBoxPersonaBrowser = wx.ListBox(choices=[],
              id=wxID_DIALOG1LISTBOXPERSONABROWSER,
              name='listBoxPersonaBrowser', parent=self, pos=wx.Point(368, 264),
              size=wx.Size(288, 192), style=wx.HSCROLL)
        self.listBoxPersonaBrowser.SetToolTipString('Elige aqui la persona relacionada, cuando aplique')
        self.listBoxPersonaBrowser.Enable(False)
        self.listBoxPersonaBrowser.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnListBoxPersonaBrowserDclick,
              id=wxID_DIALOG1LISTBOXPERSONABROWSER)
        self.listBoxPersonaBrowser.Bind(wx.EVT_LISTBOX,
              self.OnListBoxPersonaBrowserListbox,
              id=wxID_DIALOG1LISTBOXPERSONABROWSER)

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label='Con qu\xe9 persona o entidad se relaciona',
              name='staticText1', parent=self, pos=wx.Point(368, 216),
              size=wx.Size(190, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,
              label='Relacionada como', name='staticText2', parent=self,
              pos=wx.Point(8, 224), size=wx.Size(86, 13), style=0)

        self.treeCtrlVinculos = wx.TreeCtrl(id=wxID_DIALOG1TREECTRLVINCULOS,
              name='treeCtrlVinculos', parent=self, pos=wx.Point(8, 264),
              size=wx.Size(344, 192), style=wx.TR_HAS_BUTTONS | wx.TR_MULTIPLE)
        self.treeCtrlVinculos.SetAutoLayout(True)
        self.treeCtrlVinculos.SetThemeEnabled(False)
        self.treeCtrlVinculos.SetToolTipString(u'Elige el tipo de relaci\xf3n, cuando aplique\nUsa doble clic para seleccionar')
        self.treeCtrlVinculos.Enable(False)
        self.treeCtrlVinculos.Bind(wx.EVT_LEFT_DCLICK,
              self.OnTreeCtrlVinculosLeftDclick)
        self.treeCtrlVinculos.Bind(wx.EVT_TREE_SEL_CHANGED,
              self.OnTreeCtrlVinculosTreeSelChanged,
              id=wxID_DIALOG1TREECTRLVINCULOS)
        self.treeCtrlVinculos.Bind(wx.EVT_LEFT_DOWN,
              self.OnTreeCtrlVinculosLeftDown)

        self.staticTDescripcion = wx.StaticText(id=wxID_DIALOG1STATICTDESCRIPCION,
              label='Descripci\xf3n', name='staticTDescripcion', parent=self,
              pos=wx.Point(8, 120), size=wx.Size(54, 13), style=0)

        self.textDescripcion = wx.TextCtrl(id=wxID_DIALOG1TEXTDESCRIPCION,
              name='textDescripcion', parent=self, pos=wx.Point(8, 144),
              size=wx.Size(648, 24), style=0, value='')
        self.textDescripcion.SetToolTipString('Describe aqui el detalle biografico, cuando aplique')

        self.staticPersona = wx.StaticText(id=wxID_DIALOG1STATICPERSONA,
              label='__', name='staticPersona', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(648, 32), style=wx.ST_NO_AUTORESIZE)
        self.staticPersona.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.isearch = wx.TextCtrl(id=wxID_DIALOG1ISEARCH, name='isearch',
              parent=self, pos=wx.Point(368, 240), size=wx.Size(184, 21),
              style=0, value='')
        self.isearch.SetToolTipString('Buscar persona')
        self.isearch.Enable(False)
        self.isearch.Bind(wx.EVT_TEXT_ENTER, self.OnIsearchTextEnter,
              id=wxID_DIALOG1ISEARCH)
        self.isearch.Bind(wx.EVT_TEXT, self.OnIsearchText,
              id=wxID_DIALOG1ISEARCH)

        self.nuevaPersona = wx.Button(id=wxID_DIALOG1NUEVAPERSONA,
              label='Nueva persona', name='nuevaPersona', parent=self,
              pos=wx.Point(560, 240), size=wx.Size(96, 23), style=0)
        self.nuevaPersona.Enable(False)
        self.nuevaPersona.Bind(wx.EVT_BUTTON, self.OnNuevaPersonaButton,
              id=wxID_DIALOG1NUEVAPERSONA)

        self.btnGuardar = wx.Button(id=wxID_DIALOG1BTNGUARDAR,
              label='Seleccionar', name='btnGuardar', parent=self,
              pos=wx.Point(368, 464), size=wx.Size(75, 23), style=0)
        self.btnGuardar.Bind(wx.EVT_BUTTON, self.OnBtnGuardarButton,
              id=wxID_DIALOG1BTNGUARDAR)

        self.btnCancelar = wx.Button(id=wxID_DIALOG1BTNCANCELAR,
              label='Cancelar', name='btnCancelar', parent=self,
              pos=wx.Point(584, 464), size=wx.Size(75, 23), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_DIALOG1BTNCANCELAR)

        self.staticPersona2 = wx.StaticText(id=wxID_DIALOG1STATICPERSONA2,
              label='      ', name='staticPersona2', parent=self,
              pos=wx.Point(8, 184), size=wx.Size(648, 32),
              style=wx.ST_NO_AUTORESIZE)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self,
              pos=wx.Point(680, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)

        self.staticBox1 = wx.StaticBox(id=wxID_DIALOG1STATICBOX1,
              label='Tipo de dato biogr\xe1fico', name='staticBox1',
              parent=self, pos=wx.Point(8, 56), size=wx.Size(296, 64), style=0)

        self.TDB1 = wx.CheckBox(id=wxID_DIALOG1TDB1,
              label='Sin relaci\xf3n con otra persona', name='TDB1',
              parent=self, pos=wx.Point(24, 72), size=wx.Size(192, 13),
              style=0)
        self.TDB1.SetValue(True)
        self.TDB1.Bind(wx.EVT_CHECKBOX, self.OnTDB1Checkbox,
              id=wxID_DIALOG1TDB1)

        self.TDB2 = wx.CheckBox(id=wxID_DIALOG1TDB2,
              label='Relacionado con otra persona', name='TDB2', parent=self,
              pos=wx.Point(24, 96), size=wx.Size(192, 13), style=0)
        self.TDB2.SetValue(False)
        self.TDB2.Bind(wx.EVT_CHECKBOX, self.OnTDB1Checkbox,
              id=wxID_DIALOG1TDB2)

    def __init__(self, parent):
        self._init_ctrls(parent)
        LlenaAyuda(self, u'DatoBio')
        global TipoRelacion
        TipoRelacion = 0

    def OnDialogInit(self, event):
         LlenaPersonas(self.listBoxPersonaBrowser, excepto=status.personaActual)
         #ListaPersonas = session.query(Persona)
         #LlenaCtrl3(self.listBoxPersonaBrowser, [(i,i.Descriptor()) for i in ListaPersonas])
         rootElement = QueryTesNode.filter_by(name=u'T21')[0]
         LlenaTree(self.treeCtrlVinculos, None, rootElement, VOrden='C')
         self.treeCtrlVinculos.Expand(self.treeCtrlVinculos.GetRootItem())
         self.persona_a_vincular  = None
         if status.personaActual:
             self.staticPersona.SetLabel('['+str(status.personaActual.id)+'] '+ status.personaActual.Descriptor())
             self.staticPersona2.SetLabel( '['+str(status.personaActual.id)+'] '+ status.personaActual.Descriptor())
         event.Skip()


    tipoActual = None
    def OnButtonGuarda(self, event):
        
        self.Close()
        
        event.Skip()

    def OnTreeCtrlVinculosLeftDclick(self, event):
        return
        
        s = self.treeCtrlVinculos.GetSelections()[0]
        
        self.tipoActual = self.treeCtrlVinculos.GetPyData(s)
        if status.personaActual and self.persona_a_vincular and self.tipoActual:
            self.buttonGuardar.Enable()
            
        
        event.Skip()

    def OnListBoxPersonaBrowserDclick(self, event):
         
         P = self.listBoxPersonaBrowser.GetClientData(self.listBoxPersonaBrowser.Selection)
         if P == status.personaActual:
            MError(self, u'No es posible establecer una relaci\xf3n de una persona consigo misma')
         else:
            self.persona_a_vincular = P
         event.Skip()

    def OnListBoxPersonaBrowserListbox(self, event):
        self.persona_a_vincular = self.listBoxPersonaBrowser.GetClientData(self.listBoxPersonaBrowser.Selection)
        event.Skip()

    def OnTreeCtrlVinculosTreeSelChanged(self, event):
        item = self.treeCtrlVinculos.GetSelections()
        if item:
            item = item[0]
            self.tipoActual = self.treeCtrlVinculos.GetPyData(item)
        
        
        

        event.Skip()

    def OnTreeCtrlVinculosLeftDown(self, event):

        event.Skip()



    def OnDialog1Close(self, event):
        
        
        event.Skip()

    def OnIsearchTextEnter(self, event):

        event.Skip()

    def OnIsearchText(self, event):
        ctrl = event.GetEventObject()
        expr = ctrl.GetValue()
        expr = Sortable(expr, trans=module2.transWildChar)
        
        LlenaPersonas(self.listBoxPersonaBrowser, filtro2=expr, excepto=status.personaActual)
        event.Skip()

    def OnNuevaPersonaButton(self, event):
        nombre, apellido, indiv , res= DatosAltaPersona(self)
        if res:
            if ExistePersona(nombre, apellido, indiv):
                MError(self, u"Ya existe una persona con este nombre")
            else:
                if apellido != '':
                    P=Persona(nombre, apellido, indiv=indiv)
                    session.add(P)
                    FlushInfo(id=234)
                    LlenaPersonas(self.listBoxPersonaBrowser, Pselected=P)
                    status.ReloadPersona = True
                    self.persona_a_vincular = P
                    
                #ListaPersonas = session.query(Persona)
                #LlenaCtrl3(self.listBoxPersonaBrowser, [(i,i.Descriptor()) for i in ListaPersonas])
        event.Skip()

    def OnBtnGuardarButton(self, event):
        GuardaVinculo(self)
        self.Close()
        event.Skip()

    def OnBtnCancelarButton(self, event):
        self.Close()
        event.Skip()

    def OnTDB1Checkbox(self, event):
        global TipoRelacion
        ctrl = event.GetEventObject()
        for ctrlName in ['TDB1','TDB2']:
            c = getattr(self, ctrlName)
            c.SetValue(False)
        ctrl.SetValue(True)
        
        TipoRelacion = 0 if ctrl == self.TDB1 else 1
        
        s = self
        camposNoRelacion=[s.staticTDescripcion, s.textDescripcion]
        camposRelacion=[s.staticText1, s.staticText2, s.listBoxPersonaBrowser, 
                        s.treeCtrlVinculos, s.nuevaPersona, s.isearch]
        
        enableNoRelacion = TipoRelacion == 0
            
        for i in camposNoRelacion:
                i.Enable(enableNoRelacion)
        for i in camposRelacion:
                i.Enable(not enableNoRelacion)
        
        
        event.Skip()

def GuardaVinculo(self, guardar=True):
    global TipoRelacion
    if TipoRelacion == 0:
        if self.textDescripcion.GetValue():
            V=Persona_Vinculo(status.personaActual)
            V.descripcion = self.textDescripcion.GetValue()
            session.add(V)
            status.vinculoActual = V
            FlushInfo(id=101)
        else:
            MError(self, 'No hay datos suficientes para establecer este dato biogr\xe1fico. A\xfan no tiene una descripci\xf3n')
    else:
        
        if status.personaActual and self.persona_a_vincular and self.tipoActual:
                Vincula(status.personaActual, self.persona_a_vincular, self.tipoActual)
                        
        else:
                MError(self, u'No hay datos suficientes para establecer la relaci\xf3n. Verifica que asignaste el Tipo de relaci\xf3n y que seleccionaste una persona')
