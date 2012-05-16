#-----------------------------------------------------------------------------
# Name:        Frame1.py
#
#
# RCS-ID:      $Id: Frame1.py $
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
#Boa:Frame:Frame1


#enie  \xf1
#a   \xe1
#e   \xe9
#i   \xed
#o   \xf3
#u   \xfa
#interr \xbf

#U  \xda
#O \xd3

import wx
import sys
#import from cnf import db, host, user, passwd
import cnf 
import pickle
from os import name as NameOS

slash = '\\'
if NameOS in ['posix']:
    slash = '/'
def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTNCONFIGLOCAL, wxID_FRAME1BTNDATOSGENERALES, 
 wxID_FRAME1BTNGRUPOS, wxID_FRAME1BTNLOGIN, wxID_FRAME1BTNUTILS, 
 wxID_FRAME1BUTTON1, wxID_FRAME1BUTTONUSERS, wxID_FRAME1BUTTONVOCABULARIOS, 
 wxID_FRAME1CONFIGURACION, wxID_FRAME1EXPORTARDATOS, wxID_FRAME1IMPORTARDATOS, 
 wxID_FRAME1PANEL1, wxID_FRAME1STATICBITMAP1, wxID_FRAME1STATICSTATUS, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, 
 wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICVERSION, wxID_FRAME1TEXTPASSWD, 
 wxID_FRAME1TEXTUSERNAME, wxID_FRAME1TXTDB, 
] = [wx.NewId() for _init_ctrls in range(23)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(555, 12), size=wx.Size(650, 603),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Men\xfa general')
        self.SetClientSize(wx.Size(634, 567))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.Show(False)
        self.Bind(wx.EVT_ACTIVATE, self.OnFrame1Activate)
        self.Bind(wx.EVT_CLOSE, self.OnFrame1Close)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(634, 567),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(240, 240, 232))
        self.panel1.SetLabel('')
        self.panel1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'MS Shell Dlg 2'))
        self.panel1.SetHelpText('ayuda')

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label=u'Manejo de Casos.', name='button1', parent=self.panel1,
              pos=wx.Point(8, 16), size=wx.Size(160, 23), style=0)
        self.button1.Show(False)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButtonRegistrodecasos,
              id=wxID_FRAME1BUTTON1)

        self.buttonVocabularios = wx.Button(id=wxID_FRAME1BUTTONVOCABULARIOS,
              label=u'Manejo de vocabularios', name='buttonVocabularios',
              parent=self.panel1, pos=wx.Point(8, 208), size=wx.Size(160, 23),
              style=0)
        self.buttonVocabularios.Show(False)
        self.buttonVocabularios.Bind(wx.EVT_BUTTON, self.OnButtonVocabularios,
              id=wxID_FRAME1BUTTONVOCABULARIOS)

        self.btnUtils = wx.Button(id=wxID_FRAME1BTNUTILS, label=u'Herramientas',
              name='btnUtils', parent=self.panel1, pos=wx.Point(8, 112),
              size=wx.Size(160, 23), style=0)
        self.btnUtils.Show(False)
        self.btnUtils.Bind(wx.EVT_BUTTON, self.OnBtnUtils,
              id=wxID_FRAME1BTNUTILS)

        self.staticVersion = wx.StaticText(id=wxID_FRAME1STATICVERSION,
              label='Ver 2.00B 19-ago-09', name='staticVersion',
              parent=self.panel1, pos=wx.Point(496, 8), size=wx.Size(101, 13),
              style=0)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap('bin/redtdt.GIF',
              wx.BITMAP_TYPE_GIF), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self.panel1, pos=wx.Point(184, 160),
              size=wx.Size(256, 240), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Sistema de monitoreo de derechos humanos de la Red Nacional de Organismos Civiles de Derechos Humanos "Todos los derechos para todas y todos"',
              name='staticText3', parent=self.panel1, pos=wx.Point(78, 427),
              size=wx.Size(477, 61), style=wx.ST_NO_AUTORESIZE+wx.ALIGN_CENTRE)
        self.staticText3.Center(wx.HORIZONTAL)
        self.staticText3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Dise\xf1ado sobre la base del Sistema de Huridocs',
              name='staticText4', parent=self.panel1, pos=wx.Point(174, 544),
              size=wx.Size(285, 13), style=0)
        self.staticText4.Center(wx.HORIZONTAL)

        self.Configuracion = wx.Button(id=wxID_FRAME1CONFIGURACION,
              label=u'Configuraci\xf3n de campos', name='Configuracion',
              parent=self.panel1, pos=wx.Point(8, 80), size=wx.Size(160, 23),
              style=0)
        self.Configuracion.Show(False)
        self.Configuracion.Bind(wx.EVT_BUTTON, self.OnConfiguracionButton,
              id=wxID_FRAME1CONFIGURACION)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Usuari@', name='staticText2', parent=self.panel1,
              pos=wx.Point(185, 14), size=wx.Size(71, 13), style=0)

        self.textUserName = wx.TextCtrl(id=wxID_FRAME1TEXTUSERNAME,
              name='textUserName', parent=self.panel1, pos=wx.Point(256, 8),
              size=wx.Size(160, 21), style=wx.TE_PROCESS_ENTER, value='')
        self.textUserName.SetToolTipString('')
        self.textUserName.Bind(wx.EVT_TEXT_ENTER, self.OnTextUserNameTextEnter,
              id=wxID_FRAME1TEXTUSERNAME)

        self.textPasswd = wx.TextCtrl(id=wxID_FRAME1TEXTPASSWD,
              name='textPasswd', parent=self.panel1, pos=wx.Point(256, 32),
              size=wx.Size(160, 21), style=wx.TE_PASSWORD, value='')
        self.textPasswd.SetToolTipString('')

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Contrase\xf1a', name='staticText5', parent=self.panel1,
              pos=wx.Point(185, 38), size=wx.Size(71, 13), style=0)

        self.btnLogin = wx.Button(id=wxID_FRAME1BTNLOGIN, label=u'Conectar',
              name='btnLogin', parent=self.panel1, pos=wx.Point(296, 60),
              size=wx.Size(75, 23), style=0)
        self.btnLogin.SetDefault()
        self.btnLogin.Bind(wx.EVT_BUTTON, self.OnBtnLoginButton,
              id=wxID_FRAME1BTNLOGIN)

        self.buttonUsers = wx.Button(id=wxID_FRAME1BUTTONUSERS,
              label='Administraci\xf3n de usuari@s', name='buttonUsers',
              parent=self.panel1, pos=wx.Point(8, 144), size=wx.Size(160, 23),
              style=0)
        self.buttonUsers.Show(False)
        self.buttonUsers.Bind(wx.EVT_BUTTON, self.OnButtonUsersButton,
              id=wxID_FRAME1BUTTONUSERS)

        self.staticStatus = wx.StaticText(id=wxID_FRAME1STATICSTATUS,
              label=u'Un momento...', name='staticStatus', parent=self.panel1,
              pos=wx.Point(299, 96), size=wx.Size(73, 13), style=0)
        self.staticStatus.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))
        self.staticStatus.Show(False)

        self.btnConfigLocal = wx.Button(id=wxID_FRAME1BTNCONFIGLOCAL,
              label=u'Configuraci\xf3n local', name='btnConfigLocal',
              parent=self.panel1, pos=wx.Point(8, 48), size=wx.Size(160, 23),
              style=0)
        self.btnConfigLocal.Bind(wx.EVT_BUTTON, self.OnBtnConfigLocalButton,
              id=wxID_FRAME1BTNCONFIGLOCAL)

        self.btnDatosGenerales = wx.Button(id=wxID_FRAME1BTNDATOSGENERALES,
              label=u'Datos generales', name='btnDatosGenerales',
              parent=self.panel1, pos=wx.Point(8, 176), size=wx.Size(160, 23),
              style=0)
        self.btnDatosGenerales.Show(False)
        self.btnDatosGenerales.Bind(wx.EVT_BUTTON,
              self.OnBtnDatosGeneralesButton, id=wxID_FRAME1BTNDATOSGENERALES)

        self.ImportarDatos = wx.Button(id=wxID_FRAME1IMPORTARDATOS,
              label='Importar datos', name='ImportarDatos', parent=self.panel1,
              pos=wx.Point(8, 240), size=wx.Size(160, 23), style=0)
        self.ImportarDatos.Show(False)
        self.ImportarDatos.Bind(wx.EVT_BUTTON, self.OnImportarDatosButton,
              id=wxID_FRAME1IMPORTARDATOS)

        self.ExportarDatos = wx.Button(id=wxID_FRAME1EXPORTARDATOS,
              label='Exportar datos', name='ExportarDatos', parent=self.panel1,
              pos=wx.Point(8, 272), size=wx.Size(160, 23), style=0)
        self.ExportarDatos.Show(False)
        self.ExportarDatos.Bind(wx.EVT_BUTTON, self.OnExportarDatosButton,
              id=wxID_FRAME1EXPORTARDATOS)

        self.btnGrupos = wx.Button(id=wxID_FRAME1BTNGRUPOS,
              label='Administraci\xf3n de grupos', name='btnGrupos',
              parent=self.panel1, pos=wx.Point(8, 304), size=wx.Size(160, 23),
              style=0)
        self.btnGrupos.Show(False)
        self.btnGrupos.Bind(wx.EVT_BUTTON, self.OnBtnGruposButton,
              id=wxID_FRAME1BTNGRUPOS)

        self.txtDB = wx.StaticText(id=wxID_FRAME1TXTDB,
              label='                                                   ',
              name='txtDB', parent=self.panel1, pos=wx.Point(496, 40),
              size=wx.Size(153, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.Move(wx.Point(0, 0))
        self.staticVersion.SetLabel('Ver. %s %s'%(cnf.PRGversion, cnf.PRGdate))
        nombreLogo = 'bin%sredtdt.GIF'%slash
        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(nombreLogo,
              wx.BITMAP_TYPE_GIF), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self.panel1, pos=wx.Point(184, 160),
              size=wx.Size(256, 240), style=0)
        db=cnf.db
        self.db = cnf.db
        if db != 'redtdt':
            self.txtDB.SetLabel(db)
        
        self.cnfBaseCentral = db in ["redtdtcentral","'redtdtcentral'"]
        
        self.btnUtils.Enable(cnf.localhost)
        
        

    def OnButtonRegistrodecasos(self, event):
        self.staticStatus.Show()
        self.Update()
        from Frame2 import Frame2
        import FrameUser
        import module2
        self.staticStatus.Show(False)
        module2.status.usuarioActual = FrameUser.GetUser(self.textUserName.GetValue())
        
        if module2.status.usuarioActual:
            #self.Iconize(True)
            module2.status.userID = module2.status.usuarioActual.id
            module2.status.UserLevel = module2.status.usuarioActual.nivel
            print module2.status.userID, module2.status.UserLevel
            f=Frame2(self)
            f.MakeModal()
            f.Show()
            
        else:
            module2.MError(self, u"No se identifica un usuario v\xe1lido")
        event.Skip()

    def OnButtonVocabularios(self, event):
        from FrameVocab import FrameVocab
        f=FrameVocab(self)
        
        f.Show()
        event.Skip()

    

    def OnBtnUtils(self, event):
        from FrameUtils import muestraFrameUtils
        muestraFrameUtils(self)
        event.Skip()

    def OnButtonVocabularios(self, event):
        from FrameVocab import FrameVocab
        f=FrameVocab(self)
        f.MakeModal()
        f.Show()
        event.Skip()

    def OnFrame1Activate(self, event):
        
        event.Skip()

    def OnFrame1Close(self, event):
        import module2
        if module2.status.session:
            
            module2.status.session.expunge_all()
            # module2.status.engine.dispose() ???
            module2.status.session.close()
            module2.status.engine.dispose()
            
            
        
        sys.exit()
        
        event.Skip()

    def OnConfiguracionButton(self, event):
        import screenconfig  
        f=screenconfig.Frame3(self)
        f.MakeModal()
        f.Show()
        
        event.Skip()

    def OnTextUserNameTextEnter(self, event):
        import module2
        
        event.Skip()

    def OnBtnLoginButton(self, event):
        self.staticStatus.Show()
        self.Update()
        cnf.user = self.textUserName.GetValue()
        cnf.passwd = self.textPasswd.GetValue()
        
        self.btnLogin.Show(False)
        self.btnConfigLocal.Show(False)
        
        import FrameUser
        import module2
        
        
        
        
        self.staticStatus.Show(False)
        module2.status.usuarioActual = FrameUser.GetUser(self.textUserName.GetValue())
        t1 = cnf.user in cnf.adminAccount
        t3 = cnf.user in cnf.adminAccount and module2.status.OrgClave < 100 and module2.status.OrgClave > 0
        
        t2 = not t1
        if not module2.status.usuarioActual and t2:
            module2.MError(self, u"No fue posible hacer la conexi\xf3n con la base de datos. Verifique que el nombre de usuario y contrase\xf1a est\xe9n correctamente ingresados")
            sys.exit()
            
        
        
         
        if t2 and  module2.status.usuarioActual.nivel > 100:
            module2.MError(self, u"Esta cuenta de usuario no tiene acceso a la base de datos")
            sys.exit()
        
        if not module2.status.sinTablas:
              ChecaVersion(self, module2)
        
        self.btnUtils.Show(t1)
        if not module2.status.sinTablas:
            self.buttonUsers.Show(t1)
            self.Configuracion.Show(t1)
            
            self.btnDatosGenerales.Show(t1)
            self.ExportarDatos.Show(t1 and not self.cnfBaseCentral)
            self.ImportarDatos.Show(t3 and self.cnfBaseCentral)
            if t2: self.button1.SetDefault()
            self.button1.Show(t2)
            self.buttonVocabularios.Show(t3)
            self.btnGrupos.Show(t3 and self.cnfBaseCentral)

        event.Skip()

    def OnButtonUsersButton(self, event):
        
        from FrameUser import FrameUser
        f=FrameUser(self)
        f.Show()
        
        event.Skip()

    def OnBtnConfigLocalButton(self, event):
        from FrameOptions import FrameOptions
        f=FrameOptions(self)
        f.Show()
        
        event.Skip()

    def OnBtnDatosGeneralesButton(self, event):
        from screenorgconfig import FrameDataOrg
        f=FrameDataOrg(self)
        f.MakeModal()
        f.Show()
        
        
        
        
        

    def OnImportarDatosButton(self, event):
        from dashboard1 import dashboard1
        f=dashboard1(self)
        
        f.Show()
        event.Skip()

    def OnExportarDatosButton(self, event):
        from FrameExp1 import FrameExp
        f=FrameExp(self)
        f.Show()
        
        
        
        event.Skip()

    def OnBtnGruposButton(self, event):
        from FrameGrupos import FrameGrupos
        f=FrameGrupos(self)
        f.Show()
        event.Skip()

        
def ChecaVersion(self, module2):
    ConfigTdt = module2.ConfigTdt
    session = module2.session
    PRGversion = cnf.PRGversion
    DBversion = '00.80'
    registro=session.query(ConfigTdt).filter(ConfigTdt.tipo == u'DBversion').all()
    opciones = {}
    if registro:
        try:
            l = registro[0]
            opciones = pickle.loads(str(l.contenido))
            print "opciones", opciones
            if 'DBversion' in opciones.keys():
                DBversion = opciones['DBversion']
        except:
            print u"no se leyo dbversion"
    if PRGversion != DBversion:
        import FrameUpdate
        FrameUpdate.Updates(self, DBversion)
        
    
            
        
        

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
