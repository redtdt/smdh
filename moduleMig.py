#-----------------------------------------------------------------------------
# Name:        moduleMig.py
#
#
# RCS-ID:      $Id: moduleMig.py $
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
import moduleUtils
import new


from sqlalchemy import MetaData, Table, Column, Sequence, ForeignKey
from sqlalchemy import Integer, String, sql, Date, TEXT, Unicode, create_engine
from sqlalchemy.orm import create_session, mapper, relation, backref, aliased
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.orm import PropComparator, column_property, deferred
import wx
from moduleUtils import setCheckBoxValue, getCheckBoxValue
from cnf import db, host, localCountry

POcupacion = None

def GenerapersonaX(metadata, dataObject, TesMapper, tesauro):
    TablapersonaX = Table('personax',metadata,
              
            Column('id',Integer,
                   Sequence('personax_id_seq', optional=True), primary_key=True),
            Column('puntoderecoleccion', Unicode(30), nullable=False),
            Column('GrupoIndigena',Integer),
            Column('Ocupacion',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
            
            Column('Imagen', Integer),
            Column('DocID',TEXT(convert_unicode=True)),
            Column('Hijos',Integer),
            Column('Intentos',Integer),
            Column('Expulsiones',Integer),
            Column('ViajaCon',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
            Column('Motivo',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
            Column('Destino',Integer, ForeignKey('tesauro.id',onupdate="restrict", ondelete="restrict")),
            Column('Direccion',TEXT(convert_unicode=True)),
            Column('Telefono',TEXT(convert_unicode=True)),
            Column('loginfo', Integer, ForeignKey('loginfo.id',onupdate="restrict", ondelete="restrict")),
                
            )
    class PersonaX(dataObject):
        "extension de persona"
        def __init__(self, id=None):
            dataObject.__init__(self, id)
            self.puntoderecoleccion=''
        
    PersonaXMapper = mapper(PersonaX, TablapersonaX,
    properties=
        {
         'PViajaCon':relation(TesMapper, primaryjoin=tesauro.c.id == TablapersonaX.c.ViajaCon),
         'PMotivo':relation(TesMapper, primaryjoin=tesauro.c.id == TablapersonaX.c.Motivo),
         'PDestino':relation(TesMapper, primaryjoin=tesauro.c.id == TablapersonaX.c.Destino),
         'POcupacion':relation(TesMapper, primaryjoin=tesauro.c.id == TablapersonaX.c.Ocupacion),
         
         }
       )
    return TablapersonaX, PersonaX, PersonaXMapper

def MigCreaPersonaX(self, status):
    id = status.personaActual.id
    PX = status.PersonaX(id)
    status.session.add(PX)
    status.FlushInfo(id=1340)
    status.PersonaXActual = PX
    

    return

def MigSaveDataPersona(self, status):
    global POcupacion
    if status.PersonaXActual:
        px = status.PersonaXActual
        px.DocID = self.FdocID.GetValue() 
        px.Direccion = self.FDireccion.GetValue() 
        px.Telefono = self.Ftelefono.GetValue() 
        px.Hijos = self.FHijos.GetValue()
        px.Intentos = self.Fintentos.GetValue()
        px.Expulsiones = self.Fexpulsiones.GetValue()
        
        
        
        px.GrupoIndigena =  getCheckBoxValue(self.FGrupoIndigena)
        status.personaActual.Pestado_civil = self.XgetChoiceValue(self.FPEstadocivilX)
        i = self.XgetChoiceValue(self.Fviajacon)
       
        px.PViajaCon = self.XgetChoiceValue(self.Fviajacon)
        px.PDestino = self.XgetChoiceValue(self.Fdestino)
        status.personaActual.Ppais_nac_u_origen = self.XgetChoiceValue(self.FPais)
        status.personaActual.Pciudadania_o_sede = self.XgetChoiceValue(self.FCiud)
        
        
        
        px.PMotivo = self.XgetChoiceValue(self.Fmotivo)
        px.POcupacion = POcupacion
        
        status.session.add(px)
    return

def MigLoadDataPersona(self, status):
    global POcupacion
    status.PersonaXActual = None
    ctrl=hasattr(self, "FdocID")
    if status.personaActual and ctrl:
        id = status.personaActual.id
        self.FdocID.SetValue('')
        self.FDireccion.SetValue('')
        self.Ftelefono.SetValue('')
        self.Tocupacion.SetLabel('')
        self.FHijos.SetValue(0)
        self.Fintentos.SetValue(0)
        self.Fexpulsiones.SetValue(0)
        self.FGrupoIndigena.SetValue(False)
        self.FPEstadocivilX.SetSelection(-1)
        self.Fviajacon.SetSelection(-1)
        self.Fmotivo.SetSelection(-1)
        self.Fdestino.SetSelection(-1)
        self.FPais.SetSelection(-1)
        self.FCiud.SetSelection(-1)
        POcupacion = None
        
        #self.FPEstadocivilX.SetStringSelection(-1)
        
        
        
        
        px = status.session.query(status.PersonaX).filter(status.PersonaX.id == id).first()
        if px:
        
        
            status.PersonaXActual = px
            
            self.FdocID.SetValue(moduleUtils.Mvs(status.PersonaXActual.DocID))
            self.FDireccion.SetValue(moduleUtils.Mvs(status.PersonaXActual.Direccion))
            self.Ftelefono.SetValue(moduleUtils.Mvs(status.PersonaXActual.Telefono))
            self.FHijos.SetValue(status.PersonaXActual.Hijos)
            self.Fintentos.SetValue(status.PersonaXActual.Intentos)
            self.Fexpulsiones.SetValue(status.PersonaXActual.Expulsiones)
            
            self.FGrupoIndigena.SetValue(setCheckBoxValue(status.PersonaXActual.GrupoIndigena))
            self.XCtrlSelect(self.FPEstadocivilX, status.personaActual.Pestado_civil)
            self.XCtrlSelect(self.Fviajacon, status.PersonaXActual.PViajaCon)
            self.XCtrlSelect(self.Fmotivo, status.PersonaXActual.PMotivo)
            self.XCtrlSelect(self.Fdestino, status.PersonaXActual.PDestino)
            
            if status.personaActual.Pciudadania_o_sede:
                self.XCtrlSelect(self.FCiudRegion,status.personaActual.Pciudadania_o_sede.parent)
                self.XLlenaCtrlMunicipios(self.FCiud, status.personaActual.Pciudadania_o_sede.parent)
                self.XCtrlSelect(self.FCiud,status.personaActual.Pciudadania_o_sede)    
                
            if status.personaActual.Ppais_nac_u_origen:
                self.XCtrlSelect(self.FPaisRegion,status.personaActual.Ppais_nac_u_origen.parent)
                self.XLlenaCtrlMunicipios(self.FPais, status.personaActual.Ppais_nac_u_origen.parent)
                self.XCtrlSelect(self.FPais,status.personaActual.Ppais_nac_u_origen)
                pais = status.personaActual.Ppais_nac_u_origen
                local = pais.descripcion == localCountry
                if local:
                    self.XLlenaCtrlCategoria(self.FPEstado, u'T63')
                else:
                    self.XLlenaCtrlCategoria(self.FPEstado, u'', id=pais.id)
                self.XCtrlSelect(self.FPEstado,  status.personaActual.Pestado_nac_u_origen)
                
                
            
            
            
            
            
            
            self.Tocupacion.SetLabel(self.XTesNotNull(status.PersonaXActual.POcupacion))
            POcupacion = status.PersonaXActual.POcupacion
            

        
    return




ctrlsColumnaIzq=[   'srchPersona',
                    'btnBusquedaExhausticaPersona',
                    'btnBuscarPersona',
                    'staticText81',
                    'btnMostarTodasPersonas',
                    'MP0',
                    'MP1',
                    'MP2',
                    'MP3',
                    'MP4',
                    'listBoxPersonaBrowser',
                    'btnNuevaPersona',
                    'delPersona',
                    'btnRepsPersona',
                    'btnInfoPersona',
                    'staticText104',
                    'FPconfidencialidad'
                    ]
ctrlsColumnaDer={   'nombre':[1, 'CPNombre',
                    'FPNombre'],
                    'apellido':[2, 'CPApellido',
                    'FPApellido'],

                    'sexo':[3, 'CPSexo',
                    'FPSexo'],
                    'fechanac':[5, 'CPfechanac',
                    'FPTipodefecha',
                    'PFNdia',
                    'PFNmes',
                    'PFNanio'],
                    'pais':[9, 'CPPais',
                    'btnFPPais',
                    'btnRemoveFPPais',
                    'FPPais'],
                    'estado':[10, 'CPEstado',
                    'FPEstado'],
                    'municipio':[11,'CPMunicipio',
                    'FPMunicipio'],
                    
                    'ciudadania':[12, 'CPCiudadania',
                    'btnFPCiudadania',
                    'btnRemoveFPCiudadania',
                    'FPCiudadania'],
                    'escolaridad':[14, 'CPEscolaridad',
                    'FPEscolaridad'],
                    'personaActual':[-2,'staticPersonaActual0'],
                    #'guardar':['buttonPGuardar'],
                    #'tipopersona':['btnCambiaTipoPersona']
                }
                
ctrlsBajar = ['buttonPGuardar',
'btnCambiaTipoPersona',
'staticText87',
'listPersonaVinculosDB',
'staticText113',
'txtStatusC3P',
'chkRelevanteP',
'btnCopiarC3P',
'choiceGrupoP',
'staticText111',
'choiceContenedorP']
ctrlsColumnaDerExtra={ 'GpoIndigena':[13,'FGrupoIndigena','CGrupoIndigena'],
                       'DocID':[4,'CdocID','FdocID'],
                       'EdoCivil':[6,'FPEstadocivilX','CPEstadocivilX'],
                       'Direccion':[16,'FDireccion','CDireccion'],
                       'UOcupacion':[15,'CPUOcupacion','btnAddOcupacionX','Tocupacion'],
                       'Hijos':[7, 'FHijos','CHijos'],
                       'viajacon':[8,'Fviajacon','Cviajacon'],
                       'motivo':[18,'Fmotivo','Cmotivo'],
                       'telefono':[17,'Ftelefono','Ctelefono'],
                       'destino':[19,'Fdestino','Cdestino'],
                       'intentos':[20,'Fintentos','Cintentos'],
                       'expulsiones':[21,'Fexpulsiones','Cexpulsiones'],
                       'paisregion':[9,'CPaisRegion','FPaisRegion', 'FPais'],
                       'ciudregion':[12,'FCiudRegion', 'FCiud']
                       }
ctrlsQuitar= ['staticText110','FPOtroNombre', 'CPLocalidad', 'FPLocalidad',
               'btnFPPais','btnRemoveFPPais','FPPais',
               'btnFPCiudadania','btnRemoveFPCiudadania','FPCiudadania']    

def OnFPaisRegionChoice(self, event):
        ctrl = event.GetEventObject()
        i = ctrl.Selection
        padre  = ctrl.GetClientData(i)
        
        
        self.XLlenaCtrlMunicipios(self.FPais, padre)

def OnFCiudRegionChoice(self, event):
        
        ctrl = event.GetEventObject()
        i = ctrl.Selection
        padre  = ctrl.GetClientData(i)
        
        
        self.XLlenaCtrlMunicipios(self.FCiud, padre)


def OnFPaisChoice(self, event):

        ctrl = event.GetEventObject()
        i = ctrl.Selection
        pais  = ctrl.GetClientData(i)
        local = pais.descripcion == localCountry
        
        if local:
                self.XLlenaCtrlCategoria(self.FPEstado, u'T63')
        else:
                self.XLlenaCtrlCategoria(self.FPEstado, u'', id=pais.id)



def OnBtnAddOcupacionXButton(self, event):
        global POcupacion
        ocupacion = self.XgetTaxonomyTree(self, u"T10", u'Ocupaci\xf3n', help=u'getTaxonomyTreeOcupacion')
        
        if ocupacion:
             POcupacion = ocupacion
             
             self.Tocupacion.SetLabel(self.XTesNotNull(ocupacion))            

def panelPersonaMig(self):
    self.SetSize(wx.Size(1100, 760))
    for ctrlName in ctrlsColumnaIzq:
        ctrl=getattr(self, ctrlName)
        moduleUtils.moveCtrl(ctrl, dx=480)
        
    
    for ctrlLlave in ctrlsColumnaDer:    
    
       for ctrlName in ctrlsColumnaDer[ctrlLlave][1:]:
           ctrl=getattr(self, ctrlName)
           py = ctrlsColumnaDer[ctrlLlave][0]
           if py:
              y = 128 + (24 * (py - 1))
              moduleUtils.moveCtrl(ctrl, dx=-312, py=y)
           else:
              
              ctrl.Show(False)

    for ctrlName in ctrlsBajar:
        ctrl=getattr(self, ctrlName)
        moduleUtils.moveCtrl(ctrl, dy=5 * 24)

           
    for ctrlName in ctrlsQuitar:
        ctrl=getattr(self, ctrlName)
        ctrl.Show(False)
    moduleUtils.moveCtrl(self.listPersonaVinculosDB, px=520)
    moduleUtils.moveCtrl(self.staticText87, px=520)
    panel1 = self.NBPersonasGral
    
    #self.staticPersonaActual0.Reparent(panel1)
    
    [wxID_FRAME3CGRUPOINDIGENA, wxID_FRAME3CMOTIVODELVIAJE, 
 wxID_FRAME3FGRUPOINDIGENA, wxID_FRAME3FMOTIVODELVIAJE, wxID_FRAME3PANEL1, 
 wxID_FRAME3FdocID, wxID_FRAME3CdocID, wxID_FRAME3FPESTADOCIVILX, CPESTADOCIVIL,
 wxID_FRAME3CDireccion, wxID_FRAME3FDireccion,  wxID_FRAME3CPUOcupacion,
 wxID_FRAME3FHijos, wxID_FRAME3CHijos, BTNADDOCUPACIONX, wxID_FRAME3Tocupacion,
 wxID_FRAME3Cviajacon, wxID_FRAME3Fviajacon,
 wxID_FRAME3Fmotivo, wxID_FRAME3Cmotivo, wxID_FRAME3Cexpulsiones, wxID_FRAME3Fexpulsiones,
 wxID_FRAME3Ftelefono, wxID_FRAME3Ctelefono,
 wxID_FRAME3Fdestino, wxID_FRAME3Cdestino,
 wxID_FRAME3Fintentos, wxID_FRAME3Cintentos,
 wxID_FRAME3Fexpulsiones, wxID_FRAME3Cexpulsiones,
 wxID_FRAME3FPaisRegion, wxID_FRAME3CPaisRegion, wxID_FRAME3FPais,
 wxID_FRAME3FCiudRegion, wxID_FRAME3FCiud
 
 
] = [wx.NewId() for _init_ctrls in range(35)]
    
    self.FPEstadocivilX = wx.Choice(choices=[], id=wxID_FRAME3FPESTADOCIVILX,
              name='FPEstadocivilX', parent=panel1,
              pos=wx.Point(208, 288), size=wx.Size(208, 21), style=0)
              

    self.CPEstadocivilX = wx.StaticText(id=CPESTADOCIVIL,
              label='Estado civil', name='CPEstadocivilX',
              parent=panel1, pos=wx.Point(40, 288),
              size=wx.Size(112, 13), style=0)
 
    self.Fviajacon = wx.Choice(choices=[], id=wxID_FRAME3Fviajacon,
              name='Fviajacon', parent=panel1,
              pos=wx.Point(208, 288), size=wx.Size(208, 21), style=0)
              

    self.Cviajacon = wx.StaticText(id=wxID_FRAME3Cviajacon,
              label='Viaja Ud.', name='wxID_FRAME3Cviajacon',
              parent=panel1, pos=wx.Point(40, 288),
              size=wx.Size(112, 13), style=0)
              
    self.Fmotivo = wx.Choice(choices=[], id=wxID_FRAME3Fmotivo,
              name='Fmotivo', parent=panel1,
              pos=wx.Point(208, 288), size=wx.Size(208, 21), style=0)
              

    self.Cmotivo = wx.StaticText(id=wxID_FRAME3Cmotivo,
              label='Motivo', name='wxID_FRAME3Cmotivo',
              parent=panel1, pos=wx.Point(40, 288),
              size=wx.Size(112, 13), style=0)

    self.Fdestino = wx.Choice(choices=[], id=wxID_FRAME3Fdestino,
              name='Fdestino', parent=panel1,
              pos=wx.Point(208, 288), size=wx.Size(208, 21), style=0)
              

    self.Cdestino = wx.StaticText(id=wxID_FRAME3Cdestino,
              label='Destino', name='wxID_FRAME3Cdestino',
              parent=panel1, pos=wx.Point(40, 288),
              size=wx.Size(112, 13), style=0)

    self.CPUOcupacion = wx.StaticText(id=wxID_FRAME3CPUOcupacion,
              label='Ultima ocupacion', name='CPUOcupacion',
              parent=panel1, pos=wx.Point(40, 288),
              size=wx.Size(112, 13), style=0)


    self.FGrupoIndigena = wx.CheckBox(id=wxID_FRAME3FGRUPOINDIGENA,
              label='', name='FGrupoIndigena', parent=panel1,
              pos=wx.Point(208, 72), size=wx.Size(24, 13), style=0)
    self.FGrupoIndigena.SetValue(False)

    self.CGrupoIndigena = wx.StaticText(id=wxID_FRAME3CGRUPOINDIGENA,
              label='Grupo Indigena', name='CGrupoIndigena', parent=panel1,
              pos=wx.Point(40, 72), size=wx.Size(75, 13), style=0)
    self.CdocID = wx.StaticText(id=wxID_FRAME3CdocID,
              label='Documento de identificacion', name='CdocID', parent=panel1,
              pos=wx.Point(40, 72), size=wx.Size(100, 13), style=0)
    self.FdocID = wx.TextCtrl(id=wxID_FRAME3FdocID, name='FdocID',
              parent=panel1, pos=wx.Point(208, 128),
              size=wx.Size(208, 21), style=0, value='')
              
    self.CDireccion = wx.StaticText(id=wxID_FRAME3CDireccion,
              label='Direccion', name='CDireccion', parent=panel1,
              pos=wx.Point(40, 72), size=wx.Size(100, 13), style=0)
    self.FDireccion = wx.TextCtrl(id=wxID_FRAME3FDireccion, name='FDireccion',
              parent=panel1, pos=wx.Point(208, 128),
              size=wx.Size(208, 21), style=0, value='')
              
    self.Ctelefono = wx.StaticText(id=wxID_FRAME3Ctelefono,
              label='Telefono', name='Ctelefono', parent=panel1,
              pos=wx.Point(40, 72), size=wx.Size(100, 13), style=0)
    self.Ftelefono = wx.TextCtrl(id=wxID_FRAME3Ftelefono, name='Ftelefono',
              parent=panel1, pos=wx.Point(208, 128),
              size=wx.Size(208, 21), style=0, value='')




    self.CHijos = wx.StaticText(id=wxID_FRAME3CHijos,
              label='Hijos', name='CHijos', parent=panel1,
              pos=wx.Point(40, 72), size=wx.Size(100, 13), style=0)
              
              
    self.FHijos = wx.lib.intctrl.IntCtrl(allow_long=True,
              allow_none=True, default_color=wx.BLACK,
              id=wxID_FRAME3FHijos, limited=False, max=30L,
              min=0, name='FHijos', oob_color=wx.RED,
              parent=panel1, pos=wx.Point(208, 128),
              size=wx.Size(136, 21), style=0, value=0)

    self.Cintentos = wx.StaticText(id=wxID_FRAME3Cintentos,
              label='Intentos', name='Cintentos', parent=panel1,
              pos=wx.Point(40, 72), size=wx.Size(100, 13), style=0)
              
              
    self.Fintentos = wx.lib.intctrl.IntCtrl(allow_long=True,
              allow_none=True, default_color=wx.BLACK,
              id=wxID_FRAME3Fintentos, limited=False, max=100L,
              min=0, name='Fintentos', oob_color=wx.RED,
              parent=panel1, pos=wx.Point(208, 128),
              size=wx.Size(136, 21), style=0, value=0)

    self.Cexpulsiones = wx.StaticText(id=wxID_FRAME3Cexpulsiones,
              label='Expulsiones', name='Cexpulsiones', parent=panel1,
              pos=wx.Point(40, 72), size=wx.Size(100, 13), style=0)
              
              
    self.Fexpulsiones = wx.lib.intctrl.IntCtrl(allow_long=True,
              allow_none=True, default_color=wx.BLACK,
              id=wxID_FRAME3Fexpulsiones, limited=False, max=100L,
              min=0, name='Fexpulsiones', oob_color=wx.RED,
              parent=panel1, pos=wx.Point(208, 128),
              size=wx.Size(136, 21), style=0, value=0)
              
    self.FPaisRegion = wx.Choice(choices=[], id=wxID_FRAME3FPaisRegion,
              name='FPaisRegion', parent=panel1,
              pos=wx.Point(208, 288), size=wx.Size(120, 21), style=0)
              

    self.CPaisRegion = wx.StaticText(id=wxID_FRAME3CPaisRegion,
              label='Region', name='wxID_FRAME3CPaisRegion',
              parent=panel1, pos=wx.Point(40, 288),
              size=wx.Size(112, 13), style=0)
              
    self.FCiudRegion = wx.Choice(choices=[], id=wxID_FRAME3FCiudRegion,
              name='FCiudRegion', parent=panel1,
              pos=wx.Point(208, 288), size=wx.Size(120, 21), style=0)
              

    self.FCiud = wx.Choice(choices=[], id=wxID_FRAME3FCiud,
              name='FCiud', parent=panel1,
              pos=wx.Point(334, 288), size=wx.Size(140, 21), style=0)
    
              
              
    
    self.OnFPaisRegionChoice = new.instancemethod(OnFPaisRegionChoice, self, self.__class__) 
    self.OnFCiudRegionChoice = new.instancemethod(OnFCiudRegionChoice, self, self.__class__) 
    self.OnFPaisChoice = new.instancemethod(OnFPaisChoice, self, self.__class__) 
             
    self.FPaisRegion.Bind(wx.EVT_CHOICE, self.OnFPaisRegionChoice,
              id=wxID_FRAME3FPaisRegion)

    self.FCiudRegion.Bind(wx.EVT_CHOICE, self.OnFCiudRegionChoice,
              id=wxID_FRAME3FCiudRegion)

    
              
    self.FPais = wx.Choice(choices=[], id=wxID_FRAME3FPais,
              name='FPais', parent=panel1,
              pos=wx.Point(334, 288), size=wx.Size(140, 21), style=0)
              
    self.FPais.Bind(wx.EVT_CHOICE, self.OnFPaisChoice,
              id=wxID_FRAME3FPais)



              
    self.OnBtnAddOcupacionXButton = new.instancemethod(OnBtnAddOcupacionXButton, self, self.__class__)
    
    self.btnAddOcupacionX = wx.Button(id=BTNADDOCUPACIONX, label='+',
              name='btnAddOcupacionX', parent=panel1,
              pos=wx.Point(208, 152), size=wx.Size(24, 23), style=0)
    self.btnAddOcupacionX.Bind(wx.EVT_BUTTON, self.OnBtnAddOcupacionXButton,
              id=BTNADDOCUPACIONX)
    self.Tocupacion = wx.StaticText(id=wxID_FRAME3Tocupacion,
              label='                            ', name='Tocupacion', parent=panel1,
              pos=wx.Point(235, 100), size=wx.Size(100, 13), style=0)

    
        
        
    for ctrlLlave in ctrlsColumnaDerExtra: 
           for ctrlName in ctrlsColumnaDerExtra[ctrlLlave][1:]:
               ctrl=getattr(self, ctrlName)
               py = ctrlsColumnaDerExtra[ctrlLlave][0]
               y = 128 + (24 * (py - 1))
               moduleUtils.moveCtrl(ctrl, py=y)
    self.XLlenaCtrlCategoria(self.FPaisRegion   ,u"T15" )
    self.XLlenaCtrlCategoria(self.FCiudRegion   ,u"T15" )
    self.XLlenaCtrlCategoria(self.FPEstadocivilX   ,u"T08" )
    self.XLlenaCtrlCategoria(self.Fviajacon   ,u"T100" )
    self.XLlenaCtrlCategoria(self.Fdestino  ,u"T101" )
    self.XLlenaCtrlCategoria(self.Fmotivo   ,u"T102" )
    self.XLlenaCtrlCategoria(self.FPais   ,u"", id=11000 )
    panel1.Layout()
    self.Refresh()
               