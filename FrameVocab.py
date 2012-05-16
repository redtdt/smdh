#-----------------------------------------------------------------------------
# Name:        FrameVocab.py
#
#
# RCS-ID:      $Id: FrameVocab.py $
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
#Boa:Frame:FrameVocab

import wx
from module2 import TesNode, status, LlenaTree, Borrar, MError, QueryTesNode, cuentaEspacios
from DlgAltaVocab import Dialog3
from sqlalchemy.sql import select
import sys

from reportaVocab import ReportaTipo

session = status.session

listaItemsId=[]

def create(parent):
    return FrameVocab(parent)

[wxID_FRAMEVOCAB, wxID_FRAMEVOCABBUTTON1, wxID_FRAMEVOCABBUTTON2, 
 wxID_FRAMEVOCABBUTTON3, wxID_FRAMEVOCABBUTTONBORRAR, wxID_FRAMEVOCABPANEL1, 
 wxID_FRAMEVOCABSTATICTEXT1, wxID_FRAMEVOCABSTATICTEXT2, 
 wxID_FRAMEVOCABSTATICTEXT3, wxID_FRAMEVOCABTEXTCTRL1, 
 wxID_FRAMEVOCABTEXTCTRL2, wxID_FRAMEVOCABTEXTCTRLNOTAS, 
 wxID_FRAMEVOCABTREECTRLVOCAB, wxID_FRAMEVOCABTXTID, 
 wxID_FRAMEVOCABTXTLONGDESC, wxID_FRAMEVOCABTXTLONGNOTAS, 
 wxID_FRAMEVOCABTXTSTATUS, wxID_FRAMEVOCABVASTAGOS, 
] = [wx.NewId() for _init_ctrls in range(18)]

class FrameVocab(wx.Frame):
    status.NodoActual = None
    
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEVOCAB, name='', parent=prnt,
              pos=wx.Point(405, 88), size=wx.Size(808, 511),
              style=wx.DEFAULT_FRAME_STYLE, title='Manejo de Vocabularios')
        self.SetClientSize(wx.Size(792, 475))
        self.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'MS Shell Dlg 2'))
        self.Bind(wx.EVT_CLOSE, self.OnFrameVocabClose)

        self.panel1 = wx.Panel(id=wxID_FRAMEVOCABPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(792, 475),
              style=wx.TAB_TRAVERSAL)

        self.button3 = wx.Button(id=wxID_FRAMEVOCABBUTTON3,
              label='Nuevo t\xe9rmino', name='button3', parent=self.panel1,
              pos=wx.Point(96, 24), size=wx.Size(176, 23), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButtonNEW,
              id=wxID_FRAMEVOCABBUTTON3)

        self.buttonBorrar = wx.Button(id=wxID_FRAMEVOCABBUTTONBORRAR,
              label='Borrar', name='buttonBorrar', parent=self.panel1,
              pos=wx.Point(8, 440), size=wx.Size(75, 23), style=0)
        self.buttonBorrar.Bind(wx.EVT_BUTTON, self.OnButtonBorrar,
              id=wxID_FRAMEVOCABBUTTONBORRAR)

        self.button1 = wx.Button(id=wxID_FRAMEVOCABBUTTON1, label='Actualizar',
              name='button1', parent=self.panel1, pos=wx.Point(424, 368),
              size=wx.Size(75, 23), style=0)
        self.button1.Enable(False)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButtonActualizar,
              id=wxID_FRAMEVOCABBUTTON1)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAMEVOCABTEXTCTRL1,
              name='textCtrl1', parent=self.panel1, pos=wx.Point(424, 80),
              size=wx.Size(124, 21), style=0, value='')
        self.textCtrl1.Bind(wx.EVT_KEY_DOWN, self.OnTextCtrl1KeyDown)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAMEVOCABTEXTCTRL2,
              name='textCtrl2', parent=self.panel1, pos=wx.Point(424, 112),
              size=wx.Size(352, 88), style=wx.TE_MULTILINE, value='')
        self.textCtrl2.SetMaxLength(350)
        self.textCtrl2.Bind(wx.EVT_KEY_DOWN, self.OnTextCtrl2KeyDown)
        self.textCtrl2.Bind(wx.EVT_TEXT, self.OnTextCtrl2Text,
              id=wxID_FRAMEVOCABTEXTCTRL2)

        self.staticText2 = wx.StaticText(id=wxID_FRAMEVOCABSTATICTEXT2,
              label='C\xf3digo', name='staticText2', parent=self.panel1,
              pos=wx.Point(352, 88), size=wx.Size(33, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAMEVOCABSTATICTEXT3,
              label='Notas', name='staticText3', parent=self.panel1,
              pos=wx.Point(352, 216), size=wx.Size(28, 13), style=0)

        self.treeCtrlVocab = wx.TreeCtrl(id=wxID_FRAMEVOCABTREECTRLVOCAB,
              name='treeCtrlVocab', parent=self.panel1, pos=wx.Point(8, 80),
              size=wx.Size(336, 352), style=wx.TR_HAS_BUTTONS)
        self.treeCtrlVocab.Bind(wx.EVT_TREE_SEL_CHANGED,
              self.OnTreeCtrlVocabTreeSelChanged,
              id=wxID_FRAMEVOCABTREECTRLVOCAB)
        self.treeCtrlVocab.Bind(wx.EVT_TREE_ITEM_ACTIVATED,
              self.OnTreeCtrlVocabTreeItemActivated,
              id=wxID_FRAMEVOCABTREECTRLVOCAB)

        self.txtId = wx.StaticText(id=wxID_FRAMEVOCABTXTID, label='__________',
              name='txtId', parent=self.panel1, pos=wx.Point(568, 88),
              size=wx.Size(60, 13), style=0)

        self.Vastagos = wx.Button(id=wxID_FRAMEVOCABVASTAGOS,
              label='Aumentar espacio en vastagos', name='Vastagos',
              parent=self.panel1, pos=wx.Point(424, 424), size=wx.Size(168, 23),
              style=0)
        self.Vastagos.Show(False)
        self.Vastagos.Bind(wx.EVT_BUTTON, self.OnVastagosButton,
              id=wxID_FRAMEVOCABVASTAGOS)

        self.txtLongDesc = wx.StaticText(id=wxID_FRAMEVOCABTXTLONGDESC,
              label='         ', name='txtLongDesc', parent=self.panel1,
              pos=wx.Point(352, 128), size=wx.Size(27, 13), style=0)

        self.txtStatus = wx.StaticText(id=wxID_FRAMEVOCABTXTSTATUS,
              label='cargando terminos....', name='txtStatus',
              parent=self.panel1, pos=wx.Point(240, 448), size=wx.Size(105, 13),
              style=0)
        self.txtStatus.Show(False)

        self.staticText1 = wx.StaticText(id=wxID_FRAMEVOCABSTATICTEXT1,
              label='Descripci\xf3n', name='staticText1', parent=self.panel1,
              pos=wx.Point(352, 112), size=wx.Size(54, 13), style=0)

        self.textCtrlNotas = wx.TextCtrl(id=wxID_FRAMEVOCABTEXTCTRLNOTAS,
              name='textCtrlNotas', parent=self.panel1, pos=wx.Point(424, 216),
              size=wx.Size(352, 136), style=wx.TE_MULTILINE, value='')
        self.textCtrlNotas.Bind(wx.EVT_TEXT, self.OnTextCtrlNotasText,
              id=wxID_FRAMEVOCABTEXTCTRLNOTAS)

        self.txtLongNotas = wx.StaticText(id=wxID_FRAMEVOCABTXTLONGNOTAS,
              label=' ', name='txtLongNotas', parent=self.panel1,
              pos=wx.Point(352, 240), size=wx.Size(3, 13), style=0)

        self.button2 = wx.Button(id=wxID_FRAMEVOCABBUTTON2,
              label='Generar reporte', name='button2', parent=self.panel1,
              pos=wx.Point(96, 440), size=wx.Size(88, 23), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAMEVOCABBUTTON2)

    def __init__(self, parent):
        self._init_ctrls(parent)
        n = QueryTesNode.filter(TesNode.name==u"rootnode")[0]
        id = n.id
        
        self.FillTree()
        
    item = None

    def OnFrameVocabClose(self, event):
        
        self.MakeModal(False)
        self.Destroy()
        event.Skip()



            
        

    def OnButtonFWD(self, event):


        event.Skip()

    def OnButtonBack(self, event):

        
        event.Skip()

    def OnButtonNEW(self, event):


        dlg = Dialog3(self)

        dlg.ShowModal()
        clave = str(dlg.textCtrl1.GetValue()).strip()
        descripcion = dlg.textCtrl2.GetValue().strip()
        if clave and descripcion:
            status.NodoActual.append(clave, descripcion)
            
            theParent = self.getParent(status.NodoActual)
            nuevoNodo = status.NodoActual.children[clave]
            session.add(nuevoNodo)
            print nuevoNodo.id, nuevoNodo.descripcion
            
            try:
                
                session.flush()
                child = self.treeCtrlVocab.AppendItem(self.item, descripcion)
                self.treeCtrlVocab.SetPyData(child, nuevoNodo)
            except:
                MError(self, "No fue posible agregar el dato ("+str(sys.exc_info())+")")

            #self.FillTree(toExpand=theParent.name, ExpandId=theParent.id)  
            
            
        dlg.Destroy()
        event.Skip()




    def OnButtonBorrar(self, event):
        parent = status.NodoActual.parent
        thisName = status.NodoActual.name
        #thisId = status.NodoActual.id
        theParent = self.getParent(status.NodoActual)
        borrado=False
        if status.NodoActual.children:
            MError(self, u"No es posible borrar un t\xe9rmino con v\xe1stagos")
        else:
            if Borrar(self, "Borrar datos?"):
                
                try:
                   session.delete(status.NodoActual)
                   session.flush()
                   borrado=True
                   
                except:
                    MError(self, "No fue posible borrar ("+str(sys.exc_info())+")")
                if borrado:
                    del parent.children[thisName]
                    #del parent.children[thisId]
                    self.treeCtrlVocab.Delete(self.item)
                #self.FillTree(toExpand=theParent.name)
                
        
        event.Skip()

    def OnListBoxVocabCLICK(self, event):
        i = self.listBox1.Selection
        status.NodoActual  = self.listBox1.GetClientData(i)
        self.txtId.SetLabel( str(status.NodoActual.id))
        
        

        event.Skip()

    def OnButtonActualizar(self, event):
        item = self.treeCtrlVocab.GetSelection()
        NodoPadre = status.NodoActual.parent
        NombreAnterior = status.NodoActual.name
        
        status.NodoActual.name = self.textCtrl1.GetValue().strip()
        status.NodoActual.descripcion = self.textCtrl2.GetValue().strip()
        status.NodoActual.notas = self.textCtrlNotas.GetValue().strip()
        if not status.NodoActual.parent_id:
            MError(self, "Error en estructura. no se actualiza (no hay parent_id)")
            return
        try:
            session.add(status.NodoActual)
            
            session.flush()
            self.button1.Enabled = False
            self.treeCtrlVocab.SetItemText(item,           self.textCtrl2.GetValue())
            NodoPadre.children.pop(NombreAnterior)
            NodoPadre.children[status.NodoActual.name] = status.NodoActual
            #self.FillTree()
        except:
            MError(self, "No fue posible actualizar ("+str(sys.exc_info())+")")
        event.Skip()
        
        
    def FillTree(self, toExpand=None, ExpandId=None, name=u"rootnode"):
        self.treeCtrlVocab.DeleteAllItems()
        query = QueryTesNode.filter_by(name=name)
        if query.count():
            rootElement = query[0]
            LlenaTree(self.treeCtrlVocab, None, rootElement, toExpand=toExpand, id=ExpandId, treeStyle="vocab", maxDeep=2)
            #self.treeCtrlVocab.SetWindowStyle(wx.TR_HAS_BUTTONS | wx.TR_HIDE_ROOT)

    def OnTreeCtrlVocabTreeSelChanged(self, event):
        
        self.item = self.treeCtrlVocab.GetSelection()
        status.NodoActual = self.treeCtrlVocab.GetPyData(self.item)
        n= status.NodoActual
        self.textCtrlNotas.SetValue('')
        if n.descripcion:
            self.textCtrl1.SetValue(n.name)
            self.textCtrl2.SetValue(n.descripcion)
            if n.notas: self.textCtrlNotas.SetValue(n.notas)
            self.txtId.SetLabel( str(n.id))
        event.Skip()
#    def getParent(self, node):
#
#        if node.parent.name == "rootnode":
#            return node
#        else:
#            return self.getParent(node.parent)

    def getParent(self, node):
        if node.parent:
            return node.parent
        else:
            return node





    def OnTextCodigoEnter(self, event):
        self.button1.Enabled = True
        
        event.Skip()

    def OnTextDescripcionTextEnter(self, event):
        self.button1.Enabled = True
        event.Skip()

    def OnTextCtrl1KeyDown(self, event):
        self.button1.Enabled = True
        event.Skip()

    def OnTextCtrl2KeyDown(self, event):
        self.button1.Enabled = True
        event.Skip()

    def OnVastagosButton(self, event):
        n=status.NodoActual
        lista = n.allTree()
        lista.remove(n)
        for nodo in lista:
            for j in range(1,6):
                valor = nodo.getClave(j)
                if valor > 0:
                    valor = valor * 5
                    nodo.setClave(j,valor)
            session.add(nodo)
            session.flush()
            
                
        event.Skip()

    def OnTextCtrl2Text(self, event):
        cuentaEspacios(self.txtLongDesc, event)
        event.Skip()

    def OnTreeCtrlVocabTreeItemActivated(self, event):
        item = self.treeCtrlVocab.GetSelection()
        if not self.treeCtrlVocab.GetChildrenCount(item):
            self.txtStatus.Show()
            self.Update()
            nodo = self.treeCtrlVocab.GetPyData(item)
            lista = QueryTesNode.filter_by(parent_id = nodo.id).order_by(TesNode.descripcion).all()
            
            for nodoHijo  in  lista:
                LlenaTree(self.treeCtrlVocab, item, nodoHijo,  treeStyle="vocab", maxDeep=1)
            self.txtStatus.Show(False)
            self.Update()

    def OnTextCtrlNotasText(self, event):
        cuentaEspacios(self.txtLongNotas, event)
        self.button1.Enabled = True
        event.Skip()

    def OnButton2Button(self, event):
        if status.NodoActual:
            ReportaTipo(status.NodoActual.name)
            MError(self, "Reporte generado")
        else:
            MError(self, "Aun no se ha seleccionado un vocabulario")
        event.Skip()


 


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
