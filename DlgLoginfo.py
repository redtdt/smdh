#-----------------------------------------------------------------------------
# Name:        DlgLoginfo.py
#
#
# RCS-ID:      $Id: DlgLoginfo.py $
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
from module2 import MError, LlenaAyuda

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1CONTEXTHELPBUTTON1, wxID_DIALOG1STATICTEXT1, 
 wxID_DIALOG1STATICTEXT2, wxID_DIALOG1UACTUALIZACION, wxID_DIALOG1UCREACION, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(390, 240), size=wx.Size(400, 220),
              style=wx.DEFAULT_DIALOG_STYLE, title='')
        self.SetClientSize(wx.Size(392, 193))
        self.SetBackgroundColour(wx.Colour(255, 203, 151))

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label='Actualizaci\xf3n', name='staticText1', parent=self,
              pos=wx.Point(40, 96), size=wx.Size(72, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,
              label='Creaci\xf3n', name='staticText2', parent=self,
              pos=wx.Point(40, 40), size=wx.Size(72, 13), style=0)

        self.Ucreacion = wx.StaticText(id=wxID_DIALOG1UCREACION, label='',
              name='Ucreacion', parent=self, pos=wx.Point(120, 40),
              size=wx.Size(264, 13), style=0)

        self.Uactualizacion = wx.StaticText(id=wxID_DIALOG1UACTUALIZACION,
              label='', name='Uactualizacion', parent=self, pos=wx.Point(120,
              96), size=wx.Size(256, 13), style=0)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self,
              pos=wx.Point(368, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
def DlgInfo(prnt, obj):
    if obj:
        if hasattr(obj, 'PLoginfo') and obj.PLoginfo:
            dlg=Dialog1(prnt)
            LlenaAyuda(dlg, u'personaCol')
            L = obj.PLoginfo
            if L.Creador:
                strCreador = L.Creador.Descriptor()
            else:
                strCreador = str(L.userCreacion)
            if L.Actualizador:
                strActualizador = L.Actualizador.Descriptor()
            else:
                strActualizador = str(L.userActualizacion)
            dlg.Ucreacion.SetLabel( strCreador + ' ' + L.fechaCreacion.strftime("%d/%m/%Y"))   
            dlg.Uactualizacion.SetLabel( strActualizador + ' ' + L.fechaActualizacion.strftime("%d/%m/%Y"))
            
            dlg.ShowModal()
        else:
            MError(prnt, u"A\xfan no hay informaci\xf3n")
        
