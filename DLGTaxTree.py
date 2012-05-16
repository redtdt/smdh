#-----------------------------------------------------------------------------
# Name:        DLGTaxTree.py
#
#
# RCS-ID:      $Id: DLGTaxTree.py $
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
#Boa:Dialog:DialogTaxTree

import wx
import re
from module2 import LlenaTree, status, TesNode, MError, QueryTesNode, LlenaAyuda
from configmodule import getVOrden

session = status.session

def create(parent):
    return DialogTaxTree(parent)

[wxID_DIALOGTAXTREE, wxID_DIALOGTAXTREEBTNCANCELAR, 
 wxID_DIALOGTAXTREEBUTTONASIGNAR, wxID_DIALOGTAXTREECHECKBOXINVERTIR, 
 wxID_DIALOGTAXTREECONTEXTHELPBUTTON1, wxID_DIALOGTAXTREESTATICTEXTNOTAS, 
 wxID_DIALOGTAXTREETREECTRL1, 
] = [wx.NewId() for _init_ctrls in range(7)]

class DialogTaxTree(wx.Dialog):

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOGTAXTREE, name='DialogTaxTree',
              parent=prnt, pos=wx.Point(49, 17), size=wx.Size(592, 543),
              style=wx.DEFAULT_DIALOG_STYLE, title='Vocabularios')
        self.SetClientSize(wx.Size(576, 507))
        self.SetBackgroundColour(wx.Colour(225, 227, 157))
        self.Bind(wx.EVT_CLOSE, self.OnDialogTaxTreeClose)

        self.treeCtrl1 = wx.TreeCtrl(id=wxID_DIALOGTAXTREETREECTRL1,
              name='treeCtrl1', parent=self, pos=wx.Point(48, 40),
              size=wx.Size(488, 320), style=wx.TR_HAS_BUTTONS | wx.TR_MULTIPLE)
        self.treeCtrl1.SetToolTipString('')
        self.treeCtrl1.Bind(wx.EVT_TREE_SEL_CHANGED,
              self.OnTreeCtrl1TreeSelChanged, id=wxID_DIALOGTAXTREETREECTRL1)

        self.buttonAsignar = wx.Button(id=wxID_DIALOGTAXTREEBUTTONASIGNAR,
              label='Seleccionar', name='buttonAsignar', parent=self,
              pos=wx.Point(176, 472), size=wx.Size(88, 23), style=0)
        self.buttonAsignar.Bind(wx.EVT_BUTTON, self.OnButtonAsignar,
              id=wxID_DIALOGTAXTREEBUTTONASIGNAR)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self,
              pos=wx.Point(544, 0), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)

        self.staticTextNotas = wx.TextCtrl(id=wxID_DIALOGTAXTREESTATICTEXTNOTAS,
              name='staticTextNotas', parent=self, pos=wx.Point(48, 368),
              size=wx.Size(488, 88), style=wx.TE_MULTILINE, value='')
        self.staticTextNotas.SetEditable(False)

        self.checkBoxInvertir = wx.CheckBox(id=wxID_DIALOGTAXTREECHECKBOXINVERTIR,
              label='Invertir condici\xf3n', name='checkBoxInvertir',
              parent=self, pos=wx.Point(48, 8), size=wx.Size(112, 13), style=0)
        self.checkBoxInvertir.SetValue(False)
        self.checkBoxInvertir.Show(False)
        self.checkBoxInvertir.SetToolTipString('')
        self.checkBoxInvertir.Bind(wx.EVT_CHECKBOX,
              self.OnCheckBoxInvertirCheckbox,
              id=wxID_DIALOGTAXTREECHECKBOXINVERTIR)

        self.btnCancelar = wx.Button(id=wxID_DIALOGTAXTREEBTNCANCELAR,
              label='Cancelar', name='btnCancelar', parent=self,
              pos=wx.Point(320, 472), size=wx.Size(75, 23), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_DIALOGTAXTREEBTNCANCELAR)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.tipoActual = None
        self.tiposActuales = None
        self.cancelar = True
        self.help = None
        
    def OnLeftDclick(self, event):
        pt = event.GetPosition();
        item, flags = self.treeCtrl1.HitTest(pt)
        tipo = self.treeCtrl1.GetPyData(item)
        self.tipoActual = None
        if not (tipo.children):
            self.tipoActual = tipo
            self.Close()
        event.Skip()

    def OnButtonAsignar(self, event):
        self.tipoActual = None
        items = self.treeCtrl1.GetSelections()
        if items:
            item = items[0]
            
            self.tiposActuales = [self.treeCtrl1.GetPyData(i) for i in items]
            
            tipo = self.treeCtrl1.GetPyData(item)
            
    #        if not (tipo.children):
    
            self.tipoActual = tipo
            self.Close()
        else:
            if self.search:
                self.tiposActuales = []
                self.tipoActual = None
                self.Close()
        self.cancelar = False
            

        event.Skip()

    def OnDialogTaxTreeClose(self, event):
        #self.tipoActual = None
        
        
        event.Skip()

    def OnTreeCtrl1TreeSelChanged(self, event):
        items = self.treeCtrl1.GetSelections()
        if items:
            item = items[0]
            tipo = self.treeCtrl1.GetPyData(item)
            self.staticTextNotas.SetValue('')
            if tipo.notas:
                self.staticTextNotas.SetValue(tipo.notas)
                
        event.Skip()

    def OnBtnCancelarButton(self, event):
        self.tipoActual = None
        self.cancelar = True
        self.Close()
        event.Skip()

    def OnCheckBoxInvertirCheckbox(self, event):
        self.treeCtrl1.SetFocus()
        event.Skip()


    
def NOP():
    return    
def getTaxonomyTree(prnt, type, title, Pattern=None, ctrl=None, id=None, poli=None, VOrden=None, deep=None, help=u'', search=False):
        #if type in status.dlg.keys() and not search and type not in status.dlgExcepciones:
        

        if type in status.dlg[search].keys() and type not in status.dlgExcepciones:
            dlg = status.dlg[search][type]
            dlg.staticTextNotas.Clear()
            if dlg.help != help:
                LlenaAyuda(dlg, help)
                dlg.help = help
            
        else:

            dlg = DialogTaxTree(prnt)
            dlg.search = search
            dlg.staticTextNotas.Clear()
            dlg.help = help
    
            dlg.poli=poli
            VOrden = getVOrden(type)
            query = QueryTesNode.filter_by(name=type)
            cuenta = None
            try:
                cuenta = query.count()
            except:
                MError(None, u"Ocurri\xf3 un problema de acceso a la red. Se recomienda cerrar el programa y volver a ejecutarlo") 
                
            if cuenta:
                rootElement = QueryTesNode.filter_by(name=type)[0]
                if deep:
                    maxDeep = deep
                else:
                    maxDeep = 999
                
                LlenaTree(dlg.treeCtrl1, None, rootElement, NamePattern=Pattern, poli=poli, VOrden=VOrden, maxDeep=maxDeep)
                
                dlg.Title=title
                
                selecciones = dlg.treeCtrl1.GetSelections()
                dlg.checkBoxInvertir.Show(search)
                LlenaAyuda(dlg, help)
            else: # if query.count():
                MError(prnt, type +u": Vocabulario inv\xe1lido")
                dlg.Destroy()
                return None
            
            if not search and not (type in status.dlgExcepciones):
                status.dlg[search][type]=dlg

      
        dlg.treeCtrl1.CollapseAll()
        root = dlg.treeCtrl1.GetRootItem()
        dlg.treeCtrl1.Expand(root) 
        dlg.tipoActual = None    
        dlg.tiposActuales = []         
        
        dlg.ShowModal()
        if ctrl:
            ctrl.SetLabel( dlg.tipoActual.descripcion)
        tipo =     dlg.tipoActual
        tipos =    dlg.tiposActuales
        invertir = dlg.checkBoxInvertir.GetValue()
        #dlg.Destroy()
        if search:
            return tipos, invertir, dlg.cancelar 
        else:
            return tipo
        

if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = create(None)
    try:
        
        dlg.ShowModal()
    finally:
        dlg.Destroy()
    app.MainLoop()
