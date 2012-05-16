#-----------------------------------------------------------------------------
# Name:        DlgUser.py
#
#
# RCS-ID:      $Id: DlgUser.py $
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
#Boa:Dialog:DlgUser

import wx

if __name__ == '__main__':
    import cnf
    cnf.user='admin'
    cnf.passwd='redtdt'
from module2 import session, User, LlenaCtrl3, MyClientData, LlenaAyuda

def create(parent):
    return DlgUser(parent)

[wxID_DLGUSER, wxID_DLGUSERBTNCANCEL, wxID_DLGUSERBTNOK, 
 wxID_DLGUSERCHKINVERTIR, wxID_DLGUSERCONTEXTHELPBUTTON1, 
 wxID_DLGUSERLISTUSER, wxID_DLGUSERPANEL1, 
] = [wx.NewId() for _init_ctrls in range(7)]

class DlgUser(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DLGUSER, name='DlgUser', parent=prnt,
              pos=wx.Point(399, 208), size=wx.Size(449, 507),
              style=wx.DEFAULT_DIALOG_STYLE, title='Usuario')
        self.SetClientSize(wx.Size(433, 471))
        self.Bind(wx.EVT_CLOSE, self.OnDlgUserClose)

        self.panel1 = wx.Panel(id=wxID_DLGUSERPANEL1, name='panel1',
              parent=self, pos=wx.Point(16, 32), size=wx.Size(384, 424),
              style=wx.TAB_TRAVERSAL)

        self.listUser = wx.ListBox(choices=[], id=wxID_DLGUSERLISTUSER,
              name='listUser', parent=self.panel1, pos=wx.Point(64, 64),
              size=wx.Size(203, 216), style=0)

        self.btnOK = wx.Button(id=wxID_DLGUSERBTNOK, label='Seleccionar',
              name='btnOK', parent=self.panel1, pos=wx.Point(64, 296),
              size=wx.Size(75, 23), style=0)
        self.btnOK.Bind(wx.EVT_BUTTON, self.OnBtnOKButton, id=wxID_DLGUSERBTNOK)

        self.btnCANCEL = wx.Button(id=wxID_DLGUSERBTNCANCEL, label='Cancelar',
              name='btnCANCEL', parent=self.panel1, pos=wx.Point(192, 296),
              size=wx.Size(75, 23), style=0)
        self.btnCANCEL.Bind(wx.EVT_BUTTON, self.OnBtnCANCELButton,
              id=wxID_DLGUSERBTNCANCEL)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self.panel1,
              pos=wx.Point(360, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)

        self.chkInvertir = wx.CheckBox(id=wxID_DLGUSERCHKINVERTIR,
              label='Invertir condici\xf3n', name='chkInvertir',
              parent=self.panel1, pos=wx.Point(64, 40), size=wx.Size(136, 13),
              style=0)
        self.chkInvertir.SetValue(True)

    def __init__(self, parent):
        self._init_ctrls(parent)
        usuarios = [(i, i.nombre) for i in session.query(User).all()]
        LlenaCtrl3(self.listUser, usuarios)
        self.U = None
        self.cancelar = True
    def OnBtnOKButton(self, event):
        self.cancelar = False
        self.U = MyClientData(self.listUser)
        self.Close()
        #self.MakeModal(False)
        
        
        event.Skip()

    def OnBtnCANCELButton(self, event):
        self.U = None
        self.cancelar = True
        self.Close()
        #self.MakeModal(False)
        
        event.Skip()

    def OnDlgUserClose(self, event):
        #self.cancelar = True
        event.Skip()
def UserCond(prnt, invertir, help=u'dlgUserBusqueda'):
    dlg = DlgUser(prnt)
    LlenaAyuda(dlg, help)
    dlg.chkInvertir.SetValue(invertir)
    dlg.ShowModal()
    
    U = dlg.U
    dlg.Destroy()
    return U, dlg.chkInvertir.GetValue(), dlg.cancelar
    
    


if __name__ == '__main__':
    app = wx.PySimpleApp()

    dlg = create(None)
    u = UserCond(None)
    print u
    
