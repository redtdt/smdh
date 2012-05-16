#-----------------------------------------------------------------------------
# Name:        dlgRelacionar.py
#
#
# RCS-ID:      $Id: dlgRelacionar.py $
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
#Boa:Dialog:dlgRelacionar

import wx

from module2 import LlenaCtrl3, MyClientData
import module2

def create(parent):
    return dlgRelacionar(parent)

[wxID_DLGRELACIONAR, wxID_DLGRELACIONARBTNCANCELAR, 
 wxID_DLGRELACIONARBTNRELACIONAR, wxID_DLGRELACIONARLISTBOX, 
 wxID_DLGRELACIONARPANEL1, 
] = [wx.NewId() for _init_ctrls in range(5)]

class dlgRelacionar(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DLGRELACIONAR, name='dlgRelacionar',
              parent=prnt, pos=wx.Point(98, 24), size=wx.Size(560, 667),
              style=wx.DEFAULT_DIALOG_STYLE, title='Relacionar')
        self.SetClientSize(wx.Size(544, 631))
        self.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'MS Shell Dlg 2'))

        self.panel1 = wx.Panel(id=wxID_DLGRELACIONARPANEL1, name='panel1',
              parent=self, pos=wx.Point(136, 96), size=wx.Size(200, 100),
              style=wx.TAB_TRAVERSAL)

        self.listBox = wx.ListBox(choices=[], id=wxID_DLGRELACIONARLISTBOX,
              name='listBox', parent=self, pos=wx.Point(64, 56),
              size=wx.Size(448, 408), style=wx.LB_HSCROLL)

        self.btnRelacionar = wx.Button(id=wxID_DLGRELACIONARBTNRELACIONAR,
              label='Relacionar', name='btnRelacionar', parent=self,
              pos=wx.Point(64, 512), size=wx.Size(75, 23), style=0)
        self.btnRelacionar.Bind(wx.EVT_BUTTON, self.OnBtnRelacionarButton,
              id=wxID_DLGRELACIONARBTNRELACIONAR)

        self.btnCancelar = wx.Button(id=wxID_DLGRELACIONARBTNCANCELAR,
              label='Cancelar', name='btnCancelar', parent=self,
              pos=wx.Point(216, 512), size=wx.Size(75, 23), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_DLGRELACIONARBTNCANCELAR)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.resultado=None
        

    def OnBtnRelacionarButton(self, event):
        self.resultado=MyClientData(self.listBox)
        self.EndModal(wx.ID_OK)
        
        event.Skip()

    def OnBtnCancelarButton(self, event):
        self.EndModal(wx.ID_CANCEL)
        self.Close()
        event.Skip()

    
def aRelacionar(prnt, lista):
    f=dlgRelacionar(prnt)
    LlenaCtrl3(f.listBox, lista, orden=None)
    f.ShowModal()
    
    return f.resultado
    
