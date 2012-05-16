#-----------------------------------------------------------------------------
# Name:        FrameGrupos.py
#
#
# RCS-ID:      $Id: FrameGrupos.py $
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
#Boa:Frame:FrameGrupos

import wx

if __name__ == '__main__':
    import cnf
    cnf.user='admin'
    cnf.passwd='redtdt'
    
import module2
from module2 import Grupo, session, status, LlenaCtrl3, MyClientData, MError, myHash
from DlgInteger import dlgInteger

def create(parent):
    return FrameGrupos(parent)

[wxID_FRAMEGRUPOS, wxID_FRAMEGRUPOSBTNADD, wxID_FRAMEGRUPOSBTNCERRAR, 
 wxID_FRAMEGRUPOSBTNDEL, wxID_FRAMEGRUPOSBTNSAVE, wxID_FRAMEGRUPOSLISTBOX1, 
 wxID_FRAMEGRUPOSPANEL1, wxID_FRAMEGRUPOSSTATICTEXT1, 
 wxID_FRAMEGRUPOSSTATICTEXT2, wxID_FRAMEGRUPOSSTATICTEXT3, 
 wxID_FRAMEGRUPOSSTATICTEXT4, wxID_FRAMEGRUPOSSTATICTEXT5, 
 wxID_FRAMEGRUPOSTEXTCTRLCONTACTO, wxID_FRAMEGRUPOSTEXTCTRLNOMBRE, 
 wxID_FRAMEGRUPOSTEXTCTRLSIGLA, wxID_FRAMEGRUPOSTXTHASH, 
 wxID_FRAMEGRUPOSTXTID, 
] = [wx.NewId() for _init_ctrls in range(17)]

class FrameGrupos(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEGRUPOS, name='FrameGrupos',
              parent=prnt, pos=wx.Point(263, 245), size=wx.Size(862, 540),
              style=wx.DEFAULT_FRAME_STYLE, title='Grupos')
        self.SetClientSize(wx.Size(846, 504))

        self.panel1 = wx.Panel(id=wxID_FRAMEGRUPOSPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(846, 504),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'MS Shell Dlg 2'))

        self.listBox1 = wx.ListBox(choices=[], id=wxID_FRAMEGRUPOSLISTBOX1,
              name='listBox1', parent=self.panel1, pos=wx.Point(32, 40),
              size=wx.Size(160, 264), style=0)
        self.listBox1.Bind(wx.EVT_LISTBOX_DCLICK, self.OnListBox1ListboxDclick,
              id=wxID_FRAMEGRUPOSLISTBOX1)

        self.btnAdd = wx.Button(id=wxID_FRAMEGRUPOSBTNADD, label='Agregar',
              name='btnAdd', parent=self.panel1, pos=wx.Point(32, 320),
              size=wx.Size(75, 23), style=0)
        self.btnAdd.Bind(wx.EVT_BUTTON, self.OnBtnAddButton,
              id=wxID_FRAMEGRUPOSBTNADD)

        self.btnDel = wx.Button(id=wxID_FRAMEGRUPOSBTNDEL, label='Borrar',
              name='btnDel', parent=self.panel1, pos=wx.Point(120, 320),
              size=wx.Size(75, 23), style=0)
        self.btnDel.Bind(wx.EVT_BUTTON, self.OnBtnDelButton,
              id=wxID_FRAMEGRUPOSBTNDEL)

        self.staticText1 = wx.StaticText(id=wxID_FRAMEGRUPOSSTATICTEXT1,
              label='Id', name='staticText1', parent=self.panel1,
              pos=wx.Point(232, 48), size=wx.Size(10, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAMEGRUPOSSTATICTEXT2,
              label='Nombre', name='staticText2', parent=self.panel1,
              pos=wx.Point(232, 72), size=wx.Size(37, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAMEGRUPOSSTATICTEXT3,
              label='Contacto', name='staticText3', parent=self.panel1,
              pos=wx.Point(232, 120), size=wx.Size(44, 13), style=0)

        self.textCtrlNombre = wx.TextCtrl(id=wxID_FRAMEGRUPOSTEXTCTRLNOMBRE,
              name='textCtrlNombre', parent=self.panel1, pos=wx.Point(320, 64),
              size=wx.Size(512, 21), style=0, value='')

        self.textCtrlSigla = wx.TextCtrl(id=wxID_FRAMEGRUPOSTEXTCTRLSIGLA,
              name='textCtrlSigla', parent=self.panel1, pos=wx.Point(320, 88),
              size=wx.Size(512, 21), style=0, value='')

        self.staticText4 = wx.StaticText(id=wxID_FRAMEGRUPOSSTATICTEXT4,
              label='Sigla', name='staticText4', parent=self.panel1,
              pos=wx.Point(232, 96), size=wx.Size(22, 13), style=0)

        self.textCtrlContacto = wx.TextCtrl(id=wxID_FRAMEGRUPOSTEXTCTRLCONTACTO,
              name='textCtrlContacto', parent=self.panel1, pos=wx.Point(320,
              112), size=wx.Size(512, 21), style=0, value='')

        self.btnSave = wx.Button(id=wxID_FRAMEGRUPOSBTNSAVE, label='Guardar',
              name='btnSave', parent=self.panel1, pos=wx.Point(336, 320),
              size=wx.Size(75, 23), style=0)
        self.btnSave.Bind(wx.EVT_BUTTON, self.OnBtnSaveButton,
              id=wxID_FRAMEGRUPOSBTNSAVE)

        self.txtId = wx.StaticText(id=wxID_FRAMEGRUPOSTXTID, label="'00'",
              name='txtId', parent=self.panel1, pos=wx.Point(320, 48),
              size=wx.Size(16, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAMEGRUPOSSTATICTEXT5,
              label='C\xf3digo de verificaci\xf3n', name='staticText5',
              parent=self.panel1, pos=wx.Point(352, 48), size=wx.Size(106, 13),
              style=0)

        self.txtHash = wx.StaticText(id=wxID_FRAMEGRUPOSTXTHASH, label='...',
              name='txtHash', parent=self.panel1, pos=wx.Point(464, 48),
              size=wx.Size(12, 13), style=0)

        self.btnCerrar = wx.Button(id=wxID_FRAMEGRUPOSBTNCERRAR, label='Cerrar',
              name='btnCerrar', parent=self.panel1, pos=wx.Point(336, 376),
              size=wx.Size(75, 23), style=0)
        self.btnCerrar.Bind(wx.EVT_BUTTON, self.OnBtnCerrarButton,
              id=wxID_FRAMEGRUPOSBTNCERRAR)

    def __init__(self, parent):
        self._init_ctrls(parent)
        LoadCtrls(self)
        
        

    def OnBtnAddButton(self, event):

        id = dlgInteger(self)
        if ExisteGrupo(self, id):
            MError(self, "Ya existe un grupo con esa clave")
        else:
            status.grupoActual = Grupo(id)
            session.add(status.grupoActual)
            session.flush()
            LoadDataGrupo(self)
        LoadCtrls(self)
        event.Skip()

    def OnBtnDelButton(self, event):
        print "delllll"
        LoadCtrls(self)
        event.Skip()

    def OnBtnSaveButton(self, event):
        SaveDataGrupo(self)
        LoadCtrls(self)
        event.Skip()

    def OnListBox1ListboxDclick(self, event):
        status.grupoActual = MyClientData(self.listBox1)
        LoadDataGrupo(self)
        event.Skip()

    def OnBtnCerrarButton(self, event):
        self.Close()
        event.Skip()

def LoadCtrls(self):
    LlenaCtrl3(self.listBox1, [(i,i.Descriptor()) for i in session.query(Grupo)])
def SaveDataGrupo(self):
    status.grupoActual.nombre = self.textCtrlNombre.GetValue()
    status.grupoActual.contacto = self.textCtrlContacto.GetValue()
    status.grupoActual.sigla = self.textCtrlSigla.GetValue()
    session.add(status.grupoActual)
    session.flush()
    
def LoadDataGrupo(self):
    if status.grupoActual.nombre:
        
        self.textCtrlNombre.SetValue(status.grupoActual.nombre    )
    else:
        self.textCtrlNombre.SetValue('')
    if status.grupoActual.contacto:
        self.textCtrlContacto.SetValue(status.grupoActual.contacto)
    else:
        self.textCtrlContacto.SetValue('')
    if status.grupoActual.sigla:
        self.textCtrlSigla.SetValue(status.grupoActual.sigla)
    else:
        self.textCtrlSigla.SetValue('')
    
    self.txtId.SetLabel( str(status.grupoActual.id))
    Ihash = str(status.grupoActual.id)
    Ihash = myHash(Ihash)
    self.txtHash.SetLabel( str(Ihash))
    
def ExisteGrupo(self, id):
    r=session.query(Grupo).filter(Grupo.id == id).count()
    return r > 0


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
