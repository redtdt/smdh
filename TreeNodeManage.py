#-----------------------------------------------------------------------------
# Name:        TreeNodeManage.py
#
#
# RCS-ID:      $Id: TreeNodeManage.py $
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
#Boa:TreeNodeManage:TreeNodeManage

import wx
from module2 import  TesNode, QueryTesNode, status
from DialogAltaTreeNode import Dialog3

session = status.session

listaItemsId=[]
def create(parent):
    return FrameVocab(parent)

[wxID_FRAME3, wxID_FRAME3BUTTON1, wxID_FRAME3BUTTON2, wxID_FRAME3BUTTON3, 
 wxID_FRAME3LISTBOX1, wxID_FRAME3PANEL1, wxID_FRAME3STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(7)]

class FrameVocab(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME3, name='', parent=prnt,
              pos=wx.Point(359, 165), size=wx.Size(701, 505),
              style=wx.DEFAULT_FRAME_STYLE, title='Manejo de Vocabularios')
        self.SetClientSize(wx.Size(693, 475))
        self.Bind(wx.EVT_CLOSE, self.OnFrame3Close)

        self.panel1 = wx.Panel(id=wxID_FRAME3PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(693, 475),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME3STATICTEXT1,
              label='staticText1', name='staticText1', parent=self.panel1,
              pos=wx.Point(168, 24), size=wx.Size(144, 48), style=0)

        self.listBox1 = wx.ListBox(choices=[], id=wxID_FRAME3LISTBOX1,
              name='listBox1', parent=self.panel1, pos=wx.Point(168, 80),
              size=wx.Size(131, 280), style=0)

        self.button1 = wx.Button(id=wxID_FRAME3BUTTON1, label='Fwd',
              name='button1', parent=self.panel1, pos=wx.Point(288, 384),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME3BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME3BUTTON2, label='Back',
              name='button2', parent=self.panel1, pos=wx.Point(96, 384),
              size=wx.Size(75, 23), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME3BUTTON2)

        self.button3 = wx.Button(id=wxID_FRAME3BUTTON3, label='Nuevo',
              name='button3', parent=self.panel1, pos=wx.Point(352, 32),
              size=wx.Size(75, 23), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME3BUTTON3)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.filldata(1)

    def OnFrame3Close(self, event):
        self.Destroy()
        event.Skip()
        
        
    def filldata(self, id):
        
        t = QueryTesNode
        n = t.filter(TesNode.c.id==id)[0]
        
        desc = n.name
        if n.descripcion:
            desc = desc + ' ' + n.descripcion
        self.staticText1.SetLabel(desc)
        self.staticText1.node=n
        listaItemsId=[]
        
        self.listBox1.Clear()
        for i in n.children.values():
            listaItemsId.append(i.id)
            self.listBox1.Append(i.ClaveODesc(), i)
            
        

    def OnButton1Button(self, event):
        i = self.listBox1.Selection
        name  = self.listBox1.GetClientData(i).name
        id =  self.listBox1.GetClientData(i).id
        self.filldata(id)
        
        event.Skip()

    def OnButton2Button(self, event):
# back button
        if self.staticText1.node.parent_id:
            self.filldata(self.staticText1.node.parent_id)
        
        event.Skip()

    def OnButton3Button(self, event):

        dlg = Dialog3(self)

        dlg.ShowModal()
        clave = str(dlg.textCtrl1.GetValue())
        descripcion = str(dlg.textCtrl2.GetValue())
        self.staticText1.node.append(clave, descripcion)
        session.flush()
        self.filldata(self.staticText1.node.id)
        
        dlg.Destroy()
        event.Skip()
        
