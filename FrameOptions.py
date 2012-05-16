#-----------------------------------------------------------------------------
# Name:        FrameOptions.py
#
#
# RCS-ID:      $Id: FrameOptions.py $
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
#Boa:Frame:FrameOptions

import wx
from cnf import host
import codecs
from DlgError import MError
from sys import exit

from os import name as NameOS
slash = '\\'
if NameOS in ['posix']:
    slash = '/'


def create(parent):
    return FrameOptions(parent)

[wxID_FRAMEOPTIONS, wxID_FRAMEOPTIONSBUTTONCANCEL, wxID_FRAMEOPTIONSBUTTONOK, 
 wxID_FRAMEOPTIONSCHKLOCAL, wxID_FRAMEOPTIONSCONTEXTHELPBUTTON1, 
 wxID_FRAMEOPTIONSPANEL1, wxID_FRAMEOPTIONSSTATICTEXT1, 
 wxID_FRAMEOPTIONSSTATICTEXT2, wxID_FRAMEOPTIONSTXTHOST, 
] = [wx.NewId() for _init_ctrls in range(9)]



def SaveOptions(self):
    direccion = self.txtHost.GetValue()
    local = self.chkLocal.GetValue()
    if not local:
        if not direccion:
            MError(self, u"La casilla 'Ubicaci\xf3n del servidor' debe contener la direcci\xf3n IP del servidor")
            return False
    nombre = 'config%ssmdh.ini'%slash
    fileout = codecs.open(nombre,'w','utf-8')
    fileout.write('[DEFAULT]\n')
    fileout.write('\n')
    fileout.write('host = %s\n'%direccion)
    fileout.close()
    MError(self, u"El programa debe ser reiniciado ahora")
    exit()
    

class FrameOptions(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEOPTIONS, name='FrameOptions',
              parent=prnt, pos=wx.Point(447, 289), size=wx.Size(506, 259),
              style=wx.DEFAULT_FRAME_STYLE, title='Opciones')
        self.SetClientSize(wx.Size(490, 223))

        self.panel1 = wx.Panel(id=wxID_FRAMEOPTIONSPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(490, 223),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetHelpText('')
        self.panel1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'MS Shell Dlg 2'))

        self.staticText1 = wx.StaticText(id=wxID_FRAMEOPTIONSSTATICTEXT1,
              label='Ubicaci\xf3n del servidor', name='staticText1',
              parent=self.panel1, pos=wx.Point(40, 64), size=wx.Size(104, 13),
              style=0)

        self.txtHost = wx.TextCtrl(id=wxID_FRAMEOPTIONSTXTHOST, name='txtHost',
              parent=self.panel1, pos=wx.Point(160, 56), size=wx.Size(168, 21),
              style=0, value='')

        self.buttonOK = wx.Button(id=wxID_FRAMEOPTIONSBUTTONOK, label='Aceptar',
              name='buttonOK', parent=self.panel1, pos=wx.Point(152, 120),
              size=wx.Size(75, 23), style=0)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.OnButtonOKButton,
              id=wxID_FRAMEOPTIONSBUTTONOK)

        self.buttonCancel = wx.Button(id=wxID_FRAMEOPTIONSBUTTONCANCEL,
              label='Cancelar', name='buttonCancel', parent=self.panel1,
              pos=wx.Point(264, 120), size=wx.Size(75, 23), style=0)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.OnButtonCancelButton,
              id=wxID_FRAMEOPTIONSBUTTONCANCEL)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self.panel1,
              pos=wx.Point(456, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)
        self.contextHelpButton1.Bind(wx.EVT_HELP, self.OnContextHelpButton1Help,
              id=wxID_FRAMEOPTIONSCONTEXTHELPBUTTON1)

        self.chkLocal = wx.CheckBox(id=wxID_FRAMEOPTIONSCHKLOCAL, label='',
              name='chkLocal', parent=self.panel1, pos=wx.Point(312, 16),
              size=wx.Size(24, 13), style=0)
        self.chkLocal.SetValue(True)
        self.chkLocal.SetAutoLayout(False)
        self.chkLocal.Set3StateValue(0)
        self.chkLocal.SetToolTipString('')
        self.chkLocal.Bind(wx.EVT_CHECKBOX, self.OnChkLocalCheckbox,
              id=wxID_FRAMEOPTIONSCHKLOCAL)

        self.staticText2 = wx.StaticText(id=wxID_FRAMEOPTIONSSTATICTEXT2,
              label='Esta aplicaci\xf3n se ejecuta en el equipo servidor',
              name='staticText2', parent=self.panel1, pos=wx.Point(40, 16),
              size=wx.Size(226, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.txtHost.SetHelpText('Esta casilla debe contener la direccion del servidor de la base de datos. Si el equipo que usted esta operando hospeda tambien la base de datos, esta casilla queda en blanco. En caso contrario, debe contener la direccion IP, con el formato ###.###.###.###')
        self.txtHost.SetValue(host)
        setWindow(self, host)
        
            

    def OnButtonOKButton(self, event):
        res = SaveOptions(self)
        if res:
            self.Close()
        event.Skip()

    def OnButtonCancelButton(self, event):
        self.Close()
        event.Skip()

    def OnContextHelpButton1Help(self, event):
        event.Skip()

    def OnChkLocalCheckbox(self, event):
        esLocal = self.chkLocal.GetValue()
        if esLocal:
            self.txtHost.SetValue('')
            setWindow(self, '')
        else:
            setWindow(self, 'xx')
        event.Skip()
def setWindow(self, hostName):
    local = hostName in ['localhost', '', '127.0.0.1']
    self.staticText1.Show(not local)
    self.txtHost.Show(not local)
    self.chkLocal.SetValue(local)
    
    
        

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
