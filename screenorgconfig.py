#-----------------------------------------------------------------------------
# Name:        screenorgconfig.py
#
#
# RCS-ID:      $Id: screenorgconfig.py $
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
#Boa:Frame:FrameDataOrg

import wx
import wx.lib.masked.numctrl
import wx.lib.stattext
import wx.lib.filebrowsebutton
from  module2 import ConfigTdt, status, myHash, MError, LlenaCtrlCategoria, LlenaCtrlMunicipios, CtrlSelect, MyClientData, TesById
import pickle
import module2
import cnf
import sys

session = status.session

seHaGuardado = False

def create(parent):
    return FrameDataOrg(parent)

[wxID_FRAMEDATAORG, wxID_FRAMEDATAORGBTNCERRAR, wxID_FRAMEDATAORGBTNGUARDAR, 
 wxID_FRAMEDATAORGFPESTADO, wxID_FRAMEDATAORGFPMUNICIPIO, 
 wxID_FRAMEDATAORGGENSTATICTEXT1, wxID_FRAMEDATAORGPANEL1, 
 wxID_FRAMEDATAORGSTATICTEXT1, wxID_FRAMEDATAORGSTATICTEXT2, 
 wxID_FRAMEDATAORGSTATICTEXT4, wxID_FRAMEDATAORGSTATICTEXT5, 
 wxID_FRAMEDATAORGSTATICTEXT6, wxID_FRAMEDATAORGSTATICTEXT7, 
 wxID_FRAMEDATAORGTXTCLAVE, wxID_FRAMEDATAORGTXTHASH, 
 wxID_FRAMEDATAORGTXTMEMBRETE, wxID_FRAMEDATAORGTXTNOMBRE, 
] = [wx.NewId() for _init_ctrls in range(17)]

class FrameDataOrg(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEDATAORG, name='FrameDataOrg',
              parent=prnt, pos=wx.Point(323, 122), size=wx.Size(765, 507),
              style=wx.DEFAULT_FRAME_STYLE,
              title='Datos de la organizaci\xf3n')
        self.SetClientSize(wx.Size(749, 471))
        self.Bind(wx.EVT_CLOSE, self.OnFrameDataOrgClose)

        self.panel1 = wx.Panel(id=wxID_FRAMEDATAORGPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(749, 471),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetToolTipString('')
        self.panel1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'MS Shell Dlg 2'))

        self.staticText1 = wx.StaticText(id=wxID_FRAMEDATAORGSTATICTEXT1,
              label='Nombre de la organizaci\xf3n', name='staticText1',
              parent=self.panel1, pos=wx.Point(56, 56), size=wx.Size(144, 32),
              style=wx.ST_NO_AUTORESIZE)

        self.staticText2 = wx.StaticText(id=wxID_FRAMEDATAORGSTATICTEXT2,
              label='Clave', name='staticText2', parent=self.panel1,
              pos=wx.Point(56, 104), size=wx.Size(128, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAMEDATAORGSTATICTEXT4,
              label='Membrete', name='staticText4', parent=self.panel1,
              pos=wx.Point(56, 248), size=wx.Size(120, 13), style=0)

        self.txtNombre = wx.TextCtrl(id=wxID_FRAMEDATAORGTXTNOMBRE,
              name='txtNombre', parent=self.panel1, pos=wx.Point(200, 56),
              size=wx.Size(520, 40), style=0, value='')
        self.txtNombre.SetToolTipString('')

        self.txtMembrete = wx.TextCtrl(id=wxID_FRAMEDATAORGTXTMEMBRETE,
              name='txtMembrete', parent=self.panel1, pos=wx.Point(56, 264),
              size=wx.Size(664, 120), style=wx.TE_MULTILINE, value='')
        self.txtMembrete.SetToolTipString('Texto para la caratula de los reportes')

        self.genStaticText1 = wx.lib.stattext.GenStaticText(ID=wxID_FRAMEDATAORGGENSTATICTEXT1,
              label='Datos generales', name='genStaticText1',
              parent=self.panel1, pos=wx.Point(308, 10), size=wx.Size(132, 19),
              style=0)
        self.genStaticText1.Center(wx.HORIZONTAL)
        self.genStaticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.btnGuardar = wx.Button(id=wxID_FRAMEDATAORGBTNGUARDAR,
              label='Guardar', name='btnGuardar', parent=self.panel1,
              pos=wx.Point(272, 400), size=wx.Size(75, 23), style=0)
        self.btnGuardar.Bind(wx.EVT_BUTTON, self.OnBtnGuardarButton,
              id=wxID_FRAMEDATAORGBTNGUARDAR)

        self.staticText5 = wx.StaticText(id=wxID_FRAMEDATAORGSTATICTEXT5,
              label='C\xf3digo de verificaci\xf3n', name='staticText5',
              parent=self.panel1, pos=wx.Point(56, 128), size=wx.Size(106, 13),
              style=0)

        self.txtHash = wx.TextCtrl(id=wxID_FRAMEDATAORGTXTHASH, name='txtHash',
              parent=self.panel1, pos=wx.Point(200, 128), size=wx.Size(100, 16),
              style=0, value='')

        self.staticText6 = wx.StaticText(id=wxID_FRAMEDATAORGSTATICTEXT6,
              label='Estado', name='staticText6', parent=self.panel1,
              pos=wx.Point(56, 160), size=wx.Size(128, 13), style=0)

        self.staticText7 = wx.StaticText(id=wxID_FRAMEDATAORGSTATICTEXT7,
              label='Municipio', name='staticText7', parent=self.panel1,
              pos=wx.Point(56, 184), size=wx.Size(128, 13), style=0)

        self.FPEstado = wx.Choice(choices=[], id=wxID_FRAMEDATAORGFPESTADO,
              name='FPEstado', parent=self.panel1, pos=wx.Point(200, 152),
              size=wx.Size(304, 21), style=0)
        self.FPEstado.Bind(wx.EVT_CHOICE, self.OnFPEstadoChoice,
              id=wxID_FRAMEDATAORGFPESTADO)

        self.FPMunicipio = wx.Choice(choices=[],
              id=wxID_FRAMEDATAORGFPMUNICIPIO, name='FPMunicipio',
              parent=self.panel1, pos=wx.Point(200, 176), size=wx.Size(304, 21),
              style=0)
        self.FPMunicipio.Bind(wx.EVT_CHOICE, self.OnFPMunicipioChoice,
              id=wxID_FRAMEDATAORGFPMUNICIPIO)

        self.txtClave = wx.lib.masked.numctrl.NumCtrl(id=wxID_FRAMEDATAORGTXTCLAVE,
              name='txtClave', parent=self.panel1, pos=wx.Point(200, 104),
              size=wx.Size(106, 22), style=0, value=0)

        self.btnCerrar = wx.Button(id=wxID_FRAMEDATAORGBTNCERRAR,
              label='Cerrar', name='btnCerrar', parent=self.panel1,
              pos=wx.Point(360, 400), size=wx.Size(75, 23), style=0)
        self.btnCerrar.Bind(wx.EVT_BUTTON, self.OnBtnCerrarButton,
              id=wxID_FRAMEDATAORGBTNCERRAR)

    def __init__(self, parent):
        self._init_ctrls(parent)
        LoadData(self)
        if cnf.OSlinux:
            module2.choiceFix(self, __name__)

    def OnBtnGuardarButton(self, event):
        event.Skip()
        SaveData(self)
        MError(self, u"El sistema ser\xe1 cerrado ahora.")
        sys.exit()        

    def OnFrameDataOrgClose(self, event):
        if not seHaGuardado:
            MError(self, u"Advertencia: no se ha grabado la informaci\xf3n de la organizaci\xf3n")
        self.MakeModal(False) 
        self.Destroy()
        
        

        
       

    def OnFPEstadoChoice(self, event):
        
        i = self.FPEstado.Selection
        Edo  = self.FPEstado.GetClientData(i)
        
        self.Estado = Edo.id if Edo else None
        if not self.Estado:
            self.Municipio = None
            
        
            
        
        #LlenaCtrlChildren(self.FPMunicipio, Edo, orden="descripcion")
        LlenaCtrlMunicipios(self.FPMunicipio, Edo) 
        
        event.Skip()

    def OnFPMunicipioChoice(self, event):
        i = self.FPMunicipio.Selection
        Mpo = self.FPMunicipio.GetClientData(i)
        self.Municipio = Mpo.id if Mpo else None
        event.Skip()

    def OnBtnCerrarButton(self, event):
        if not seHaGuardado:
            MError(self, u"Advertencia: no se ha grabado la informaci\xf3n de la organizaci\xf3n")
        self.MakeModal(False) 
        self.Destroy()
        self.Close()
        
def nada():
    return  
def LoadData(self):
    self.registro=session.query(ConfigTdt).filter(ConfigTdt.tipo == u'OrgData').all()
    registro = self.registro
    opciones = {}
    if registro:
        registro = registro[0]
        try:
            opciones = pickle.loads(str(registro.contenido))
        except:
            opciones = {}
    
    llaves = opciones.keys()
    for campo in ['txtNombre','txtClave','txtMembrete','txtHash' ]:
        ctrl=getattr(self,campo)
        try:
            ctrl.SetValue(opciones[campo].decode( "utf-8" ) if campo in opciones.keys() else '')
        except:
            print "no se pudo fijar valor de ",campo
    
    LlenaCtrlCategoria(self.FPEstado, u'T63')
    self.Estado = 0
    self.Municipio = 0
    if 'Estado' in opciones.keys():
        try:
           self.Estado = opciones['Estado']
           Edo = TesById(self.Estado)
           
           CtrlSelect(self.FPEstado, Edo.descripcion)
        except:
            self.Estado = 0
    if 'Municipio' in opciones.keys():
        try:
            self.Municipio = opciones['Municipio']
            Mpo = TesById(self.Municipio)
            Tmunicipo = ''
            if Mpo:
                Tmunicipo = Mpo.descripcion
        except:
            self.Municipio = 0
    if self.Estado:
        
        LlenaCtrlMunicipios(self.FPMunicipio,Edo, selected=Tmunicipo)
    
    
def SaveData(self):
    global seHaGuardado
    self.registro=session.query(ConfigTdt).filter(ConfigTdt.tipo == u'OrgData').all()
    registro = self.registro
    if registro:
        registro = registro[0]
    else:
        registro = ConfigTdt(u'OrgData')
        registro.descripcion = u'Datos de la organizacion'
    opciones = {}
    for campo in ['txtNombre','txtMembrete','txtHash']:
        ctrl=getattr(self,campo)
        tmpA = ctrl.GetValue()
        opciones[campo]= tmpA.encode( "utf-8" )
    i=self.txtClave.GetValue()
    opciones['txtClave']=str(i).encode("utf-8")
    
    #opciones['browserLogo'] = self.browserLogo.GetValue()
    opciones['Estado']=self.Estado
    opciones['Municipio']=self.Municipio
    errorHash=False
    if opciones['txtHash']:
        if opciones['txtHash'] != myHash(opciones['txtClave']):
            MError(self, u"El c\xf3digo de verificaci\xf3n no corresponde a la clave de la organizaci\xf3n. Debes corregirlo o dejarlo en blanco")
            errorHash = True
    else:
        MError(self, u"El c\xf3digo de verificaci\xf3n no esta presente")
    aDebug =     pickle.dumps(opciones)
    if not errorHash:
        registro.contenido=pickle.dumps(opciones)
        session.add(registro)
        session.flush()
        MError(self, u"Se ha grabado la informaci\xf3n de la organizaci\xf3n")
        seHaGuardado = True
    else:
        MError(self, u"La informaci\xf3n de la organizaci\xf3n no se ha grabado")

    
        



    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
