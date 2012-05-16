#-----------------------------------------------------------------------------
# Name:        DlgDireccion.py
#
#
# RCS-ID:      $Id: DlgDireccion.py $
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
#Boa:Dialog:DlgDireccion

import wx
from module2 import LlenaCtrlCategoria, CtrlSelect, Mvs, MyClientData, LlenaAyuda
import module2
import cnf

def create(parent):
    return DlgDireccion(parent)

[wxID_DLGDIRECCION, wxID_DLGDIRECCIONBTNCANCELAR, 
 wxID_DLGDIRECCIONBUTTONGUARDAR, wxID_DLGDIRECCIONCHOICETIPODIRECCION, 
 wxID_DLGDIRECCIONCONTEXTHELPBUTTON1, wxID_DLGDIRECCIONSTATICTEXT1, 
 wxID_DLGDIRECCIONSTATICTEXT2, wxID_DLGDIRECCIONSTATICTEXT3, 
 wxID_DLGDIRECCIONSTATICTEXT4, wxID_DLGDIRECCIONSTATICTEXT5, 
 wxID_DLGDIRECCIONSTATICTEXT6, wxID_DLGDIRECCIONTEXTCTRLCELULAR, 
 wxID_DLGDIRECCIONTEXTCTRLCORREO, wxID_DLGDIRECCIONTEXTCTRLDIRECCION, 
 wxID_DLGDIRECCIONTEXTCTRLTEL, wxID_DLGDIRECCIONTEXTCTRLWEB, 
] = [wx.NewId() for _init_ctrls in range(16)]

class DlgDireccion(wx.Dialog):
    Return=0
    
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DLGDIRECCION, name='DlgDireccion',
              parent=prnt, pos=wx.Point(30, 59), size=wx.Size(713, 391),
              style=wx.DEFAULT_DIALOG_STYLE, title='Direcci\xf3n')
        self.SetClientSize(wx.Size(697, 355))
        self.SetBackgroundColour(wx.Colour(210, 210, 255))
        self.Bind(wx.EVT_INIT_DIALOG, self.OnDlgDireccionInitDialog)

        self.choiceTipoDireccion = wx.Choice(choices=[],
              id=wxID_DLGDIRECCIONCHOICETIPODIRECCION,
              name='choiceTipoDireccion', parent=self, pos=wx.Point(136, 48),
              size=wx.Size(130, 21), style=0)
        self.choiceTipoDireccion.Bind(wx.EVT_CHOICE,
              self.OnChoiceTipoDireccionChoice,
              id=wxID_DLGDIRECCIONCHOICETIPODIRECCION)

        self.textCtrlDireccion = wx.TextCtrl(id=wxID_DLGDIRECCIONTEXTCTRLDIRECCION,
              name='textCtrlDireccion', parent=self, pos=wx.Point(136, 96),
              size=wx.Size(464, 64), style=wx.TE_MULTILINE, value='')
        self.textCtrlDireccion.SetMaxLength(200)

        self.staticText1 = wx.StaticText(id=wxID_DLGDIRECCIONSTATICTEXT1,
              label='Tipo de direcci\xf3n', name='staticText1', parent=self,
              pos=wx.Point(32, 56), size=wx.Size(80, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_DLGDIRECCIONSTATICTEXT2,
              label='Direcci\xf3n', name='staticText2', parent=self,
              pos=wx.Point(32, 104), size=wx.Size(43, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_DLGDIRECCIONSTATICTEXT3,
              label='Tel\xe9fono / Fax', name='staticText3', parent=self,
              pos=wx.Point(32, 184), size=wx.Size(71, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_DLGDIRECCIONSTATICTEXT4,
              label='P\xe1gina WEB', name='staticText4', parent=self,
              pos=wx.Point(32, 256), size=wx.Size(57, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_DLGDIRECCIONSTATICTEXT5,
              label='Celular', name='staticText5', parent=self, pos=wx.Point(32,
              208), size=wx.Size(33, 13), style=0)

        self.textCtrlCelular = wx.TextCtrl(id=wxID_DLGDIRECCIONTEXTCTRLCELULAR,
              name='textCtrlCelular', parent=self, pos=wx.Point(136, 200),
              size=wx.Size(464, 21), style=0, value='')
        self.textCtrlCelular.SetMaxLength(180)

        self.textCtrlCorreo = wx.TextCtrl(id=wxID_DLGDIRECCIONTEXTCTRLCORREO,
              name='textCtrlCorreo', parent=self, pos=wx.Point(136, 224),
              size=wx.Size(464, 21), style=0, value='')
        self.textCtrlCorreo.SetMaxLength(200)

        self.textCtrlTel = wx.TextCtrl(id=wxID_DLGDIRECCIONTEXTCTRLTEL,
              name='textCtrlTel', parent=self, pos=wx.Point(136, 176),
              size=wx.Size(464, 21), style=0, value='')
        self.textCtrlTel.SetMaxLength(180)

        self.buttonGuardar = wx.Button(id=wxID_DLGDIRECCIONBUTTONGUARDAR,
              label='Seleccionar', name='buttonGuardar', parent=self,
              pos=wx.Point(264, 296), size=wx.Size(75, 23), style=0)
        self.buttonGuardar.Bind(wx.EVT_BUTTON, self.OnButtonGuardarButton,
              id=wxID_DLGDIRECCIONBUTTONGUARDAR)

        self.textCtrlWeb = wx.TextCtrl(id=wxID_DLGDIRECCIONTEXTCTRLWEB,
              name='textCtrlWeb', parent=self, pos=wx.Point(136, 248),
              size=wx.Size(464, 21), style=0, value='')
        self.textCtrlWeb.SetMaxLength(200)

        self.staticText6 = wx.StaticText(id=wxID_DLGDIRECCIONSTATICTEXT6,
              label='Correo electr\xf3nico', name='staticText6', parent=self,
              pos=wx.Point(32, 232), size=wx.Size(88, 13), style=0)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self,
              pos=wx.Point(672, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)

        self.btnCancelar = wx.Button(id=wxID_DLGDIRECCIONBTNCANCELAR,
              label='Cancelar', name='btnCancelar', parent=self,
              pos=wx.Point(384, 296), size=wx.Size(75, 23), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_DLGDIRECCIONBTNCANCELAR)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.guardar = False
        LlenaAyuda(self, u'Direcciones')
        if cnf.OSlinux:
            module2.choiceFix(self, __name__)
        
    


    def OnDlgDireccionInitDialog(self, event):
        self.ctrls = [self.textCtrlDireccion, self.textCtrlTel, 
                      self.textCtrlCorreo, self.textCtrlCelular,
                      self.textCtrlWeb, self.buttonGuardar]
        self.enableCtrls(False)
        d=MyClientData(self.choiceTipoDireccion)
        if d: self.enableCtrls(True)
        event.Skip()

    def OnButton1Button(self, event):
        self.EndModal(1)
        event.Skip()
    def enableCtrls(self, op):
        for i in self.ctrls:
            i.Enable(op)
    
    
    def OnChoiceTipoDireccionChoice(self, event):
        d = MyClientData(event)
        if d: self.enableCtrls(True)
        else: self.enableCtrls(False)
        event.Skip()

    def OnButtonGuardarButton(self, event):
        self.guardar = True
        self.EndModal(1)
        event.Skip()

    def OnBtnCancelarButton(self, event):
        self.guardar = False
        self.EndModal(1)
        event.Skip()
def MaintDireccion(parent, obj):
    dlg = DlgDireccion(parent)
    LlenaCtrlCategoria(dlg.choiceTipoDireccion, u'T40')
    if obj.PTesauro:
        CtrlSelect(dlg.choiceTipoDireccion, obj.PTesauro)
    if obj.masinformacion:
        dlg.textCtrlDireccion.SetValue(obj.masinformacion)
    dlg.textCtrlTel.SetValue(Mvs(obj.telefono))
    dlg.textCtrlCorreo.SetValue(Mvs(obj.correo_e))
    dlg.textCtrlCelular.SetValue(Mvs(obj.celular))
    dlg.textCtrlWeb.SetValue(Mvs(obj.web))
    
        
        
    
    dlg.ShowModal()
    if dlg.guardar:
    
        obj.masinformacion =   dlg.textCtrlDireccion.GetValue()
        obj.PTesauro = dlg.choiceTipoDireccion.GetClientData(dlg.choiceTipoDireccion.Selection)
        obj.telefono = dlg.textCtrlTel.GetValue()
        obj.correo_e = dlg.textCtrlCorreo.GetValue()
        obj.celular  = dlg.textCtrlCelular.GetValue()
        obj.web      = dlg.textCtrlWeb.GetValue()
    dlg.Destroy()
