#-----------------------------------------------------------------------------
# Name:        Diagnostico.py
#
#
# RCS-ID:      $Id: Diagnostico.py $
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
#Boa:Dialog:Diagnostico

import wx
from getFileDialog import selectFile
import codecs
from module2 import MError
import datetime

def create(parent):
    return Diagnostico(parent)

[wxID_DIAGNOSTICO, wxID_DIAGNOSTICOBUTTON1, wxID_DIAGNOSTICOTEXTO, 
] = [wx.NewId() for _init_ctrls in range(3)]

class Diagnostico(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIAGNOSTICO, name='Diagnostico',
              parent=prnt, pos=wx.Point(325, 200), size=wx.Size(1081, 620),
              style=wx.DEFAULT_DIALOG_STYLE, title='Diagn\xf3stico')
        self.SetClientSize(wx.Size(1073, 593))
        self.Bind(wx.EVT_CLOSE, self.OnDiagnosticoClose)

        self.texto = wx.TextCtrl(id=wxID_DIAGNOSTICOTEXTO, name='texto',
              parent=self, pos=wx.Point(32, 32), size=wx.Size(1024, 520),
              style=wx.TE_MULTILINE, value='')
        self.texto.SetEditable(False)

        self.button1 = wx.Button(id=wxID_DIAGNOSTICOBUTTON1,
              label='Guardar reporte', name='button1', parent=self,
              pos=wx.Point(32, 8), size=wx.Size(104, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_DIAGNOSTICOBUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnDiagnosticoClose(self, event):
        self.Destroy()
        event.Skip()

    def OnButton1Button(self, event):
        fecha=datetime.datetime.now()
        fecha=fecha.isoformat()[:16].replace(':','')
        default='c:/smdh2/archivos/diag'+str(self.grupo)+'-'+fecha+'.txt'
        nombre = selectFile(self, mask='*.txt', path="/smdh2/archivos", default=default, accion='Guardar', titulo='Guardar reporte')
        f=codecs.open(nombre,'w','utf-8')
        f.write(self.texto.GetValue())
        
        f.close()
        MError(self, u'El reporte ha sido guardado como '+nombre)
        event.Skip()
        
def DespliegaDiagnostico(parent, mensajes, grupo=None):
    f=Diagnostico(parent)
    lista=u'No fue posible importar las siguientes entidades:\n\n'
    for i in mensajes:
        #lista = lista + i.decode( "latin-1", 'replace' )+'\n'
        lista = lista + i+'\n\n'
    f.texto.SetValue(lista)
    f.grupo=grupo
    f.ShowModal()

    
