#-----------------------------------------------------------------------------
# Name:        FrameUser.py
#
#
# RCS-ID:      $Id: FrameUser.py $
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
#Boa:Frame:FrameUser


import wx
import sys
import re
from dlggetpass import MyPass


from sqlalchemy import MetaData, Table, Column, Sequence, ForeignKey
from sqlalchemy import Integer, String, sql, Date, TEXT, Unicode, create_engine
from sqlalchemy.orm import create_session, mapper, relation, backref, aliased
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.orm import PropComparator, column_property, deferred
from sqlalchemy.sql import select


from module2 import MError, User, LlenaCtrl3, status, MyClientData, CtrlSelect, Borrar
from dlggetdescrip import MyDescrip
from cnf import db
import module2
import cnf

session = status.session


#HOST='localhost'
#PASS='macana'
#specAdmin = 'postgres://postgres:'+PASS+'@'+HOST+'/'+'redtdt'
#metadataAdmin = MetaData(specAdmin)
#engineAdmin = create_engine(specAdmin)
#session = create_session(bind=engineAdmin)
     

def GenericPermissions():
    session.bind.echo = True
    r=session.execute("select tablename from pg_tables where schemaname = 'public'")
    tablas=r.fetchall()
    r=session.execute("select relname from pg_class where relkind = 'S'")
    secuencias = r.fetchall()
    
    if 'usuario' in tablas:
        tablas.remove('usuario')
    tablas = [i[0] for i in tablas]
    tablas = ','.join(tablas)
    
    secuencias = [i[0] for i in secuencias]
    secuencias = ','.join(secuencias)
    
    # checa si existe el rol tdt_editor y en ese caso crear el rol
    r=session.execute("select rolname from pg_roles where rolname = 'tdt_editor'")
    x = r.fetchall()
    
    if not x:
        session.begin()
        x=session.execute("create role tdt_editor")
        session.commit()
    # checa si existe el rol tdt_lector y en ese caso crear el rol   
    r=session.execute("select rolname from pg_roles where rolname = 'tdt_lector'")
    x= r.fetchall()
    if not x:
        session.begin()
        x=session.execute("create role tdt_lector")
        session.commit()
   
    # concede derechos de conexion a la base de datos redtdt a ambos roles
    session.begin()
    # mucho ojo
    myDB = db.replace("'",'')
    comando = "GRANT connect on database %s to tdt_lector"%myDB
    x=session.execute(comando)
    
    comando = "GRANT connect on database %s to tdt_editor"%myDB
    x=session.execute(comando)
    session.commit()

    
    
    # concede derechos de lectura  al rol tdt_lector a las tablas existentes.
    session.begin()
    comando = "GRANT USAGE ON SCHEMA public to tdt_lector, tdt_editor"
    x=session.execute(comando)
    session.commit()
    
    comando = "GRANT SELECT on %s to tdt_lector"%tablas
    session.begin()
    x=session.execute(comando)
    
    # concede derechos de lectura u escritura al rol tdt_editor a las tablas existentes. excluir luego 
    # la tabla de usuario   
    comando = "GRANT SELECT,insert, update, delete on %s to tdt_editor"%tablas
    x=session.execute(comando)

    
    comando = "GRANT USAGE, SELECT, UPDATE on %s to tdt_editor"%secuencias
    x=session.execute(comando)
    session.commit()
    
    
def ReasignaPerms(self):
    usuarios = session.query(User)
    for U in usuarios:
        
        
        
        
        
          if U.nivel <=10:
                grupo = 'tdt_editor'
          elif U.nivel < 100:
                grupo = 'tdt_lector'
          else:
                grupo = None
          res = sqlAddUser(self, U.nombre,'')
          if res:
              MError(self, u"Debido a la recuperaci\xf3n del respaldo, debes asignar de nuevo la contrase\xf1a del usuario"%U.nombre)
          sqlAssignPerm(self, U.nombre, grupo)



def sqlAddUser(self, name, passwd):
    comando = "CREATE ROLE %s LOGIN INHERIT PASSWORD '%s'"%(name, passwd)
    try:
        session.begin()
        session.execute(comando)
        session.commit()
        return True
    except:
        session.rollback()
        x = sqlChangePass(self, name, passwd)
        return x
    
def sqlChangePass(self, name, passwd):
    comando = "ALTER ROLE %s PASSWORD '%s'"%(name, passwd)
    try:
        session.begin()
        session.execute(comando)
        session.commit()
        return True
    except:
        session.rollback()
        return False
def sqlDelUser(self, usuarioAborrar):
    name = usuarioAborrar.nombre
    comando = "DROP ROLE %s "%(name)
    try:
        session.begin()
        session.execute(comando)
        session.delete(usuarioAborrar)
        
        session.commit()
        session.flush()
        return True
    except:
        return False
def sqlAssignPerm(self, name, group):
    
    try:
        session.begin()
        comando = "REVOKE tdt_lector from %s "%(name)
        session.execute(comando)
        session.commit()
    except:
        session.commit()
        nada = 1
    try:
        session.begin()
        comando = "REVOKE tdt_editor from %s"%(name)
        session.execute(comando)
        session.commit()
    except:
        session.commit()
        nada =1
    
    if group:
        try:
            comando = "GRANT %s to %s"%(group, name)
            session.begin()
            session.execute(comando)
            session.commit()
            return True
        except:
            return False

def create(parent):
    return FrameUser(parent)

[wxID_FRAMEUSER, wxID_FRAMEUSERBTNCERRAR, wxID_FRAMEUSERBUTTONDELUSER, 
 wxID_FRAMEUSERCHANGEPASSWORD, wxID_FRAMEUSERCHOICE1, wxID_FRAMEUSERLISTUSER, 
 wxID_FRAMEUSERNUEVA, wxID_FRAMEUSERSTATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(8)]


def LlenaNombres(self): 
    usuarios = [(i, i.nombre) for i in session.query(User).filter(User.id < 9999).all()]
    LlenaCtrl3(self.listUser, usuarios)
    niveles = [(i,Niveles[i]) for i in Niveles.keys()]
    niveles.sort(lambda x,y:cmp(x[0] ,y[0]))
    
    LlenaCtrl3(self.choice1, niveles, orden=None)
def GetUser(nombre):
    print "get user"
    try:
        q=session.query(User)
        U = q.filter(User.nombre == nombre).all()
        U = U[0] if U else None
    except:
        return None
    return U

Niveles = {999:u"Sin acceso",
           #01:u"Administraci\xf3n",
           05:u"Sin restricciones",
           10:u"Captura, consulta y reportes",
           20:u"Reportes y consulta",
           30:u"Solo lectura"
           }
    
    
    
class FrameUser(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEUSER, name='FrameUser',
              parent=prnt, pos=wx.Point(336, 104), size=wx.Size(617, 312),
              style=wx.DEFAULT_FRAME_STYLE, title='Usuarias y usuarios')
        self.SetClientSize(wx.Size(601, 276))

        self.nueva = wx.Button(id=wxID_FRAMEUSERNUEVA, label='Nuev@ usuari@',
              name='nueva', parent=self, pos=wx.Point(16, 136),
              size=wx.Size(112, 23), style=0)
        self.nueva.Bind(wx.EVT_BUTTON, self.OnNuevaButton,
              id=wxID_FRAMEUSERNUEVA)

        self.choice1 = wx.Choice(choices=[], id=wxID_FRAMEUSERCHOICE1,
              name='choice1', parent=self, pos=wx.Point(376, 16),
              size=wx.Size(216, 21), style=0)
        self.choice1.SetLabel('')
        self.choice1.SetToolTipString('Nivel de acceso')
        self.choice1.Enable(False)
        self.choice1.Bind(wx.EVT_CHOICE, self.OnChoice1Choice,
              id=wxID_FRAMEUSERCHOICE1)

        self.staticText1 = wx.StaticText(id=wxID_FRAMEUSERSTATICTEXT1,
              label='Cambiar nivel de acceso', name='staticText1', parent=self,
              pos=wx.Point(256, 24), size=wx.Size(115, 32),
              style=wx.ST_NO_AUTORESIZE)

        self.listUser = wx.ListBox(choices=[], id=wxID_FRAMEUSERLISTUSER,
              name='listUser', parent=self, pos=wx.Point(16, 16),
              size=wx.Size(224, 111), style=0)
        self.listUser.Bind(wx.EVT_LISTBOX_DCLICK, self.OnListUserListboxDclick,
              id=wxID_FRAMEUSERLISTUSER)

        self.buttonDelUser = wx.Button(id=wxID_FRAMEUSERBUTTONDELUSER,
              label='Baja de usuari@', name='buttonDelUser', parent=self,
              pos=wx.Point(136, 136), size=wx.Size(107, 23), style=0)
        self.buttonDelUser.Enable(False)
        self.buttonDelUser.Bind(wx.EVT_BUTTON, self.OnButtonDelUserButton,
              id=wxID_FRAMEUSERBUTTONDELUSER)

        self.btnCerrar = wx.Button(id=wxID_FRAMEUSERBTNCERRAR, label='Cerrar',
              name='btnCerrar', parent=self, pos=wx.Point(240, 240),
              size=wx.Size(75, 23), style=0)
        self.btnCerrar.Bind(wx.EVT_BUTTON, self.OnBtnCerrarButton,
              id=wxID_FRAMEUSERBTNCERRAR)

        self.changePassword = wx.Button(id=wxID_FRAMEUSERCHANGEPASSWORD,
              label='Cambiar contrase\xf1a', name='changePassword', parent=self,
              pos=wx.Point(256, 64), size=wx.Size(112, 23), style=0)
        self.changePassword.Enable(False)
        self.changePassword.Bind(wx.EVT_BUTTON, self.OnChangePasswordButton,
              id=wxID_FRAMEUSERCHANGEPASSWORD)

    def __init__(self, parent):
        self._init_ctrls(parent)
        LlenaNombres(self)
        GenericPermissions()
        self.nombreValido = re.compile('[a-z][a-z0-9]*')
        self.passValida = re.compile('[a-z][a-z0-9]*', re.IGNORECASE)
        if cnf.OSlinux:
            module2.choiceFix(self, __name__)
        
        #ReasignaPerms(self)

    def OnNuevaButton(self, event):
        nombre = MyDescrip(self, titulo='Nombre de la persona')
        nombre = nombre.strip()
        
                
        nombres = [i.nombre for i in session.query(User).all()]
        if nombre:
            if nombre not in nombres:
                res = self.nombreValido.match(nombre)
                if res:
                    if res.group() != nombre:
                          MError(self, u"El nombre de usuario s\xf3lo puede contener letras en min\xfascula y n\xfameros")
                          return
                else:
                    MError(self, u"El nombre de usuario s\xf3lo puede contener letras en min\xfascula y n\xfameros")
                    return
                
                passwd = MyDescrip(self, titulo=u'Contrase\xf1a')
                res = self.passValida.match(passwd)
                if not res:
                    MError(self, u"La contrase\xf1a de usuario s\xf3lo puede contener letras en may\xfascula o min\xfascula, y n\xfameros. Debe comenzar con una letra")
                    return
                if res.group() != passwd:
                    MError(self, u"La contrase\xf1a de usuario s\xf3lo puede contener letras en may\xfascula o min\xfascula, y n\xfameros. Debe comenzar con una letra")
                    return
                
                if passwd:
                    U = User(nombre,10)
                    x = sqlAddUser(self, nombre, passwd)
                    if x:
                        session.add(U)
                    
                        session.flush()
                        sqlAssignPerm(self, U.nombre, 'tdt_editor')
                    else:
                        MError(self, "No fue posible dar de alta este usuario")
                        return
                    LlenaNombres(self)
                    
                    
                else:
                   MError(self, u"La contrase\xf1a es obligatoria. Proceso abortado") 
                   return
            else:
                MError(self, u"Ya existe una persona dada de alta con este nombre")
                return
        

    def OnListUserListboxDclick(self, event):
        status.usuarioActual = MyClientData(event)
        status.userID = status.usuarioActual.id
        status.UserLevel = status.usuarioActual.nivel
        #self.textPass.SetValue('')
        if status.UserLevel in Niveles.keys():
            CtrlSelect(self.choice1, Niveles[status.UserLevel])
        self.choice1.Enable()
        self.changePassword.Enable()
        self.buttonDelUser.Enable()
        event.Skip()

    def OnChoice1Choice(self, event):
        c = event.GetEventObject()
        nivel = c.GetClientData(c.GetSelection())
        
        if status.usuarioActual:
            U = status.usuarioActual
            U.nivel = nivel
            session.add(status.usuarioActual)
            try:
                session.flush()
            except:
                MError(self, "No fue posible guardar cambios")
            
            if nivel <=10:
                grupo = 'tdt_editor'
            elif nivel < 100:
                grupo = 'tdt_lector'
            else:
                grupo = None
            x = sqlAssignPerm(self, U.nombre, grupo)
            if not x:
                nada=1
                #MError(self, "No fue posible asignar privilegios ("+str(sys.exc_info()[1])+')')
                
                
        event.Skip()



    def OnButtonGuardarButton(self, event):
        if status.usuarioActual:
            U = status.usuarioActual
            if self.textPass.GetValue():
                passwd = self.textPass.GetValue()
                passwd = passwd.strip()
                res = self.passValida.match(passwd)
                
                if res and res.group() == passwd:
                    sqlAddUser(self, U.nombre, passwd)
                    
                    nivel = U.nivel
                    if nivel <=10:
                        grupo = 'tdt_editor'
                    elif nivel < 100:
                        grupo = 'tdt_lector'
                    else:
                        grupo = None
                    x = sqlAssignPerm(self, U.nombre, grupo)
                
                    
                    x = sqlChangePass(self, U.nombre, passwd)
                    
                    if not x:
                        MError(self, u"La contrase\xf1a no pudo ser asignada")
                        return
                    else:
                        MError(self, u"Los cambios fueron aplicados")
                else:
                    MError(self, u"La contrase\xf1a de usuario s\xf3lo puede contener letras en may\xfascula o min\xfascula, y n\xfameros. Debe comenzar con una letra")
                    return
                    
                
                
            
        event.Skip()

    def OnButtonDelUserButton(self, event):
        usuarioAborrar = MyClientData(self.listUser)
        if usuarioAborrar.sepuedeborrar():
            if Borrar(self, "Borrar cuenta de usuario?"):
                
                
                session.flush()
                sqlDelUser(self, usuarioAborrar)
                LlenaNombres(self)
                
        else:
            MError(self, u"Este usuario no puede ser borrado ya que tiene datos registrados en el sistema. Puedes desactivar la cuenta asign\xe1ndole el nivel sin acceso")    
            
        event.Skip()

    def OnBtnCerrarButton(self, event):
        self.Close()
        event.Skip()

    def OnChangePasswordButton(self, event):
        print "pidiendo pass"
        if status.usuarioActual:
            U = status.usuarioActual
            
            pass1 = MyPass(self, titulo="Nueva contrase\xf1a")
            pass2 = MyPass(self, titulo="Confirmar contrase\xf1a")
            if pass1 == pass2:
                passwd = pass1.strip()
                res = self.passValida.match(passwd)
                    
                if res and res.group() == passwd:
                    sqlAddUser(self, U.nombre, passwd)
                    
                    nivel = U.nivel
                    if nivel <=10:
                        grupo = 'tdt_editor'
                    elif nivel < 100:
                        grupo = 'tdt_lector'
                    else:
                        grupo = None
                    x = sqlAssignPerm(self, U.nombre, grupo)
                    x = sqlChangePass(self, U.nombre, passwd)
                    MError(self, u"Contrase\xf1a actualizada")
                else:
                    MError(self, u'La contrase\xf1a de usuario s\xf3lo puede contener letras en may\xfascula o min\xfascula, y n\xfameros. Debe comenzar con una letra')
            else:
                MError(self, u'Las contrase\xf1as no coinciden')



if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
