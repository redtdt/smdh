#-----------------------------------------------------------------------------
# Name:        FrameUpdate.py
#
#
# RCS-ID:      $Id: FrameUpdate.py $
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
#Boa:Frame:FrameUpdate

import wx
import cnf
import sys
from module2 import MError, session, ConfigTdt, status
import pickle
import os
import path_postgres


def create(parent):
    return FrameUpdate(parent)

[wxID_FRAMEUPDATE] = [wx.NewId() for _init_ctrls in range(1)]

class FrameUpdate(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEUPDATE, name='FrameUpdate',
              parent=prnt, pos=wx.Point(88, 88), size=wx.Size(408, 507),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame3')
        self.SetClientSize(wx.Size(392, 471))

    def __init__(self, parent):
        self._init_ctrls(parent)
        
def Updates(self, DBversion):
    PRGversion = cnf.PRGversion
    Actualizar = True
    if Actualizar:

        if DBversion < PRGversion:
            if (cnf.user not in cnf.adminAccount) or (not cnf.localhost):
                MError(self, "La base de datos debe ser actualizada antes de proseguir usando el programa. Por favor vuelva a entrar con la cuenta de usuario 'Admin' desde el servidor")
                sys.exit()
            else:
                MError(self, "La base de datos debe ser actualizada antes de proseguir usando el programa")
                Actualiza(self, DBversion, PRGversion)
                return
def Actualiza(self, DBversion, PRGversion):
    Parche(self, DBversion)
    MError(self, u"La base de datos acaba de ser actualizada a la versi\xf3n %s . El programa ser\xe1 cerrado ahora."%str(PRGversion))
    sys.exit()
def Parche(self, DBversion):
    pgpath = path_postgres.path_postgres()
    if pgpath:
        try:
                
                comando = '%s\\parches\\aplicaparchev25.bat %s %s "%s" '%(status.drive+status.path, cnf.passwd, cnf.db, pgpath)
                
                os.system(comando)
                FijaVersion(self, cnf.PRGversion)           
                
        except:
                MError(self, u"La operaci\xf3n no pudo ser efectuada")
                tb=sys.exc_info()[2]
    
                traceback.print_exc()
                
                sys.exit()
    else:
        MError(self, u"No fue posible localizar la instalacion de PostgreSQL")
     
    return       
def FijaVersion(self, PRGversion):
    registro=session.query(ConfigTdt).filter(ConfigTdt.tipo == u'DBversion').all()
    opciones = {}
    l = None
    if registro:
        try:
            l = registro[0]
            opciones = pickle.loads(str(l.contenido))
        except:
            print "error de pickle en fijaversion"
    if not l:
        l = ConfigTdt(u'DBversion')
        
        l.descripcion = u'Version de la base de datos'
    opciones['DBversion']=  PRGversion
    l.contenido=pickle.dumps(opciones)
    session.add(l)
    session.flush()        
    return

