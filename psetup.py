#-----------------------------------------------------------------------------
# Name:        psetup.py
#
#
# RCS-ID:      $Id: psetup.py $
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
#Boa:Frame:Frame3

# pregunta por un password para ser utilizado cuando se instala el postgres.

import sys

if False:
	print sys.prefix
	#str = raw_input("Enter your input: ")
	#import time
	#time.sleep(8) 
	exit()
   
import wx

import re
from DlgError import MError
import os







def create(parent):
    return Frame3(parent)

[wxID_FRAME3, wxID_FRAME3CANCELAR, wxID_FRAME3INSTALAR, wxID_FRAME3RADIOBOX1, 
 wxID_FRAME3STATICTEXT1, wxID_FRAME3TEXTPASS, wxID_FRAME3TXTSTATUS, 
] = [wx.NewId() for _init_ctrls in range(7)]



nombreValido = re.compile('[a-z][a-z0-9]*')
passValida = re.compile('[a-z][a-z0-9]*', re.IGNORECASE)

class Frame3(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME3, name='', parent=prnt,
              pos=wx.Point(449, 207), size=wx.Size(400, 250),
              style=wx.DEFAULT_FRAME_STYLE, title='Instalacion de Postgres')
        self.SetClientSize(wx.Size(384, 214))

        self.textPass = wx.TextCtrl(id=wxID_FRAME3TEXTPASS, name='textPass',
              parent=self, pos=wx.Point(184, 8), size=wx.Size(100, 16), style=0,
              value='')

        self.Instalar = wx.Button(id=wxID_FRAME3INSTALAR, label='Instalar',
              name='Instalar', parent=self, pos=wx.Point(32, 120),
              size=wx.Size(75, 23), style=0)
        self.Instalar.Bind(wx.EVT_BUTTON, self.OnInstalarButton,
              id=wxID_FRAME3INSTALAR)

        self.Cancelar = wx.Button(id=wxID_FRAME3CANCELAR, label='Cancelar',
              name='Cancelar', parent=self, pos=wx.Point(216, 120),
              size=wx.Size(75, 23), style=0)
        self.Cancelar.Bind(wx.EVT_BUTTON, self.OnCancelarButton,
              id=wxID_FRAME3CANCELAR)

        self.staticText1 = wx.StaticText(id=wxID_FRAME3STATICTEXT1,
              label=u'Password de administracion', name='staticText1',
              parent=self, pos=wx.Point(32, 8), size=wx.Size(143, 13), style=0)

        self.txtStatus = wx.StaticText(id=wxID_FRAME3TXTSTATUS,
              label='                                         ',
              name='txtStatus', parent=self, pos=wx.Point(64, 160),
              size=wx.Size(176, 13), style=0)

        self.radioBox1 = wx.RadioBox(choices=['32 bits', '64 bits '],
              id=wxID_FRAME3RADIOBOX1, label='Tipo de plataforma',
              majorDimension=1, name='radioBox1', parent=self, pos=wx.Point(32,
              32), size=wx.Size(260, 68), style=wx.RA_SPECIFY_COLS)
        self.radioBox1.SetToolTipString('Lea el manual para seleccionar')

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnInstalarButton(self, event):
        self.txtStatus.SetLabel('')
        i = self.radioBox1.GetSelection()
        bits = 64 if i else 32
        passwd = self.textPass.GetValue()
        passwd = passwd.strip()
        res = passValida.match(passwd)
        if res and res.group() == passwd:
            self.Instalar.Disable()
            self.Cancelar.Disable()
            Instala(self, passwd, bits)    
            self.txtStatus.SetLabel('Proceso completo')
            self.Cancelar.SetLabel("Cerrar")
            self.Cancelar.Enable()
        else:
            MError(self, u"La contrasena solo puede contener letras en mayuscula o minuscula, y numeros. Debe comenzar con una letra")

    def OnCancelarButton(self, event):
        self.Close()
        
        



def Instala(self, passwd, bits):
    #try:
    #    comando = "net user postgres /delete"
    #    err=os.system(comando)
    #    print 1111
    #except:
    #    nada=1
    #comando = 'msiexec /i postgresql-8.3-int.msi /qr INTERNALLAUNCH=1 SERVICEACCOUNT="postgres" SERVICEPASSWORD="xyz" CREATESERVICEUSER=1 SUPERUSER="admin"  SUPERPASSWORD="%s" LISTENPORT=5432  PERMITREMOTE=1 ENCODING=UTF8  CLENCODE=UTF8 BASEDIR="%%ProgramFiles%%\postgresql\8.3"'%passwd
    #os.system(comando)
    if bits==32:
        comando = "setup2-32 %s"%passwd
    if bits==64:
        comando = "setup2-64 %s"%passwd
    os.system(comando)
if __name__ == '__main__':
    
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
