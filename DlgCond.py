#-----------------------------------------------------------------------------
# Name:        DlgCond.py
#
#
# RCS-ID:      $Id: DlgCond.py $
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
#Boa:Dialog:Condicion

import wx

from module2 import LlenaAyuda

def create(parent):
    return Condicion(parent)

[wxID_CONDICION, wxID_CONDICIONBTNCANCELAR, wxID_CONDICIONBUTTON1, 
 wxID_CONDICIONCHECKBOX1, wxID_CONDICIONCHKINVERTIR, 
 wxID_CONDICIONCHKSINFECHA, wxID_CONDICIONCONTEXTHELPBUTTON1, 
 wxID_CONDICIONDATEVALUEF, wxID_CONDICIONDATEVALUEI, 
 wxID_CONDICIONSTATICTEXT1, wxID_CONDICIONSTATICTEXT2, 
] = [wx.NewId() for _init_ctrls in range(11)]

class Condicion(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_CONDICION, name='Condicion',
              parent=prnt, pos=wx.Point(528, 332), size=wx.Size(408, 203),
              style=wx.DEFAULT_DIALOG_STYLE, title='Condici\xf3n')
        self.SetClientSize(wx.Size(392, 167))
        self.SetBackgroundColour(wx.Colour(141, 199, 199))
        self.Bind(wx.EVT_CLOSE, self.OnCondicionClose)

        self.dateValueI = wx.DatePickerCtrl(id=wxID_CONDICIONDATEVALUEI,
              name='dateValueI', parent=self, pos=wx.Point(208, 23),
              size=wx.Size(96, 21), style=wx.DP_SHOWCENTURY)
        self.dateValueI.Show(False)

        self.button1 = wx.Button(id=wxID_CONDICIONBUTTON1, label='Seleccionar',
              name='button1', parent=self, pos=wx.Point(120, 120),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_CONDICIONBUTTON1)

        self.dateValueF = wx.DatePickerCtrl(id=wxID_CONDICIONDATEVALUEF,
              name='dateValueF', parent=self, pos=wx.Point(208, 48),
              size=wx.Size(96, 21), style=wx.DP_SHOWCENTURY)
        self.dateValueF.Show(False)

        self.staticText1 = wx.StaticText(id=wxID_CONDICIONSTATICTEXT1,
              label='Entre el d\xeda', name='staticText1', parent=self,
              pos=wx.Point(88, 31), size=wx.Size(54, 13), style=0)
        self.staticText1.Show(False)

        self.staticText2 = wx.StaticText(id=wxID_CONDICIONSTATICTEXT2,
              label='y el d\xeda', name='staticText2', parent=self,
              pos=wx.Point(88, 56), size=wx.Size(34, 13), style=0)
        self.staticText2.Show(False)

        self.checkBox1 = wx.CheckBox(id=wxID_CONDICIONCHECKBOX1,
              label='Exportar', name='checkBox1', parent=self, pos=wx.Point(32,
              88), size=wx.Size(232, 13), style=wx.ALIGN_RIGHT)
        self.checkBox1.SetToolTipString('Confidencialidad')
        self.checkBox1.SetValue(True)
        self.checkBox1.Show(False)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self,
              pos=wx.Point(360, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)

        self.chkInvertir = wx.CheckBox(id=wxID_CONDICIONCHKINVERTIR,
              label='Invertir condici\xf3n', name='chkInvertir', parent=self,
              pos=wx.Point(80, 8), size=wx.Size(104, 13), style=wx.ALIGN_RIGHT)
        self.chkInvertir.SetToolTipString('Confidencialidad')
        self.chkInvertir.SetValue(False)
        self.chkInvertir.Show(False)

        self.chkSinFecha = wx.CheckBox(id=wxID_CONDICIONCHKSINFECHA,
              label='Sin fecha', name='chkSinFecha', parent=self,
              pos=wx.Point(232, 8), size=wx.Size(70, 13), style=wx.ALIGN_RIGHT)
        self.chkSinFecha.SetValue(True)
        self.chkSinFecha.Show(False)
        self.chkSinFecha.Bind(wx.EVT_CHECKBOX, self.OnChkSinFechaCheckbox,
              id=wxID_CONDICIONCHKSINFECHA)

        self.btnCancelar = wx.Button(id=wxID_CONDICIONBTNCANCELAR,
              label='Cancelar', name='btnCancelar', parent=self,
              pos=wx.Point(224, 120), size=wx.Size(75, 23), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_CONDICIONBTNCANCELAR)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.cancelar = True


    def OnButton1Button(self, event):
        self.cancelar = False
        self.Close()
        event.Skip()

    def OnChkSinFechaCheckbox(self, event):
        T = self.chkSinFecha.GetValue()
        T = not(T)
        self.dateValueI.Show(T)
        self.dateValueF.Show(T)
        
        event.Skip()

    def OnBtnCancelarButton(self, event):
        self.cancelar = True
        self.Close()

    def OnCondicionClose(self, event):
        #self.cancelar = True
        event.Skip()
        
        
def DlgCond(self, type, param, help=u''):
    dlg=Condicion(self)
    if type == 'Date':
        dlg.dateValueI.Show(not(param.sinFecha))
        dlg.dateValueF.Show(not(param.sinFecha))
        dlg.staticText1.Show()
        dlg.staticText2.Show()
        dlg.chkInvertir.Show()
        dlg.chkSinFecha.SetValue(False)

        dlg.chkSinFecha.Show(param.conTipoDeFecha)
        if param:
            if param.DateI:
                dlg.dateValueI.SetValue(param.DateI)
            if param.DateF:
                dlg.dateValueF.SetValue(param.DateF)
            dlg.chkInvertir.SetValue(param.invertir)
            if param.sinFecha:
                dlg.chkSinFecha.SetValue(param.sinFecha)
            
                
    
    LlenaAyuda(dlg, help)        
        
    dlg.ShowModal()
    if not dlg.cancelar:
        param.DateI = dlg.dateValueI.GetValue()
        param.DateF = dlg.dateValueF.GetValue()
        param.invertir = dlg.chkInvertir.GetValue()
        param.sinFecha = dlg.chkSinFecha.GetValue()
    param.borrar = dlg.cancelar
def DlgChk(self, type, param, help=u'', descripcion='Exportar'):
    dlg=Condicion(self)
    if type == 'Chk':
        dlg.checkBox1.Show()
        dlg.checkBox1.SetLabel(descripcion)
        dlg.chkInvertir.Show(False)
    LlenaAyuda(dlg, help)
    dlg.ShowModal()
    if not dlg.cancelar:
        param.Value = 0
        if dlg.checkBox1.GetValue():
            param.Value = 1
    param.borrar = dlg.cancelar
    
    
    
    
def findall(L, value, start=0):
        # generator version
        i = start - 1
        try:
            i = L.index(value, i+i)
            yield i
        except ValueError:
            pass
