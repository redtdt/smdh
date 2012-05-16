#-----------------------------------------------------------------------------
# Name:        Locldetalles.py
#
#
# RCS-ID:      $Id: Locldetalles.py $
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

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BTNCERRAR, wxID_DIALOG1STATICEDO, 
 wxID_DIALOG1STATICLOCALIDAD, wxID_DIALOG1STATICLOCALIDADNOTAS, 
 wxID_DIALOG1STATICMPO, wxID_DIALOG1STATICMPONOTAS, wxID_DIALOG1STATICPAIS, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(28, 69), size=wx.Size(829, 326),
              style=wx.DEFAULT_DIALOG_STYLE, title='Localizaci\xf3n')
        self.SetClientSize(wx.Size(813, 290))
        self.SetToolTipString('')
        self.SetBackgroundColour(wx.Colour(184, 184, 112))

        self.staticPais = wx.StaticText(id=wxID_DIALOG1STATICPAIS, label='',
              name='staticPais', parent=self, pos=wx.Point(40, 56),
              size=wx.Size(112, 13), style=0)

        self.staticEdo = wx.StaticText(id=wxID_DIALOG1STATICEDO, label='',
              name='staticEdo', parent=self, pos=wx.Point(40, 88),
              size=wx.Size(112, 13), style=0)

        self.staticMpo = wx.StaticText(id=wxID_DIALOG1STATICMPO, label='',
              name='staticMpo', parent=self, pos=wx.Point(40, 120),
              size=wx.Size(288, 13), style=0)

        self.staticLocalidad = wx.StaticText(id=wxID_DIALOG1STATICLOCALIDAD,
              label='', name='staticLocalidad', parent=self, pos=wx.Point(40,
              176), size=wx.Size(368, 40), style=wx.ST_NO_AUTORESIZE)

        self.staticMpoNotas = wx.StaticText(id=wxID_DIALOG1STATICMPONOTAS,
              label='', name='staticMpoNotas', parent=self, pos=wx.Point(496,
              120), size=wx.Size(288, 48), style=wx.ST_NO_AUTORESIZE)

        self.staticLocalidadNotas = wx.StaticText(id=wxID_DIALOG1STATICLOCALIDADNOTAS,
              label='', name='staticLocalidadNotas', parent=self,
              pos=wx.Point(496, 176), size=wx.Size(288, 48),
              style=wx.ST_NO_AUTORESIZE)

        self.btnCerrar = wx.Button(id=wxID_DIALOG1BTNCERRAR, label='Cerrar',
              name='btnCerrar', parent=self, pos=wx.Point(376, 232),
              size=wx.Size(75, 23), style=0)
        self.btnCerrar.Bind(wx.EVT_BUTTON, self.OnBtnCerrarButton,
              id=wxID_DIALOG1BTNCERRAR)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        print 'modal'

    def OnBtnCerrarButton(self, event):
        self.Close()
        print 'no modal'
        
        event.Skip()
        
def LocDetalles(prnt, pais, estado, mpo, localidad, NotasCiudad, NotasLocalidad):
    pop=create(prnt)
    if pais:
        pop.staticPais.SetLabel( u"Pa\xeds        %s" % pais)
    if estado:
        pop.staticEdo.SetLabel(  "Estado     %s" % estado)
    if mpo:
        pop.staticMpo.SetLabel(        "Municipio  %s" % mpo)
    if localidad:
        pop.staticLocalidad.SetLabel(  "Localidad  %s" % localidad)
    if NotasCiudad:
        pop.staticMpoNotas.SetLabel(  "Notas  %s" % NotasCiudad)
    if NotasLocalidad:
        pop.staticLocalidadNotas.SetLabel(  "Notas  %s" % NotasLocalidad)

    pop.ShowModal()
    

