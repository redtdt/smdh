# -*- coding: latin-1 -*-
#Boa:Frame:FrameBusqueda
#-----------------------------------------------------------------------------
# Name:        FrameBusqueda
#
#
# RCS-ID:      $Id: App1.py $
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
#!/usr/bin/env python






import wx
import wx.lib.flatnotebook
from module2 import *
import module2
from DLGTaxTree import getTaxonomyTree
from dlggetdescrip import MyDescrip
from DlgCond import DlgCond, DlgChk
from midataset import GeneraQueryCaso, GeneraQueryPersona
from dlgpersona import PersonaDlg
from DlgUser import UserCond
from DlgTipoCond import Condicion
import cnf

session = status.session

def create(parent):
    return FrameBusqueda(parent, [])

[wxID_FRAMEBUSQUEDA, wxID_FRAMEBUSQUEDAADDCOND, wxID_FRAMEBUSQUEDABTNREGRESAR, 
 wxID_FRAMEBUSQUEDACONTEXTHELPBUTTON1, wxID_FRAMEBUSQUEDACTRLCAMPO, 
 wxID_FRAMEBUSQUEDADELALL, wxID_FRAMEBUSQUEDADELCOND, wxID_FRAMEBUSQUEDAFN, 
 wxID_FRAMEBUSQUEDALISTCONDS, wxID_FRAMEBUSQUEDAPANEL1, 
 wxID_FRAMEBUSQUEDASTATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(11)]

class LocalVal(object):
    pass

L=LocalVal()

#condiciones = []
L.OperadorO = None
L.OperadorY = None
class QueryObject(object):
    def __init__(self, prnt):
        self.MisCondiciones=[]
        self.prnt = prnt
        #self.initCampos()
        self.nuevo = True
        self.borrar = False
    def edit(self):
        editor = FrameBusqueda(self.prnt, self)
        editor.MakeModal()
        editor.Show()
    def FiltroActivo(self, clase="Caso"):
        
        if clase=="Caso":
            if self.MisCondiciones and module2.status.applySearch:
                return True
        if clase=="Persona":
            if self.MisCondiciones and module2.status.applySearchPersona:
                return True
        return False
        
    def execute(self):
        
        
        
        
        q = self.GeneraQuery([i.dependencia for i in self.MisCondiciones], id=False)
        # "id=False" debido a que necesitamos la lista de casos como objetos, no una coleccion de ids
        
        #print 'condiciones:',[i for i in self.MisCondiciones]
        print 'execute q:',q
        
        
        #print 'dependencias:',[i.dependencia for i in self.MisCondiciones]
        self.busquedaActualDependencias = [i.dependencia for i in self.MisCondiciones]
        condicionesAnd = ListSplit(self, self.MisCondiciones, L.OperadorO)
        
        
        
        lista3 = []
        for segment2 in ListSplit(self, self.MisCondiciones, L.OperadorY):
           lista2 = []
           for segment in ListSplit(self, segment2 , L.OperadorO):
                lista1 = []
                for i in segment:
                     lista1.append(i.ToFilter())
                Cand2 = sql.and_(*lista1)    
                lista2.append(Cand2)
           Cor1 = sql.or_(*lista2)
           lista3.append(Cor1)
        Cand1 = sql.and_(*lista3)
        
        print "filtro:", Cand1
        filtrado = q.filter(Cand1)



        
        
        
        Q=filtrado
        print "query:",Q
        return Q
    def Filtro(self):
        condicionesAnd = ListSplit(self, self.MisCondiciones, L.OperadorO)
        filtrado = sql.or_(*[sql.and_(*[i.ToFilter() for i in  segment]) for segment in condicionesAnd] )
        return filtrado
    def Dependencias(self):
        return [i.dependencia for i in self.MisCondiciones]
        
    def __repr__(self):
        if self.MisCondiciones:
            return self.MisCondiciones
        else:
            return '--'

class QueryCaso(QueryObject):
    def __init__(self, prnt):
        QueryObject.__init__(self, prnt)
        self.initCampos()
        self.GeneraQuery = GeneraQueryCaso
        self.busquedaActualDependencias=[]
        
    
        
    def initCampos(self):
            """ esta es una lista de posibles condiciones para hacer query sobre un caso
            cada definicion contiene:
                la entidad (ej Caso)
                el campo (ej Caso.observaciones
                la descripcion de la condicion
                el tipo de condicion, a saber:
                    T texto libre
                    I entero
                    B booleano
                    C Taxonomia ej. ('C', u'T22') (T22 = taxonomia # 22)
                    Z entidades relacionadas existente
                    F fecha
                    P persona
                    U usuario
                Dependencias asociadas, segun midataset.GeneraQueryCaso
            """
            
            
            
            self.campos = \
    [
    (None, None, " O bien...",('O')),
    (None, None, u" Y tambi\xe9n...",('Y')),
    
    (Caso, Caso.descripcion, u"Nombre del caso", ('T'),''),  #Caso.descripci\xf3n like S
    (Caso, Caso.id, u"No. de registro del caso", ('I'),''),
    (Caso, Caso.resumen_descripcion, u"Resumen de la descripci\xf3n del caso", ('T'),''),
    (Caso, Caso.observaciones, u"Observaciones sobre el caso", ('T'),''),    
    (Caso, Caso.no_persona_afectadas, u"No. de personas afectadas en el caso", ('T'),''), 
    (Caso, Caso.comentarios, u"Comentarios sobre el caso", ('T'),''), 
    (Caso, Caso.archivos, u"Archivos del caso", ('T'),''), 
    
    (Caso, Caso.proyecto_grupo, u"Proyecto local", ('T'),''), 
    (Caso, Caso.proyecto_conjunto, u"Proyecto conjunto RedTDT", ('T'),''), 
    
    #(Caso, Caso.confidencialidad, u"Confidencialidad de caso",('B'),''),
    
    (Caso_vinculo, Caso_vinculo.comentarios, u"Comentarios sobre la relaci\xf3n entre casos", ('T'),'V'),
    (Caso_vinculo, Caso_vinculo.observaciones, u"Observaciones sobre la relaci\xf3n entre casos", ('T'),'V'),
    (Caso_vinculo, Caso_vinculo.Ptipo, u"Tipo de relaci\xf3n entre casos", ('C', u'T22'),'V2'),
    (Caso_vinculo, Caso_vinculo.id, u"No. de registro de la relaci\xf3n entre casos", ('I'),'V'),
    (Caso_vinculo, Caso_vinculo.id, u"Caso relacionado con otros casos", ('Z'),'V'),
    
    
    
 
    
    
    (EventoTipificacionDerechosAfectados, EventoTipificacionDerechosAfectados.tipificacion, "Derechos afectados", ('C', u'T03'),'EA'), # "EventoTipificacionDerechosAfectados.tipificacion == C"    
    (EventoTipificacionTemas, EventoTipificacionTemas.tipificacion, u"Temas del caso", ('C', u'T01'),'FA'), # EventoTipificacionTemas.tipificacion == C"
    (EventoTipificacionLegisNac, EventoTipificacionLegisNac.tipificacion, u"Legislaci\xf3n nacional", ('C', u'T62'),'L'), # EventoTipificacionTemas.tipificacion == C"
    (EventoTipificacionLegisNac, EventoTipificacionLegisNac.notas, u"Notas sobre legislaci\xf3n nacional", ('T'),'L'), # EventoTipificacionTemas.notas == txt"
    (EventoTipificacionInstInt, EventoTipificacionInstInt.tipificacion, u"Instrumentos internacionales", ('C', u'T06'),'M'), # EventoTipificacionTemas.tipificacion == C"
    (EventoTipificacionInstInt, EventoTipificacionInstInt.notas, u"Notas sobre instrumentos internacionales", ('T'),'M'), # EventoTipificacionTemas.notas == txt"
    
    (Caso, (Caso.fecha_inicio, Caso.tipo_fecha_inicio),u"Fecha inicial del caso",('F'),''),
    (Caso, (Caso.fecha_final, Caso.tipo_fecha_final),u"Fecha final del caso",('F'),''),
    (Caso, (Caso.frecepcion, Caso.tipo_frecepcion),u"Fecha de recepción de la información sobre el caso",('F'),''),
    (Caso, Caso.descripcion_narrativa,u"Descripci\xf3n narrativa del caso",('T'),''),
    (Caso, Caso.exportar, u"Exportar caso",('B'),'', 'CondicionExportar'),
    (Caso, Caso.exportarrelaciones, u"Exportar las relaciones de caso",('B'),'', 'CondicionExportar'),
    (Caso,Caso.Pmonitoreo, u"Estatus del caso", ('C',u'T46'),''),
    
    (Acto, (Acto.fechainicio, Acto.tipofechainicio),u"Fecha inicial del acto",('F'),'A'),
    (Acto, (Acto.fechafin, Acto.tipofechafinal),u"Fecha final del acto",('F'),'A'),
    (Acto, Acto.id, u"No. de registro del acto", ('I'),'A'),
    (Acto, Acto.PTipodelugar,u"Tipo de lugar donde ocurri\xf3 el acto",('C',u'T17'),'A'),
    (Acto, Acto.PEstatusvictima,u"Estatus de la v\xedctima",('C',u'T25'),'A'),
    (Acto, Acto.Pvictima,u"V\xedctima del acto",('P'),'A'),
    (Acto, Acto.PTipodeacto,u"Tipo de acto o VDH",('C',u'T04'),'A'),
    (Acto, Acto.PEstatusvdh,u"Estatus VDH",('C',u'T41'),'A'),
    (Acto, Acto.observaciones, u"Observaciones sobre el acto", ('T'),'A'), 
    (Acto, Acto.edad_victima, u"Edad de la víctima cuando ocurri\xf3 el acto", ('I'),'A'), 
    
    (Acto, Acto.exportar, u"Exportar acto",('B'),'A','CondicionExportar'),
    (Acto, Acto.exportarnormatividad, u"Exportar normatividad de acto",('B'),'A', 'CondicionExportar'),
    (Acto, Acto.id, u"Caso con actos",('Z'),'A'),
    (Caracrelevantes, Caracrelevantes.Pcaracteristicarelevante, u"Caracter\xedsticas relevantes de la v\xedctima",('C',u'T23'),'AE'),
    
    
    (Involucramiento, Involucramiento.Ptipoperpetrador, u"Tipo de perpetrador",('C',u'T24'),'AA'),
    (Involucramiento, Involucramiento.id, u"No. de registro del perpetrador", ('I'),'AA'),
    (Involucramiento, Involucramiento.Pgradoinvolucramiento, u"Grado de involucramiento del perpetrador",('C',u'T18'),'AA'),
    (Involucramiento, Involucramiento.Pultimostatusperpetrador, u"\xdaltimo estatus del perpetrador",('C',u'T26'),'AA'),
    (Involucramiento, Involucramiento.persona,u'Perpetrador del acto',('P'),'AA'),
    (Involucramiento, Involucramiento.observaciones, u"Observaciones sobre el perpetrador", ('T'),'AA'), 
    #(Involucramiento, Involucramiento.confidencialidad, u"Confidencialidad sobre el perpetrador",('B'),'AA'),
    (Involucramiento, Involucramiento.exportar, u"Exportar perpetrador",('B'),'AA', 'CondicionExportar'),
    

    
    (Fuente, Fuente.id, u"Caso con fuentes personales", ('Z'),'J'),
    (Fuente, Fuente.id, u"No. de registro de la fuente personal", ('I'),'J'),
    (Fuente, Fuente.PPersona, u"Persona sobre quien proporciona información la fuente personal", ('P'),'J'),
    (Fuente, Fuente.PPersona_como_fuente, u"Nombre de la fuente personal", ('P'),'J'),
    
    (Fuente, (Fuente.fecha, Fuente.tipofecha),u"Fecha de la información proporcionada por la fuente personal",('F'),'J'),
    (Fuente, Fuente.PConexion_info,u"Conexi\xf3n de la fuente personal con la informaci\xf3n que proporciona",('C',u'T19'),'J'),
    (Fuente, Fuente.PIdioma,u"Idioma de la fuente personal",('C',u'T14'),'J'),
    (Fuente, Fuente.PLengua_indigena,u"Lengua ind\xedgena de la fuente personal",('C',u'T66'),'J'),
    (Fuente, Fuente.PConfiabilidad,u"Confiabilidad de la fuente personal",('C',u'T42'),'J'),
    (Fuente, Fuente.observaciones, u"Observaciones sobre la fuente personal", ('T'),'J'), 
    (Fuente, Fuente.comentarios, u"Comentarios sobre la fuente personal", ('T'),'J'),
    
    (Fuente, Fuente.exportar, u"Exportar fuente personal",('B'),'J', 'CondicionExportar'),
    
    (Publicacion, Publicacion.id, u"Caso con fuentes documentales", ('Z'),'H'),
    (Publicacion, Publicacion.id, u"No. de registro de la fuente documental", ('I'),'H'),
    #(Publicacion, Publicacion.titulo, u"T\xedtulo de la fuente documental",('T'),'H'),
    (Publicacion, Publicacion.datos_publicacion, u"Datos de la fuente documental",('T'),'H'),
    (Publicacion, (Publicacion.fecha, Publicacion.tipofecha), u"Fecha de la fuente documental",('F'),'H'),
    (Publicacion, (Publicacion.fecha_consulta, Publicacion.tipofechaconsulta), u"Fecha de consulta del registro de la fuente documental",('F'),'H'),
    (Publicacion, Publicacion.Nombre_del_sitio, u"Nombre del sitio donde se localiza la fuente documental",('T'),'H'),
    (Publicacion, Publicacion.Liga_publicacion, u"Liga del sitio de la fuente documental",('T'),'H'),
    (Publicacion, Publicacion.PTipopublicacion,u"Tipo de la fuente documental",('C',u'T16'),'H'),
    (Publicacion, Publicacion.PIdioma,u"Idioma de la fuente documental",('C',u'T14'),'H'),
    (Publicacion, Publicacion.PLengua_indigena,u"Lengua ind\xedgena de la fuente documental",('C',u'T66'),'H'),
    (Publicacion, Publicacion.PConfiabilidad,u"Confiabilidad de la fuente documental",('C',u'T42'),'H'),
    (Publicacion, Publicacion.observaciones, u"Observaciones sobre la fuente documental", ('T'),'H'), 
    (Publicacion, Publicacion.comentarios, u"Comentarios sobre la fuente documental", ('T'),'H'),
    (Publicacion, Publicacion.PPersonareferenciada, u"Persona sobre quien proporciona información la fuente documental", ('P'),'H'),
    (Publicacion, Publicacion.exportar, u"Exportar fuente documental",('B'),'H', 'CondicionExportar'),
    (Publicacion, Publicacion.titulo_de_parte, u"Identificaci\xf3n de la fuente documental",('T'),'H'),
    
    (Intervencion, Intervencion.id, u"Caso con intervenciones",('Z'),'I'),
    (Intervencion, Intervencion.id, u"No. de registro de la intervenci\xf3n", ('I'),'I'),
    (Intervencion,Intervencion.tipo, u"Tipo de intervenci\xf3n", ('C',u'T20'),'I'),
    (Intervencion,Intervencion.Pinterviniente, u"Persona que inicia o realiza la intervenci\xf3n", ('P'),'I'),
    (Intervencion,Intervencion.contraparte, u"Persona a quien se le dirigi\xf3 la intervenci\xf3n", ('P'),'I'),
    (Intervencion,Intervencion.solicitante, u"Persona sobre quien se interviene", ('P'),'I'),
    #(Intervencion,Intervencion.Pestatus, u"Estatus del expediente", ('C',u'T46'),'I'),
    (Intervencion,Intervencion.observaciones, u"Observaciones sobre la intervenci\xf3n", ('T'),'I'), 
    (Intervencion,Intervencion.comentarios, u"Comentarios sobre la intervenci\xf3n", ('T'),'I'), 
    (Intervencion,Intervencion.respuesta, u"Respuesta a la intervenci\xf3n", ('T'),'I'), 
    (Intervencion,Intervencion.impacto, u"Impacto de la intervenci\xf3n", ('T'),'I'), 
    (Intervencion, (Intervencion.fecha, Intervencion.tipofecha), u"Fecha de la intervenci\xf3n",('F'),'I'),
    (Intervencion, Intervencion.exportar, u"Exportar intervenci\xf3n",('B'),'I', 'CondicionExportar'),
    
    
    (Involucramiento,Involucramiento.id, u"Caso con actos con perpetradores", ('Z'),'AA'),
    (PerPerpetrador,PerPerpetrador.Psexo, u"Sexo del perpetrador", ('C',u'T39'),'AAAA'),
    (PerPerpetrador,PerPerpetrador.Pocupacion, u"Ocupación del perpetrador", ('C',u'T10'),'AAAB'),
    (PersonaTipificacionPerpEtnico,PersonaTipificacionPerpEtnico.PTesauro, u"Origen étnico del perpetrador", ('C',u'T13'),'AAAC'),
    
    (PerVictima,PerVictima.Psexo, u"Sexo de la víctima", ('C',u'T39'),'ADA'),
    (PerVictima,PerVictima.Pocupacion, u"Ocupación de la víctima", ('C',u'T10'),'ADB'),
    (PersonaTipificacionVicEtnico,PersonaTipificacionVicEtnico.PTesauro, u"Origen étnico de la víctima", ('C',u'T13'),'ADC'),
    
# XXX busqueda sobre edad

    

    
    (Localidad, Localidad.Estado, u"Estado de la Rep\xfablica", ('C',u'T63', 2),'G'),
    (Localidad, Localidad.Municipio, u"Municipio", ('C',u'T63'),'G'),
    (Localidad, Localidad.Pais, u"Pa\xeds", ('C',u'T15'),'G'),
    (Localidad, Localidad.localidad, u"Localidad", ('T'),'G'),
    (Localidad, Localidad.notas_municipio, u"Notas sobre el municipio donde ocurri\xf3 el caso", ('T'),'G'),
    (Localidad, Localidad.notas_localidad, u"Notas sobre la localidad donde ocurri\xf3 el caso", ('T'),'G'),
    
    (LoginfoCaso,(LoginfoCaso.fechaCreacion,None), u'Fecha de creaci\xf3n del registro del caso',('F'),'K'),
    
    (LoginfoCaso,LoginfoCaso.Creador, u'Creador del registro del caso',('U'),'K'),
    (LoginfoCaso,LoginfoCaso.Actualizador, u'Actualizador del registro del caso',('U'),'K'),
    
    (LoginfoActo,(LoginfoActo.fechaCreacion,None), u'Fecha de creaci\xf3n del registro del acto',('F'),'AF'),
    (LoginfoCaso,(LoginfoCaso.fechaActualizacion,None), u'Fecha de actualizaci\xf3n del caso',('F'),'K'),
    (LoginfoActo,(LoginfoActo.fechaActualizacion,None), u'Fecha de actualizaci\xf3n del acto',('F'),'AF'),
    
    (LoginfoActo,LoginfoActo.Creador, u'Creador del registro del acto',('U'),'AF'),
    (LoginfoActo,LoginfoActo.Actualizador, u'Actualizador del registro del acto',('U'),'AF'),
    
    
    (LoginfoInvol,(LoginfoInvol.fechaCreacion,None), u'Fecha de creaci\xf3n del registro del perpetrador',('F'),'AAC'),
    (LoginfoInvol,(LoginfoInvol.fechaActualizacion,None), u'Fecha de actualizaci\xf3n del registro del perpetrador',('F'),'AAC'),
    
    (LoginfoInvol,LoginfoInvol.Creador, u'Creador del registro del perpetrador',('U'),'AAC'),
    (LoginfoInvol,LoginfoInvol.Actualizador, u'Actualizador del registro del perpetrador',('U'),'AAC'),
    
    
    (LoginfoIntervencion,(LoginfoIntervencion.fechaCreacion,None), u'Fecha de creaci\xf3n del registro de la intervenci\xf3n',('F'),'IF'),
    (LoginfoIntervencion,(LoginfoIntervencion.fechaActualizacion,None), u'Fecha de actualizaci\xf3n del registro de la intervenci\xf3n',('F'),'IF'),
    
    (LoginfoIntervencion,LoginfoIntervencion.Creador, u'Creador del registro de la intervenci\xf3n',('U'),'IF'),
    (LoginfoIntervencion,LoginfoIntervencion.Actualizador, u'Actualizador del registro de la intervenci\xf3n',('U'),'IF'),
    
    (LoginfoFuente,(LoginfoFuente.fechaCreacion,None), u'Fecha de creaci\xf3n del registro de la fuente personal',('F'),'JF'),
    (LoginfoFuente,(LoginfoFuente.fechaActualizacion,None), u'Fecha de actualizaci\xf3n del registro de la fuente personal',('F'),'JF'),
 
 
    (LoginfoFuente,LoginfoFuente.Creador, u'Creador del registro de la fuente personal',('U'),'JF'),
    (LoginfoFuente,LoginfoFuente.Actualizador, u'Actualizador del registro de la fuente personal',('U'),'JF'),
 
    (LoginfoPub,(LoginfoPub.fechaCreacion,None), u'Fecha de creaci\xf3n del registro de la fuente documental',('F'),'HF'),
    (LoginfoPub,(LoginfoPub.fechaActualizacion,None), u'Fecha de actualizaci\xf3n del registro de la fuente documental',('F'),'HF'),
    
    (LoginfoFuente,LoginfoPub.Creador, u'Creador del registro de la fuente documental',('U'),'HF'),
    (LoginfoFuente,LoginfoPub.Actualizador, u'Actualizador del registro de la fuente documental',('U'),'HF'),
    
    (LoginfoCasoVinculo,(LoginfoCasoVinculo.fechaCreacion,None), u'Fecha de creaci\xf3n del registro de la relaci\xf3n entre casos',('F'),'V1'),
    (LoginfoCasoVinculo,(LoginfoCasoVinculo.fechaActualizacion,None), u'Fecha de actualización del registro de la relaci\xf3n entre casos',('F'),'V1'),
    (LoginfoCasoVinculo,LoginfoCasoVinculo.Creador, u'Creador del registro de la relaci\xf3n entre casos',('U'),'V1'),
    (LoginfoCasoVinculo,LoginfoCasoVinculo.Actualizador, u'Actualizador del registro de la relaci\xf3n entre casos',('U'),'V1'),
    
    (LoginfoEvTip,(LoginfoEvTip.fechaCreacion,None), u'Fecha de creaci\xf3n del registro de normatividad del acto',('F'),'OA'),
    (LoginfoEvTip,(LoginfoEvTip.fechaActualizacion,None), u'Fecha de actualización del registro de normatividad del acto',('F'),'OA'),
    (LoginfoEvTip,LoginfoEvTip.Creador, u'Creador del registro de normatividad del acto',('U'),'OA'),
    (LoginfoEvTip,LoginfoEvTip.Actualizador, u'Actualizador del registro de normatividad del acto',('U'),'OA'),

    
    ]
    
            if status.SE:
                 self.campos.append( (Caso, Caso.proyecto_se, u"Proyecto SE", ('T'),'') )
    
    
    
# T = texto
# F = Fecha
# C = Tesauro
# X = Coleccion ?


class QueryPersona(QueryObject):
    def __init__(self, prnt):
        QueryObject.__init__(self, prnt)
        self.initCampos()
        self.GeneraQuery = GeneraQueryPersona
        self.busquedaActualDependencias=[]
        
        
    def initCampos(self):
            self.campos = \
    [
    (None, None, u" O bien...",('O')),
    #(None, None, u" Y tambi\xe9n...".encode("latin_1", 'replace'),('Y')),
    (None, None, u" Y tambi\xe9n...",('Y')),
    (Persona, Persona.id, u"No. de registro de la persona", ('I'),''),
    (Persona, Persona.localidad_nac_u_origen, u"Localidad de nacimiento o de origen", ('T'),''),
    (Persona, Persona.descripcion_del_grupo, u"Descripción del grupo", ('T'),''),
    (Persona, Persona.observaciones, u"Observaciones sobre la persona", ('T'),''),
    (Persona, Persona.comentarios, u"Comentarios sobre la persona", ('T'),''),
    (Persona, Persona.archivos, u"Archivos", ('T'),''),
    (Persona, Persona.proyecto_grupo, u"Proyecto local", ('T'),''),
    (Persona, Persona.proyecto_conjunto, u"Proyecto conjunto RedTDT", ('T'),''),
    (Persona, Persona.apellido, u"Nombre de la persona colectiva", ('T'),''),
    (Persona, Persona.nombre, u"Sigla de la persona colectiva", ('T'),''),
    (Persona, Persona.apellido, u"Apellido de la persona individual", ('T'),''),
    (Persona, Persona.nombre, u"Nombre de la persona individual", ('T'),''),
    (Persona, Persona.otro_nombre, u"Otro nombre", ('T'),''),
    
    (Persona, (Persona.fecha_nac_o_fund, Persona.tipo_fecha_nac_o_fund), u"Fecha de nacimiento o creaci\xf3n", ('F'),''),
    (Persona, (Persona.frecepcion, None), u"Fecha de recepci\xf3n de la informaci\xf3n sobre la persona", ('F'),''),
    (Persona, Persona.habla_lengua_local,u'Habla y entiende espa\xf1ol',('B'),''),
    (Persona, Persona.no_dependientes,u'No. de dependientes',('I'),''),
    (Persona, Persona.no_dependientes,u'No. de personas en el grupo',('I'),''),
    (Persona, Persona.exportar,u'Exportar persona',('B'),'', 'CondicionExportar'),
    
    (LoginfoPersona,(LoginfoPersona.fechaCreacion,None), u'Fecha de creaci\xf3n del registro de la persona',('F'),'K'),
    (LoginfoPersona,(LoginfoPersona.fechaActualizacion,None), u'Fecha de actualización del registro de la persona',('F'),'K'),
    (LoginfoPersona,LoginfoPersona.Creador, u'Creador del registro de la persona',('U'),'K'),
    (LoginfoPersona,LoginfoPersona.Actualizador, u'Actualizador del registro de la persona',('U'),'K'),
    

    
    (Persona, Persona.Preligion,u"Religi\xf3n",('C',u'T12'),'R'),
    (Persona, Persona.Ptipo,u'Tipo de grupo',('C',u'T07'),'G'),
    (Persona, Persona.Psexo,u'Sexo',('C',u'T39'),'S'),
    (Persona, Persona.Ppais_nac_u_origen,u'País de nacimiento o de origen',('C',u'T15'),'P'),
    #(Persona, Persona.Pciudadania_o_sede,u'País de sede o ciudadan\xeda',('C',u'T15'),'P'),
    (Persona, Persona.Pestado_nac_u_origen,u'Estado de nacimiento o de origen',('C',u'T63'),'E'),
    (Persona, Persona.Pmpio_nac_u_origen,u'Municipio de nacimiento o de origen',('C',u'T63'),'M'),
    (Persona, Persona.Pciudadania_o_sede,u'Ciudadanía o País sede',('C',u'T15'),'C'),
    (Persona, Persona.Pescolaridad,u'Escolaridad',('C',u'T09'),'0'),
    (Persona, Persona.Pocupacion,u'Ocupaci\xf3n',('C',u'T10'),'1'),
    
    (Persona, Persona.Pestado_civil,u'Estado civil',('C',u'T08'),'3'),
    (Persona, Persona.Pmonitoreo,u'Monitoreo',('C',u'T43'),'5'),
    (Persona, Persona.Pmonitoreo,u'Con algun rol',('R'), ''),
    #(Persona, Persona.personarelacionadac3,u'Presente en C3',('0'),''),
    
    (PersonaTipificacionTipoGrupo, PersonaTipificacionTipoGrupo.PTesauro,u'Origen étnico',('C',u'T13'),'U1'),
    (PersonaTipificacionLengua, PersonaTipificacionLengua.PTesauro,u'Lengua indígena',('C',u'T66'),'Q1'),
    (PersonaTipificacionIdioma, PersonaTipificacionIdioma.PTesauro,u'Idioma',('C',u'T14'),'T1'),
    
    (PersonaTipificacionDireccion, PersonaTipificacionDireccion.celular,u'Direcci\xf3n',('A'),'V'),
    
    (DetalleBiografico, DetalleBiografico.id, u"Persona con datos biográficos", ('Z'),'D'),
    (DetalleBiografico, DetalleBiografico.descripcion, u"Descripción de un dato biográfico", ('T'),'D'),
    (DetalleBiografico, DetalleBiografico.observaciones, u"Observaciones sobre un dato biográfico", ('T'),'D'),
    (DetalleBiografico, DetalleBiografico.comentarios, u"Comentarios sobre un dato biográfico", ('T'),'D'),
    (DetalleBiografico, DetalleBiografico.puesto, u"Puesto o cargo (en un dato biográfico)", ('T'),'D'),
    (DetalleBiografico, DetalleBiografico.rango, u"Rango (en un dato biográfico)", ('T'),'D'),
    
    
    (DetalleBiografico, (DetalleBiografico.Fecha_inicial, None), u"Fecha inicial de un dato biográfico", ('F'),'D'),
    (DetalleBiografico, (DetalleBiografico.Fecha_final, None), u"Fecha final de un dato biográfico", ('F'),'D'),
    (DetalleBiografico, (DetalleBiografico.fecha_info_vigente, None), u"Fecha de vigencia de un dato biográfico", ('F'),'D'),
    
    (DetalleBiografico, DetalleBiografico.exportar, u"Exportar dato biográfico", ('B'),'D', 'CondicionExportar'),
    (DetalleBiografico, DetalleBiografico.tipo, u"Tipo de relación en dato biográfico", ('C',u'T21'),'D'),
    
    (LoginfoDatoBio, (LoginfoDatoBio.fechaCreacion, None), u'Fecha de creaci\xf3n de registro de un dato biográfico',('F'),'D1'),
    (LoginfoDatoBio, (LoginfoDatoBio.fechaActualizacion, None), u'Fecha de actualizaci\xf3n de registro de un dato biográfico',('F'),'D1'),
    
    (LoginfoDatoBio, LoginfoDatoBio.Creador, u'Creador del registro de dato biográfico',('U'),'D1'),
    (LoginfoDatoBio, LoginfoDatoBio.Actualizador, u'Actualizador del registro de dato biográfico',('U'),'D1'),
    
    ]
            if status.SE:
                self.campos.append( (Persona, Persona.proyecto_se, u"Proyecto SE", ('T'),'') )
                self.campos.append( (Persona, Persona.personarelacionadac3,u'Presente en C3',('0'),'') )
        



class Filtro(object):
    def __init__(self, entidad, campo, descripcion, dependencia):
        self.entidad = entidad
        self.campo = campo
        self.descripcion = descripcion.encode("latin_1", 'replace')
        self.dependencia = dependencia
        self.borrar = False
        self.nuevo = True
        self.negativo = False
        
class FiltroO(object):
    def __init__(self):
        self.dependencia = ''
        self.borrar = False
        
    def __repr__(self):
        return "O bien..."
    def edit(self,prnt):
        return

class FiltroY(object):
    def __init__(self):
        self.dependencia = ''
        self.borrar = False
        
    def __repr__(self):
        return u" Y tambi\xe9n...".encode("latin_1", 'replace')
        #return " Y tambien..."
    def edit(self,prnt):
        return

    
class FiltroColeccion(Filtro):
    def __init__(self, entidad, campo, descripcion, codigo, dependencia):
        Filtro.__init__(self, entidad, campo, descripcion, dependencia)
        self.codigo = codigo
    def edit(self,prnt):
        #self.tipos = getTaxonomyTree(prnt, self.codigo, self.descripcion, poli=True)
        tiposElejidos, invertir, cancelar = getTaxonomyTree(prnt, self.codigo, self.descripcion, poli=True, search=True, help=u'getTaxonomyTreeBusqueda')
        if not cancelar:
            self.tipos=[]
            self.negativo = invertir
            for i in tiposElejidos:
                for j in i.allTree():
                   self.tipos.append(j)
        self.borrar = cancelar and self.nuevo
    def ToFilter(self):
        F = sql.or_(*[self.campo.contains(t2) for t2 in self.tipos])
        if self.negativo:
            F = sql.not_(F)
        return  F
    def __repr__(self):
        return self.descripcion +' es "'+ str([i.descripcion +'/' for i in self.tipos])

class FiltroTesauro(Filtro):
    def __init__(self, entidad, campo, descripcion, codigo, dependencia, deep=None):
        Filtro.__init__(self, entidad, campo, descripcion, dependencia)
        self.codigo = codigo
        self.deep = deep
        
    def edit(self,prnt):
        tiposElejidos, invertir, cancelar = getTaxonomyTree(prnt, self.codigo, self.descripcion, poli=True, deep=self.deep, search=True, help=u'getTaxonomyTreeBusqueda')
        if not cancelar:
            self.negativo = invertir
            self.tipos=[]
            if tiposElejidos:
                for i in tiposElejidos:
                    for j in i.allTree():
                       self.tipos.append(j)
        self.borrar = cancelar and self.nuevo
       
                
                   
    def ToFilter(self):
        if self.tipos:
            F = sql.or_(*[self.campo == t2 for t2 in self.tipos])
        #ojo experimental
        else:
            F = (self.campo == None)
        if self.negativo:
            F = sql.not_(F)
            if self.tipos:
                F = sql.or_(*[F, self.campo == None])
        
        return F
    def __repr__(self):
        
        #return self.descripcion +' es "'+ str([i.descripcion.encode("latin_1", 'replace') +'/' for i in self.tipos])
        
        if self.tipos:
            cadena = ",".join([i.descripcion  for i in self.tipos])[:200]
            resultado = "%s:%s%s"%(self.descripcion,"No " if self.negativo else '', cadena.encode("latin_1", 'replace'))
        else:
            if self.negativo:
                resultado = "%s: NO en blanco"%self.descripcion
            else:
                resultado = "%s: En blanco"%self.descripcion
        
            
        return resultado
    
    
class FiltroPersona(Filtro):
    def __init__(self, entidad, campo, descripcion, dependencia):
        Filtro.__init__(self, entidad, campo, descripcion, dependencia)
        self.personaElejida=None

    def edit(self,prnt):
        personaElejida, negativo, cancelar = PersonaDlg(prnt, search=True, invertir=self.negativo)
        if cancelar:
            self.borrar = self.nuevo
        else:
            self.personaElejida, self.negativo = personaElejida, negativo
        
    def ToFilter(self):
        F =  self.campo ==   self.personaElejida
        if self.negativo:
            F = sql.not_(F)
        return F
    def __repr__(self):
        
        desc = self.personaElejida.Descriptor() if self.personaElejida else "%s blanco"%("en" if self.negativo else "En ")
        #return self.descripcion +' es '+ desc.encode("iso-8859-1", 'replace')
        negativo = " No es " if self.negativo else ''
        return self.descripcion +':'+negativo+ desc.encode("latin_1", 'replace')
        

class FiltroUsuario(Filtro):
    def __init__(self, entidad, campo, descripcion, dependencia):
        Filtro.__init__(self, entidad, campo, descripcion, dependencia)
        print "creando filtro usuario con entidad",entidad," campo ",campo
        self.personaElejida=None

    def edit(self,prnt):
        
        personaElejida, negativo, cancelar = UserCond(prnt, self.negativo)
        if cancelar:
            self.borrar = self.nuevo
        else:
            self.personaElejida, self.negativo = personaElejida, negativo
    def ToFilter(self):
        F =  self.campo ==   self.personaElejida
        if self.negativo:
            F = sql.not_(F)
        return F
    def __repr__(self):
        desc = self.personaElejida.Descriptor() if self.personaElejida else "%s blanco"%("en" if self.negativo else "En ")
        #return self.descripcion +' es '+ desc.encode("iso-8859-1", 'replace')
        negativo = ' No es ' if self.negativo else ''
        return self.descripcion +':'+ negativo + desc.encode("latin_1", 'replace')




class FiltroFecha(Filtro):
    # ojo agregar condicion para tipo fecha de manera general
    def __init__(self, entidad, campo, descripcion, dependencia):
        Filtro.__init__(self, entidad, campo, descripcion, dependencia)
        self.param = LocalVal()
        self.param.DateI=None
        self.param.DateF=None
        self.param.Type=None
        self.param.invertir=False
        self.param.sinFecha=False
        self.param.borrar = False
        self.borrar = False
        self.param.conTipoDeFecha = True if self.campo[1] else False
    def edit(self,prnt):
        
        DlgCond(prnt,"Date", self.param, help=u'condicionFecha')
        self.negativo = self.param.invertir
        self.borrar = self.param.borrar and self.nuevo
    def ToFilter(self):

        #return sql.and_(*[self.campo >= DateTimeString(self.param.Date), Caso.tipo_fecha_inicio > 0])
        if self.param.sinFecha:
            if self.campo[1]:
                F = self.campo[1] == None
        else:
            if self.campo[1]:
                condTipoFecha = self.campo[1] > 0
            else:
                condTipoFecha = None
            F = sql.and_(*[self.campo[0] >= DateTimeString(self.param.DateI), 
                              self.campo[0] <= DateTimeString(self.param.DateF),
                              condTipoFecha])
            
        if self.negativo:
            F = sql.not_(F)                  
        return F
    def __repr__(self):
        if self.param.sinFecha:
            descCondicion = " %s registrada"%('' if self.negativo else 'no')
            return self.descripcion + descCondicion
        else:    
            descCondicion = ' no entre ' if  self.negativo else ' entre '
            return self.descripcion + descCondicion + DateTimeString(self.param.DateI)+'" y '+DateTimeString(self.param.DateF)

class FiltroCadena(Filtro):
    def __init__(self, entidad, campo, descripcion, dependencia):
        Filtro.__init__(self, entidad, campo, descripcion, dependencia)
    def edit(self, prnt):
        cadenaBusqueda, negativo, cancelar = MyDescrip(prnt, help=u'MyDescripBusqueda', search=True, invertir=self.negativo)
        print "cancelar:",cancelar," self.nuevo:",self.nuevo
        if cancelar:
            self.borrar = self.nuevo
        else:
            self.cadenaBusqueda, self.negativo = cadenaBusqueda, negativo
    def ToFilter(self):
        if self.cadenaBusqueda:
            F = self.campo.ilike('%'+self.cadenaBusqueda+'%')
        else:
            F = (self.campo == '')
        if self.negativo:
            F = sql.not_(F)        
        return F
    def __repr__(self):
        a = self.descripcion
        cadena = self.cadenaBusqueda.encode("latin_1", 'replace')
        b = "'"+cadena+"'" if cadena else "en blanco"
        c1 = "no" if self.negativo else ""
        c2 = 'es' if cadena else "está"
        return "%s %s %s %s"%(a,c1, c2,b)
    
    
    
    
class FiltroDireccionPersona(Filtro):
    def __init__(self, entidad, campo, descripcion, dependencia):
        Filtro.__init__(self, entidad, campo, descripcion, dependencia)
    def edit(self, prnt):
        cadenaBusqueda, negativo, cancelar = MyDescrip(prnt, help=u'MyDescripBusqueda', search=True, invertir=self.negativo)
        if cancelar:
            self.borrar = self.nuevo
        else:
            self.cadenaBusqueda, self.negativo = cadenaBusqueda, negativo
        
    def ToFilter(self):
        #if self.cadenaBusqueda:
        F = sql.or_(*[PersonaTipificacion.telefono.ilike('%'+self.cadenaBusqueda+'%'), 
                      PersonaTipificacion.celular.ilike('%'+self.cadenaBusqueda+'%'),
                      PersonaTipificacion.masinformacion.ilike('%'+self.cadenaBusqueda+'%'),
                      PersonaTipificacion.web.ilike('%'+self.cadenaBusqueda+'%'),
                      PersonaTipificacion.correo_e.ilike('%'+self.cadenaBusqueda+'%')
                      ])
        #else:
        #    F = sql.and_(*[PersonaTipificacion.codigo == 910,
        #                   PersonaTipificacion.codigo != None]
        #                   )
                            
                           
        
        if self.negativo:
            F = sql.not_(F)        
        #F = sql.and_(F, PersonaTipificacion.codigo==910)
        return F
    def __repr__(self):
        a = self.descripcion
        b = self.cadenaBusqueda.encode("latin_1", 'replace')
        c = "no contiene" if self.negativo else "contiene"
        return "%s %s '%s'"%(a,c,b)
    

class FiltroEntero(Filtro):
    def __init__(self, entidad, campo, descripcion, dependencia):
        Filtro.__init__(self, entidad, campo, descripcion, dependencia)
    def edit(self, prnt):
        cadenaBusqueda, negativo, cancelar = MyDescrip(prnt, search=True, invertir=self.negativo)
        if cancelar:
            self.borrar = self.nuevo
        else:
            self.cadenaBusqueda, self.negativo = cadenaBusqueda, negativo
            
    def ToFilter(self):
        if self.cadenaBusqueda:
            F =  self.campo == self.cadenaBusqueda
        else:
            F = self.campo == None
        if self.negativo:
            F = sql.not_(F)
        return F
    
    def __repr__(self):
        a = self.descripcion
        b = self.cadenaBusqueda.encode("latin_1", 'replace')
        if self.cadenaBusqueda:
            c = "no es" if self.negativo else "es"
            return "%s %s '%s'"%(a,c,b)
        else:
            c = "Con " if self.negativo else "Sin "
            return "%s %s"%(c, a.lower())


class FiltroCero(Filtro):
    ' solo para buscar personas en contenedor 2 que esten presentes en C3'
    def __init__(self, entidad, campo, descripcion, dependencia):
        Filtro.__init__(self, entidad, campo, descripcion, dependencia)
        self.param=LocalVal()
        self.param.Value=0

    def edit(self, prnt):
        DlgChk(prnt,"Chk", self.param, descripcion=self.descripcion)
        self.borrar = self.param.borrar and self.nuevo
    def ToFilter(self):
        F1 =  sql.or_(self.campo == 0, self.campo == None) 
        F2 =  Persona.clavestatus == 2
        if self.param.Value == 1:
            F1 = sql.not_(F1)
        F = sql.and_(F1, F2)
        return F
    
    def __repr__(self):
        a = self.descripcion
        
        c = "no " if self.param.Value == 0 else ""
        return "%s %s "%(a,c)

    
    
class FiltroChk(Filtro):
    def __init__(self, entidad, campo, descripcion, dependencia, help=None):
        Filtro.__init__(self, entidad, campo, descripcion, dependencia)
        self.param=LocalVal()
        self.param.Value=0
        self.help=help
        
        
    def edit(self, prnt):
        DlgChk(prnt,"Chk", self.param, descripcion=self.descripcion, help=self.help)
        self.borrar = self.param.borrar and self.nuevo
        
    def ToFilter(self):
        F =  self.campo == self.param.Value
        return F
    def __repr__(self):
        if self.param.Value == 1:
            res = 'Si'
        else:
            res = "No"
        return self.descripcion +':' + res
class FiltroRol(Filtro):
    def __init__(self, entidad, campo, descripcion, dependencia):
        Filtro.__init__(self, entidad, campo, descripcion, dependencia)
        self.param=LocalVal()
        self.param.Value=0
        
    def edit(self, prnt):
        DlgChk(prnt,"Chk", self.param, descripcion=self.descripcion)
        self.borrar = self.param.borrar and self.nuevo
    def ToFilter(self):
        c1I=Persona.Intervenciones_como_interviniente.any()
        c2I=Persona.Intervenciones_solicitadas_a_la_persona.any()
        c3I=Persona.Intervenciones_solicitadas_por_la_persona.any()
        c1A=Persona.Victima_en.any()
        c1P=Persona.Involucrado.any()
        c1F=Persona.fuentes.any()
        c2F=Persona.como_fuente.any()
        c1D=Persona.PPublicaciones.any()
        
        F = sql.or_(c1I, c2I, c3I, c1A, c1P, c1F, c2F, c1D)  
        if self.param.Value == 0:
            F = sql.not_(F)
        return F
    def __repr__(self):
        if self.param.Value == 1:
            res = 'Si'
        else:
            res = "No"
        return self.descripcion +' es "' + res
    
class FiltroVacio(Filtro):
    def __init__(self, entidad, campo, descripcion, dependencia):
        Filtro.__init__(self, entidad, campo, descripcion, dependencia)
        self.param=LocalVal()
        self.param.Value=0
        
        
    def edit(self, prnt):
        DlgChk(prnt,"Chk", self.param, descripcion=self.descripcion)
        self.borrar = self.param.borrar and self.nuevo
        
    def ToFilter(self):
        F =  self.campo == None
        if self.param.Value == 1:
            F =  self.campo <> None
        return F
    def __repr__(self):
        if self.param.Value == 1:
            res = ': Si '
        else:
            res = ": No "
        return self.descripcion + res
        
class FrameBusqueda(wx.Frame):
    def _init_coll_FN_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=True,
              text='B\xfasqueda')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEBUSQUEDA, name='FrameBusqueda',
              parent=prnt, pos=wx.Point(260, 172), size=wx.Size(675, 320),
              style=wx.DEFAULT_FRAME_STYLE, title='B\xfasqueda exhaustiva')
        self.SetClientSize(wx.Size(659, 284))
        self.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'MS Shell Dlg 2'))
        self.Bind(wx.EVT_ACTIVATE, self.OnFrameBusquedaActivate)
        self.Bind(wx.EVT_CLOSE, self.OnFrameBusquedaClose)

        self.FN = wx.lib.flatnotebook.FlatNotebook(id=wxID_FRAMEBUSQUEDAFN,
              name='FN', parent=self, pos=wx.Point(0, 0), size=wx.Size(659,
              284), style=0)

        self.panel1 = wx.Panel(id=wxID_FRAMEBUSQUEDAPANEL1, name='panel1',
              parent=self.FN, pos=wx.Point(0, 0), size=wx.Size(659, 258),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(223, 252, 255))

        self.ctrlCampo = wx.Choice(choices=[], id=wxID_FRAMEBUSQUEDACTRLCAMPO,
              name='ctrlCampo', parent=self.panel1, pos=wx.Point(392, 48),
              size=wx.Size(112, 21), style=0)
        self.ctrlCampo.Show(False)

        self.staticText1 = wx.StaticText(id=wxID_FRAMEBUSQUEDASTATICTEXT1,
              label='Campo', name='staticText1', parent=self.panel1,
              pos=wx.Point(344, 48), size=wx.Size(33, 13), style=0)
        self.staticText1.Show(False)

        self.addCond = wx.Button(id=wxID_FRAMEBUSQUEDAADDCOND,
              label=u'Agregar condici\xf3n', name='addCond', parent=self.panel1,
              pos=wx.Point(16, 192), size=wx.Size(104, 23), style=0)
        self.addCond.Bind(wx.EVT_BUTTON, self.OnAddCond,
              id=wxID_FRAMEBUSQUEDAADDCOND)

        self.listConds = wx.ListBox(choices=[], id=wxID_FRAMEBUSQUEDALISTCONDS,
              name='listConds', parent=self.panel1, pos=wx.Point(16, 80),
              size=wx.Size(608, 104), style=wx.HSCROLL)
        self.listConds.Bind(wx.EVT_LISTBOX_DCLICK, self.OnListCondsDclick,
              id=wxID_FRAMEBUSQUEDALISTCONDS)
        self.listConds.Bind(wx.EVT_LEFT_DCLICK, self.OnListCondsLeftDclick)
        self.listConds.Bind(wx.EVT_KEY_DOWN, self.OnListCondsKeyDown)

        self.btnRegresar = wx.Button(id=wxID_FRAMEBUSQUEDABTNREGRESAR,
              label='Regresar', name='btnRegresar', parent=self.panel1,
              pos=wx.Point(296, 224), size=wx.Size(75, 23), style=0)
        self.btnRegresar.Bind(wx.EVT_BUTTON, self.OnBtnRegresarButton,
              id=wxID_FRAMEBUSQUEDABTNREGRESAR)

        self.delCond = wx.Button(id=wxID_FRAMEBUSQUEDADELCOND,
              label='Borrar una condici\xf3n', name='delCond',
              parent=self.panel1, pos=wx.Point(520, 192), size=wx.Size(104, 23),
              style=0)
        self.delCond.Bind(wx.EVT_BUTTON, self.OnDelCondButton,
              id=wxID_FRAMEBUSQUEDADELCOND)

        self.delAll = wx.Button(id=wxID_FRAMEBUSQUEDADELALL,
              label='Borrar todas', name='delAll', parent=self.panel1,
              pos=wx.Point(520, 224), size=wx.Size(104, 23), style=0)
        self.delAll.Bind(wx.EVT_BUTTON, self.OnDelAllButton,
              id=wxID_FRAMEBUSQUEDADELALL)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self.panel1,
              pos=wx.Point(632, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)

        self._init_coll_FN_Pages(self.FN)

    def __init__(self, parent, ObjetoQuery):
        
        self._init_ctrls(parent)
        self.MakeModal(True)
        self.FN.Layout()
        
        
        self.ObjetoQuery = ObjetoQuery
        self.condiciones=ObjetoQuery.MisCondiciones
        for i in self.condiciones:
            self.listConds.Append(str(i))
        
        self.ListaDeCampos=    [(i, i[2]    ) for i in ObjetoQuery.campos]
        LlenaCtrl3(self.ctrlCampo, [(i, i[2]    ) for i in ObjetoQuery.campos])
        L.OperadorO = FiltroO()
        L.OperadorY = FiltroY()
        LlenaAyuda(self, u'frameBusqueda')
        if cnf.OSlinux:
            module2.choiceFix(self, __name__)
        

    def OnFrameBusquedaActivate(self, event):

 
        event.Skip()

    def OnCtrlCampoChoice(self, event):

            
        event.Skip()

    def OnBtnBuscar(self, event):


        
                
        event.Skip()

    def OnAddCond(self, event):
        # c = campo
        
        #c=self.ctrlCampo.GetClientData(self.ctrlCampo.GetSelection())
        lista = self.ListaDeCampos
        c = Condicion(self, lista)
        
        ayuda=None
        if len(c) >5:
            ayuda = c[5]
        if c:
            # metodo = tipo de campo a filtrar
            # T tesauro, F fecha, O or, C caracter, B booleano
            metodo=c[3][0]
            f=None
            if metodo == "T": #texto
                f=FiltroCadena(c[0], c[1], c[2], c[4])
            if metodo == "A":
                f=FiltroDireccionPersona(c[0], c[1], c[2], c[4])            
            if metodo == "I":  #entero
                f=FiltroEntero(c[0], c[1], c[2], c[4])
            if metodo == "F": #fecha
                f=FiltroFecha(c[0], c[1], c[2], c[4])
            if metodo == "O":
                f=L.OperadorO
            if metodo == "Y":
                f=L.OperadorY
            if metodo == 'C':  #taxonomia
                deep=None
                if len(c[3]) > 2:
                    deep=c[3][2]
                f=FiltroTesauro(c[0], c[1], c[2], c[3][1], c[4], deep=deep)
            if metodo == 'P': #persona
                f=FiltroPersona(c[0], c[1], c[2], c[4])
            if metodo == 'U': #usuario
                f=FiltroUsuario(c[0], c[1], c[2], c[4])
                
            if metodo == 'B': #chk
                f=FiltroChk(c[0], c[1], c[2], c[4], help=ayuda)
            if metodo == 'Z': #vacio
                f=FiltroVacio(c[0], c[1], c[2], c[4])
                
                
            if metodo == 'X':
                f=FiltroColeccion(c[0], c[1], c[2], c[3][1], c[4])
            if metodo == 'R':
                f=FiltroRol(c[0], c[1], c[2], c[4])
            if metodo == '0':
                f=FiltroCero(c[0], c[1], c[2], c[4])    
                
            #ojo
            
            if f:    
            # editar parametros de la condicion
            
               f.edit(self)
               print "f.borrar", f.borrar
               if f.borrar:
                   del f
               else:
                   f.nuevo = False
                   self.condiciones.append(f)
                   #print self.condiciones.encode("latin_1", 'replace')
                   self.listConds.Append(str(f))
                   #desc.encode("latin_1", 'replace')
        


    def OnListCondsListbox(self, event):

        event.Skip()

    def OnListCondsDclick(self, event):
        i=self.listConds.GetSelection()
        f=self.condiciones[i]
        f.edit(self)
        if f.borrar:
            self.condiciones.remove(f)
            self.listConds.Clear()
            for i in self.condiciones:
                    self.listConds.Append(str(i))
            del f
        else:
            self.listConds.SetString(i,str(f))
        event.Skip()

    def OnListCondsLeftDclick(self, event):

        event.Skip()

    def OnListCondsKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            i=self.listConds.GetSelection()
            f=self.condiciones[i]
            self.listConds.Delete(i)
            del self.condiciones[i]
            del f
            
            
        event.Skip()

    def OnBtnBuscarButton(self, event):
        res=status.filtroCaso.execute()
        
        
        event.Skip()

    def OnFrameBusquedaClose(self, event):
        self.MakeModal(False)
        event.Skip()

    def OnBtnRegresarButton(self, event):
        self.MakeModal(False)
        self.Close()
        event.Skip()

    def OnDelCondButton(self, event):
        i=self.listConds.GetSelection()
        f=self.condiciones[i]
        self.listConds.Delete(i)
        del self.condiciones[i]
        del f
        event.Skip()

    def OnDelAllButton(self, event):
        for f in self.condiciones:
            del f
        
        self.listConds.Clear()
        self.ObjetoQuery.MisCondiciones=[]
        self.condiciones=self.ObjetoQuery.MisCondiciones
        
        event.Skip()
        
def ListSplit(self, l, delim):
    i=0
    j=[]
    k=[]
    delim_repr = delim.__repr__()
    while i < len(l):
         
         while i < len(l) and l[i].__repr__() != delim_repr :
             #st1 = l[i].__repr__()
             #st2 = delim.__repr__()
             #print st1.encode("latin_1", 'replace')
             #print st2.encode("latin_1", 'replace')
             #if self.listConds.IsChecked(l.index(l[i])):
             # ojoooooo
             j.append(l[i]  )
             i = i+1
         k.append(j)
         i=i+1
         j=[]
    return [a for a in k if len(a) > 0]


  

        

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
