#-----------------------------------------------------------------------------
# Name:        module2.py
#
#
# RCS-ID:      $Id: module2.py $
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

# -*- coding: utf-8 -*-

"""Basic functionality for redtdt"""

#enie  \xf1
#a   \xe1
#e   \xe9
#i   \xed
#o   \xf3
#u   \xfa


import sqlalchemy
from sqlalchemy import MetaData, Table, Column, Sequence, ForeignKey
from sqlalchemy import Integer, String, sql, Date, TEXT, Unicode, create_engine
from sqlalchemy.orm import create_session, mapper, relation, backref, aliased
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.orm import PropComparator, column_property, deferred
from sqlalchemy.sql import select
from configmodule import VDefault
from string import maketrans, upper, translate

import pickle
import sys
import operator

import hashlib

from moduleFechas import camposFechasValidas

print sqlalchemy.__version__



import datetime
import DlgError
import wx
import operator
import re
import sys

from cnf import db, host, localCountry
import cnf
from os import name as NameOS


user   = cnf.user
passwd = cnf.passwd

if __name__ == '__main__':
    user='admin'
    passwd='redtdt'
#spec = 'postgres://postgres:macana@'+host+'/'+db

meses = ['','ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic']
if not user:
    print "error: no hay user"
    sys.exit()
    
if not host:
    host = 'localhost'
#host='tdtdb.dyndns.org'        
spec = 'postgres://'+user+':'+passwd+'@'+host+'/'+db
print spec
metadata = MetaData(spec)


DefaultDate = datetime.date(1900, 1, 1)

import sqlalchemy.types as types


def seExporta(miObj):
    if miObj:
        if hasattr(miObj, 'exportar'):
            valor = getattr(miObj,'exportar')
            return valor == 1
        else:
            return True
    else:
        return False



def diagRefCaso(C):
    res=''
    severidad=0
    if C.noValido():
        res +=u'El caso ' +C.Descriptor()+' presenta problemas:'+C.noValido()
        severidad = 2
    else:
        if not seExporta(C):
            res +=u'El caso '+C.Descriptor()+' no se exporta'
            severidad = 1
    
    return (severidad, res)



def diagRefPersona(P, rol):
    res=''
    severidad=0
    if P.noValido():
        res +=u'La persona en rol de '+rol+' '+P.Descriptor()+' presenta problemas:'+P.noValido()
        severidad = 2
    else:
        if not seExporta(P):
            res +=u'La persona en rol de '+rol+' '+P.Descriptor()+' no se exporta'
            severidad = 1
    
    return (severidad, res)



class StatusClass:
    pass
class dataObject(object):
    def __init__(self, id, Log=None):
        if id:
            self.id = id
        if Log:
            self.loginfo = Log
        
    def CR(self):
        return ''
    def noValido(self):
        return ''
    def Descriptor(self):
        return self.__doc__
    def tipoDescriptor(self):
        tipo = type(self)
        strTipo = objetoDescrip[tipo] if tipo in objetoDescrip.keys() else ' '
        return '%s: %s'%(strTipo, self.Descriptor())
    
    
    def borrar(self):
        myLoginfo = None

        ## ojo
        #if hasattr(self, 'PLoginfo'):
        #    myLoginfo = self.PLoginfo
        #    self.PLoginfo = None
        #    session.add(self)
        #    session.flush()
            
        print "borrando ", self
        session.delete(self)
        ## ojo incluyendo session.flush
        print session.dirty
        session.flush()

        #session.flush()
        print "borrado ", self

        ## ojo
        #if myLoginfo:
        #    print "borrando tambien", myLoginfo
        #    myLoginfo.borrar()
        #    session.flush()
            
            



user = Table('usuario',metadata,
              
            Column('id',Integer,
                   Sequence('user_id_seq', optional=True), primary_key=True),
            Column('nombre', Unicode(30), nullable=False),
            Column('nivel', Integer),
            Column('clavegrupo', Integer),
            Column('clavestatus', Integer),
            )
configTdt = Table('configtdt', metadata,
    Column('id', Integer, Sequence('cfg_id_seq', optional=True), primary_key=True),
    Column('tipo', Unicode(30), nullable=False),
    Column('descripcion',Unicode(300), nullable=False),
    Column('contenido',TEXT(convert_unicode=False)),
    #Column('parche_v2',Integer)
    )
    
tesauro = Table('tesauro', metadata,
            Column('id', Integer, Sequence('tes_id_seq', optional=True),
                   primary_key=True),
            Column('parent_id', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict"), nullable=True),
        
            Column('name', Unicode(30), nullable=False),
            # name = clave de vocablo, de hecho la clave jerarquica, numerica
            Column('descripcion',Unicode(350),nullable=False),
            Column('notas',TEXT(convert_unicode=True)),
    
   
            )
grupo = Table('grupos',metadata,
          Column('id', Integer, primary_key=True),
          Column('nombre', Unicode(150), nullable=False),
          Column('contacto', Unicode(150)),
          Column('sigla', Unicode(30)),
          Column('ultimolotet1fecha', Date),
          Column('ultimolotet1archivo', Unicode(150)),
          Column('ultimolotet2fecha', Date),
          Column('ultimolotet2archivo', Unicode(150)),
          Column('loginfo', Integer, ForeignKey('loginfo.id',onupdate="restrict", ondelete="restrict")),
          )
 
          
          
          

persona = Table('persona', metadata,
                Column('id', Integer, Sequence('per_id_seq', optional=True),
                       primary_key=True),
                Column('nombre',Unicode(350), nullable=False),
                Column('apellido',Unicode(350), nullable=False),
                Column('esindividual',Integer),
                Column('confidencialidad',Integer),
                Column('otro_nombre',Unicode(350)),
                #Column('otro_apellido',Unicode(250)), #borrar
                Column('sexo',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                #Column('edad',Integer), #borrar
                #Column('aniosexistencia',Integer), #borrar
                Column('fecha_nac_o_fund',Date),
                Column('tipo_fecha_nac_o_fund',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                Column('pais_nac_u_origen',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                Column('estado_nac_u_origen',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                Column('mpio_nac_u_origen',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                Column('localidad_nac_u_origen',Unicode(120)),
                Column('ciudadania_o_sede',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                Column('escolaridad',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                Column('ocupacion',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                Column('habla_lengua_local',Integer),
                #Column('origen_etnico',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #borrar? (es repetible)
                Column('religion',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                Column('estado_civil',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                Column('no_dependientes',Integer),
                Column('descripcion_del_grupo',Unicode(120)),
                Column('observaciones',TEXT(convert_unicode=True)),
                #Column('confiabilidad',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #borrar
                Column('monitoreo',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                Column('comentarios',TEXT(convert_unicode=True)),
                Column('proyecto_grupo',TEXT(convert_unicode=True)),
                Column('proyecto_conjunto',TEXT(convert_unicode=True)),
                Column('proyecto_se',TEXT(convert_unicode=True)),
                Column('archivos',TEXT(convert_unicode=True)),
                Column('loginfo', Integer, ForeignKey('loginfo.id',onupdate="restrict", ondelete="restrict")),
                Column('tipo',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),

                Column('frecepcion', Date),
                Column('tipo_frecepcion',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                Column('exportar',Integer),
                Column('clavegrupo', Integer),
                Column('clavestatus', Integer),
                Column('personarelacionadac3', Integer),
                Column('clavestatusc3', Integer),
                
                )
                




class Obj1(object):
    pass




publicacion = Table('publicacion', metadata,
                Column('id', Integer, Sequence('publ_id_seq', optional=True),
                       primary_key=True),
                Column('caso_id', Integer, ForeignKey('caso.id',onupdate="restrict", ondelete="restrict")),
                Column('titulo_de_parte', Unicode(140)),
                #Column('titulo', Unicode(550)), #borrar                      
                Column('datos_publicacion', Unicode(240)),
                Column('tipofecha',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #T48
                Column('tipofechaconsulta',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #T48
                Column('fecha',Date),
                Column('Nombre_del_sitio', Unicode(200)),
                Column('Liga_publicacion', Unicode(500)),
                Column('fecha_consulta',Date),
                Column('tipopublicacion',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #16
                Column('idioma',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #T14
                Column('lengua_indigena',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #T66
                Column('confiabilidad',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),  #42
                Column('observaciones',TEXT(convert_unicode=True)),
                Column('comentarios',TEXT(convert_unicode=True)),
                Column('persona_referenciada_id', Integer, ForeignKey('persona.id',onupdate="restrict", ondelete="restrict")),
                
                Column('loginfo', Integer, ForeignKey('loginfo.id',onupdate="restrict", ondelete="restrict")),
                Column('exportar',Integer),
                Column('clavegrupo', Integer),
                Column('clavestatus', Integer),
                
                       
                       )
                    
                  
                
loginfo = Table('loginfo',metadata,
                Column('org',Integer),
                Column('id',Integer, Sequence('loginfo_id_seq', optional=True),
                       primary_key=True),
                Column('fechaCreacion', Date),
                Column('userCreacion', Integer, ForeignKey('usuario.id',onupdate="restrict", ondelete="restrict")),
                Column('fechaActualizacion', Date),
                Column('userActualizacion', Integer, ForeignKey('usuario.id',onupdate="restrict", ondelete="restrict")),
                Column('clavegrupo', Integer),
                Column('clavestatus', Integer),
                )
                

class Grupo(dataObject):
    "grupos"
    def __init__(self, id):
        self.id = id
        self.nombre = ' '
    def Descriptor(self):
        return self.nombre
    def __repr__(self):
        return self.Descriptor()
    
    
class User(dataObject):
    "usuario"
    def __init__(self, nombre, nivel, id=None):
        self.nombre = nombre
        self.nivel = nivel
        if id:
            self.id = id
    def Descriptor(self):
        return self.nombre
    def sepuedeborrar(self):
        if self.creadorEn:
            return False
        if self.actualizadorEn:
            return False
        return True
    def __repr__(self):
        return self.Descriptor()

class Loginfo(dataObject):
    "Info de creacion"
    def __init__(self, id=None,userCreacion=None, userActualizacion=None):
        dataObject.__init__(self, id)
        self.org = status.org
        self.fechaCreacion = datetime.datetime.now()
        self.fechaActualizacion = datetime.datetime.now()
        if userCreacion:
            self.userCreacion = userCreacion
        else:
            if not status.importacion:
                self.Creador = status.usuarioActual
        if userActualizacion:
            self.userActualizacion = userActualizacion
            
        else:
            if not status.importacion:
                self.Actualizador  = status.usuarioActual
    def PrtCreacion(self):
        return "%s por %s"%(strDate(self.fechaCreacion),self.Creador)
        
    def PrtActualizacion(self):
        return "%s por %s"%(strDate(self.fechaActualizacion),self.Actualizador)
    def __repr__(self):
        return  'LogInfo:' +str(self.id)  
        
        
def NewLoginfo(flush=True):
    
    L = Loginfo()
    session.add(L)
    if flush:
        FlushInfo(id=102)
    return L

LoginfoMapper = mapper(Loginfo,loginfo,
                    properties=
                            {'Creador':relation(User, primaryjoin=user.c.id == loginfo.c.userCreacion, backref="creadorEn"),
                             'Actualizador':relation(User, primaryjoin=user.c.id == loginfo.c.userActualizacion, backref="actualizadorEn"),
                             }

                )

                




caso = Table('caso',metadata,
             Column('id', Integer, Sequence('caso_id_seq', optional=True),
                       primary_key=True),
             Column('descripcion',Unicode(200), nullable=False),
#             
             Column('confidencialidad', Integer),
             Column('fecha_inicio', Date),
             Column('tipo_fecha_inicio', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
             Column('fecha_final', Date),
             Column('tipo_fecha_final', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),

             Column('descripcion_narrativa', TEXT(convert_unicode=True)),
             Column('resumen_descripcion', TEXT(convert_unicode=True)),
             Column('observaciones', TEXT(convert_unicode=True)),
             Column('no_persona_afectadas', TEXT(convert_unicode=True)),
             Column('comentarios', TEXT(convert_unicode=True)),
             Column('archivos', TEXT(convert_unicode=True)),
             Column('monitoreo', Integer,ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #43
             Column('loginfo', Integer, ForeignKey('loginfo.id',onupdate="restrict", ondelete="restrict")),
             
             Column('proyecto_grupo',TEXT(convert_unicode=True)),
             Column('proyecto_conjunto',TEXT(convert_unicode=True)),
             Column('proyecto_se',TEXT(convert_unicode=True)),
             Column('frecepcion', Date),
             Column('tipo_frecepcion',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
             Column('exportar',Integer),
             Column('exportarrelaciones',Integer),
             Column('clavegrupo', Integer),
             Column('clavestatus', Integer),
             Column('clavestatusc3', Integer),
             Column('casorelacionadoc3',Integer), #si el caso no esta en C3, con que caso se ha relacionado?

            
             )

acto = Table('acto',metadata,
             Column('id', Integer, Sequence('acto_id_seq', optional=True),
                       primary_key=True),
             
             Column('caso_id', Integer, ForeignKey('caso.id',onupdate="restrict", ondelete="restrict")),
             Column('victima_id',Integer,ForeignKey('persona.id',onupdate="restrict", ondelete="restrict")),
             Column('confidencialidad',Integer),
             Column('tipodeacto',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
             Column('tipofechainicio',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
             Column('tipofechafinal',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
             Column('tipolugar',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
             Column('estatusvdh',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
             Column('estatusvictima',Integer,ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
             Column('observaciones',TEXT(convert_unicode=True)),
             Column('fechainicio', Date),
             Column('fechafin', Date),
             Column('loginfo', Integer, ForeignKey('loginfo.id',onupdate="restrict", ondelete="restrict")),
             Column('localizacion_id',Integer, ForeignKey('localidad.id',onupdate="restrict", ondelete="restrict")),
             
             Column('legislacion_nacional',Integer,ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #borrar
             Column('instrumentos_internacionales',Integer,ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),  #borrar
             Column('legislacion_nacional_notas',TEXT(convert_unicode=True)),
             Column('instrumentos_internacionales_notas',TEXT(convert_unicode=True)),
           
             Column('edad_victima', Integer),
             Column('edad_victima_tipo',Integer),
             Column('exportar',Integer),
             Column('exportarnormatividad',Integer),
             Column('clavegrupo', Integer),
             Column('clavestatus', Integer),
             
             )


derechoviolado = Table('derechoviolado', metadata,
                Column('id', Integer, Sequence('dv_id_seq', optional=True),
                       primary_key=True),
                Column('acto_id', Integer, ForeignKey('acto.id',onupdate="restrict", ondelete="restrict")),
                Column('derechoviolado_id', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                Column('loginfo', Integer, ForeignKey('loginfo.id',onupdate="restrict", ondelete="restrict")),
                Column('clavegrupo', Integer),
                Column('clavestatus', Integer),
                )
                
caracrelevantes = Table('caracrelevantes', metadata,
                Column('id', Integer, Sequence('cr_id_seq', optional=True),
                       primary_key=True),
                Column('acto_id', Integer, ForeignKey('acto.id',onupdate="restrict", ondelete="restrict")),
                Column('caracrelevantes_id', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                Column('loginfo', Integer, ForeignKey('loginfo.id',onupdate="restrict", ondelete="restrict")),
                Column('clavegrupo', Integer),
                Column('clavestatus', Integer),
                
                )     
class Caracrelevantes(dataObject):
    "caracteristica relevante"
    def __init__(self, id=None):
        dataObject.__init__(self, id)
        
        return
    def __repr__(self):
        return  'CaracRel:' +str(self.id)           
    def Descriptor(self):
        if self.Pcaracteristicarelevante:
            return self.Pcaracteristicarelevante.descripcion
        else:
            return ''
    def borrar(self):
        #self.acto_id=None
        ## ojo

        ##ojo
        #session.add(self)
        #session.flush()

        dataObject.borrar(self)
    






persona_vinculo = Table('persona_vinculo', metadata,
                             Column('id', Integer, Sequence('pc_id_seq', optional=True),
                                            primary_key=True),
                             Column('persona_1_id', Integer, ForeignKey('persona.id',onupdate="restrict", ondelete="restrict")),
                             Column('persona_2_id', Integer, ForeignKey('persona.id',onupdate="restrict", ondelete="restrict")),
                             Column('tipo_id', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                             Column('loginfo', Integer, ForeignKey('loginfo.id',onupdate="restrict", ondelete="restrict")),
                             Column('Fecha_inicial', Date),
                             Column('tipofecha_inicial',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #T48
                             Column('Fecha_final', Date),
                             Column('tipofecha_final',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #T48
                             Column('observaciones',TEXT(convert_unicode=True)),
                             Column('puesto',Unicode(250)),
                             Column('rango',Unicode(250)),
                             Column('confidencialidad',Integer),
                             
                             Column('comentarios',TEXT(convert_unicode=True)),
                             Column('fecha_info_vigente',Date),
                             Column('tipofecha_info_vigente', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #T48
                             Column('descripcion', Unicode(240)),
                             Column('exportar',Integer),
                             Column('clavegrupo', Integer),
                             Column('clavestatus', Integer),
                             )
caso_vinculo = Table('caso_vinculo', metadata,
                             Column('id', Integer, Sequence('cv_id_seq', optional=True),
                                            primary_key=True),
                             Column('caso_1_id', Integer, ForeignKey('caso.id',onupdate="restrict", ondelete="restrict")),
                             Column('caso_2_id', Integer, ForeignKey('caso.id',onupdate="restrict", ondelete="restrict")),
                             Column('tipo_id', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #T22
                             Column('loginfo', Integer, ForeignKey('loginfo.id',onupdate="restrict", ondelete="restrict")),
                             Column('observaciones',TEXT(convert_unicode=True)),
                             Column('comentarios',TEXT(convert_unicode=True)),
                             Column('clavegrupo', Integer),
                             Column('clavestatus', Integer),
                             )

#acto_persona = Table('acto_persona', metadata,
#                     Column('id', Integer, Sequence('acto_per_id_seq', optional=True),
#                       primary_key=True),
#                     Column('persona_id', Integer, ForeignKey('persona.id',onupdate="restrict", ondelete="restrict")),
#                     Column('acto_id', Integer, ForeignKey('acto.id',onupdate="restrict", ondelete="restrict")),
#                     Column('tesauro_id', Integer,ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
#                     Column('loginfo', Integer, ForeignKey('loginfo.id',onupdate="restrict", ondelete="restrict")),
#                     )
involucramiento = Table('involucramiento', metadata,
                       Column('id', Integer, Sequence('invol_id_seq', optional=True),
                       primary_key=True),
                       Column('acto_id', Integer, ForeignKey('acto.id',onupdate="restrict", ondelete="restrict")),
                       Column('persona_id', Integer, ForeignKey('persona.id',onupdate="restrict", ondelete="restrict")),
                       Column('tesauro_id', Integer,ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                       Column('tipo_id',Integer),
                       Column('confidencialidad',Integer),
                       Column('gradoinvolucramiento',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                       Column('tipoperpetrador',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                       Column('ultimostatusperpetrador',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                       Column('observaciones',TEXT(convert_unicode=True)),
                       Column('loginfo', Integer, ForeignKey('loginfo.id',onupdate="restrict", ondelete="restrict")),
                       Column('exportar',Integer),
                       Column('clavegrupo', Integer),
                       Column('clavestatus', Integer),
                       
                        )

                       
evento_tipificacion = Table('evento_tipificacion',metadata,
                     Column('id', Integer, Sequence('evento_per_id_seq', optional=True),
                       primary_key=True),
                     Column('evento_id', Integer, ForeignKey('caso.id',onupdate="restrict", ondelete="restrict")), 
                     Column('tesauro_id', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                     Column('codigo',Integer),
                    
                     # codigo == 153 -> Derecho afectado
                     # codigo == 154 -> Tema
                     # codigo == 2154 -> legislacion nacional
                     # codigo == 2155 -> instrumentos internacionales
                      Column('acto_id', Integer),
                      Column('notas', TEXT(convert_unicode=True)),

                      Column('loginfo', Integer, ForeignKey('loginfo.id',onupdate="restrict", ondelete="restrict")),
                      Column('clavegrupo', Integer),
                      Column('clavestatus', Integer),
                     ) 

persona_tipificacion = Table('persona_tipificacion',metadata,
                     Column('id', Integer, Sequence('persona_tip_id_seq', optional=True),
                       primary_key=True),
                     Column('persona_id', Integer, ForeignKey('persona.id',onupdate="restrict", ondelete="restrict")), 
                     Column('tesauro_id', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                     Column('codigo',Integer),
                     Column('masinformacion',Unicode(240)),
                     Column('telefono',Unicode(200)),
                     Column('celular',Unicode(200)),
                     Column('web',Unicode(240)),
                     Column('correo_e',Unicode(240)),
                     
                     # codigo == 945 -> Idioma
                     # codigo == 66  -> Lengua
                     # codigo == 942 -> Origen etnico
                     #        == 944 -> Caracteristicas relevantes
                     #        == 910 -> Direccion
                     Column('loginfo', Integer, ForeignKey('loginfo.id',onupdate="restrict", ondelete="restrict")),
                     Column('clavegrupo', Integer),
                     Column('clavestatus', Integer),
                     )



fuente = Table('fuente',metadata,
                     Column('id', Integer, Sequence('source_id_seq', optional=True),
                       primary_key=True),
                     
                
                     Column('caso_id', Integer, ForeignKey('caso.id',onupdate="restrict", ondelete="restrict")),
                     Column('persona_referenciada_id', Integer, ForeignKey('persona.id',onupdate="restrict", ondelete="restrict")),
                     Column('persona_fuente_id', Integer, ForeignKey('persona.id',onupdate="restrict", ondelete="restrict")),
                     Column('confidencialidad',Integer),
                     Column('tipofecha',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #T48
                     Column('fecha',Date),
                     Column('conexion_con_informacion',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #T19
                     Column('idioma',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #T14
                     Column('lengua_indigena',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #T66
                     Column('confiabilidad',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),  #42
                     Column('observaciones',TEXT(convert_unicode=True)),
                     Column('comentarios',TEXT(convert_unicode=True)),
                     Column('loginfo', Integer, ForeignKey('loginfo.id',onupdate="restrict", ondelete="restrict")),
                     Column('exportar',Integer),
                     Column('clavegrupo', Integer),
                     Column('clavestatus', Integer),
                     
                     ) 

intervencion = Table('intervencion',metadata,
                     Column('id', Integer, Sequence('intervencion_id_seq', optional=True),
                       primary_key=True),
                     #Column('descripcion', Unicode(100), nullable=False),
                     Column('evento_id', Integer, ForeignKey('caso.id',onupdate="restrict", ondelete="restrict")),
#                     Column('acto_id',Integer, ForeignKey('acto.id')),
#                     Column('persona_id', Integer, ForeignKey('persona.id')),
                     Column('tesauro_id', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),  
                     Column('persona_id_dequien',Integer, ForeignKey('persona.id')),
                     Column('persona_id_aquien',Integer, ForeignKey('persona.id')), 
                     Column('persona_id_interviniente',Integer, ForeignKey('persona.id')), 
                     Column('loginfo', Integer, ForeignKey('loginfo.id',onupdate="restrict", ondelete="restrict")),
                     #Column('respuesta_id', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),  
                     Column('estatus_id', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),  
                     #Column('impacto_id', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),  
                     Column('observaciones',TEXT(convert_unicode=True)),
                     Column('comentarios',TEXT(convert_unicode=True)),
                     Column('respuesta',TEXT(convert_unicode=True)),
                     Column('impacto',TEXT(convert_unicode=True)),
                     Column('fecha',Date),
                     Column('tipofecha',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")), #T48
                     #Column('parteinterviniente', Unicode(150)),
                     Column('exportar',Integer),
                     Column('clavegrupo', Integer),
                     Column('clavestatus', Integer),
                     
                     )


                
localidad = Table('localidad',metadata,
#                Column('org_id',Integer, primary_key=True),
                Column('id', Integer, Sequence('localidad_id_seq', optional=True),
                        primary_key=True),
                Column('caso_id', Integer, ForeignKey('caso.id',onupdate="restrict", ondelete="restrict")),
                Column('pais_id', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                Column('estado_id', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                Column('municipio_id', Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
                Column('notas_localidad', Unicode(180), nullable=True),
                Column('notas_municipio', Unicode(180), nullable=True),
                Column('localidad',Unicode(180), nullable=True),
                Column('loginfo', Integer, ForeignKey('loginfo.id')),
                Column('clavegrupo', Integer),
                Column('clavestatus', Integer),
                )
                
class ConfigTdt(dataObject):
    "configuracion"
    def __init__(self, tipo):
        self.tipo=tipo
    def Descriptor(self):
        return self.descripcion
    
    


class Involucramiento(dataObject):
    "perpetrador"
    def __init__(self, id=None, Log=None):
        dataObject.__init__(self, id, Log=Log)
        if not self.loginfo: self.PLoginfo = NewLoginfo()
        self.exportar = 1
        
    def noValido(self):
        res=''
        if not   self.loginfo: res += u"No hay informaci\xf3n de creaci\xf3n de registro. "
        if not self.persona_id: res += u"No hay informaci\xf3n de un perpetrador. "
        
        
        
        return res

    def noExportable(self):
        severidad, res=0,''
        if self.persona:
            (severidad, res) = diagRefPersona(self.persona, 'perpetrador')
            return (severidad, res)
        else:
            return 2, '' #ojo: agregar mensaje
    


    def __repr__(self):
        return  'Involucramiento:' +str(self.id)
    def PrtID(self):
        return "%i"%self.id
    def Observaciones(self):
        if self.observaciones:
            return self.observaciones
        else:
            return ''
    def Descriptor(self):
        if self.persona:
            return self.persona.Descriptor()
        else:
            return ''
    def borrar(self):
        #self.acto_id=None
        ## ojo
        #session.add(self)
        #session.flush()
        dataObject.borrar(self)
        
class Fuente(dataObject):
    "fuente personal"
    def __init__(self, persona_fuente,persona_referenciada=None, id=None, Log=None):
        dataObject.__init__(self, id, Log=Log)
        if not self.loginfo: self.PLoginfo = NewLoginfo()
        self.PCaso = status.casoActual
        if type(persona_fuente) == type(1):
            self.persona_fuente_id = persona_fuente
        else:
            self.PPersona_como_fuente = persona_fuente
        if persona_referenciada:
            if type(persona_referenciada) == type(1):
                self.persona_referenciada_id = persona_referenciada
            else:
                self.PPersona = persona_referenciada
        self.fecha = DefaultDate
        self.exportar = 1
        self.comentarios = u''
    
    def noValido(self):
        res=''
        if not   self.loginfo: res += u"No hay informaci\xf3n de creaci\xf3n de registro. "
        if not   self.persona_fuente_id: res += u"No hay informaci\xf3n de la persona. "
        
        
        return res

    def __repr__(self):
        return  'Fuente personal:' +str(self.id)

    def noExportable(self):
        res1, res2='',''
        severidad1, severidad2 = 0,0
        if self.PPersona_como_fuente:
            (severidad1, res1) = diagRefPersona(self.PPersona_como_fuente, u'fuente personal')
        else:
            return (2, '') # ojo: poner algun mensaje
        if self.PPersona:
            (severidad2, res2) = diagRefPersona(self.PPersona, u'sobre quien se aporta  informaci\xf3n')
        severidad = max(severidad1, severidad2)
        res = '\n'.join(i for i in [res1,res2] if i)
        return (severidad, res)
    def Descriptor(self):
        if self.PPersona_como_fuente:
            return self.PPersona_como_fuente.Descriptor()
        else:
            return 'Fuente personal no identificada'
    def PrtID(self):
        return "%i"%self.id
    def Pfecha(self):
        return self.fecha, self.PTipofecha
    
    def borrar(self):
        #self.caso_id=None
        ## ojo
        #session.add(self)
        #session.flush()
        dataObject.borrar(self)
    
        
class Caso_vinculo(dataObject):
    u"V\xednculo de caso"
    def __init__(self, caso1, caso2, tipoRel, id=None, Log=None):
        dataObject.__init__(self, id, Log=Log)
        if type(caso1) == type(1):
            self.caso_1_id = caso1
        else:
            self.Pcaso_1 = caso1
        if type(caso2) == type(1):
            self.caso_2_id = caso2
        else:    
            self.Pcaso_2 = caso2
        if type(tipoRel) == type(1):
            self.tipo_id = tipoRel
        else:
            self.Ptipo   = tipoRel
        self.fecha_inicio = DefaultDate
        self.fecha_final = DefaultDate
        self.frecepcion = DefaultDate
        self.comentarios = u''
        if not self.loginfo: self.PLoginfo = NewLoginfo()
    def Descriptor(self):
        if self.Pcaso_2:
            desc = self.Pcaso_2.Descriptor()
        else:
            desc = "[Caso faltante!!!]"
            
        
        return u'Relacionado con '+desc
    def borrar(self):
        #self.caso_1_id=None
        #self.caso_2_id=None
        ## ojo

        ## ojo
        #session.add(self)
        #session.flush()

        dataObject.borrar(self)
        
    def noValido(self):
        res=''
        if not self.loginfo: res += u"No hay informaci\xf3n de creaci\xf3n de registro. "
        if not self.caso_2_id: res += u"No hay informaci\xf3n del caso relacionado. "
        if not self.tipo_id: res += u"No hay informaci\xf3n del tipo de relaci\xf3n. "
        return res   
    
    
    def noExportable(self):
        res1, res2='',''
        severidad1, severidad2 = 0,0
        if self.Pcaso_1:
            (severidad1, res1) = diagRefCaso(self.Pcaso_1)
        else:
            return (2, 'Caso no existente!!!') # ojo: poner algun mensaje mas explicativo
        if self.Pcaso_2:
            (severidad2, res2) = diagRefCaso(self.Pcaso_2)
        else:
            return (2, 'Caso no existente!!!') # ojo: poner algun mensaje mas explicativo
            
        severidad = max(severidad1, severidad2)
        res = '\n'.join(i for i in [res1,res2] if i)
        return (severidad, res) 
        
    def __repr__(self):
        return  'Caso vinculo:' +str(self.id)
    def PrtID(self):
        return "%i"%self.id

def coma(str):
    if str:
        return ', '
    else:
        return ''
class Localidad(dataObject):
    "localidad de caso"
    def __init__(self, caso_id, id=None, Log=None):
        dataObject.__init__(self, id, Log=Log)
        self.caso_id = caso_id
        self.notas_localidad = ''
        self.notas_municipio = ''
        self.localidad = ''
        
        if not self.loginfo: 
            self.PLoginfo = NewLoginfo()
            self.Pais = getDefault('T15')
    def borrar(self):
        miCaso = self.caso

        ## ojo
        #for a in miCaso.actos:
        #    if a.PLocalidad == self:
        #        a.PLocalidad = None
        #        print "blanqueando ",a ### ojo!!!!!!!!!!!!!!
        #        session.add(a)
        #session.flush()        
                
        #self.caso_id=None
        ## ojo

        ## ojo
        #session.add(self)
        dataObject.borrar(self)
               
        
        
     
    def Descriptor(self, perm=True):
        flagNotas = "*" if self.notas_municipio or self.notas_localidad else ' '
        perm = True
        if perm:
             strMpio = tesDesc(self.Municipio)    
             strLocalidad =   self.localidad 
        else:
            strMpio = "Dato no accesible"
            strLocalidad = strMpio
        return '%(pais)-12s|%(Estado)-20s|%(Mpio)-30s|%(Localidad)-20s'%\
               {'pais':tesDesc(self.Pais)+flagNotas,'Estado':tesDesc(self.Estado),\
               'Mpio':strMpio, 'Localidad':strLocalidad}
    def PrtDescriptor(self, perm=True):
        perm=True
        if perm:
             strMpio = tesDesc(self.Municipio)    
             strLocalidad =   self.localidad 
        else:
            strMpio = "Dato no accesible"
            strLocalidad = strMpio
        condNotas = seImprime(status.prt_entidad,'PrtLocalidadesNotas',status.prt_tipoRep)
        prtMunicipio = " (%s)"%self.notas_municipio if (self.notas_municipio and condNotas) else ''
        prtLocalidad = " (%s)"%self.notas_localidad if (self.notas_localidad and condNotas) else ''
        
        
        return '%(Localidad)s %(Mpio)s %(Estado)s %(pais)s'%\
               {'pais':tesDesc(self.Pais),'Estado':tesDesc(self.Estado)+coma(tesDesc(self.Estado)),\
               'Mpio':strMpio+prtMunicipio+coma(strMpio+prtMunicipio), 'Localidad':strLocalidad+prtLocalidad+coma(strLocalidad+prtLocalidad)}
    def PrtID(self):
        return "%i"%self.id
    def strPais(self):
        return '%(Pais)-20s'%{'Pais':tesDesc(self.Pais)} if self.Pais else None
    def strEstado(self):
        return '%(Estado)-20s'%{'Estado':tesDesc(self.Estado)} if self.Estado else None
    def strMpio(self):
        return '%(Mpio)-20s'%{'Mpio':tesDesc(self.Municipio)} if self.Municipio else None
    def strLocalidad(self):
        return self.localidad
    def prtMpio(self):
        cond = seImprime(status.prt_entidad , 'prtMpioNotas', status.prt_tipoRep)
        expr = "%s %s"%(tesDesc(self.Municipio), "(%s)"%self.notas_municipio if (self.notas_municipio and cond) else '') if self.Municipio else None
        
        return expr
    def prtMpioNotas(self):
        expr = "%s"%self.notas_municipio if self.notas_municipio else ''
        return expr
        
    def prtLocalidad(self):
        cond = seImprime(status.prt_entidad , 'prtLocalidadNotas', status.prt_tipoRep)
        expr = "%s %s"%(self.localidad, "(%s)"%self.notas_localidad if (self.notas_localidad and cond) else '') if self.localidad else None
        #expr = "%s "%(self.localidad) if self.localidad else None
        return expr
    def prtLocalidadNotas(self):
        expr = "%s"%self.notas_localidad if self.notas_localidad else ''
        return expr
    def __repr__(self):
        return  'Localidad:' +str(self.id)            
    

class Intervencion(dataObject):
    "intervencion"
    def __init__(self, P, T, C, id=None, Log=None):
        dataObject.__init__(self, id, Log=Log)
        if type(P) == type(1):
            self.persona_id_interviniente = P
        else:
            self.Pinterviniente = P
        if T:
            self.tipo = T
        if type(C) == type(1):
            self.evento_id = C
        else:
            self.Pcaso = C
        if not self.loginfo: self.PLoginfo = NewLoginfo()
        self.fecha = DefaultDate
        self.exportar = 1
        self.comentarios=u''
    def noValido(self):
        res=''
        if not   self.loginfo: res += u"No hay informaci\xf3n de creaci\xf3n de registro. "
        if not   self.tesauro_id: res += u"No hay informaci\xf3n del tipo de intervenci\xf3n. "
        if not   self.persona_id_interviniente: res += u"No hay informaci\xf3n de la parte interviniente. "
        return res    
    
    def noExportable(self):
        res1, res2, res3='','',''
        severidad1, severidad2, severidad3 = 0,0,0
        if self.solicitante:
            (severidad1, res1) = diagRefPersona(self.solicitante, u'sobre qui\xe9n se interviene')
        
        if self.contraparte:
            (severidad2, res2) = diagRefPersona(self.contraparte, u'a qui\xe9n se le dirigi\xf3 esta intervenci\xf3n')
        
        if self.Pinterviniente:
            (severidad3, res3) = diagRefPersona(self.Pinterviniente, u'qui\xe9n inicia o realiza esta intervenci\xf3n')
        else:
            (severidad3, res3)=(2, '') # ojo: poner algun mensaje
        severidad = max(severidad1, severidad2, severidad3)
        res = '\n'.join(i for i in [res1,res2, res3] if i)
        return (severidad, res)
    
    def __repr__(self):
        return  'Interv:' +str(self.id)
    def Descriptor(self):
        expr1 ='Sin detalles'
        expr2 = 'Sin detalles'
        if self.tipo:
            expr1 = self.tipo.descripcion
        if self.Pinterviniente:
            expr2 = self.Pinterviniente.Descriptor()
        
        return expr1 + '/'+ expr2
    def PrtID(self):
        return "%i"%self.id
    def Pfecha(self):
        return self.fecha, self.PTipofecha
    def borrar(self):
        #self.evento_id=None
        ##ojo
        #session.add(self)
        #session.flush()
        miself=self
        #dataObject.borrar(self)
        session.delete(self)
        if miself.solicitante:
            if miself in miself.solicitante.Intervenciones_solicitadas_por_la_persona:
               print "1 rem ",miself, " de ",miself.solicitante 
               miself.solicitante.Intervenciones_solicitadas_por_la_persona.remove(miself)
               
        if miself.contraparte:
            if miself in miself.contraparte.Intervenciones_solicitadas_a_la_persona:
                print "2 rem ",miself, " de ",miself.contraparte
                miself.contraparte.Intervenciones_solicitadas_a_la_persona.remove(miself)
                
        if miself.Pinterviniente:
            if miself in miself.Pinterviniente.Intervenciones_como_interviniente:
                print "3 rem ",miself, " de ",miself.Pinterviniente
                miself.Pinterviniente.Intervenciones_como_interviniente.remove(miself)
                
        session.flush()



    
class Persona_Vinculo(dataObject):
    "vinculo personal"
    def __init__(self, P, id=None, Log=None):
        dataObject.__init__(self, id, Log=Log)
        if not self.loginfo: self.PLoginfo = NewLoginfo()
        self.descripcion =''
        if type(P) == type(1):
           self.persona_1_id  = P
        else:
            self.vinculo1 =P
        self.vinculo2 =None
        self.Fecha_inicial = DefaultDate
        self.Fecha_final = DefaultDate
        self.fecha_info_vigente = DefaultDate
        self.exportar = 1
        self.comentarios = u''
    def borrar(self):
        #self.persona_1_id=None
        #self.persona_2_id=None
        ## ojo
        #session.add(self)
        #session.flush()
        dataObject.borrar(self)
        
        
    def PFecha_inicial(self):
        return self.Fecha_inicial, self.Ptipofecha_inicial
    def PFecha_final(self):
        return self.Fecha_final, self.Ptipofecha_final
    def PFecha_info_vigente(self):
        return self.fecha_info_vigente, self.Ptipofecha_info_vigente
    
    
    
        
    def Descriptor(self):
        if self.descripcion:
            return self.descripcion
        else:
            if self.vinculo2:
                return self.vinculo2.Descriptor()+" ["+terminoReciproco(status.reciprocoRelacionPersonas, self.tipo.name, self.tipo.ClaveODesc())+"]"
            else:
                return ''
    def __repr__(self):
        return  'Per vinculo:' +str(self.id)            
    def Descriptor_R(self):
        
        return self.vinculo1.Descriptor()+" ["+self.tipo.ClaveODesc()+"]"
        #return self.vinculo1.Descriptor()+" ["+terminoReciproco(status.reciprocoRelacionPersonas, self.tipo.name, self.tipo.ClaveODesc())+"]"

class Derechoviolado(dataObject):
    "derecho violado"
    
    def __init__(self, id=None, Log=None):
        dataObject.__init__(self, id, Log=Log)
        if not self.loginfo: self.PLoginfo = NewLoginfo()
    def __repr__(self):
        return  'Derecho violado:' +str(self.id)
class PersonaTipificacion(dataObject):
    "tipificacion de persona"
    def __init__(self, codigo, Persona, Tesauro, id=None, Log=None):
        dataObject.__init__(self, id, Log=Log)
        self.codigo = codigo
        if type(Persona) == type(1):
            self.persona_id = Persona
        else:
            self.persona_id = Persona.id
        if type(Tesauro) == type(1):
            self.tesauro_id = Tesauro
        else:
            self.PTesauro = Tesauro
        self.masinformacion=''
        self.telefono =''
        self.celular =''
        self.correo_e =''
        self.web =''
        if not self.loginfo: self.PLoginfo = NewLoginfo()
    def __repr__(self):
        return  'Per tipificacion:' +str(self.id)       
    def borrar(self):
        #self.persona_id=None
        ## ojo
        
        #session.add(self)
        #session.flush()
        dataObject.borrar(self)




class EventoTipificacion(dataObject):
    "tipificacion de caso"

    def __init__(self, event, tipification, tipification_type, tipification_obj, acto_id=None, id=None, Log=None):
        dataObject.__init__(self, id, Log=Log)
        self.evento_id = event #caso_id
        self.tesauro_id = tipification # codigo de tesauro
        if tipification_obj:
            self.tipificacion = tipification_obj 
        self.codigo = tipification_type 
                     # codigo == 153 -> Derecho afectado
                     # codigo == 154 -> Tema
                     # codigo == 2154 -> legislacion nacional
                     # codigo == 2155 -> instrumentos internacionales
        self.acto_id=acto_id
        self.notas=''
        if not self.loginfo: self.PLoginfo = NewLoginfo()
    def __repr__(self):
        return  'EvTip:' +str(self.id)
    def Descriptor(self):
        if self.tipificacion:
            return TesNotNull(self.tipificacion)
    def borrar(self):
        #self.evento_id=None
        ## ojo
        #session.add(self)
        #session.flush()
        dataObject.borrar(self)
    



    
class TesNode(dataObject):
    "Termino de tesauro"
    def __init__(self, name, descripcion, notas='', parent_id=None):
        self.name = name
        self.parent = None
        self.id = None
        self.parent_id = parent_id
        self.descripcion = descripcion
        self.notas=notas
    def Descriptor(self):
        return self.descriptor
    
    def setClave(self, i, value):
        Size = 3
        b=   ((i+1) * Size) - 1
        a= b - (Size - 1)
        j=0
        s=u''
        while j < i:
            
            s=s + '%03i'%self.getClave(j)
            j=j+1
        s=s+'%03i'%value
        
        j=i+1
        while j < 7:
            v=self.getClave(j)
            if v > 0:
                 s=s + '%03i'%v
            j=j+1
        self.name= s
        
    def getClave(self, i):
        Size = 3
        b=   ((i+1) * Size) - Size
        
        
        try:
            r=self.name[b:b+Size]
            r=int(r)
        except: r=0

        return r



    def append(self, clave, descripcion):
        if isinstance(clave, str):
            node = TesNode(clave, descripcion)
            
        else: print "problemas!!!"
        node.parent = self
        
        self.children[node.name] = node
        #self.children[node.id] = node
    def __repr__(self):
        return "TesNode:"+str(self.id)
    def __str__(self):
        return self._getstring(0, False)
    def _getstring(self, level, expand = False):
        s = ('  ' * level) + "%s %s (%s,%s, %d)" % (
            self.name, self.descripcion, self.id,self.parent_id,id(self)) + '\n'
        if expand:
            s += ''.join([n._getstring(level+1, True)
                          for n in self.children.values()])
        return s
    def print_tes(self):
        return self._getstring(0, True)
    def ClaveODesc(self):
        if self.descripcion:
            return self.descripcion
        else:
            return self.name
        
    def allTree(self):
        if self.children.values():
            l=[self]
            for i in  [i.allTree() for i in self.children.values()]:
                if type(i) == list:
                    for j in i:
                        l.append(j)
                else:
                    l.append(i)
            return l
        else:
            return [self]
    def DescriptorCompleto_L(self):
        nodo = self
        padre = nodo.parent
        res = [nodo.descripcion]
        if padre.id > 1:
            while padre.parent.parent:
                nodo = nodo.parent
                padre = nodo.parent
                res.append(nodo.descripcion)
        res.reverse()
        return res
    def DescriptorCompleto(self):
        l=self.DescriptorCompleto_L()
        
        return ' / '.join(l)
                
                


class Persona(dataObject):
    """persona"""
    def __init__(self, nombre, apellido, indiv=1, id=None, Log=None ):
        dataObject.__init__(self, id, Log=Log)
        
        self.nombre=nombre.strip()
        self.apellido=apellido.strip()
        self.esindividual=indiv
        self.comentarios = u''
        if not self.loginfo:
            self.Ppais_nac_u_origen = getDefault('T15')
            self.Pciudadania_o_sede = getDefault('T15')
            self.PLoginfo = NewLoginfo()
            self.fecha_nac_o_fund = DefaultDate
            self.frecepcion = DefaultDate
            self.exportar = 1
    def borrar(self):
        print "a borrar - persona " , self
        porBorrar = self.Pdetallesyvinculosbiograficos + self.Ptipificacion
        print porBorrar
        for o in porBorrar:
            o.borrar()
            session.flush()
        dataObject.borrar(self)
        session.flush()
    def __repr__(self):
        return  'Pers:' +str(self.id)
    
    def noValido(self):
        res=''
        if not   self.loginfo: res += u"No hay informaci\xf3n de creaci\xf3n de registro. "
        if self.esindividual != 1:
           if not   self.tipo: res += u"No hay informaci\xf3n del tipo de grupo. "
        if not   self.apellido: 
            if self.esindividual == 1:
                res += u"No hay informaci\xf3n del apellido. "
            else:
                res += u"No hay informaci\xf3n del nombre del grupo u organizaci\xf3n. "
        
        
        return res
    def Descriptor(self, perm=True):
        """ obtener datos de la persona de manera amigable dependiendo si es 
            individual, colectiva, institucion """
        perm = True
        if perm:
            if self.esindividual == 1:
               return self.apellido + ", " + self.nombre
            else:
               
               if self.nombre:
                 return self.apellido + " (" + self.nombre +")"
               else:
                 return self.apellido  
        else:
            return "Dato no accesible"
    def PrtDescriptor(self, perm=True):
        """ obtener datos de la persona para reportes dependiendo si es 
            individual o colectiva """
        perm = True
        if perm:
            if self.esindividual == 1:
               lista = [i for i in [self.apellido, self.nombre] if i]
               return ', '.join(lista)
               #return  self.nombre + ' ' + self.apellido
            else:
               
               if self.nombre:
                 return self.apellido + " (" + self.nombre +")"
               else:
                 return self.apellido  
        else:
            return "Dato no accesible"
    def PrtID(self):
        return "%i"%self.id

    def Direcciones(self):
        s=''
        for i in DireccionesPersona(self):
            s = s + i[1] + '<br>'  
        return s
    def DetallesBio(self):
      lista=[]
      P = self
      for i  in P.LaOtra2:
          if i.vinculo2:
            i.PersonaVin = i.vinculo2
            i.descriptorVin = i.Descriptor()

            i.tipoVin="D"
            lista.append(i)
    
      for i  in P.LaOtra1:
          if i.vinculo1:
             i.PersonaVin = i.vinculo1
             i.descriptorVin = i.Descriptor_R()
             i.tipoVin="R"
             lista.append(i)
    
      for i  in P.LaOtra2:
          if i.descripcion:
             i.PersonaVin = None
             i.descriptorVin = i.Descriptor()
             i.tipoVin="B"
             lista.append(i)
      return lista
    
    def Idiomas(self):
        return '<br>'.join([TesNotNull(i.PTesauro) for i in self.PIdiomas])
    def Lenguas(self):
        lista = [TesNotNull(i.PTesauro) for i in self.PLenguas]
        lista = sorted(lista)
        return '<br>'.join(lista)
    def OrigenEtnico(self):
        return '<br>'.join([TesNotNull(i.PTesauro) for i in self.POrigenEtnico])
    def CaracteristicasRelevantes(self):
        return '<br>'.join([TesNotNull(i.PTesauro) for i in self.PCaracteristicasRelevantes])
    def Roles(self):
        """ obtener un diccionario de casos (no siempre)
             con los roles de esta persona"""
        p = self
        return {u'V\xedctima':unicos([o.caso for o in p.Victima_en]),
                u'Perpetrador':unicos([o.acto.caso for o in    p.Involucrado if o.acto]),

                u'Fuente personal':unicos([o.PCaso for o in   p.como_fuente ]),
                u'Informaci\xf3n sobre esta persona':unicos([o.PCaso for o in    p.fuentes] ),
                u'Sobre quien se solicita una intervenci\xf3n':unicos([o.Pcaso for o in p.Intervenciones_solicitadas_por_la_persona] ),
                u'Hay una intervenci\xf3n solicitada a esta persona':unicos([o.Pcaso for o in p.Intervenciones_solicitadas_a_la_persona] ),
                u'Inicia o realiza una  intervenci\xf3n':unicos([o.Pcaso for o in p.Intervenciones_como_interviniente] ),
                
                }

    def Roles2(self):
        """ obtener un diccionario de casos (no siempre)
             con los roles de esta persona"""
        p = self
        print p,p.apellido
        print u'V\xedctima',unicos([o.caso for o in p.Victima_en])
        print u'Perpetrador',unicos([o.acto.caso for o in    p.Involucrado if o.acto])

        print u'Fuente personal',unicos([o.PCaso for o in   p.como_fuente ])
        print         u'Informaci\xf3n sobre esta persona',unicos([o.PCaso for o in    p.fuentes] )
        print         u'Sobre quien se solicita una intervenci\xf3n',unicos([o.Pcaso for o in p.Intervenciones_solicitadas_por_la_persona] )
        print         u'Hay una intervenci\xf3n solicitada a esta persona',unicos([o.Pcaso for o in p.Intervenciones_solicitadas_a_la_persona] )
        print         u'Inicia o realiza una  intervenci\xf3n',unicos([o.Pcaso for o in p.Intervenciones_como_interviniente] )
                
                


    def strRoles(self):
        d=self.Roles()
        s=''
        for k in d.keys():
            if d[k]:
                en = ' en el caso ' if len(d[k]) < 2 else ' en los casos '
                t = k + en + ', '.join([i.descripcion for i in d[k]]) + '<br>'
                s = s + t
        return s
    def Pfecha_nac_o_fund(self):
        return self.fecha_nac_o_fund, self.Ptipo_fecha_nac_o_fund
    
    def Pfrecepcion(self):
        return self.frecepcion, self.Ptipo_frecepcion
    
    def PrtTitulo1(self):
        return "DATOS GENERALES"
    def PrtTitulo2(self):
        return u"DETALLES"
    def PrtTitulo3(self):
        return u"INFORMACI\xd3N ADMINISTRATIVA"
    def PrtTitulo4(self):
        return u"DATOS BIOGRAFICOS"
    

class Caso(dataObject):
    """registro de casos"""
    def __init__(self, descripcion, localizacion_id=None, id=None, Log=None):
        dataObject.__init__(self, id, Log=Log)
        self.descripcion = descripcion
        self.localizacion_id= localizacion_id
        self.exportar = 1
        self.exportarrelaciones = 1
        if not self.loginfo: self.PLoginfo = NewLoginfo()
        self.fecha_inicio = DefaultDate
        self.fecha_final = DefaultDate
        self.frecepcion = DefaultDate
        self.descripcion_narrativa = u''
        self.resumen_descripcion = u''
        self.observaciones = u''
        self.no_persona_afectadas = u''
        self.comentarios = u''
        self.archivos = u''
        self.proyecto_grupo = u''
        self.proyecto_conjunto = u''
        self.proyecto_se = u''
        

    def noValido(self):
        res=''
        if not   self.loginfo: res += u"No hay informaci\xf3n de creaci\xf3n de registro del caso. "
        
        if not self.resumen_descripcion: res += u"No hay res\xfamen de la descripci\xf3n del caso. "
        if not camposFechasValidas(self.tipo_fecha_inicio, self.fecha_inicio, self.tipo_fecha_final, self.fecha_final, status):
            res += u"La fecha final del caso es anterior a fecha inicial. "
        
        
        
        return res
    def borrar(self):
        porBorrar = self.actos + self.tipificaciones  + self.localidades + self.intervenciones + self.fuentes + self.PPublicaciones + self.Pvinculos + self.PvinculosInversos
        print "caso - por borrar",porBorrar
        for o in porBorrar:
            o.borrar()
        dataObject.borrar(self)
        #session.flush()
    
    def refrescar(self):
        session.refresh(self)
        porRefrescar = self.actos + self.tipificaciones  + self.localidades + self.intervenciones + self.fuentes + self.PPublicaciones + self.Pvinculos
        
        for o in porRefrescar:
            session.refresh(o)
    
    
    def Descriptor(self):
        return self.descripcion
    def __repr__(self):
        return  'Caso:' +str(self.id)
    
    
    def PrtDescriptor(self):
        return "%s"%(self.Descriptor())
    def PrtID(self):
        return "%i"%self.id
    def Pfecha_inicio(self):
        return self.fecha_inicio, self.Ptipo_fecha_inicio
    def PrtLocalidades(self):
        r=''
        for l in self.localidades:
            r = r + l.PrtDescriptor() + '<br>' 
        return r
    def setLocalidades(self):
        se = set([])
        sm = set([])
        for l in self.localidades:
            se.add(l.estado_id)
            sm.add(l.municipio_id) 
        return se,sm
    
    def Pfecha_final(self):
        return self.fecha_final, self.Ptipo_fecha_final
    
    def Pfrecepcion(self):
        return self.frecepcion, self.Ptipo_frecepcion
    
    def strTemas(self):
        r=''
        for i in self.Ptemas:
            if i:
                r=r+i.descripcion+'\n'
        return r
    def strDerechosAfectados(self):
        r=''
        for i in self.Pderechosafectados:
            if i:
                r=r+i.descripcion+'\n'
        return r
    def setDerechosAfectados(self):
        r=set([])
        for i in self.derechosafectados:
            if i:
                r.add(i.tesauro_id)
        return r
    def setTemas(self):
        r=set([])
        for i in self.temas:
            if i:
                r.add(i.tesauro_id)
        return r

    
    def Personas_relacionadas(self):
        en_intervenciones_1 = [i.solicitante for i in self.intervenciones if i.solicitante != None]
        en_intervenciones_2 = [i.contraparte for i in self.intervenciones if i.contraparte != None]
        # aqui hay un campo de intervenciones pendiente
        en_perpetradores = [perp for perp in [acto.Perpetradores for acto in self.actos] if perp != None]
        en_victimas = [p for p in self.victimas if p != None]
        en_fuente_1 = [f.PPersona for f in self.fuentes if f.PPersona != None]
        en_fuente_2 = [f.PPersona_como_fuente for f in self.fuentes if f.PPersona_como_fuente != None]
        en_publicaciones = [pub.PPersonareferenciada for pub in self.PPublicaciones if pub.PPersonareferenciada != None]
        en_interviniente = [i.Pinterviniente for i in self.intervenciones if i.Pinterviniente != None]
        l = []
        todos= en_intervenciones_1 + en_intervenciones_2 + en_perpetradores + en_victimas + en_fuente_1 + en_fuente_2 + en_publicaciones + en_interviniente
        for i in todos:
          if type(i) == Persona:
              if i not in l:
                l.append(i)
          else:
             for j in i:
                 if j not in l:
                    l.append(j)
        return l
    def Personas_relacionadas_id(self):
        "regresa una lista de id de personas relacionadas"
        return [i.id for i in self.Personas_relacionadas()]
    def Personas_relacionadas_filtro(self):
        l = self.Personas_relacionadas_id()
        filtro = sql.or_(*[Persona.id == i for i in l])
        return filtro
    
    def PrtCasosRelacionados(self):
        listaDirecta = [i.Pcaso_2.descripcion +
                        ': ' +
                        terminoReciproco(status.reciprocoRelacionCasos, i.Ptipo.name, i.Ptipo.descripcion) for i in self.PelCaso2 if i.Ptipo and i.Pcaso_2]
        listaReciproca = [i.Pcaso_1.descripcion + ': '+TesNotNull(i.Ptipo) for i in self.PelCaso1 if i.Ptipo and i.Pcaso_1]        
        lista = listaDirecta + listaReciproca
        r = "\n".join(lista)
        return r        
    def PrtTitulo1(self):
        return "DATOS GENERALES"
    def PrtTitulo2(self):
        return u"INFORMACI\xd3N NARRATIVA"
    def PrtTitulo3(self):
        return u"INFORMACI\xd3N ADMINISTRATIVA"
    def PrtTitulo4(self):
        return u"TIPIFICACIONES"
    def PrtTitulo5(self):
        return u"ACTOS, VICTIMAS, PERPETRADORES"
    def PrtTitulo6(self):
        return u"NORMATIVIDAD"
    def PrtTitulo7(self):
        return u"FUENTES"
    def PrtTitulo8(self):
        return u"INTERVENCIONES"
    def PrtTitulo9(self):
        return u"PERSONAS RELACIONADAS CON EL CASO"
    def PrtTitulo10(self):
        return u"RELACIONES ENTRE CASOS"
    

class Acto(dataObject):
    """registro de actos"""
    def __init__(self, victima, tipodeacto, id=None, Log=None, caso_id=None):
        dataObject.__init__(self, id, Log=Log)
        if type(victima) == type(1):
            self.victima_id = victima
        else:
            self.Pvictima = victima
        if caso_id:
            self.caso_id = caso_id
        self.PTipodeacto = tipodeacto
        self.descripcion = u'.'
        if not self.loginfo: self.PLoginfo = NewLoginfo()
        self.fechainicio = DefaultDate
        self.fechafin = DefaultDate
        self.exportar = 1
        self.exportarnormatividad  = 1
        self.observaciones = u''
        self.legislacion_nacional_notas = u''
        self.instrumentos_internacionales_notas = u''
        self.edad_victima_tipo=0
    def borrar(self):
        #self.localizacion_id=None
        #self.caso_id=None
        ## ojo
        #session.add(self)
        #session.flush()
        porBorrar = self.PCaracRelevantes + self.RolPerpetradores
        print porBorrar
        for o in porBorrar:
            o.borrar()
        session.delete(self)
        if self.Pvictima:
            print "rem victima ",self.Pvictima, " de ",self
            self.Pvictima.Victima_en.remove(self)
        session.flush()
        #dataObject.borrar(self)
        
    def noExportable(self):
        if self.Pvictima:
            (severidad, res) = diagRefPersona(self.Pvictima, u'v\xedctima')
            return (severidad, res)
        else:
            return 2,'' #ojo: agregar mensaje
    def noValido(self):
        res=''
        if not   self.loginfo: res += u"No hay informaci\xf3n de creaci\xf3n de registro. "
        if not self.tipodeacto: res += u"No hay informaci\xf3n de tipo de acto. "
        if not self.victima_id: res += u"No hay informaci\xf3n de victima. "
        if not camposFechasValidas(self.tipofechainicio, self.fechainicio, self.tipofechafinal, self.fechafin, status):
            res += u"La fecha final del acto es anterior a la fecha inicial. "
        
        return res    
        
    def __repr__(self):
        return  'Acto:' +str(self.id)
    
    def Perpetradores(self):
        return [i.persona for i in self.RolPerpetradores]
    def Descriptor(self):
        if self.Pvictima: nombre = self.Pvictima.Descriptor()
        else:
            nombre = ''
        return '%(persona)s / %(derecho)s'%{'persona':nombre, 'derecho':tesDesc(self.PTipodeacto)}

    def PrtID(self):
        return "%i"%self.id
    def NombreVictima(self):
        if self.Pvictima:
            return self.Pvictima.Descriptor()
        else:
            return ''
    def Pfechainicio(self):
        return self.fechainicio, self.PTipodefechainicio
    def Pfechafin(self):
        return self.fechafin, self.PTipodefechafin
    def strLegisNac(self):
        r=''
        lista = [i for i in self.caso.PLegisNac if i.acto_id == self.id]
        r ="\n".join([ "%s %s"%(i.Descriptor(), " (Nota: %s)"%i.notas if i.notas else '') for i in lista])

        return r
    def strEdad_victima(self):
        if self.edad_victima:
            return u"%i a\xf1os"%self.edad_victima
        return ''
    def strCaracRelevantes(self):
        r=''
        
        lista = [i.Descriptor() for i in self.PCaracRelevantes]
        lista.sort()
        
        for i in lista:
            if i:
                r=r+i+'\n'
        return r
    
    
    
    def strLegisInt(self):
        r=''
        lista = [i for i in self.caso.PLegisInt if i.acto_id == self.id]
        for i in lista:
            if i:
                nota = ''
                if i.notas:
                    nota=" (Nota: "+i.notas+")"
                r=r+i.Descriptor()+nota+'\n'
        return r
    
    
    
class Publicacion(dataObject):
    """publicacion"""
    def __init__(self, caso, titulo, id=None, Log=None):
        dataObject.__init__(self, id, Log=Log)
        if not self.loginfo: self.PLoginfo = NewLoginfo()
        if type(caso) == type(1):
            self.caso_id = caso
        else:
            self.PCaso = caso
        self.titulo_de_parte = titulo
        self.PPersonareferenciada = None
        self.PTipofecha = None
        self.PTipopublicacion = None
        self.PIdioma = None
        self.PLengua_indigena = None
        self.PConfiabilidad = None
        self.fecha = DefaultDate
        self.fecha_consulta = DefaultDate
        self.exportar = 1
        self.comentarios = u''
        
    def __repr__(self):
        return  'Fuente documental:' +str(self.id)
    
    def noValido(self):
        res=''
        if not   self.loginfo: res += u"No hay informaci\xf3n de creaci\xf3n de registro. "
        if not   self.titulo_de_parte: res += u"No hay informaci\xf3n de identificaci\xf3n. "
    def noExportable(self):
        res=''
        severidad=0
        if self.PPersonareferenciada:
            (severidad, res) = diagRefPersona(self.PPersonareferenciada, u'sobre qui\xe9n se aporta informaci\xf3n')
        return (severidad, res)
        
        
        
        return res
    def Descriptor(self):
        return self.titulo_de_parte
    def Pfecha(self):
        return self.fecha, self.PTipofecha
    def Pfecha_consulta(self):
        return self.fecha_consulta, self.PTipofechaConsulta
    
    def PrtID(self):
        return "%i"%self.id

    def borrar(self):
        #self.caso_id=None
        ## ojo
        #session.add(self)
        #session.flush()
        dataObject.borrar(self)
    
UserMapper =    mapper(User, user) 
GruposMapper = mapper(Grupo, grupo)

ConfigTdtMapper = mapper(ConfigTdt, configTdt)
    
TesMapper = mapper(TesNode, 
                   tesauro, 
                   properties={
                               'children': relation(TesNode, 
                                        cascade="all, delete",
                                        backref=backref("parent", 
                                                        remote_side=[tesauro.c.id]),
                                                        collection_class=attribute_mapped_collection('name'),
                                                        lazy=True
                                                        )
                                }
                )
                         
Caso_relMapper = mapper(Caso_vinculo, caso_vinculo,
                            properties=
                            {'Pcaso_1':relation(Caso, primaryjoin=caso.c.id == caso_vinculo.c.caso_1_id, backref="PelCaso2"),
                             'Pcaso_2':relation(Caso, primaryjoin=caso.c.id == caso_vinculo.c.caso_2_id, backref="PelCaso1"),
                             
                             'Ptipo':relation(TesMapper,
                                             primaryjoin=(tesauro.c.id == caso_vinculo.c.tipo_id)), 
                             'PLoginfo':relation(LoginfoMapper)
                             }
                             )

EventoTipificacionMapper = mapper(EventoTipificacion, evento_tipificacion,
                                  properties=
                                  {'tipificacion':relation(TesNode),
                                  'PLoginfo':relation(LoginfoMapper),

                                      }
                                  )

LocalidadMapper = mapper(Localidad, localidad,
                                  properties=
                                  {'Pais':relation(TesMapper, primaryjoin=tesauro.c.id == localidad.c.pais_id),
                                   'Estado':relation(TesMapper, primaryjoin=tesauro.c.id == localidad.c.estado_id),
                                   'Municipio':relation(TesMapper, primaryjoin=tesauro.c.id == localidad.c.municipio_id),
                                   'PLoginfo':relation(LoginfoMapper),
                                   })

#ActoPersonaMapper = mapper(Acto_Persona,acto_persona,properties=
#                           {
#                             'persona':relation(Persona,backref='acto_persona'),
#                             'PLoginfo':relation(LoginfoMapper),
#                            }
#                           )

PersonaMapper = mapper(Persona, persona,properties=
                  {
                  #'SexoCodigo':column_property(
                  #    
                  #         select([tesauro.c.name], tesauro.c.id == persona.c.sexo).as_scalar().label("Sexo")
                  #         ),
                   'Psexo':relation(TesMapper, primaryjoin=tesauro.c.id == persona.c.sexo),
                   'Ptipo_fecha_nac_o_fund':relation(TesMapper, primaryjoin=tesauro.c.id == persona.c.tipo_fecha_nac_o_fund),
                   'Ppais_nac_u_origen':relation(TesMapper, primaryjoin=tesauro.c.id == persona.c.pais_nac_u_origen),
                   'Pestado_nac_u_origen':relation(TesMapper, primaryjoin=tesauro.c.id == persona.c.estado_nac_u_origen),
                   'Pmpio_nac_u_origen':relation(TesMapper, primaryjoin=tesauro.c.id == persona.c.mpio_nac_u_origen),
                   'Pciudadania_o_sede':relation(TesMapper, primaryjoin=tesauro.c.id == persona.c.ciudadania_o_sede),
                   'Pescolaridad':relation(TesMapper, primaryjoin=tesauro.c.id == persona.c.escolaridad),
                   'Pocupacion':relation(TesMapper, primaryjoin=tesauro.c.id == persona.c.ocupacion),
                   #'Porigen_etnico':relation(TesMapper, primaryjoin=tesauro.c.id == persona.c.origen_etnico),
                   'Preligion':relation(TesMapper, primaryjoin=tesauro.c.id == persona.c.religion),
                   'Pestado_civil':relation(TesMapper, primaryjoin=tesauro.c.id == persona.c.estado_civil),
                   'Ptipodefecha':relation(TesMapper, primaryjoin=tesauro.c.id == persona.c.tipo_fecha_nac_o_fund),
                   'Ptipo_frecepcion':relation(TesMapper, primaryjoin=tesauro.c.id == persona.c.tipo_frecepcion),
                   #'Pconfiabilidad':relation(TesMapper, primaryjoin=tesauro.c.id == persona.c.confiabilidad),
                   'Pmonitoreo':relation(TesMapper, primaryjoin=tesauro.c.id == persona.c.monitoreo),
                   'Ptipo':relation(TesMapper, primaryjoin=tesauro.c.id == persona.c.tipo),
                   'PLoginfo':relation(LoginfoMapper),
                   'Pdetallesbiograficos':relation(Persona_Vinculo, 
                                          primaryjoin=sql.and_(persona.c.id==persona_vinculo.c.persona_1_id,
                                                               persona_vinculo.c.persona_2_id == None)
                                                    ),
                   'PpersonasRelacionadas':relation(Persona,
                                                    secondary=persona_vinculo,
                                                    primaryjoin=persona.c.id==persona_vinculo.c.persona_1_id,
                                                    secondaryjoin=persona.c.id==persona_vinculo.c.persona_2_id),
                   'PpersonasRelacionadasInv':relation(Persona,
                                                    secondary=persona_vinculo,
                                                    primaryjoin=persona.c.id==persona_vinculo.c.persona_2_id,
                                                    secondaryjoin=persona.c.id==persona_vinculo.c.persona_1_id),
                   'Pdetallesyvinculosbiograficos':relation(Persona_Vinculo, 
                                          primaryjoin=sql.or_(persona.c.id==persona_vinculo.c.persona_1_id,
                                                              persona.c.id==persona_vinculo.c.persona_2_id
                                                              )
                                                    )
                                                            
                  }
                )


Persona_VinculoMapper = mapper(Persona_Vinculo, persona_vinculo, properties=
                          {'vinculo1':relation(Persona, primaryjoin=persona.c.id==persona_vinculo.c.persona_1_id,  backref='LaOtra2'),
                           'vinculo2':relation(Persona,  primaryjoin=persona.c.id==persona_vinculo.c.persona_2_id,   backref='LaOtra1'),
                           'tipo':relation(TesMapper,
                                             primaryjoin=(tesauro.c.id == persona_vinculo.c.tipo_id)), 
                            'PLoginfo':relation(LoginfoMapper),
                            'Ptipofecha_inicial':relation(TesMapper,
                            primaryjoin=(tesauro.c.id == persona_vinculo.c.tipofecha_inicial)),
                            'Ptipofecha_info_vigente':relation(TesMapper,
                            primaryjoin=(tesauro.c.id == persona_vinculo.c.tipofecha_info_vigente)),

                            'Ptipofecha_final':relation(TesMapper,
                            primaryjoin=(tesauro.c.id == persona_vinculo.c.tipofecha_final)),
                            
                          })



IntervencionMapper = mapper(Intervencion, intervencion,
                     properties=
                       {'solicitante':relation(PersonaMapper,
                                             primaryjoin=(persona.c.id == intervencion.c.persona_id_dequien), 
                                             backref='Intervenciones_solicitadas_por_la_persona'),
                        'contraparte':relation(PersonaMapper,
                                             primaryjoin=(persona.c.id == intervencion.c.persona_id_aquien), 
                                             backref='Intervenciones_solicitadas_a_la_persona'),
                        'Pinterviniente':relation(PersonaMapper,
                                             primaryjoin=(persona.c.id == intervencion.c.persona_id_interviniente), 
                                             backref='Intervenciones_como_interviniente'),
                        'tipo':relation(TesMapper,
                                             primaryjoin=(tesauro.c.id == intervencion.c.tesauro_id), 
                                        ),
                        #'Pimpacto':relation(TesMapper,
                        #                     primaryjoin=(tesauro.c.id == intervencion.c.impacto_id), 
                        #                ),
                        #'Prespuesta':relation(TesMapper,
                        #                     primaryjoin=(tesauro.c.id == intervencion.c.respuesta_id), 
                        #                ),
                                        
                        'Pestatus':relation(TesMapper,
                                             primaryjoin=(tesauro.c.id == intervencion.c.estatus_id), 
                                        ),
                                        
                        'PTipofecha':relation(TesMapper, primaryjoin=(intervencion.c.tipofecha == tesauro.c.id)),
                        'PLoginfo':relation(LoginfoMapper),
                                        
                        }
                     )

InvolucramientoMapper = mapper(Involucramiento, involucramiento, properties=
                    {'acto':relation(Acto),
                     'persona':relation(Persona, primaryjoin=(involucramiento.c.persona_id==persona.c.id), backref='Involucrado'),
                     'Pgradoinvolucramiento':relation(TesMapper, primaryjoin=(involucramiento.c.gradoinvolucramiento == tesauro.c.id)),
                     'Ptipoperpetrador':relation(TesMapper, primaryjoin=(involucramiento.c.tipoperpetrador == tesauro.c.id)),
                     'Pultimostatusperpetrador':relation(TesMapper, primaryjoin=(involucramiento.c.ultimostatusperpetrador == tesauro.c.id)),
                     'PLoginfo':relation(LoginfoMapper),
                     }
                               )


ActoMapper = mapper(Acto, acto, properties=
                    {
                    
                    'Pvictima':relation(Persona, backref='Victima_en'),
                    
                    #'involucrados':relation(InvolucramientoMapper),
                    'RolPerpetradores':relation(Involucramiento, primaryjoin=involucramiento.c.acto_id == acto.c.id),
                    'Perpetradores':relation(Persona, secondary=involucramiento,
                                             primaryjoin=involucramiento.c.acto_id == acto.c.id,
                                             secondaryjoin=involucramiento.c.persona_id==persona.c.id),
                     'PTipodeacto':relation(TesMapper, primaryjoin=(acto.c.tipodeacto == tesauro.c.id)),
                     'PEstatusvdh':relation(TesMapper, primaryjoin=(acto.c.estatusvdh == tesauro.c.id)),
                     'PTipodefechainicio':relation(TesMapper, primaryjoin=(acto.c.tipofechainicio == tesauro.c.id)),
                     'PTipodefechafin':relation(TesMapper, primaryjoin=(acto.c.tipofechafinal == tesauro.c.id)),
                     'PEstatusvictima':relation(TesMapper, primaryjoin=(acto.c.estatusvictima == tesauro.c.id)),
                     'PTipodelugar':relation(TesMapper, primaryjoin=(acto.c.tipolugar == tesauro.c.id)),
                     'PLoginfo':relation(LoginfoMapper),
                     'PLocalidad':relation(LocalidadMapper),
                     
                     'PGradoinvolucramiento':relation(TesMapper, secondary=involucramiento,
                                             primaryjoin=acto.c.id == involucramiento.c.acto_id,
                                             secondaryjoin=involucramiento.c.gradoinvolucramiento== tesauro.c.id),
                     'PTipoperpetrador':relation(TesMapper, secondary=involucramiento,
                                             primaryjoin=acto.c.id == involucramiento.c.acto_id,
                                             secondaryjoin=involucramiento.c.tipoperpetrador== tesauro.c.id),
                     'PUltimostatusperpetrador':relation(TesMapper, secondary=involucramiento,
                                             primaryjoin=acto.c.id == involucramiento.c.acto_id,
                                             secondaryjoin=involucramiento.c.ultimostatusperpetrador== tesauro.c.id),


                                             
                     
                         
                    }
                   )

DerechovioladoMapper = mapper(Derechoviolado, derechoviolado, properties= 
                     {
                     'Pacto':relation(ActoMapper, backref='PDerechosvioladosBack'),
                     'Pderecho':relation(TesMapper),
                     'PLoginfo':relation(LoginfoMapper),
                     }
                        )
                            
CasoMapper = mapper(Caso, caso, properties=
                    {'actos':relation(ActoMapper, backref='caso'),
                     'victimas':relation(Persona, secondary=acto,
                                         primaryjoin=caso.c.id == acto.c.caso_id,
                                         secondaryjoin=acto.c.victima_id == persona.c.id),
                     'PcasosRelacionados':relation(Caso, secondary=caso_vinculo,
                                         primaryjoin=caso.c.id == caso_vinculo.c.caso_1_id,
                                         secondaryjoin=caso_vinculo.c.caso_2_id == caso.c.id),
                     'PcasosRelacionadosReciprocos':relation(Caso, secondary=caso_vinculo,
                                         primaryjoin=caso.c.id == caso_vinculo.c.caso_2_id,
                                         secondaryjoin=caso_vinculo.c.caso_1_id == caso.c.id),
                     'Pvinculos':relation(Caso_vinculo,
                                         primaryjoin=caso.c.id == caso_vinculo.c.caso_1_id
                                        ), 
                     'PvinculosInversos':relation(Caso_vinculo,
                                         primaryjoin=caso.c.id == caso_vinculo.c.caso_2_id
                                        ),
                    
                     'tipificaciones':relation(EventoTipificacionMapper),
                     'derechosafectados':relation(EventoTipificacionMapper,primaryjoin=
                     sql.and_(evento_tipificacion.c.evento_id == caso.c.id, evento_tipificacion.c.codigo==153)
                     ),
                     'derechosafectadosL':relation(EventoTipificacionMapper,primaryjoin=
                     sql.and_(evento_tipificacion.c.evento_id == caso.c.id, evento_tipificacion.c.codigo==153)
                     ),
                     'Pderechosafectados':relation(TesMapper, secondary=evento_tipificacion,
                     primaryjoin=
                     sql.and_(evento_tipificacion.c.evento_id == caso.c.id, evento_tipificacion.c.codigo==153),
                     secondaryjoin=(evento_tipificacion.c.tesauro_id  == tesauro.c.id),
                     ), 
                     'temas':relation(EventoTipificacionMapper,primaryjoin=
                     sql.and_(evento_tipificacion.c.evento_id == caso.c.id, evento_tipificacion.c.codigo==154),
                     ),
                     
                     'Ptemas':relation(TesMapper, secondary=evento_tipificacion,
                               primaryjoin=
                               sql.and_(evento_tipificacion.c.evento_id == caso.c.id, evento_tipificacion.c.codigo==154),
                               secondaryjoin=(evento_tipificacion.c.tesauro_id  == tesauro.c.id)
                               ),
                     
                     

                     'intervenciones':relation(Intervencion, backref='Pcaso'),
                     'Ptipo_fecha_inicio':relation(TesMapper, primaryjoin=(caso.c.tipo_fecha_inicio == tesauro.c.id)),
                     'Ptipo_fecha_final':relation(TesMapper, primaryjoin=(caso.c.tipo_fecha_final == tesauro.c.id)),
                     'Ptipo_frecepcion':relation(TesMapper, primaryjoin=(caso.c.tipo_frecepcion == tesauro.c.id)),
                     'Pmonitoreo':relation(TesMapper, primaryjoin=(caso.c.monitoreo == tesauro.c.id)),

                     'localidades':relation(Localidad, backref='caso'), 
                     'PLoginfo':relation(LoginfoMapper),
                     'PLegisNac':relation(EventoTipificacion,
                                         primaryjoin=
                                         sql.and_(evento_tipificacion.c.evento_id == caso.c.id,  evento_tipificacion.c.codigo==2154),
                                         ),
                     'PLegisInt':relation(EventoTipificacion,
                                         primaryjoin=
                                         sql.and_(evento_tipificacion.c.evento_id == caso.c.id,  evento_tipificacion.c.codigo==2155)
                                         ),
                     'Pactonormatividad':relation(EventoTipificacion,
                                         primaryjoin=
                                         sql.and_(evento_tipificacion.c.evento_id == caso.c.id,  sql.or_(evento_tipificacion.c.codigo==2155,
                                                                                                         evento_tipificacion.c.codigo==2154 )                                  )
                                         ),
                    }
                   )

FuenteMapper = mapper(Fuente, fuente, properties=
                      {
                      'PCaso':relation(CasoMapper, backref='fuentes'),

                      'PPersona':relation(PersonaMapper, primaryjoin=(persona.c.id == fuente.c.persona_referenciada_id), backref='fuentes'),
                      'PPersona_como_fuente':relation(PersonaMapper, primaryjoin=(persona.c.id == fuente.c.persona_fuente_id), backref='como_fuente'),
                      'PConexion_info':relation(TesMapper, primaryjoin=(fuente.c.conexion_con_informacion == tesauro.c.id)),
                      'PTipofecha':relation(TesMapper, primaryjoin=(fuente.c.tipofecha == tesauro.c.id)),
                      'PIdioma':relation(TesMapper, primaryjoin=(fuente.c.idioma == tesauro.c.id)),
                      'PLengua_indigena':relation(TesMapper, primaryjoin=(fuente.c.lengua_indigena == tesauro.c.id)),
                      'PConfiabilidad':relation(TesMapper, primaryjoin=(fuente.c.confiabilidad == tesauro.c.id)),
                      'PLoginfo':relation(LoginfoMapper),
                      
                      
                       }
                      )
PublicacionMapper = mapper(Publicacion, publicacion, properties=
                      {
                      'PCaso':relation(CasoMapper, backref='PPublicaciones'),
                      'PLoginfo':relation(LoginfoMapper),
                      'PPersonareferenciada':relation(PersonaMapper, primaryjoin=(persona.c.id == publicacion.c.persona_referenciada_id), backref='PPublicaciones'),
                      'PTipofecha':relation(TesMapper, primaryjoin=(publicacion.c.tipofecha == tesauro.c.id)),
                      'PTipofechaConsulta':relation(TesMapper, primaryjoin=(publicacion.c.tipofechaconsulta == tesauro.c.id)),
                      'PTipopublicacion':relation(TesMapper, primaryjoin=(publicacion.c.tipopublicacion == tesauro.c.id)),
                      'PIdioma':relation(TesMapper, primaryjoin=(publicacion.c.idioma == tesauro.c.id)),
                      'PLengua_indigena':relation(TesMapper, primaryjoin=(publicacion.c.lengua_indigena == tesauro.c.id)),
                      'PConfiabilidad':relation(TesMapper, primaryjoin=(publicacion.c.confiabilidad == tesauro.c.id)),
                      
                      
                      
                      }
                    )
                      
CaracrelevantesMapper = mapper(Caracrelevantes, caracrelevantes,
                       properties= 
                     {
                      'Pacto':relation(ActoMapper, backref='PCaracRelevantes'),
                      'PLoginfo':relation(LoginfoMapper),
                      'Pcaracteristicarelevante':relation(TesMapper)}
                      
                    )

PersonaTipificacionMapper = mapper(PersonaTipificacion, persona_tipificacion,
                                   properties=
                                   {
                                   
                                   'PPersona':relation(PersonaMapper,primaryjoin=
                                    persona_tipificacion.c.persona_id == persona.c.id, backref="Ptipificacion"),
                                   'PPersona1':relation(PersonaMapper,primaryjoin=
                                    sql.and_(persona_tipificacion.c.persona_id == persona.c.id, persona_tipificacion.c.codigo==945), backref="PIdiomas"),
                                    # 945 = Idioma que habla
                                    'PPersona2':relation(PersonaMapper,primaryjoin=
                                    sql.and_(persona_tipificacion.c.persona_id == persona.c.id, persona_tipificacion.c.codigo==946), backref="PLenguas"),
                                    # 946 = lengua (predominante)
                                    'PPersona3':relation(PersonaMapper,primaryjoin=
                                    sql.and_(persona_tipificacion.c.persona_id == persona.c.id, persona_tipificacion.c.codigo==942), backref="POrigenEtnico"),
                                    # 942 = origen etnico
                                    'PPersona4':relation(PersonaMapper,primaryjoin=
                                    sql.and_(persona_tipificacion.c.persona_id == persona.c.id, persona_tipificacion.c.codigo==944), backref="PCaracteristicasRelevantes"),
                                    
                                    'PPersona5':relation(PersonaMapper,primaryjoin=
                                    sql.and_(persona_tipificacion.c.persona_id == persona.c.id, persona_tipificacion.c.codigo==910), backref="PDirecciones"),
                                    'PTesauro':relation(TesMapper, primaryjoin=tesauro.c.id == persona_tipificacion.c.tesauro_id),
                                    'PLoginfo':relation(LoginfoMapper),
                                    }
                                )

def TesDescrip(i):
    return i.descripcion.encode('ascii', 'ignore')
def TesName(i):
    if hasattr(i, "name"):
         return i.name
    else:
         return i.descripcion.encode('ascii', 'ignore')
def TesNamebyId(id):
    if id:
        t=QueryTesNode.filter(TesNode.id == id)
        if t.count():
            v=t[0]
            
            return v.descripcion
        else:
            return ''
    else:
        return ''
def TesById(id):
    if id:
        t=QueryTesNode.filter(TesNode.id == id).first()
        return t
def TesNotNull(n):
    if n:
        return n.descripcion
    else:
        return ''

def StrNotNull(n):
    if n:
        return n
    else:
        return ''
    
def TesNombre(id):
    if id:
        n = session.query(TesNode).filter(TesNode.id == id).first()
        return TesNotNull(n)



    
def LlenaCtrlCategoria(ctrl, raiz, selected=None, orden="name", Tselected=None):
        ctrl.Clear()
        t = QueryTesNode
        q =  t.filter(TesNode.name==raiz)
        if q.count():
           n = q[0]
           lista = n.children.values()
           if orden == "descripcion":
               lista.sort(key=TesDescrip)
           else:
               lista.sort(key=TesName)
           #if raiz == u'T48':    ojo
           ctrl.Append('', None)
           for i in lista:
               ctrl.Append(i.ClaveODesc(), i)
           if Tselected: selected = Tselected.descripcion
           if selected: CtrlSelect(ctrl, selected)
           else: ctrl.SetSelection(-1)
        else:
            
            ctrl.Append('??????????')

def LlenaCtrlMunicipios(ctrl, objRaiz, selected=None):
        ctrl.Clear()
        if objRaiz:
            lista = session.query(TesNode).filter(TesNode.parent == objRaiz).order_by(TesNode.descripcion).all()
            ctrl.Append('', None)
            for i in lista:
                ctrl.Append(i.ClaveODesc(), i)
            if selected: CtrlSelect(ctrl, selected)
                 
def LlenaCtrlChildren(ctrl, objRaiz, selected=None, orden="name", Tselected=None, expr=None):
        ctrl.Clear()
        if objRaiz:
            lista = objRaiz.children.values()
            if expr:
                pattern = re.compile('(?i).*'+expr)
                l = filter(lambda a:pattern.match(a.descripcion), lista)
                lista = l
            
            if lista:
               if orden == "descripcion":
                   lista.sort(key=TesDescrip)
               else:
                   lista.sort(key=TesName)
               ctrl.Append('', None)
               for i in lista:
                   ctrl.Append(i.ClaveODesc(), i)
               if Tselected: selected = Tselected.descripcion
               if selected: CtrlSelect(ctrl, selected)
            else:
                
                ctrl.Append('(Municipio no encontrado)')            
                
def LlenaCtrl(ctrl, objeto, selected=None, orden="name"):
        q=session.query(objeto)
#        n=session.query(objeto).list()
        n=[i for i in q]
        if orden == "descripcion":
            lista.sort(key=TesDescrip)
        else:
            n.sort(key=TesName)
        ctrl.Clear()
        for i in n:
            ctrl.Append(i.descripcion, i)
            
        if selected: CtrlSelect(ctrl, selected)
        

trans={u'\xc1':'A', u'\xc9':'E',u'\xcd':'I',u'\xd3':'O',u'\xda':'U',u'\xd1':u'\xd1'}
#trans={u'\xc1':'A', u'\xc9':'E',u'\xcd':'I',u'\xd3':'O',u'\xda':'U'}
transWildChar={u'\xc1':'_', u'\xc9':'_',u'\xcd':'_',u'\xd3':'_',u'\xda':'_',u'A':'_', u'E':'_',u'I':'_',u'O':'_',u'U':'_',u'\xd1':u'\xd1'}
transCR={u'\n':' '}

def MyTranslate(s, trans):
    if s:
        s1=s
        n=len(s1)
        
        for i in range(n):
            
    
             if s1[i] in trans.keys():
                 
                 s1=s1[:i]+trans[s1[i]]+s1[i+1:]
        
        return s1
    else:
        return ''

    
def Sortable(s, trans=trans):
      
    s1=upper(s)
    n=len(s1)
    
    for i in range(n):
        

         if s1[i] in trans.keys():
             
             s1=s1[:i]+trans[s1[i]]+s1[i+1:]
             
         else:
             if ord(s1[i]) > 127:
                 s1=s1[:i]+'?'+s1[i+1:]
                 
    
    return s1



    
def sortableDescriptor(self):
    #return upper(self.Descriptor())
    return Sortable(self.Descriptor())

def filtraPorContenedores(q, Clase):
    if status.filtroGrupo:
        q = q.filter(Clase.clavegrupo == status.filtroGrupo)
    if status.filtroContenedor:
        q = q.filter(Clase.clavestatus == status.filtroContenedor)
    return q

def LlenaCtrlCasos(ctrl, selected=None, filtroIsearch=None, NotMyself=False, dataset=None):
    
    q=session.query(Caso)
    #q = filtraPorContenedores(q, Caso)
    if status.filtroGrupo:
        q = q.filter(Caso.clavegrupo == status.filtroGrupo)
    if status.filtroContenedor:
        q = q.filter(Caso.clavestatus == status.filtroContenedor)
    if filtroIsearch:
        q = q.filter(Caso.descripcion.ilike('%'+filtroIsearch+'%'))
    seleccionados = 0
    if dataset != None:
        N=dataset
        total = len(N)
    else:
        N=q.all()
        status.casosSeleccionados = N
        total=q.count()
    if NotMyself:
        N = [i for i in N if i != status.casoActual]
    #N.sort(cmp=lambda x,y:Sortable(x.descripcion) < Sortable(x.descripcion))
    N.sort(key=sortableDescriptor)

    ctrl.Clear()
    for i in N:
        ctrl.Append(i.descripcion, i)
    if selected: CtrlSelect(ctrl, selected)
    return total

        


def LlenaCtrl2(ctrl, lista, selected=None, orden="name"):
        if orden == "descripcion":
            lista.sort(key=TesDescrip)
        else:
            lista.sort(key=TesName)
        ctrl.Clear()
        for i in lista:
            ctrl.Append(i.descripcion, i)
            
            
        if selected: CtrlSelect(ctrl, selected)
        
def LlenaCtrl3(ctrl, lista, selected=None, append=None, orden="name"):

        
        if not append:
            ctrl.Clear()
        
        if orden=='name':
            lista.sort(key=operator.itemgetter(1))
        for i in lista:
            if i[1]:
                ctrl.Append(i[1], i[0])
            else:
                ctrl.Append('????', i[0])
            
            
        if selected: CtrlSelect(ctrl, selected)
        return len(lista)
        
        
def LlenaCtrlTipificacion(ctrl, codigo, event):
    ctrl.Clear()
    for i in event.tipificaciones:
           if i.codigo == codigo:
              ctrl.Append(i.tipificacion.descripcion, i ) 


def LlenaCtrlPersonaTipificacion(ctrl, collection):
    ctrl.Clear()
    L = [(i.PTesauro.descripcion, i ) for i in collection]
    L=sorted(L, key=operator.itemgetter(0))

    
    for i in L:
        
              ctrl.Append(i[0], i[1] ) 



def CtrlSelect(ctrl,expr):
    
    if sameType(expr, u"a"):
      if expr:
          ctrl.SetStringSelection(expr)
      else:
          ctrl.SetSelection(-1)
    else:
        if expr:
            if hasattr(expr, 'descripcion'):
                ctrl.SetStringSelection(expr.descripcion)
            else:
                if hasattr(expr, 'Descriptor'):
                    
                    ctrl.SetStringSelection(expr.Descriptor())
        else:
            ctrl.SetSelection(-1)
def LlenaTree(tree, element, node, expand=True, toExpand=None, NamePattern=None, id=None, poli=None, treeStyle=None, VOrden=None, maxDeep=999):
    
    if maxDeep >0:
        desc = node.descripcion
        name = node.name
     
        
        if NamePattern:
            if not(NamePattern.match(name)):
                return
        if not desc: desc = "???"
        if element:
            child = tree.AppendItem(element, desc)
            
            
        else:
            child = tree.AddRoot(desc)
            child.IsRoot=True
        
        tree.SetPyData(child, node)
        if node.id == id:
            
            tree.EnsureVisible(child)
            tree.SelectItem(child)
            
        ClaveOrden = None
        if VOrden:
            ClaveOrden = VOrden[0]        
        if ClaveOrden == "C":
            ColumnaOrden = TesNode.name
        else:
            ColumnaOrden = TesNode.descripcion
        # ojo ojo
        if node.id in status.padres:
            try:
                q = session.query(TesNode).filter(TesNode.parent == node).order_by(ColumnaOrden).all()
            except:
                MError(None, u"Ocurri\xf3 un problema de lectura en la red. Se recomienda cerrar el programa y volver a entrar") 
            
            ListaClaves = [i.name for i in q]
        else:
            ListaClaves = []
        #ListaClaves = node.children.keys()

        #if ClaveOrden == "C":
        #    ListaClaves.sort()
        if VOrden:
            if len(VOrden) > 1:
                orden = VOrden[1:]
            else:
                orden = VOrden
        else:
            orden = None
        for subnodeKey in ListaClaves:
            
            LlenaTree(tree, child, node.children[subnodeKey], expand=False, toExpand=toExpand, NamePattern=NamePattern, id=id, treeStyle=treeStyle, VOrden=orden, maxDeep = maxDeep - 1)
        #if not ClaveOrden or ClaveOrden == "A":
        #    tree.SortChildren(child)
        if expand:
            
              tree.Expand(child)
              pass
        if node.name == toExpand:
            tree.Expand(child)
            tree.EnsureVisible(child)
        
        
        if treeStyle == "vocab":
            pass
        else:
            
            estilo = wx.TR_HAS_BUTTONS | wx.TR_HIDE_ROOT
            
            if poli:
                estilo= estilo | wx.TR_MULTIPLE
                
            tree.SetWindowStyle(estilo)
def StrNotNull(MyStr, titulo='', delim=''):
    if MyStr: return titulo+MyStr+delim
    else: return ''
def DireccionesPersona(P, delim='<br>'):
    
    return [(i, TesNotNull(i.PTesauro)+': '+   MyTranslate(StrNotNull(i.masinformacion,delim=delim), transCR)+StrNotNull(i.telefono, titulo='Tel/Fax. ',delim=delim)+\
                StrNotNull(i.celular,titulo='Cel. ',delim=delim)+StrNotNull(i.correo_e,titulo='Mail: ',delim=delim)+StrNotNull(i.web,titulo='Web: ',delim=delim)) for i in P.PDirecciones]

def LlenaAyuda(self, Pantalla):
    
    if not Pantalla: return
    q = session.query(TesNode)
    padre = q.filter(TesNode.name == Pantalla).first()
    
    
    if not padre:
        print "No hay ayuda para ", Pantalla
        return
    ayudas = q.filter(TesNode.parent == padre).all()
    if ayudas:
        for ayuda in ayudas:
            
            names = [i.strip() for i in ayuda.name.split(',')]
            if names and names != [u'']:
                #print names ,' de ', Pantalla
                for name in names:
                    if hasattr(self, name):
                        ctrl = getattr(self, name)
                        ctrl.SetHelpText(ayuda.notas)
                        ctrl.SetToolTipString('')
                        if status.debug:
                            print "estableciendo ayuda para "+name+" en ",Pantalla
                            #print ctrl.GetHelpText().encode('latin-1', 'replace')
                    else:
                        print "AYUDA: no existe el control "+name+ ' en '+Pantalla

            else:
                self.SetHelpText(ayuda.notas)  
                print "por omision se cargo ayuda para " ,Pantalla
                        
                

    else:
        print "no hay ayudas para ", Pantalla    
    
        
def LlenaPersonas(ctrl, filtro='Todas', filtro2='', Pselected=None, dataset=None, excepto=None):
    
    q = session.query(Persona)
    
    q=filtraPorContenedores(q, Persona)
    
    
    if excepto:
        q = q.filter(Persona.id != excepto.id)
    
    
    lista=[]
    if filtro2:
        lista = q.filter(sql.or_(Persona.apellido.ilike('%'+filtro2+'%'),Persona.nombre.ilike('%'+filtro2+'%') )).order_by(Persona.apellido).all()
    elif dataset != None:
        lista=dataset    
    else:
        if filtro == 'Todas':
            lista = q.order_by(Persona.apellido).all()

        if filtro == 'Individual':
            lista = q.filter(Persona.esindividual == 1).order_by(Persona.apellido).all()
                
        if filtro == 'Colectiva':
            lista = q.filter(Persona.esindividual == 0).order_by(Persona.apellido).all()
        if filtro == 'Relacionadas con el caso':
            if status.casoActual:
                session.refresh(status.casoActual)
                miFiltro = status.casoActual.Personas_relacionadas_filtro()
                lista = q.filter(miFiltro).order_by(Persona.apellido).all()
                
                #lista = status.casoActual.Personas_relacionadas()
                
    ctrl.Clear()
    
    lista.sort(key=sortableDescriptor)
    for i in lista:
        ctrl.Append(i.Descriptor(), i)
    total = len(lista)
    
    if status.personaActual:
        CtrlSelect(ctrl, status.personaActual.Descriptor())
    if Pselected:
        CtrlSelect(ctrl, Pselected.Descriptor())
    return total
        
def BorraPersona(P):
    if P:
        d= P.Roles()
        Razones = ','.join([i for i in d.keys() if d[i]])
        if not Razones:
            try:
                 session.delete(P)
                 FlushInfo(id=135)
                 status.personaActual = None
            except:
                 MError(self, 'Esta persona no pudo ser dada de baja')
                 print "Unexpected error:", sys.exc_info()


            
def LlenaPerpetradores(self, ctrl):
        """ llena una lista con registros de involucramiento en rol de perpetrador """
        lista = [i for i in status.actoActual.RolPerpetradores]
        ctrl.Clear()
        
        lista.sort(lambda x,y:cmp(sortableDescriptor(x.persona), sortableDescriptor(y.persona)))
        #lista.sort(key=operator.itemgetter(0).persona.sortableDescriptor)
        for i in lista:
            ctrl.Append(i.persona.Descriptor(), i)
        if status.involActual:
            CtrlSelect(ctrl, status.involActual.persona.Descriptor())
        t=len(lista)
        self.statixText50.SetLabel("%i Perpetradores"%t)
        
            
def Vincula(p1,p2,tipo):
    v=Persona_Vinculo(p1)
    
    v.vinculo2=p2
    
    v.tipo=tipo
    
    session.add(v)
    
    FlushInfo(id=103)
    
    status.vinculoActual=v
def MError(prnt, mensaje, priv=False):
    #print mensaje
    if priv and user!='adolfo':return

    dlg = DlgError.Dialog2(prnt)
    
    
    dlg.MSG.AppendText(mensaje)
    dlg.ShowModal()
def setDateField(ctrl):
    myDate = ctrl.GetValue()
    return datetime.date(myDate.GetYear(), myDate.GetMonth() + 1, myDate.GetDay())

def setDateField2(ctrl,err="de fecha"):
    try:
       return datetime.date(toIntegerDateField(ctrl[2].GetValue(), default=1990), toIntegerDateField(ctrl[1].GetValue()), toIntegerDateField(ctrl[0].GetValue()))
    except:
       
       MError(None, "Error guardando campo "+err)

def validDate(ctrl, err='', Posterior = True):
    NoErr = 0
    try:
        valor = ctrl[2].GetValue()
        anio = valor if valor else 1900
        d = datetime.datetime(toIntegerDateField(ctrl[2].GetValue(), default=1990), toIntegerDateField(ctrl[1].GetValue()), toIntegerDateField(ctrl[0].GetValue()))
        
        
        if anio < 1880:
             tipodeerror = u"El a\xf1o no debe ser anterior a 1880"
             MError(None, u"La fecha %s no es v\xe1lida: %s"%(err, tipodeerror))
             return False
        if Posterior:
            if d > status.today:
                tipodeerror = u"No debe ser posterior al d\xeda de hoy"
                MError(None, u"La fecha %s no es v\xe1lida: %s"%(err, tipodeerror))
                return False
        return True
    except:
        
        tipodeerror = u"est\xe1 mal formada. Debe ser d\xeda/mes/a\xf1o"
            
        MError(None, u"La fecha de %s no es v\xe1lida: %s "%(err, tipodeerror))
        return False



def setDateString(ctrl):
    "retorna un string de fecha a partir de un control de fecha"
    myDate = ctrl.GetValue()
    return '%i/%i/%i'%(myDate.GetYear(), myDate.GetMonth() + 1, myDate.GetDay())

def DateTimeString(myDate):
    "retorna un string de fecha a partir de un objeto datetime"
    
    return '%i/%i/%i'%(myDate.GetYear(), myDate.GetMonth() + 1, myDate.GetDay())


def setDateCtrl(ctrl, myDate):
    a=wx.DateTime()
    
    #a.SetToCurrent()
    a=DefaultDate
    
    if myDate:
        
        
        #a.SetYear(myDate.year)
        #a.SetDay(myDate.day)        
        #a.SetMonth(myDate.month - 1)
        a=wx.DateTimeFromDMY(myDate.day, myDate.month - 1, myDate.year)

    ctrl.SetValue(a)
    
def toIntegerDateField(value, default=1):
    try:
        i=int(value)
    except:
        i=default
    if i==0:
        i=default
    return i
    
def claveContenedor(i):
    'determina a que contenedir pertenece la entidad'
    if not cnf.baseCentral:
        return 0 # no aplica
    i = str(i)
    if len(i) <4 :
        return 0 # ta raro....
    contenedor = i[:-3][:1]
    return contenedor

def setDateCtrl2(ctrl, myDate, tipoFecha):
    
    if myDate:
        
        

        #a=wx.DateTimeFromDMY(myDate.day, myDate.month - 1, myDate.year)
        ctrl[0].SetValue(int(myDate.day))
        ctrl[1].SetValue(int(myDate.month))
        ctrl[2].SetValue(int(myDate.year))
    else:
        ctrl[0].SetValue(1)
        ctrl[1].SetValue(1)
        ctrl[2].SetValue(1900)
        
    ActivaCtrlFecha2(tipoFecha, ctrl)
    
            
            
def HideCtrlFecha(ctrl):
    for i in range(3):
        ctrl[i].Show(False)
            
def ActivaCtrlFecha2(tipoFecha, ctrl):
    HideCtrlFecha(ctrl)

    
    
    if tipoFecha:
        if hasattr(tipoFecha, 'name'):
            codigo = tipoFecha.name
            
            ctrl[2].Show(codigo in [status.UnknownMonthDate, status.UnknownDayDate, status.AproxDate, status.SharpDate])
            ctrl[1].Show(codigo in [status.UnknownDayDate, status.AproxDate, status.SharpDate])
            ctrl[0].Show(codigo in [status.AproxDate, status.SharpDate])
            
    if not tipoFecha:
                ctrl[0].SetValue(1)
                ctrl[1].SetValue(1)
                ctrl[2].SetValue(1900)
        
    
        

def MviMask(value):
    if value:
        return str(value)
        
    else: 
        return ''

def getChoiceValueId(ctrl):
    if ctrl.Selection == -1:
        return None
    
    this = ctrl.GetClientData(ctrl.Selection)
    
    return this.id

def getChoiceValue(ctrl):
    if ctrl.Selection == -1:
        return None
    this = ctrl.GetClientData(ctrl.Selection)
    
    return this

def getCheckBoxValue(ctrl):
    if ctrl.GetValue() == True:
        return 1
    else:
        return 0
    
def setCheckBoxValue(value):
    if value == 1:
        return True
    else:
        return False
def tesDesc(obj):
    "return a descripcion from tesaurus, if obj is not None"
    
    if obj:
        if hasattr(obj, 'descripcion'):
             return obj.descripcion
        else:
            print obj, "llamada erronea"
            return "llamada erronea"
    else:
        return ''

def UpdateLogInfo(L, id=None):
    if L:
      
      L.fechaActualizacion = datetime.datetime.now()
      L.userActualizacion  = status.userID
      #if id: L.userActualizacion  = id
      L.Actualizador = status.usuarioActual
      try:
          session.add(L)
      except:
          MError(self, u"No hay conexi\xf3n con el servidor")
          

def nonEmpty(s):
    if s: return s
    else: return ''
    
def Borrar(self, mensaje):
    
    
        dlg = wx.MessageDialog(self, mensaje,
                               'Alerta',
                               #wx.OK | wx.ICON_INFORMATION
                               wx.YES_NO | wx.CANCEL
                               )
        ret= dlg.ShowModal()
        dlg.Destroy()
        
        return ret == wx.ID_YES

def ParentsPattern(node, raiz):
    if not node:
        return ''
    if node.name==raiz:
        return ''
    
    parentname = ParentsPattern(node.parent, raiz)
    if parentname:
        return '^'+node.name +'$|'+ parentname
    else:
        return '^'+node.name+'$'

            
def FlushInfo(id=None):

    for i in session.dirty:
        itemModified = None
        try:
            itemModified = session.is_modified(i)
        except:
            AlertaRed()
        if itemModified:  

            #print "type in ",type(i),  type(i) in [Persona, Persona_Vinculo, PersonaTipificacion]
            if CanEdit(status.casoActual) or \
               (CanEditPersona(status.personaActual) and (type(i) in [Persona, Persona_Vinculo, PersonaTipificacion, User])):
                print "saving ", i ,"[id ",id,"]"
                if hasattr(i, 'PLoginfo'):
                    if i.PLoginfo:
                        UpdateLogInfo(i.PLoginfo, id=id)
                    else:
                        i.PLoginfo = NewLoginfo(flush=False)
            
                
                
            else:
                if not status.cnfBaseCentral and not status.AlertaGrabarDatos:
                    MError(None,u'El usuario de s\xf3lo lectura no puede guardar datos')
                    print 'session.dirty', session.dirty
                    status.AlertaGrabarDatos=True
                session.expire_all()
                
                #session.expunge_all()
                
                break
                
            
    try:
        if status.debug:
            session.bind.echo = True
        session.flush()    
        if status.debug:
            session.bind.echo = False
    except:
        print "Unexpected error:", sys.exc_info()
        MError(None, u"El \xfaltimo dato no pudo ser grabado. Es recomendable volver a cargar el programa ("+str(sys.exc_info())+")")
   
def sameType(one, two):
    return type(one) == type(two)

def Mvs(value):
    if value:
        return value
    else:
        return ''
def unicos(l):
     r = []
     if l:
         for i in l:

             if i and i not in r:
                r.append(i)
         
         r.sort(cmp=lambda x,y:x.id - y.id)
     return r  

def allChildren(node):
    lista = []
    for i in node.children.values():
        lista.append(i)
        for j in allChildren(i):
            lista.append(j)
    return lista

def cuentaEspacios(ctrlLeyenda, event):
        ctrl = event.GetEventObject()
        
        
        
        l = len(ctrl.GetValue())
        ctrlLeyenda.SetLabel("%i espacios"%(l))

def DictReciproco(name):
    t=QueryTesNode.filter(TesNode.name == name)
    dict = {}
    if t.count():
        t1 = t[0]
        
        for i in allChildren(t1):
            dict[i.name] = i.descripcion
    return dict

def ExistePersona(nombre, apellido, indiv):
    q=session.query(Persona)
    if indiv == 1:
        #r = q.filter(sql.and_(Persona.nombre == nombre.strip(), Persona.apellido == apellido.strip()))
        r = q.filter(sql.and_(Persona.nombre.ilike(nombre.strip()), 
                              Persona.apellido.ilike(apellido.strip())
                              )
                    )
    else:
        r = q.filter(Persona.apellido.ilike(apellido.strip()))
    
    r2 = r.all()
    

    return r2
def LimpiaString(st):
    st=st.strip()
    st=st.replace('   ',' ')
    st=st.replace('   ',' ')
    st=st.replace('  ',' ')
    st=st.replace('  ',' ')
    st=st.replace('  ',' ')
    return st
    

def ExistePersonaID(id):
    p=session.query(Persona).filter(Persona.id == id).first()
    return p
    
    
def ExisteCaso(descrip, casoActual=None):
    
    q = session.query(Caso)
    d = descrip.strip()
    r = q.filter(Caso.descripcion.ilike(d))
    if casoActual:
        r= r.filter(Caso.id != casoActual.id)
    r1=[]
    try:
        r1 = r.all()
    except:
        AlertaRed()
    return r1

def AlertaRed():
    MError(None, 
    u"""Aparentemente hay problemas de conexi\xf3n con el servidor de base de datos.\
     Es recomendable cerrar el programa y volver a entrar""" +str(sys.exc_info()[1])
     )
    
def adaptaId(id, status):
    
       Sid=str(id)
       s=Sid[:-4]+str(status)+Sid[-3:] 
       return int(s)

def getPersona(id):
    p=session.query(Persona).filter(Persona.id == id).first()
    if p:
         return p
    else:
         return None
    
def casoDescriptor(id):
    c=session.query(Caso).filter(Caso.id == id).first()
    if c: 
        return c.Descriptor()
    else:
        return ''
    
def personaDescriptor(id):
    c=session.query(Persona).filter(Persona.id == id).first()
    if c: 
        return c.Descriptor()
    else:
        return ''

def MyClientDataSelection(event):
    ' retorna una lista de objetos seleccionados de una listbox con seleccion multiple'
    
        
    ctrl = event.GetEventObject()
    
    S = ctrl.GetSelections()
    lista = []
    # S contiene los indice de los elementos seleccionados 
    for i in S: 
        obj = ctrl.GetClientData(i)
        lista.append(obj)
    return lista

def updateStatusC3(self, obj):
    pers = type(obj) == Persona
    ctrl = self.txtStatusC3P if pers  else self.txtStatusC3
    ctrl2 = self.btnCopiarC3P if pers else self.btnCopiarC3
    ctrl3 = self.chkRelevanteP if pers else self.chkRelevante
    ctrl.SetLabel(statusC3(obj.clavestatusc3))
    HabilitarCopiarC3 = obj.clavestatusc3 != 1
    ctrl2.Enable(status.filtroContenedor == 2 and HabilitarCopiarC3)
    
    ctrl3.Enable(obj.clavestatusc3 < 2)
    ctrl3.SetValue((obj.clavestatusc3 == 1))

def statusC3(valor):
    
    if valor:
        if valor == 1:
            return "No relevante"
        if valor == 2:
            return "Presente en C3"
        if valor == 3:
            return "Relacionado con C3"
    return "Pendiente"
    
def MyClientData(event):
    
    if type(event) in [wx._core.CommandEvent, wx._core.KeyEvent]:
        
        c = event.GetEventObject()
    else:
        c = event # es una ventana
    i = c.Selection
    if i > -1:
         try:
             obj = c.GetClientData(c.GetSelection())
             if obj:
                 session.refresh(obj)
         except:
             MError(None, u"No fue posible cargar informaci\xf3n"+str(sys.exc_info()[1]))
    else:
         obj = None
    return obj
def strDate(dateField, Ptipofecha=None):
    if dateField:
        if not Ptipofecha:
            return '%02i/%02i/%04i'%(dateField.day,dateField.month,dateField.year)
        if Ptipofecha.name == '001':
            return '%02i/%02i/%04i'%(dateField.day,dateField.month,dateField.year)
        if Ptipofecha.name == '002':
            return '%02i/%02i/%04i (%s)'%(dateField.day,dateField.month,dateField.year, Ptipofecha.descripcion)
        if Ptipofecha.name == '003':
            return '%02i/%04i (%s)'%(dateField.month,dateField.year, Ptipofecha.descripcion)
        if Ptipofecha.name == '004':
            return '%04i (%s)'%(dateField.year, Ptipofecha.descripcion)
        
            
        
    else:
        return None
    
def strDate2(dateField, Ptipofecha=None):
    if dateField:
        strMonth = meses[dateField.month]
        if not Ptipofecha:
            return '%02i/%s/%04i'%(dateField.day,strMonth,dateField.year)
        if Ptipofecha.name == '001':
            return '%02i/%s/%04i'%(dateField.day,strMonth,dateField.year)
        if Ptipofecha.name == '002':
            return '%02i/%s/%04i (Fecha aproximada)'%(dateField.day,strMonth,dateField.year)
        if Ptipofecha.name == '003':
            return '%s/%04i'%(strMonth,dateField.year)
        if Ptipofecha.name == '004':
            return '%04i'%(dateField.year)
        
            
        
    else:
        return None
    
def terminoReciproco(dict, name, default):
    
    if name in dict:
        return dict[name]
    else:
        
        return default
def MatNotNull(matriz, i, j):
    "regresa un valor de una matriz bidimensional, en caso de que el valor exista"
    if i in matriz.keys():
        
        if j in matriz[i].keys():
            print "valor:",i, j, matriz[i][j]
            return matriz[i][j]
    return 0

def DesNotNull(obj):
    if obj:
        if hasattr(obj, 'descripcion'):
            return obj.descripcion
        elif hasattr(obj, 'Descriptor'):
            return obj.Descriptor()
        else:
            return 'obj:'+str(obj.id)
    else:
        return "(informacion no disponible)"
    
def nameDescriptor(obj):
    if obj:
        if hasattr(obj, 'name'):
            return obj.name
        else:
            return "(inf. no disponible)"
        
def Descriptor(clase,i):
    if i:
         r = session.query(clase).filter_by(id = i).first()
         r = DesNotNull(r)
    else:
        r = ' NULO'
    return r

def nameTesauro(clase, i):
    if i:
         r = session.query(clase).filter_by(id = i).first()
         r = nameDescriptor(r)
    else:
         r = ' NULO'
    return r

def tesauroProfundidad(id, raiz):

    prof = 0
    nodo = TesById(id)
    padre = None
    if nodo:
        padre=nodo.parent
    while padre and padre.parent and padre != raiz:
        prof += 1                
        padre = padre.parent
    return prof
def nameLongTesauro(clase, i):
    if i:
         r = session.query(clase).filter_by(id = i).first()
         r = r.DescriptorCompleto()
    else:
         r = ' NULO'
    return r
    
    
        
    
    
def CanSee(Caso):
    if status.UserLevel <=10:
        return True
    if status.UserLevel <=20:
        
        if Caso.PLoginfo.userCreacion == status.userID:
            return True
        else:
            if Caso.confidencialidad == 1:
                return False
    if Caso.confidencialidad == 1:
        return False
    return True
def getDefault(tesauro):
   if tesauro in VDefault.keys():
       t=QueryTesNode.filter(TesNode.id == VDefault[tesauro])
       if t.count():
           return t[0]
    
   return None
def ErrorSoloLectura(self):
    MError(self, "No es posible hacer modificaciones sobre esta entidad")

def CanEdit(obj):
    if obj:
        if obj.clavestatus in [1,2]:
            return False
    if status.cnfBaseCentral and status.filtroContenedor != 3:
        return False
    
    if status.superuser:
        return True
    if status.creacionReciente:
        status.creacionReciente = False
        return True
    if status.UserLevel <=5:
        return True
    if status.UserLevel <=10:
        if obj in status.objdehoy:
            return True
    if obj:
        if status.userID == obj.PLoginfo.userCreacion:
            return True
    return False
def CanEditPersona(obj):
    if obj:
        if obj.clavestatus in [1,2]:
            return False
    
    if status.cnfBaseCentral and status.filtroContenedor != 3:
        return False
    if status.UserLevel <=10:
        return True
    return False
def CanCreate():
    if cnf.baseCentral: 
        return False
    if status.UserLevel <=10 :
        return True
    if CanEdit(status.casoActual):
        return True
    return False

def CanCreateCaso():
    if cnf.baseCentral: 
        return False
    if status.UserLevel <=10:
        return True
    return False
    

def CanReport():
    if status.UserLevel <=20:
        return True
    return False

def PutDesc(ctrl, field):
    descrip = ''
    
    if field: descrip = field.__getattribute__("descripcion")
    ctrl.SetLabel(descrip)

def NoRegistros(obj):
    n=session.query(obj).count()
    return n

def myHash(a):
    return hashlib.sha224(a).hexdigest()[:6]
    
def GetDatosOrg(self):
    try:
        registro=session.query(ConfigTdt).filter(ConfigTdt.tipo == u'OrgData').all()
    except:
        error = sys.exc_info()
        error = str(error[1])
        diagnostico1 = "permission denied for relation"
        errorMsg = u"No fue posible hacer la conexi\xf3n con la base de datos. Verifique su contrase\xf1a y configuraci\xf3n"
        if error.find(diagnostico1) > -1:
            errorMsg = u"No es posible el acceso a la base de datos con esta cuenta de usuario. Es necesario reasignar la contrase\xf1a o revisar su nivel de acceso"
        print "error:", error    
        MError(self, errorMsg)
        return False
        
    
    opciones = {}
    if registro:
        try:
            registro = registro[0]
            opciones = pickle.loads(str(registro.contenido))
        except:
            print "no se cargaron datos de org"
        
    t = 'txtNombre' 
    if  t in opciones.keys():
        status.OrgNombre = opciones[t].decode( "utf-8" )

    t = 'txtMembrete'
    if  t in opciones.keys():
        status.OrgMembrete = opciones[t].decode( "utf-8" )






    t = 'txtClave' 
    if  t in opciones.keys():
        try:
            status.OrgClave  = int(opciones[t])
        except:
            status.OrgClave = 0
    t = 'txtHash' 
    status.OrgHash = ''
    if  t in opciones.keys():
        try:
            status.OrgHash  = opciones[t]
        except:
            status.OrgHash = ''
    
    
    t="Estado"
    if  t in opciones.keys():
        try:
            id = opciones[t]
            status.EdoDef  = TesById(id)
        except:
            status.EdoDef = None
    
    t="Municipio"
    if  t in opciones.keys():
        try:
            id = opciones[t]
            status.MpoDef = TesById(id)
        except:
            status.MpoDef = None 
    return True
    
def borrarTodo():
    for c in session.query(Caso):
        c.borrar()
    for p in session.query(Persona):
        p.borrar()
def borrarC3():
    for c in session.query(Caso).filter(Caso.clavestatus == 3):
        c.borrar()
    for p in session.query(Persona).filter(Persona.clavestatus == 3):
        p.borrar()
    for p in session.query(Persona).filter(Persona.personarelacionadac3 != None):
        p.personarelacionadac3 = None
        session.add(p)
    session.flush()

def nada():
    return

def borrarEnContenedores():
    session.bind.echo = True
    for c in session.query(Caso).filter(Caso.clavestatus > 0):
        c.borrar()
        print "-----------------------"
    for p in session.query(Persona).filter(Persona.clavestatus > 0):
        p.borrar()

    session.flush()  

def choiceFix(self, modulo):
    from moduleCtrls import CtrlChoice
    if modulo in CtrlChoice.keys():
        controles = CtrlChoice[modulo]
        for ctrlName in controles:            
            ctrl = getattr(self, ctrlName)
            ctrl.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Sans'))  


def setCamposSololectura(self, editable):
    for k in camposEntidad.keys():
        CamposSololectura(self,camposEntidad[k], editable)
         
def CamposSololectura(self, listadecampos, editable):
    for campo in listadecampos:
        c=self.__getattribute__(campo)
        tipo_de_c = str(type(c))
        

        if type(c)==wx.ListBox:
            
            NOP()
        elif type(c)==wx.Button:
            c.Enable(editable)
            
                    
        elif type(c) == wx.CheckBox:
            NOP()
            
        elif type(c)==wx.StaticText:
            NOP()
        elif type(c)==wx.Choice:
            NOP()

        elif hasattr(c, 'Value'):
            
            c.SetEditable(editable)
            
            
        else: print "!!!!!"
def NOP():
    return

def seImprime(entidad, campo, tipoRep):
    print "checando ",campo," en ",entidad, tipoRep
    status.prt_entidad = entidad
    status.prt_tipoRep = tipoRep
    if entidad in status.printOpt.keys():
        if tipoRep in status.printOpt[entidad].keys():
             if campo in status.printOpt[entidad][tipoRep].keys():
                 
                print "regresando ",status.printOpt[entidad][tipoRep][campo], " para ",entidad, tipoRep, campo
                return status.printOpt[entidad][tipoRep][campo]
    return True
        



status = StatusClass()
status.prt_entidad = None
status.prt_tipoRep = None
status.grupoActual = None
status.casoActual = None
status.actoActual = None
status.personaActual = None
status.intervencionActual = None
status.tipificacionActual = None
status.nuevoacto = False
status.TesNode = None
status.fuenteActual = None
status.tipoActual = None
status.tiposActuales = None
status.involActual = None
status.pubActual = None
status.vinculoActual = None
status.org = 100

status.usuarioActual = None
status.userID = 211
status.UserLevel=10

status.UnknownDate = '000'
status.SharpDate = '001'
status.AproxDate = '002'
status.UnknownDayDate = '003'
status.UnknownMonthDate = '004'
status.personaIndividual=True
status.PantAnterior = None
status.filtroCaso = None
status.filtroPersona = None
status.casoRelActual = None
status.instrActual = None
status.legisActual = None
status.reciprocoRelacionCasos = {}
status.reciprocoRelacionPersonas = {}
status.debug = 0
status.objdehoy=set([])
status.persdehoy=set([])
status.personaReciente = None
status.TotalCasos = 0
status.casoIdseleccionados=None
status.printOpt = {}
status.printConfigActual = None
status.casosSeleccionados = None
status.session = None
status.engine = None
status.today = datetime.datetime.now()
status.strDiadehoy = '%02i/%02i/%04i'%(status.today.day,status.today.month,status.today.year)
status.OrgNombre=''
status.OrgClave=''
status.OrgMembrete=''
status.ReloadPersona = False
status.casoRelaciones=set([])
status.padres = None
status.localCountry = localCountry
#status.busquedaActualDependenciasCaso = []
status.creacionReciente = False
status.dlg = {False:{},True:{}}
status.dlgExcepciones=[u'T04']
status.SE = False
status.panelPersonasEnabled = False
status.superuser = False #??????????
status.importacion = False
status.filtroGrupo = None
status.filtroContenedor = None
status.MpoDef = None
status.EdoDef = None
status.baseCentral=False
status.cnfBaseCentral=False
status.tipoPersona='Todas'
status.nombreCasoActual=''
status.idPersonas = set([])
status.path = 'smdh2'
status.drive = 'c:\\'
status.sinTablas=False
status.AlertaGrabarDatos=False
status.totalPersonas = 0
status.canEditCaso = False
status.canEditPersona = False
status.diagnostico=None
status.applySearch=False
status.applySearchPersona=False
status.num_renglon = 0
status.log = open('out.log','a')
status.Reporte_con_todos_los_campos='Reporte con todos los campos'




if cnf.db in ["redtdtcentral","limpia","'redtdtcentral'","'limpia'"]:
    status.cnfBaseCentral=True



status.slash = '\\'
if NameOS in ['posix']:
    status.slash = '/'
    status.drive = '/usr/lib'
   


    




EventoTipificacionDerechosAfectados = aliased(EventoTipificacion)
EventoTipificacionTemas = aliased(EventoTipificacion)
EventoTipificacionLegisNac = aliased(EventoTipificacion)
EventoTipificacionInstInt = aliased(EventoTipificacion)
EventoTipificacionNormatividadActo = aliased(EventoTipificacion)

PersonaVictima = aliased(Persona)
PersonaPerpetrador = aliased(Persona)

PerVictima = aliased(Persona)
PerPerpetrador = aliased(Persona)
PerSolicitante = aliased(Persona)
TesConfiabilidad = aliased(TesNode)
TesLengua_indigena = aliased(TesNode)
TesConexion_info = aliased(TesNode)
TesCaracRelevante = aliased(TesNode)
PerPersona_como_fuente = aliased(Persona)
PerFuenPersona = aliased(Persona)
TesIntervTipo = aliased(TesNode)
TesIntervEstatus = aliased(TesNode)
PerInterviniente = aliased(Persona)
PerContraparte = aliased(Persona)
PerSolicitante = aliased(Persona)
TesTipoPerpetrador = aliased(TesNode)
TesPubConfiabilidad = aliased(TesNode)
TesFuenConfiabilidad = aliased(TesNode)
TesPubLengua_indigena = aliased(TesNode)
TesFuenLengua_indigena = aliased(TesNode)
TesPubIdioma = aliased(TesNode)
TesFuenIdioma = aliased(TesNode)
TesTipopublicacion = aliased(TesNode)
PerPersonareferenciada = aliased(Persona)

TesPerIdioma = aliased(TesNode)
TesPerLengua = aliased(TesNode)
TesPerTipoGrupo = aliased(TesNode)
TesPerSexo = aliased(TesNode)
TesPerPais = aliased(TesNode)
TesPerEstado = aliased(TesNode)
TesPerMpo = aliased(TesNode)
TesPerCiudadania = aliased(TesNode)
TesPerReligion = aliased(TesNode)
TesPerEscolaridad = aliased(TesNode)
TesPerEstadoCivil = aliased(TesNode)
TesPerMonitoreo = aliased(TesNode)
TesPerOcupacion = aliased(TesNode)
TesPerOrigenEtnico = aliased(TesNode)
TesPerConfiabilidad = aliased(TesNode)

PersonaTipificacionIdioma= aliased(PersonaTipificacion)
PersonaTipificacionLengua= aliased(PersonaTipificacion)
PersonaTipificacionTipoGrupo= aliased(PersonaTipificacion)
PersonaTipificacionDireccion= aliased(PersonaTipificacion)

DetalleBiografico = aliased(Persona_Vinculo)





#TipificacionTema = aliased(EventoTipificacion)
#TipificacionDerecho = aliased(EventoTipificacion)
TesTipodeacto = aliased(TesNode)
TesTipodelugar = aliased(TesNode)
TesTipoVinculo = aliased(TesNode)
TesDerechoAfectado = aliased(TesNode)
TesTema = aliased(TesNode)
TesPais = aliased(TesNode)
TesEstado = aliased(TesNode)
TesMunicipio = aliased(TesNode)
PerPubPersonareferenciada = aliased(Persona)
PerContraparte = aliased(Persona)
TesPerpSexo = aliased(TesNode)
TesVicSexo = aliased(TesNode)
TesPerpOcupacion = aliased(TesNode)
TesVicOcupacion = aliased(TesNode)
TesPerpEtnico = aliased(TesNode)
TesVicEtnico = aliased(TesNode)
TesRelacionCasos = aliased(TesNode)
PersonaTipificacionPerpEtnico = aliased(PersonaTipificacion)
PersonaTipificacionVicEtnico = aliased(PersonaTipificacion)
LoginfoCaso = aliased(Loginfo)
LoginfoActo = aliased(Loginfo)
LoginfoFuente = aliased(Loginfo)
LoginfoPub= aliased(Loginfo)
LoginfoIntervencion = aliased(Loginfo)
LoginfoPersona = aliased(Loginfo)
LoginfoInvol = aliased(Loginfo)
LoginfoDatoBio = aliased(Loginfo)
LoginfoCasoVinculo = aliased(Loginfo)
LoginfoActoCaracRel = aliased(Loginfo)
LoginfoEvTip = aliased(Loginfo)


Caso_vinculoAlias = aliased(Caso_vinculo)

ClassAliases={}

ClassAliases['EventoTipificacion']=['EventoTipificacionDerechosAfectados','EventoTipificacionTemas']
ClassAliases['Persona']=['PerContraparte', 'PerPubPersonareferenciada', 'PerPersonareferenciada', 
                         'PerSolicitante', 'PerContraparte', 'PerInterviniente', 'PerFuenPersona',
                         'PerPersona_como_fuente', 'PerSolicitante', 'PerPerpetrador', 'PerVictima',
                         'PersonaPerpetrador', 'PersonaVictima']
ClassAliases['TesNode']=['TesConfiabilidad',
'TesLengua_indigena',
'TesConfiabilidad',
'TesLengua_indigena',
'TesConexion_info',
'TesIntervTipo',
'TesIntervEstatus',
'TesPubConfiabilidad',
'TesFuenConfiabilidad',
'TesPubLengua_indigena',
'TesFuenLengua_indigena',
'TesPubIdioma',
'TesFuenIdioma',
'TesTipopublicacion',
'TesTipodeacto',
'TesTipodelugar',
'TesDerechoAfectado',
'TesTema',
'TesPais',
'TesEstado',
'TesMunicipio',
'TesPerpSexo',
'TesVicSexo',
'TesPerpOcupacion',
'TesVicOcupacion',
'TesPerpEtnico',
'TesVicEtnico'
]
Req={}
Req['Involucramiento']=Acto

Roles = {'perpetrador':2, 'fuente':3}
#metadata.bind.echo = False
#session.bind.echo = False
#ojo
#t = session.query(TesNode)
#n = t.filter(TesNode.c.id==1)[0]

objetoDescrip = {}
objetoDescrip[Persona]='Persona'
objetoDescrip[Caso]='Caso'
objetoDescrip[Acto]='Acto'
objetoDescrip[Involucramiento]='Perpetrador'
objetoDescrip[Fuente]='Fuente personal'
objetoDescrip[Caso_vinculo]=u'Relaci\xf3n con otro caso'
objetoDescrip[Localidad]=u'Localizaci\xf3n de un caso'
objetoDescrip[Intervencion]=u'Intervenci\xf3n'
objetoDescrip[Derechoviolado]=u'Derecho violado'
objetoDescrip[PersonaTipificacion]=u'Tipificacion de una persona'
objetoDescrip[Publicacion]=u'Fuente documental'


engine = create_engine(spec)
status.engine = engine
if not status.sinTablas:
    try:
        
        metadata.create_all()
        
        
    except:
        error = sys.exc_info()
        error = str(error[1])
        
        print error    
        errorMsg = u"No fue posible hacer la conexi\xf3n con la base de datos. Verifique su contrase\xf1a y configuraci\xf3n"
        if error.find('5432') > -1:
            errorMsg = u"No fue posible hacer la conexi\xf3n con la base de datos. Verifique su configuraci\xf3n, aseg\xfarese que la base de datos este activa en el servidor y que su equipo este correctamente conectado a la red local"
        if error.find('password') > -1:
            errorMsg = u"No fue posible hacer la conexi\xf3n con la base de datos. Verifique que el nombre de usuario y contrase\xf1a esten correctamente ingresados"
        if error.find('translate host') > -1:
            errorMsg = u"No fue posible hacer la conexi\xf3n con la base de datos. Verifique que los datos de ubicaci\xf3n del servidor esten correctamente ingresados en la funci\xf3n de configuraci\xf3n local"    
        if error.find('pg_hba') > -1:
            errorMsg = u"No fue posible hacer la conexi\xf3n con la base de datos. Probablemente hay un problema de configuracion en el servidor de base de datos" 
        if error.find('does not exist') > -1 or error.find('no existe') > -1:

            errorMsg = u"El motor de base de datos es funcional. Sin embargo, las tablas de la base de datos aun no han sido creadas. Localice las instrucciones de creaci\xf3n de la base de datos en el manual de instalaci\xf3n"
            status.sinTablas= True   
            
            
        MError(None, errorMsg)
    
        if not status.sinTablas:
            sys.exit()

            
    #if status.sinTablas:
    #    print "mostrando herr..."  
    #    sys.exit()
          


        

        
session = create_session(bind=engine)

status.session = session
print 1
#try:
#    q=session.query(configTdt).first()
#except:
#    error = sys.exc_info()
#    error = str(error[1])
#    diagnostico1 = 'parche'
#    if error.find(diagnostico1) > -1:
#        print "hace falta el parche", diagnostico1
#        status.diagnostico = "hace falta el parche "+diagnostico1
3        #sys.exit()
#print 2

#session.bind.echo=True

QueryTesNode = session.query(TesNode)
if not status.sinTablas and not status.diagnostico:
    res=GetDatosOrg(None)
    if not res: sys.exit()
    
    
    q=session.query(TesNode.parent_id).distinct()
    
    status.padres = [padre_id[0] for padre_id in q.all()]
    
    registro=session.query(ConfigTdt).filter(ConfigTdt.tipo == u'OrgData').all()
    claveOrg = 0
    if registro:
        registro = registro[0]
        try:
            opciones = pickle.loads(str(registro.contenido))
        except:
            opciones = None
        if opciones:
            claveOrg = opciones['txtClave']
            try:
                claveOrg = int(claveOrg)
            except:
                claveOrg = 99999
        else:
            claveOrg = 99999
    if claveOrg == 1:
        status.SE=True

    Tiposfecha=session.query(TesNode).filter(TesNode.name == u'T48')[0].children

    status.idExacta = Tiposfecha['001'].id
    status.idAprox  = Tiposfecha['002'].id
    status.idSinDia = Tiposfecha['003'].id
    status.idSinMes = Tiposfecha['004'].id





