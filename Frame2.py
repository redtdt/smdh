#-----------------------------------------------------------------------------
# Name:        Frame2.py
#
#
# RCS-ID:      $Id: Frame2.py $
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
#Boa:Frame:Frame2
 
# -*- coding: utf-8 -*-

#enie  \xf1
#a   \xe1
#e   \xe9
#i   \xed
#o   \xf3
#u   \xfa



import wx
import wx.lib.masked.textctrl
import wx.lib.intctrl
import wx.lib.flatnotebook
import traceback
from module2 import LlenaCtrlCategoria, LlenaCtrl, LlenaCtrlTipificacion, LlenaCtrl2, Caso, Acto, status, TesNode, LlenaTree, EventoTipificacion, LlenaPerpetradores, Fuente, Localidad, Publicacion
from module2 import Involucramiento, Intervencion, Persona, LlenaCtrl3, getChoiceValueId, CtrlSelect, getChoiceValue, setDateCtrl, setDateField
from module2 import setCheckBoxValue, getCheckBoxValue, Derechoviolado, MError, Borrar, LlenaCtrlChildren, tesDesc, Loginfo, UpdateLogInfo, Caracrelevantes, FlushInfo
from module2 import PersonaTipificacion, LlenaCtrlPersonaTipificacion, MyClientData, LlenaPersonas, ParentsPattern, LlenaCtrlCasos, TesNotNull, StrNotNull, Caso_vinculo, TesNamebyId, Mvs, DictReciproco, terminoReciproco, NoRegistros, DireccionesPersona
from module2 import cuentaEspacios, QueryTesNode, CanCreate, CanCreateCaso, ExistePersona, setDateCtrl2, MviMask, toIntegerDateField, setDateField2, validDate, ErrorSoloLectura, ExisteCaso, PutDesc
from module2 import LlenaAyuda, LlenaCtrlMunicipios, Grupo, LimpiaString
from DlgLocalidad import LocalidadMaint
from DlgDireccion import MaintDireccion
from DlgAltaActo import NuevoActo
from DlgAltaPersona import DatosAltaPersona
from FrameBusquedas import *
from DlgCaso import GetCaso
import module2
from moduleRep1 import printObj
from DlgInterv import DialogIntervencion
import Locldetalles
import webbrowser
import frameRep5
import screenconfig
from listacampos import camposEntidad, boxEntidad
import moduleCtrls
import  moduleFechas
import cnf

session = status.session


provider = wx.SimpleHelpProvider()
wx.HelpProvider_Set(provider)

#import Dialog1
import DlgVincular
from DLGTaxTree import getTaxonomyTree

from dlgpersona import PersonaDlg
from dlggetdescrip import MyDescrip
import re
from DlgLoginfo import DlgInfo

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2ACTUALIZARACTO, wxID_FRAME2ADDLOCALIZACION, 
 wxID_FRAME2AFFANIO, wxID_FRAME2AFFDIA, wxID_FRAME2AFFMES, wxID_FRAME2AFIANIO, 
 wxID_FRAME2AFIDIA, wxID_FRAME2AFIMES, wxID_FRAME2ALTACASO, 
 wxID_FRAME2BFFANIO, wxID_FRAME2BFFDIA, wxID_FRAME2BFFMES, wxID_FRAME2BFIANIO, 
 wxID_FRAME2BFIDIA, wxID_FRAME2BFIMES, wxID_FRAME2BFVANIO, wxID_FRAME2BFVDIA, 
 wxID_FRAME2BFVMES, wxID_FRAME2BTNABRIRLIGA, wxID_FRAME2BTNACTOINSTRINT, 
 wxID_FRAME2BTNACTOLEGISLACION, wxID_FRAME2BTNACTUALIZARCASO1, 
 wxID_FRAME2BTNADDDOC, wxID_FRAME2BTNADDDOCLENGUAINDIGENA, 
 wxID_FRAME2BTNADDFPTIPO, wxID_FRAME2BTNADDFTECONFIABILIDAD, 
 wxID_FRAME2BTNADDFTELENGUAINDIGENA, wxID_FRAME2BTNADDFTEPERSONAREL, 
 wxID_FRAME2BTNADDOCUPACION, wxID_FRAME2BTNADDPUBCONFIABILIDAD, 
 wxID_FRAME2BTNADDRELACION, wxID_FRAME2BTNAGREGARCARACRELEVANTES, 
 wxID_FRAME2BTNBUSCARPERSONA, wxID_FRAME2BTNBUSQUEDAEXHAUSTICAPERSONA, 
 wxID_FRAME2BTNCAMBIATIPOPERSONA, wxID_FRAME2BTNCASOREL, 
 wxID_FRAME2BTNCOPIARC3, wxID_FRAME2BTNCOPIARC3P, 
 wxID_FRAME2BTNDELDOCLENGUAINDIGENA, wxID_FRAME2BTNDELFPTIPO, 
 wxID_FRAME2BTNDELFTECONFIABILIDAD, wxID_FRAME2BTNDELFTELENGUAINDIGENA, 
 wxID_FRAME2BTNDELOCUPACION, wxID_FRAME2BTNDELPUBCONFIABILIDAD, 
 wxID_FRAME2BTNDPERSONAAQUIEN, wxID_FRAME2BTNDPERSONAFUENTE, 
 wxID_FRAME2BTNDPERSONAPARTEINT, wxID_FRAME2BTNDPERSONAPERPETRADOR, 
 wxID_FRAME2BTNDPERSONAREL, wxID_FRAME2BTNDPERSONAREL2, 
 wxID_FRAME2BTNDPERSONASOBRE, wxID_FRAME2BTNDPERSONAVICTIMA, 
 wxID_FRAME2BTNFPCIUDADANIA, wxID_FRAME2BTNFPPAIS, wxID_FRAME2BTNINFOACTO, 
 wxID_FRAME2BTNINFOBIO, wxID_FRAME2BTNINFOCASO, wxID_FRAME2BTNINFOCASOREL, 
 wxID_FRAME2BTNINFODOC, wxID_FRAME2BTNINFOFTE, wxID_FRAME2BTNINFOINTER, 
 wxID_FRAME2BTNINFOINTERV, wxID_FRAME2BTNINFOINVOL, wxID_FRAME2BTNINFOLEGIS, 
 wxID_FRAME2BTNINFOPERSONA, wxID_FRAME2BTNINTPINT, wxID_FRAME2BTNLOCMASINFO, 
 wxID_FRAME2BTNMOSTARTODASPERSONAS, wxID_FRAME2BTNNUEVAPERSONA, 
 wxID_FRAME2BTNPANTANTERIOR, wxID_FRAME2BTNPRELACIONADA, 
 wxID_FRAME2BTNPUBTIPOPUB, wxID_FRAME2BTNREMOVEFPCIUDADANIA, 
 wxID_FRAME2BTNREMOVEFPPAIS, wxID_FRAME2BTNREMOVEFTEPERSONAREL, 
 wxID_FRAME2BTNREMOVEPUBTIPOPUB, wxID_FRAME2BTNREPS, 
 wxID_FRAME2BTNREPSPERSONA, wxID_FRAME2BTNSAVEPUB, wxID_FRAME2BTNSAVEVINCULO, 
 wxID_FRAME2BTNSEARCH, wxID_FRAME2BTNSERACHEXECUTE, wxID_FRAME2BTNSHOWALL, 
 wxID_FRAME2BTNTIPODEACTO, wxID_FRAME2BTNTIPORELCASO, 
 wxID_FRAME2BTNTIPOVINCULO, wxID_FRAME2BUTTON2, 
 wxID_FRAME2BUTTONACTUALIZARCASO2, wxID_FRAME2BUTTONACTUALIZARCASO3, 
 wxID_FRAME2BUTTONACTUALIZARINVOL, wxID_FRAME2BUTTONADDINTERVENCION, 
 wxID_FRAME2BUTTONADDPERPETRADOR, wxID_FRAME2BUTTONAQUIEN, 
 wxID_FRAME2BUTTONCASODERECHOAFECTADO, wxID_FRAME2BUTTONDEQUIEN, 
 wxID_FRAME2BUTTONESTATUSDELAVICTIMA, wxID_FRAME2BUTTONFTEACTUALIZARDATOS, 
 wxID_FRAME2BUTTONFTECONEXIONINFORMACION, wxID_FRAME2BUTTONFTENUEVA, 
 wxID_FRAME2BUTTONINTERVENCIONACTUALIZAR, wxID_FRAME2BUTTONNUEVOACTO, 
 wxID_FRAME2BUTTONPGUARDAR, wxID_FRAME2BUTTONPUBADDPERSON, 
 wxID_FRAME2BUTTONPUBREMOVEPERSON, wxID_FRAME2BUTTONREMOVEAQUIEN, 
 wxID_FRAME2BUTTONREMOVEDEQUIEN, wxID_FRAME2BUTTONREMOVEESTATUSDELAVICTIMA, 
 wxID_FRAME2BUTTONREMOVEESTATUSVDH, wxID_FRAME2BUTTONREMOVEFTECONEXIONINF, 
 wxID_FRAME2BUTTONREMOVEGRADOINVOL, wxID_FRAME2BUTTONREMOVETIPODELUGAR, 
 wxID_FRAME2BUTTONREMOVETIPOPERP, wxID_FRAME2BUTTONREMOVEULTSTATUSPERP, 
 wxID_FRAME2BUTTONSELECTESTATUSVDH, wxID_FRAME2BUTTONSELECTIPODELUGAR, 
 wxID_FRAME2BUTTONSELGRADOINVOL, wxID_FRAME2BUTTONSELPERPETRADOR, 
 wxID_FRAME2BUTTONSELTIPOPERP, wxID_FRAME2BUTTONSELULTSTATUSPERP, 
 wxID_FRAME2BUTTONTIPOINTERVENCION, wxID_FRAME2BUTTONVINCULAR, 
 wxID_FRAME2CASOISEARCH, wxID_FRAME2CFFANIO, wxID_FRAME2CFFDIA, 
 wxID_FRAME2CFFMES, wxID_FRAME2CFIANIO, wxID_FRAME2CFIDIA, wxID_FRAME2CFIMES, 
 wxID_FRAME2CFRANIO, wxID_FRAME2CFRDIA, wxID_FRAME2CFRMES, 
 wxID_FRAME2CHECKBOXCASOCONFIDENCIALIDAD, 
 wxID_FRAME2CHECKBOXCASOEXPORTARRELACIONES, 
 wxID_FRAME2CHECKBOXFTECONFIDENCIALIDAD, wxID_FRAME2CHECKBOXINTEXPORTAR, 
 wxID_FRAME2CHECKBOXPUBEXPORTAR, wxID_FRAME2CHKRELEVANTE, 
 wxID_FRAME2CHKRELEVANTEP, wxID_FRAME2CHOICECONTENEDOR, 
 wxID_FRAME2CHOICECONTENEDORP, wxID_FRAME2CHOICEFTEIDIOMA, 
 wxID_FRAME2CHOICEFTETIPOFECHA, wxID_FRAME2CHOICEGRUPO, 
 wxID_FRAME2CHOICEGRUPOP, wxID_FRAME2CHOICEINTTIPOFECHA, 
 wxID_FRAME2CHOICEMONITOREO, wxID_FRAME2CHOICEPUBIDIOMA, 
 wxID_FRAME2CHOICEPUBTIPOFECHA, wxID_FRAME2CHOICEPUBTIPOFECHACONSULTA, 
 wxID_FRAME2CHOICETIPOEDAD, wxID_FRAME2CHOICETIPOFECHAFINAL, 
 wxID_FRAME2CHOICETIPOFECHAINICIAL, wxID_FRAME2CONTEXTHELPBUTTON1, 
 wxID_FRAME2CONTEXTHELPBUTTON10, wxID_FRAME2CONTEXTHELPBUTTON13, 
 wxID_FRAME2CONTEXTHELPBUTTON14, wxID_FRAME2CONTEXTHELPBUTTON15, 
 wxID_FRAME2CONTEXTHELPBUTTON16, wxID_FRAME2CONTEXTHELPBUTTON17, 
 wxID_FRAME2CONTEXTHELPBUTTON2, wxID_FRAME2CONTEXTHELPBUTTON3, 
 wxID_FRAME2CONTEXTHELPBUTTON4, wxID_FRAME2CONTEXTHELPBUTTON5, 
 wxID_FRAME2CONTEXTHELPBUTTON6, wxID_FRAME2CONTEXTHELPBUTTON7, 
 wxID_FRAME2CONTEXTHELPBUTTON8, wxID_FRAME2CONTEXTHELPBUTTON9, 
 wxID_FRAME2CPAPELLIDO, wxID_FRAME2CPARCHIVOS, wxID_FRAME2CPCIUDADANIA, 
 wxID_FRAME2CPDESCRIPCIONDELGRUPO, wxID_FRAME2CPESCOLARIDAD, 
 wxID_FRAME2CPESTADO, wxID_FRAME2CPESTADOCIVIL, wxID_FRAME2CPFECHANAC, 
 wxID_FRAME2CPHABLAYENTIENDEESPANOL, wxID_FRAME2CPIDIOMA, wxID_FRAME2CPLENGUA, 
 wxID_FRAME2CPLOCALIDAD, wxID_FRAME2CPMONITOREO, wxID_FRAME2CPMUNICIPIO, 
 wxID_FRAME2CPNODEPENDIENTES, wxID_FRAME2CPNOMBRE, wxID_FRAME2CPOBSERVACIONES, 
 wxID_FRAME2CPOCUPACION, wxID_FRAME2CPORIGENETNICO, wxID_FRAME2CPPAIS, 
 wxID_FRAME2CPRELIGION, wxID_FRAME2CPSEXO, wxID_FRAME2CPTIPO, 
 wxID_FRAME2CRGUARDAR, wxID_FRAME2DELACTO, wxID_FRAME2DELCARACREL, 
 wxID_FRAME2DELCASO, wxID_FRAME2DELDATOBIO, wxID_FRAME2DELDERECHO, 
 wxID_FRAME2DELDIRECCION, wxID_FRAME2DELFUENTEDOC, wxID_FRAME2DELFUENTEPER, 
 wxID_FRAME2DELIDIOMA, wxID_FRAME2DELINSTRINT, wxID_FRAME2DELINTERV, 
 wxID_FRAME2DELLEGISLACION, wxID_FRAME2DELLENGUA, wxID_FRAME2DELLOCALIZACION, 
 wxID_FRAME2DELORIGEN, wxID_FRAME2DELPERPETRATOR, wxID_FRAME2DELPERSONA, 
 wxID_FRAME2DELRELACION, wxID_FRAME2DELTEMA, wxID_FRAME2FACARACRELEVANTE, 
 wxID_FRAME2FACONFIDENCIALIDAD, wxID_FRAME2FAEDAD_VICTIMA, 
 wxID_FRAME2FAESTATUSVDH, wxID_FRAME2FAESTATUSVICTIMA, wxID_FRAME2FAEXPORTAR, 
 wxID_FRAME2FAINSTR, wxID_FRAME2FAINSTRUMENTOS_INT_NOTAS, wxID_FRAME2FALEGIS, 
 wxID_FRAME2FALEGISLACION_NACIONAL_NOTAS, wxID_FRAME2FALOCALIDAD, 
 wxID_FRAME2FAOBSERVACIONES, wxID_FRAME2FATIPOACTO, wxID_FRAME2FATIPODELUGAR, 
 wxID_FRAME2FATIPOFECHAFIN, wxID_FRAME2FATIPOFECHAINICIO, 
 wxID_FRAME2FAVICTIMA, wxID_FRAME2FBCOMENTARIOS, 
 wxID_FRAME2FBCONFIDENCIALIDAD, wxID_FRAME2FBDESCRIPCION, 
 wxID_FRAME2FBFECHAFINALTIPO, wxID_FRAME2FBFECHAINFO_VIGENTETIPO, 
 wxID_FRAME2FBFECHAINICIALTIPO, wxID_FRAME2FBOBSERVACIONES, 
 wxID_FRAME2FBPUESTO, wxID_FRAME2FBRANGO, wxID_FRAME2FCPROYECTO_CONJUNTO, 
 wxID_FRAME2FCPROYECTO_GRUPO, wxID_FRAME2FCPROYECTO_SE, 
 wxID_FRAME2FCTIPO_FRECEPCION, wxID_FRAME2FDFANIO, wxID_FRAME2FDFCANIO, 
 wxID_FRAME2FDFCDIA, wxID_FRAME2FDFCMES, wxID_FRAME2FDFDIA, wxID_FRAME2FDFMES, 
 wxID_FRAME2FICONFIDENCIALIDAD, wxID_FRAME2FIGRADOINVOLUCRAMIENTO, 
 wxID_FRAME2FIPERPETRADOR, wxID_FRAME2FITIPOPERPETRADOR, 
 wxID_FRAME2FIULTIMOSTATUSPERPETRADOR, wxID_FRAME2FPADDDIRECCIONES, 
 wxID_FRAME2FPADDIDIOMA, wxID_FRAME2FPADDLENGUA, wxID_FRAME2FPADDORIGENETNICO, 
 wxID_FRAME2FPAPELLIDO, wxID_FRAME2FPARCHIVOS, wxID_FRAME2FPCIUDADANIA, 
 wxID_FRAME2FPCOMENTARIOS, wxID_FRAME2FPCONFIDENCIALIDAD, 
 wxID_FRAME2FPDESCRIPCIONDELGRUPO, wxID_FRAME2FPDIRECCIONES, 
 wxID_FRAME2FPESCOLARIDAD, wxID_FRAME2FPESTADO, wxID_FRAME2FPESTADOCIVIL, 
 wxID_FRAME2FPFANIO, wxID_FRAME2FPFDIA, wxID_FRAME2FPFMES, 
 wxID_FRAME2FPHABLAYENTIENDEESPANOL, wxID_FRAME2FPIDIOMA, wxID_FRAME2FPLENGUA, 
 wxID_FRAME2FPLOCALIDAD, wxID_FRAME2FPMONITOREO, wxID_FRAME2FPMUNICIPIO, 
 wxID_FRAME2FPNODEPENDIENTES, wxID_FRAME2FPNOMBRE, wxID_FRAME2FPOBSERVACIONES, 
 wxID_FRAME2FPORIGENETNICO, wxID_FRAME2FPOTRONOMBRE, wxID_FRAME2FPPAIS, 
 wxID_FRAME2FPPROYECTO_CONJUNTO, wxID_FRAME2FPPROYECTO_GRUPO, 
 wxID_FRAME2FPPROYECTO_SE, wxID_FRAME2FPRELIGION, wxID_FRAME2FPSEXO, 
 wxID_FRAME2FPSTROCUPACION, wxID_FRAME2FPTIPODEFECHA, 
 wxID_FRAME2FPTIPODEFECHARECEPCION, wxID_FRAME2FRCCASOREL, 
 wxID_FRAME2FRCCASORELCOMENTARIOS, wxID_FRAME2FRCCASORELOBSERVACIONES, 
 wxID_FRAME2FRCCASORELTIPO, wxID_FRAME2GUARDARNORMATIVIDAD, wxID_FRAME2IFANIO, 
 wxID_FRAME2IFDIA, wxID_FRAME2IFMES, wxID_FRAME2LA1, wxID_FRAME2LA14, 
 wxID_FRAME2LA2, wxID_FRAME2LC1, wxID_FRAME2LC12, wxID_FRAME2LC14, 
 wxID_FRAME2LC15, wxID_FRAME2LC2, wxID_FRAME2LC3, wxID_FRAME2LC4, 
 wxID_FRAME2LC5, wxID_FRAME2LC6, wxID_FRAME2LC7, wxID_FRAME2LC9, 
 wxID_FRAME2LISTACASOS, wxID_FRAME2LISTACTOS, 
 wxID_FRAME2LISTBOXACTOPERPETRADORES, wxID_FRAME2LISTBOXCASOREL, 
 wxID_FRAME2LISTBOXDERECHOSAFECTADOS, wxID_FRAME2LISTBOXDOCS, 
 wxID_FRAME2LISTBOXFTE, wxID_FRAME2LISTBOXINTERVENCIONES, 
 wxID_FRAME2LISTBOXPERPETRADORES, wxID_FRAME2LISTBOXPERSONABROWSER, 
 wxID_FRAME2LISTBOXTEMAS, wxID_FRAME2LISTBOXVINCULOS, 
 wxID_FRAME2LISTLOCALIZACION, wxID_FRAME2LISTPERSONAVINCULOSDB, 
 wxID_FRAME2LONGCOMRELCASOS, wxID_FRAME2LONGOBSRELCASOS, 
 wxID_FRAME2LONGPERARCH, wxID_FRAME2LONGPERCOM, wxID_FRAME2LONGPERDBCOM, 
 wxID_FRAME2LONGPERDBOBS, wxID_FRAME2LONGPEROBS, wxID_FRAME2MP0, 
 wxID_FRAME2MP1, wxID_FRAME2MP2, wxID_FRAME2MP3, wxID_FRAME2MP4, 
 wxID_FRAME2NBACTOS, wxID_FRAME2NBACTOSGRAL, wxID_FRAME2NBACTOSPERP, 
 wxID_FRAME2NBCASOS, wxID_FRAME2NBCASOSADM, wxID_FRAME2NBCASOSGRAL, 
 wxID_FRAME2NBCASOSNARRATIVA, wxID_FRAME2NBCASOSRELACIONES, 
 wxID_FRAME2NBCASOSTIPIFICA, wxID_FRAME2NBFUENTEDOCUMENTAL, 
 wxID_FRAME2NBFUENTEPERSONAL, wxID_FRAME2NBFUENTES, 
 wxID_FRAME2NBINTERVENCIONES, wxID_FRAME2NBMAIN, wxID_FRAME2NBNORMATIVIDAD, 
 wxID_FRAME2NBPERSONAS, wxID_FRAME2NBPERSONASADM, wxID_FRAME2NBPERSONASBIO, 
 wxID_FRAME2NBPERSONASDETALLES, wxID_FRAME2NBPERSONASGRAL, 
 wxID_FRAME2PANTANTERIOR, wxID_FRAME2PFNANIO, wxID_FRAME2PFNDIA, 
 wxID_FRAME2PFNMES, wxID_FRAME2PFRANIO, wxID_FRAME2PFRDIA, wxID_FRAME2PFRMES, 
 wxID_FRAME2PGUARDAR2, wxID_FRAME2PGUARDAR3, wxID_FRAME2SRCHPERSONA, 
 wxID_FRAME2STATICCONTENEDOR, wxID_FRAME2STATICDOCLENGUAINDIGENA, 
 wxID_FRAME2STATICFPTIPO, wxID_FRAME2STATICFTECONFIABILIDAD, 
 wxID_FRAME2STATICFTELENGUAINDIGENA, wxID_FRAME2STATICGRUPO, 
 wxID_FRAME2STATICLINE1, wxID_FRAME2STATICLINE2, wxID_FRAME2STATICLINE3, 
 wxID_FRAME2STATICPERSONAACTUAL0, wxID_FRAME2STATICPERSONAACTUAL1, 
 wxID_FRAME2STATICPERSONAACTUAL2, wxID_FRAME2STATICPERSONAACTUAL3, 
 wxID_FRAME2STATICPUBCONFIABILIDAD, wxID_FRAME2STATICTEXT1, 
 wxID_FRAME2STATICTEXT10, wxID_FRAME2STATICTEXT100, wxID_FRAME2STATICTEXT101, 
 wxID_FRAME2STATICTEXT102, wxID_FRAME2STATICTEXT103, wxID_FRAME2STATICTEXT104, 
 wxID_FRAME2STATICTEXT105, wxID_FRAME2STATICTEXT106, wxID_FRAME2STATICTEXT107, 
 wxID_FRAME2STATICTEXT108, wxID_FRAME2STATICTEXT109, wxID_FRAME2STATICTEXT11, 
 wxID_FRAME2STATICTEXT110, wxID_FRAME2STATICTEXT111, wxID_FRAME2STATICTEXT112, 
 wxID_FRAME2STATICTEXT113, wxID_FRAME2STATICTEXT12, wxID_FRAME2STATICTEXT13, 
 wxID_FRAME2STATICTEXT14, wxID_FRAME2STATICTEXT15, wxID_FRAME2STATICTEXT16, 
 wxID_FRAME2STATICTEXT17, wxID_FRAME2STATICTEXT18, wxID_FRAME2STATICTEXT19, 
 wxID_FRAME2STATICTEXT2, wxID_FRAME2STATICTEXT20, wxID_FRAME2STATICTEXT21, 
 wxID_FRAME2STATICTEXT22, wxID_FRAME2STATICTEXT23, wxID_FRAME2STATICTEXT24, 
 wxID_FRAME2STATICTEXT25, wxID_FRAME2STATICTEXT26, wxID_FRAME2STATICTEXT27, 
 wxID_FRAME2STATICTEXT28, wxID_FRAME2STATICTEXT29, wxID_FRAME2STATICTEXT3, 
 wxID_FRAME2STATICTEXT30, wxID_FRAME2STATICTEXT31, wxID_FRAME2STATICTEXT32, 
 wxID_FRAME2STATICTEXT33, wxID_FRAME2STATICTEXT34, wxID_FRAME2STATICTEXT35, 
 wxID_FRAME2STATICTEXT36, wxID_FRAME2STATICTEXT37, wxID_FRAME2STATICTEXT38, 
 wxID_FRAME2STATICTEXT39, wxID_FRAME2STATICTEXT4, wxID_FRAME2STATICTEXT40, 
 wxID_FRAME2STATICTEXT41, wxID_FRAME2STATICTEXT42, wxID_FRAME2STATICTEXT43, 
 wxID_FRAME2STATICTEXT44, wxID_FRAME2STATICTEXT45, wxID_FRAME2STATICTEXT46, 
 wxID_FRAME2STATICTEXT47, wxID_FRAME2STATICTEXT48, wxID_FRAME2STATICTEXT49, 
 wxID_FRAME2STATICTEXT5, wxID_FRAME2STATICTEXT50, wxID_FRAME2STATICTEXT51, 
 wxID_FRAME2STATICTEXT52, wxID_FRAME2STATICTEXT53, wxID_FRAME2STATICTEXT54, 
 wxID_FRAME2STATICTEXT55, wxID_FRAME2STATICTEXT56, wxID_FRAME2STATICTEXT57, 
 wxID_FRAME2STATICTEXT58, wxID_FRAME2STATICTEXT59, wxID_FRAME2STATICTEXT6, 
 wxID_FRAME2STATICTEXT60, wxID_FRAME2STATICTEXT61, wxID_FRAME2STATICTEXT62, 
 wxID_FRAME2STATICTEXT63, wxID_FRAME2STATICTEXT64, wxID_FRAME2STATICTEXT65, 
 wxID_FRAME2STATICTEXT66, wxID_FRAME2STATICTEXT67, wxID_FRAME2STATICTEXT68, 
 wxID_FRAME2STATICTEXT69, wxID_FRAME2STATICTEXT7, wxID_FRAME2STATICTEXT70, 
 wxID_FRAME2STATICTEXT71, wxID_FRAME2STATICTEXT72, wxID_FRAME2STATICTEXT73, 
 wxID_FRAME2STATICTEXT74, wxID_FRAME2STATICTEXT75, wxID_FRAME2STATICTEXT76, 
 wxID_FRAME2STATICTEXT77, wxID_FRAME2STATICTEXT78, wxID_FRAME2STATICTEXT79, 
 wxID_FRAME2STATICTEXT8, wxID_FRAME2STATICTEXT80, wxID_FRAME2STATICTEXT81, 
 wxID_FRAME2STATICTEXT82, wxID_FRAME2STATICTEXT83, wxID_FRAME2STATICTEXT84, 
 wxID_FRAME2STATICTEXT85, wxID_FRAME2STATICTEXT86, wxID_FRAME2STATICTEXT87, 
 wxID_FRAME2STATICTEXT88, wxID_FRAME2STATICTEXT89, wxID_FRAME2STATICTEXT9, 
 wxID_FRAME2STATICTEXT90, wxID_FRAME2STATICTEXT91, wxID_FRAME2STATICTEXT92, 
 wxID_FRAME2STATICTEXT93, wxID_FRAME2STATICTEXT94, wxID_FRAME2STATICTEXT95, 
 wxID_FRAME2STATICTEXT96, wxID_FRAME2STATICTEXT97, wxID_FRAME2STATICTEXT98, 
 wxID_FRAME2STATICTEXT99, wxID_FRAME2STATICTEXTCONEXIONINFO, 
 wxID_FRAME2STATICTEXTEDADOCURREACTO, wxID_FRAME2STATICTEXTFTEPERSONA, 
 wxID_FRAME2STATICTEXTPUBPERSONA, wxID_FRAME2STATICTEXTRELPERSONA, 
 wxID_FRAME2STATICTXTPRELACIONADA, wxID_FRAME2STATICTXTTIPODERELACION, 
 wxID_FRAME2STATIXTEXT50, wxID_FRAME2TEXTCTRLCAARCHIVOS, 
 wxID_FRAME2TEXTCTRLCACOMENTARIOS, wxID_FRAME2TEXTCTRLDESCRIPCIONNARRATIVA, 
 wxID_FRAME2TEXTCTRLFTECOMENTARIOS, wxID_FRAME2TEXTCTRLFTEOBSERVACIONES, 
 wxID_FRAME2TEXTCTRLINOBSERVACIONES, wxID_FRAME2TEXTCTRLNOPERSONASAFECTADAS, 
 wxID_FRAME2TEXTCTRLOBSERVACIONES, wxID_FRAME2TEXTCTRLPUBCOMENTARIOS, 
 wxID_FRAME2TEXTCTRLPUBDATOS, wxID_FRAME2TEXTCTRLPUBLIGASITIO, 
 wxID_FRAME2TEXTCTRLPUBNOMBRESITIO, wxID_FRAME2TEXTCTRLPUBOBSERVACIONES, 
 wxID_FRAME2TEXTCTRLPUBTITULOPARTE, wxID_FRAME2TEXTCTRLRESUMEN, 
 wxID_FRAME2TEXTDESCRIPCION, wxID_FRAME2TXTCASOSSELECCIONADOS, 
 wxID_FRAME2TXTINTCOMENTARIOS, wxID_FRAME2TXTINTIMPACTO, 
 wxID_FRAME2TXTINTOBSERVACIONES, wxID_FRAME2TXTINTPARTE, 
 wxID_FRAME2TXTINTRESPUESTA, wxID_FRAME2TXTLONGADMARCH, 
 wxID_FRAME2TXTLONGADMCOMENT, wxID_FRAME2TXTLONGFAOBS, 
 wxID_FRAME2TXTLONGFDCOMENT, wxID_FRAME2TXTLONGFDDATOS, 
 wxID_FRAME2TXTLONGFDOBS, wxID_FRAME2TXTLONGFPCOMENT, wxID_FRAME2TXTLONGFPOBS, 
 wxID_FRAME2TXTLONGINOBS, wxID_FRAME2TXTLONGINTCOMENT, 
 wxID_FRAME2TXTLONGINTIMP, wxID_FRAME2TXTLONGINTOBS, wxID_FRAME2TXTLONGINTRES, 
 wxID_FRAME2TXTLONGNARRA, wxID_FRAME2TXTLONGNORINS, wxID_FRAME2TXTLONGNORLEG, 
 wxID_FRAME2TXTLONGOBS, wxID_FRAME2TXTLONGRESDESC, wxID_FRAME2TXTPRELACIONADA, 
 wxID_FRAME2TXTPUBTIPOPUB, wxID_FRAME2TXTSTATUSC3, wxID_FRAME2TXTSTATUSC3P, 
 wxID_FRAME2TXTTIPOVINCULO, wxID_FRAME2TXTTOTALCASOS, 
 wxID_FRAME2TXTTOTALPERSONAS, wxID_FRAME2TXTTOTALPERSONASSELECCIONADAS, 
] = [wx.NewId() for _init_ctrls in range(550)]

class Frame2(wx.Frame):
    def _init_coll_NBPersonas_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.NBPersonasGral, select=False,
              text='Datos generales')
        parent.AddPage(imageId=-1, page=self.NBPersonasDetalles, select=False,
              text='Detalles')
        parent.AddPage(imageId=-1, page=self.NBPersonasAdm, select=False,
              text='Informaci\xf3n administrativa')
        parent.AddPage(imageId=-1, page=self.NBPersonasBio, select=True,
              text='Datos biogr\xe1ficos')

    def _init_coll_NBCasos_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.NBCasosGral, select=True,
              text='Datos generales')
        parent.AddPage(imageId=-1, page=self.NBCasosNarrativa, select=False,
              text='Informaci\xf3n narrativa')
        parent.AddPage(imageId=-1, page=self.NBCasosAdm, select=False,
              text='Informaci\xf3n administrativa')
        parent.AddPage(imageId=-1, page=self.NBCasosTipifica, select=False,
              text='Tipificaciones')
        parent.AddPage(imageId=-1, page=self.NBCasosRelaciones, select=False,
              text='Relaciones')

    def _init_coll_NBActos_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.NBActosGral, select=True,
              text='Informaci\xf3n general')
        parent.AddPage(imageId=-1, page=self.NBActosPerp, select=False,
              text='Perpetradores')
        parent.AddPage(imageId=-1, page=self.NBNormatividad, select=False,
              text='Normatividad')

    def _init_coll_NBFuentes_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.NBFuentePersonal, select=True,
              text='Fuente personal')
        parent.AddPage(imageId=-1, page=self.NBFuenteDocumental, select=False,
              text='Fuente documental')

    def _init_coll_NBMain_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.NBCasos, select=True, text='Casos')
        parent.AddPage(imageId=-1, page=self.NBActos, select=False,
              text='Actos')
        parent.AddPage(imageId=-1, page=self.NBIntervenciones, select=False,
              text='Intervenciones')
        parent.AddPage(imageId=-1, page=self.NBFuentes, select=False,
              text='Fuentes')
        parent.AddPage(imageId=-1, page=self.NBPersonas, select=False,
              text='Personas')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(318, 56), size=wx.Size(860, 655),
              style=wx.DEFAULT_FRAME_STYLE, title='Manejo de Casos')
        self.SetClientSize(wx.Size(844, 619))
        self.SetBackgroundColour(wx.Colour(243, 220, 139))
        self.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'Tahoma'))
        self.Bind(wx.EVT_CLOSE, self.OnFrame2Close)
        self.Bind(wx.EVT_PAINT, self.OnFrame2Paint)

        self.NBMain = wx.lib.flatnotebook.FlatNotebook(id=wxID_FRAME2NBMAIN,
              name='NBMain', parent=self, pos=wx.Point(0, 0), size=wx.Size(844,
              619), style=0)
        self.NBMain.Enable(True)
        self.NBMain.SetLabel('panel')
        self.NBMain.SetBackgroundColour(wx.Colour(243, 220, 139))
        self.NBMain.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING,
              self.OnNBMainNotebookPageChanging, id=wxID_FRAME2NBMAIN)
        self.NBMain.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED,
              self.OnNBMainNotebookPageChanged, id=wxID_FRAME2NBMAIN)

        self.NBIntervenciones = wx.Panel(id=wxID_FRAME2NBINTERVENCIONES,
              name='NBIntervenciones', parent=self.NBMain, pos=wx.Point(0, 0),
              size=wx.Size(844, 593), style=wx.TAB_TRAVERSAL)
        self.NBIntervenciones.Enable(True)

        self.buttonAddIntervencion = wx.Button(id=wxID_FRAME2BUTTONADDINTERVENCION,
              label='Agregar una \nintervenci\xf3n',
              name='buttonAddIntervencion', parent=self.NBIntervenciones,
              pos=wx.Point(7, 320), size=wx.Size(81, 40), style=0)
        self.buttonAddIntervencion.Bind(wx.EVT_BUTTON,
              self.OnButtonIntervencionADD,
              id=wxID_FRAME2BUTTONADDINTERVENCION)

        self.staticText11 = wx.StaticText(id=wxID_FRAME2STATICTEXT11,
              label='Intervenciones', name='staticText11',
              parent=self.NBIntervenciones, pos=wx.Point(48, 40),
              size=wx.Size(73, 13), style=0)

        self.listBoxIntervenciones = wx.ListBox(choices=[],
              id=wxID_FRAME2LISTBOXINTERVENCIONES, name='listBoxIntervenciones',
              parent=self.NBIntervenciones, pos=wx.Point(8, 64),
              size=wx.Size(192, 248), style=wx.HSCROLL)
        self.listBoxIntervenciones.Bind(wx.EVT_LISTBOX,
              self.OnListBoxIntervencionesListbox,
              id=wxID_FRAME2LISTBOXINTERVENCIONES)
        self.listBoxIntervenciones.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnListBoxIntervencionesDclick,
              id=wxID_FRAME2LISTBOXINTERVENCIONES)
        self.listBoxIntervenciones.Bind(wx.EVT_KEY_DOWN,
              self.OnListBoxIntervencionesKeyDown)

        self.staticText16 = wx.StaticText(id=wxID_FRAME2STATICTEXT16,
              label='Tipo de intervenci\xf3n', name='staticText16',
              parent=self.NBIntervenciones, pos=wx.Point(208, 69),
              size=wx.Size(120, 13), style=0)

        self.buttonTipoIntervencion = wx.Button(id=wxID_FRAME2BUTTONTIPOINTERVENCION,
              label='+', name='buttonTipoIntervencion',
              parent=self.NBIntervenciones, pos=wx.Point(352, 61),
              size=wx.Size(24, 23), style=0)
        self.buttonTipoIntervencion.Bind(wx.EVT_BUTTON,
              self.OnSelectTipoIntervencion,
              id=wxID_FRAME2BUTTONTIPOINTERVENCION)

        self.buttonAQuien = wx.Button(id=wxID_FRAME2BUTTONAQUIEN, label='+',
              name='buttonAQuien', parent=self.NBIntervenciones,
              pos=wx.Point(352, 201), size=wx.Size(24, 23), style=0)
        self.buttonAQuien.Bind(wx.EVT_BUTTON, self.selectIntervAQuien,
              id=wxID_FRAME2BUTTONAQUIEN)

        self.staticText18 = wx.StaticText(id=wxID_FRAME2STATICTEXT18, label='',
              name='staticText18', parent=self.NBIntervenciones,
              pos=wx.Point(424, 69), size=wx.Size(320, 13), style=0)

        self.staticText19 = wx.StaticText(id=wxID_FRAME2STATICTEXT19,
              label='_____________________________________________________________',
              name='staticText19', parent=self.NBIntervenciones,
              pos=wx.Point(440, 201), size=wx.Size(352, 28),
              style=wx.ST_NO_AUTORESIZE)

        self.staticText9 = wx.StaticText(id=wxID_FRAME2STATICTEXT9,
              label='A qui\xe9n se le dirigi\xf3 esta intervenci\xf3n',
              name='staticText9', parent=self.NBIntervenciones,
              pos=wx.Point(208, 200), size=wx.Size(136, 24), style=0)

        self.buttonIntervencionActualizar = wx.Button(id=wxID_FRAME2BUTTONINTERVENCIONACTUALIZAR,
              label='Guardar', name='buttonIntervencionActualizar',
              parent=self.NBIntervenciones, pos=wx.Point(520, 480),
              size=wx.Size(75, 23), style=0)
        self.buttonIntervencionActualizar.Bind(wx.EVT_BUTTON,
              self.OnButtonIntervencionActualizar,
              id=wxID_FRAME2BUTTONINTERVENCIONACTUALIZAR)

        self.staticText21 = wx.StaticText(id=wxID_FRAME2STATICTEXT21,
              label='Sobre qui\xe9n se interviene', name='staticText21',
              parent=self.NBIntervenciones, pos=wx.Point(208, 176),
              size=wx.Size(136, 24), style=0)

        self.buttonDeQuien = wx.Button(id=wxID_FRAME2BUTTONDEQUIEN, label='+',
              name='buttonDeQuien', parent=self.NBIntervenciones,
              pos=wx.Point(352, 176), size=wx.Size(24, 23), style=0)
        self.buttonDeQuien.Bind(wx.EVT_BUTTON, self.selectIntervDeQuien,
              id=wxID_FRAME2BUTTONDEQUIEN)

        self.staticText17 = wx.StaticText(id=wxID_FRAME2STATICTEXT17, label='',
              name='staticText17', parent=self.NBIntervenciones,
              pos=wx.Point(440, 176), size=wx.Size(352, 24),
              style=wx.ST_NO_AUTORESIZE)

        self.LC5 = wx.StaticText(id=wxID_FRAME2LC5, label='Caso:', name='LC5',
              parent=self.NBIntervenciones, pos=wx.Point(16, 8),
              size=wx.Size(600, 13), style=0)
        self.LC5.SetToolTipString('Caso actual')

        self.btnInfoInterv = wx.Button(id=wxID_FRAME2BTNINFOINTERV, label='I',
              name='btnInfoInterv', parent=self.NBIntervenciones,
              pos=wx.Point(176, 320), size=wx.Size(24, 23), style=0)
        self.btnInfoInterv.Bind(wx.EVT_BUTTON, self.OnBtnInfoInterv,
              id=wxID_FRAME2BTNINFOINTERV)

        self.NBCasos = wx.lib.flatnotebook.FlatNotebook(id=wxID_FRAME2NBCASOS,
              name='NBCasos', parent=self.NBMain, pos=wx.Point(0, 0),
              size=wx.Size(844, 593), style=0)
        self.NBCasos.Bind(wx.lib.flatnotebook.EVT_FLATNOTEBOOK_PAGE_CHANGED,
              self.OnNBCasosFlatnotebookPageChanged, id=wxID_FRAME2NBCASOS)

        self.NBCasosGral = wx.Panel(id=wxID_FRAME2NBCASOSGRAL,
              name='NBCasosGral', parent=self.NBCasos, pos=wx.Point(0, 0),
              size=wx.Size(844, 567), style=wx.TAB_TRAVERSAL)
        self.NBCasosGral.SetBackgroundColour(wx.Colour(243, 220, 139))
        self.NBCasosGral.Show(False)

        self.NBCasosTipifica = wx.Panel(id=wxID_FRAME2NBCASOSTIPIFICA,
              name='NBCasosTipifica', parent=self.NBCasos, pos=wx.Point(0, 0),
              size=wx.Size(844, 567), style=wx.TAB_TRAVERSAL)

        self.staticText3 = wx.StaticText(id=wxID_FRAME2STATICTEXT3,
              label='Nombre del caso', name='staticText3',
              parent=self.NBCasosGral, pos=wx.Point(344, 120), size=wx.Size(79,
              13), style=0)

        self.textDescripcion = wx.TextCtrl(id=wxID_FRAME2TEXTDESCRIPCION,
              name='textDescripcion', parent=self.NBCasosGral, pos=wx.Point(432,
              112), size=wx.Size(360, 21), style=0, value='')
        self.textDescripcion.SetMaxLength(200)

        self.AltaCaso = wx.Button(id=wxID_FRAME2ALTACASO, label='Nuevo caso',
              name='AltaCaso', parent=self.NBCasosGral, pos=wx.Point(16, 280),
              size=wx.Size(80, 23), style=0)
        self.AltaCaso.SetToolTipString('Alta de caso')
        self.AltaCaso.Bind(wx.EVT_BUTTON, self.OnAltaCaso,
              id=wxID_FRAME2ALTACASO)

        self.listaCasos = wx.ListBox(choices=[], id=wxID_FRAME2LISTACASOS,
              name='listaCasos', parent=self.NBCasosGral, pos=wx.Point(16, 120),
              size=wx.Size(312, 152), style=wx.HSCROLL)
        self.listaCasos.SetLabel('')
        self.listaCasos.SetStringSelection('?')
        self.listaCasos.SetToolTipString('Lista de casos')
        self.listaCasos.SetAutoLayout(True)
        self.listaCasos.Bind(wx.EVT_LISTBOX_DCLICK, self.OnListaCasosDclick,
              id=wxID_FRAME2LISTACASOS)

        self.btnActualizarCaso1 = wx.Button(id=wxID_FRAME2BTNACTUALIZARCASO1,
              label='Guardar', name='btnActualizarCaso1',
              parent=self.NBCasosGral, pos=wx.Point(376, 440), size=wx.Size(75,
              23), style=0)
        self.btnActualizarCaso1.Bind(wx.EVT_BUTTON,
              self.OnBtnActualizarCaso1Button,
              id=wxID_FRAME2BTNACTUALIZARCASO1)

        self.staticText29 = wx.StaticText(id=wxID_FRAME2STATICTEXT29,
              label='Exportar caso', name='staticText29',
              parent=self.NBCasosGral, pos=wx.Point(16, 440), size=wx.Size(67,
              13), style=0)

        self.staticText30 = wx.StaticText(id=wxID_FRAME2STATICTEXT30,
              label='Fecha inicial', name='staticText30',
              parent=self.NBCasosGral, pos=wx.Point(344, 176), size=wx.Size(80,
              13), style=0)

        self.staticText31 = wx.StaticText(id=wxID_FRAME2STATICTEXT31,
              label='Fecha final', name='staticText31', parent=self.NBCasosGral,
              pos=wx.Point(344, 200), size=wx.Size(80, 16), style=0)

        self.choiceTipoFechaInicial = wx.Choice(choices=[],
              id=wxID_FRAME2CHOICETIPOFECHAINICIAL,
              name='choiceTipoFechaInicial', parent=self.NBCasosGral,
              pos=wx.Point(432, 168), size=wx.Size(208, 21), style=0)
        self.choiceTipoFechaInicial.Bind(wx.EVT_CHOICE,
              self.OnChoiceTipoFechaInicialChoice,
              id=wxID_FRAME2CHOICETIPOFECHAINICIAL)

        self.choiceTipoFechaFinal = wx.Choice(choices=[],
              id=wxID_FRAME2CHOICETIPOFECHAFINAL, name='choiceTipoFechaFinal',
              parent=self.NBCasosGral, pos=wx.Point(432, 192), size=wx.Size(208,
              21), style=0)
        self.choiceTipoFechaFinal.Bind(wx.EVT_CHOICE,
              self.OnChoiceTipoFechaFinal, id=wxID_FRAME2CHOICETIPOFECHAFINAL)

        self.staticText32 = wx.StaticText(id=wxID_FRAME2STATICTEXT32,
              label='No. de personas afectadas', name='staticText32',
              parent=self.NBCasosGral, pos=wx.Point(16, 421), size=wx.Size(130,
              13), style=0)

        self.checkBoxCasoConfidencialidad = wx.CheckBox(id=wxID_FRAME2CHECKBOXCASOCONFIDENCIALIDAD,
              label='', name='checkBoxCasoConfidencialidad',
              parent=self.NBCasosGral, pos=wx.Point(128, 440), size=wx.Size(24,
              13), style=0)
        self.checkBoxCasoConfidencialidad.SetValue(True)
        self.checkBoxCasoConfidencialidad.Bind(wx.EVT_CHECKBOX,
              self.OnCheckBoxCasoConfidencialidadCheckbox,
              id=wxID_FRAME2CHECKBOXCASOCONFIDENCIALIDAD)

        self.LC1 = wx.StaticText(id=wxID_FRAME2LC1, label='Caso:', name='LC1',
              parent=self.NBCasosGral, pos=wx.Point(16, 8), size=wx.Size(30,
              13), style=0)
        self.LC1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))
        self.LC1.SetToolTipString('Caso actual')

        self.listLocalizacion = wx.ListBox(choices=[],
              id=wxID_FRAME2LISTLOCALIZACION, name='listLocalizacion',
              parent=self.NBCasosGral, pos=wx.Point(16, 320), size=wx.Size(696,
              63), style=wx.LB_HSCROLL)
        self.listLocalizacion.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Fixedsys'))
        self.listLocalizacion.SetLabel('')
        self.listLocalizacion.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnListLocalizacionDclick, id=wxID_FRAME2LISTLOCALIZACION)
        self.listLocalizacion.Bind(wx.EVT_LISTBOX,
              self.OnListLocalizacionListbox, id=wxID_FRAME2LISTLOCALIZACION)

        self.staticText2 = wx.StaticText(id=wxID_FRAME2STATICTEXT2,
              label='Localizaci\xf3n', name='staticText2',
              parent=self.NBCasosGral, pos=wx.Point(384, 304), size=wx.Size(80,
              13), style=0)

        self.AddLocalizacion = wx.Button(id=wxID_FRAME2ADDLOCALIZACION,
              label='Nueva localizaci\xf3n', name='AddLocalizacion',
              parent=self.NBCasosGral, pos=wx.Point(248, 384), size=wx.Size(128,
              23), style=0)
        self.AddLocalizacion.Bind(wx.EVT_BUTTON, self.OnAddLocalizacionButton,
              id=wxID_FRAME2ADDLOCALIZACION)

        self.textCtrlNoPersonasAfectadas = wx.TextCtrl(id=wxID_FRAME2TEXTCTRLNOPERSONASAFECTADAS,
              name='textCtrlNoPersonasAfectadas', parent=self.NBCasosGral,
              pos=wx.Point(160, 413), size=wx.Size(552, 21), style=0, value='')
        self.textCtrlNoPersonasAfectadas.SetMaxLength(180)

        self.btnInfoCaso = wx.Button(id=wxID_FRAME2BTNINFOCASO, label='I',
              name='btnInfoCaso', parent=self.NBCasosGral, pos=wx.Point(304,
              280), size=wx.Size(24, 23), style=0)
        self.btnInfoCaso.SetToolTipString('Informacion de actualizacion')
        self.btnInfoCaso.Bind(wx.EVT_BUTTON, self.OnBtnInfoCaso,
              id=wxID_FRAME2BTNINFOCASO)

        self.listBoxTemas = wx.ListBox(choices=[], id=wxID_FRAME2LISTBOXTEMAS,
              name='listBoxTemas', parent=self.NBCasosTipifica, pos=wx.Point(40,
              288), size=wx.Size(656, 152), style=wx.LB_SORT)
        self.listBoxTemas.Bind(wx.EVT_KEY_DOWN, self.OnListBoxTemasKeyDown)
        self.listBoxTemas.Bind(wx.EVT_LISTBOX, self.OnListBoxTemasListbox,
              id=wxID_FRAME2LISTBOXTEMAS)

        self.listBoxDerechosafectados = wx.ListBox(choices=[],
              id=wxID_FRAME2LISTBOXDERECHOSAFECTADOS,
              name='listBoxDerechosafectados', parent=self.NBCasosTipifica,
              pos=wx.Point(40, 64), size=wx.Size(656, 152), style=wx.LB_SORT)
        self.listBoxDerechosafectados.Bind(wx.EVT_KEY_DOWN,
              self.OnListBoxDerechosafectadosKeyDown)
        self.listBoxDerechosafectados.Bind(wx.EVT_LISTBOX,
              self.OnListBoxDerechosafectadosListbox,
              id=wxID_FRAME2LISTBOXDERECHOSAFECTADOS)

        self.buttonCasoDerechoafectado = wx.Button(id=wxID_FRAME2BUTTONCASODERECHOAFECTADO,
              label='Agregar derecho', name='buttonCasoDerechoafectado',
              parent=self.NBCasosTipifica, pos=wx.Point(40, 224),
              size=wx.Size(120, 23), style=0)
        self.buttonCasoDerechoafectado.SetToolTipString('')
        self.buttonCasoDerechoafectado.Bind(wx.EVT_BUTTON,
              self.OnButtonCasoDerechoafectado,
              id=wxID_FRAME2BUTTONCASODERECHOAFECTADO)

        self.button2 = wx.Button(id=wxID_FRAME2BUTTON2, label='Agregar tema',
              name='button2', parent=self.NBCasosTipifica, pos=wx.Point(40,
              448), size=wx.Size(96, 23), style=0)
        self.button2.SetToolTipString('')
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME2BUTTON2)

        self.staticText8 = wx.StaticText(id=wxID_FRAME2STATICTEXT8,
              label='Temas', name='staticText8', parent=self.NBCasosTipifica,
              pos=wx.Point(40, 272), size=wx.Size(38, 13), style=0)
        self.staticText8.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))

        self.staticText7 = wx.StaticText(id=wxID_FRAME2STATICTEXT7,
              label='Derechos afectados', name='staticText7',
              parent=self.NBCasosTipifica, pos=wx.Point(40, 48),
              size=wx.Size(112, 13), style=0)
        self.staticText7.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))

        self.LC2 = wx.StaticText(id=wxID_FRAME2LC2, label='Caso:', name='LC2',
              parent=self.NBCasosTipifica, pos=wx.Point(16, 8), size=wx.Size(30,
              13), style=0)
        self.LC2.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))
        self.LC2.SetToolTipString('Caso actual')

        self.NBCasosNarrativa = wx.Panel(id=wxID_FRAME2NBCASOSNARRATIVA,
              name='NBCasosNarrativa', parent=self.NBCasos, pos=wx.Point(0, 0),
              size=wx.Size(844, 567), style=wx.TAB_TRAVERSAL)
        self.NBCasosNarrativa.SetBackgroundColour(wx.Colour(243, 220, 139))

        self.NBCasosAdm = wx.Panel(id=wxID_FRAME2NBCASOSADM, name='NBCasosAdm',
              parent=self.NBCasos, pos=wx.Point(0, 0), size=wx.Size(844, 567),
              style=wx.TAB_TRAVERSAL)

        self.LC7 = wx.StaticText(id=wxID_FRAME2LC7, label='Caso:', name='LC7',
              parent=self.NBCasosNarrativa, pos=wx.Point(16, 8),
              size=wx.Size(30, 13), style=0)
        self.LC7.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))
        self.LC7.SetToolTipString('Caso actual')

        self.staticText34 = wx.StaticText(id=wxID_FRAME2STATICTEXT34,
              label='Descripci\xf3n narrativa', name='staticText34',
              parent=self.NBCasosNarrativa, pos=wx.Point(304, 40),
              size=wx.Size(168, 13), style=0)

        self.textCtrlDescripcionNarrativa = wx.TextCtrl(id=wxID_FRAME2TEXTCTRLDESCRIPCIONNARRATIVA,
              name='textCtrlDescripcionNarrativa', parent=self.NBCasosNarrativa,
              pos=wx.Point(32, 64), size=wx.Size(648, 88),
              style=wx.TE_MULTILINE, value='')
        self.textCtrlDescripcionNarrativa.Bind(wx.EVT_TEXT,
              self.OnTextCtrlDescripcionNarrativaText,
              id=wxID_FRAME2TEXTCTRLDESCRIPCIONNARRATIVA)

        self.staticText35 = wx.StaticText(id=wxID_FRAME2STATICTEXT35,
              label='Resumen de la descripci\xf3n', name='staticText35',
              parent=self.NBCasosNarrativa, pos=wx.Point(296, 168),
              size=wx.Size(168, 13), style=0)

        self.textCtrlResumen = wx.TextCtrl(id=wxID_FRAME2TEXTCTRLRESUMEN,
              name='textCtrlResumen', parent=self.NBCasosNarrativa,
              pos=wx.Point(32, 184), size=wx.Size(648, 64),
              style=wx.TE_MULTILINE, value='')
        self.textCtrlResumen.SetMaxLength(7000)
        self.textCtrlResumen.Bind(wx.EVT_TEXT, self.OnTextCtrlResumenText,
              id=wxID_FRAME2TEXTCTRLRESUMEN)

        self.staticText36 = wx.StaticText(id=wxID_FRAME2STATICTEXT36,
              label='Observaciones', name='staticText36',
              parent=self.NBCasosNarrativa, pos=wx.Point(312, 272),
              size=wx.Size(144, 13), style=0)

        self.textCtrlObservaciones = wx.TextCtrl(id=wxID_FRAME2TEXTCTRLOBSERVACIONES,
              name='textCtrlObservaciones', parent=self.NBCasosNarrativa,
              pos=wx.Point(32, 288), size=wx.Size(648, 96),
              style=wx.TE_MULTILINE, value='')
        self.textCtrlObservaciones.Bind(wx.EVT_TEXT,
              self.OnTextCtrlObservacionesText,
              id=wxID_FRAME2TEXTCTRLOBSERVACIONES)

        self.buttonActualizarCaso2 = wx.Button(id=wxID_FRAME2BUTTONACTUALIZARCASO2,
              label='Guardar', name='buttonActualizarCaso2',
              parent=self.NBCasosNarrativa, pos=wx.Point(320, 400),
              size=wx.Size(75, 23), style=0)
        self.buttonActualizarCaso2.SetToolTipString('Guarda informacion del caso')
        self.buttonActualizarCaso2.Bind(wx.EVT_BUTTON,
              self.OnButtonActualizarCaso2,
              id=wxID_FRAME2BUTTONACTUALIZARCASO2)

        self.FCproyecto_grupo = wx.TextCtrl(id=wxID_FRAME2FCPROYECTO_GRUPO,
              name='FCproyecto_grupo', parent=self.NBCasosAdm, pos=wx.Point(176,
              56), size=wx.Size(472, 21), style=0, value='')
        self.FCproyecto_grupo.SetMaxLength(500)

        self.FCproyecto_conjunto = wx.TextCtrl(id=wxID_FRAME2FCPROYECTO_CONJUNTO,
              name='FCproyecto_conjunto', parent=self.NBCasosAdm,
              pos=wx.Point(176, 88), size=wx.Size(472, 21), style=0, value='')
        self.FCproyecto_conjunto.SetMaxLength(500)

        self.FCproyecto_se = wx.TextCtrl(id=wxID_FRAME2FCPROYECTO_SE,
              name='FCproyecto_se', parent=self.NBCasosAdm, pos=wx.Point(176,
              120), size=wx.Size(472, 21), style=0, value='')
        self.FCproyecto_se.SetMaxLength(500)
        self.FCproyecto_se.Show(False)

        self.textCtrlCAComentarios = wx.TextCtrl(id=wxID_FRAME2TEXTCTRLCACOMENTARIOS,
              name='textCtrlCAComentarios', parent=self.NBCasosAdm,
              pos=wx.Point(176, 160), size=wx.Size(472, 80),
              style=wx.TE_MULTILINE, value='')
        self.textCtrlCAComentarios.Bind(wx.EVT_TEXT,
              self.OnTextCtrlCAComentariosText,
              id=wxID_FRAME2TEXTCTRLCACOMENTARIOS)

        self.choiceMonitoreo = wx.Choice(choices=[],
              id=wxID_FRAME2CHOICEMONITOREO, name='choiceMonitoreo',
              parent=self.NBCasosAdm, pos=wx.Point(176, 256), size=wx.Size(248,
              21), style=0)
        self.choiceMonitoreo.Bind(wx.EVT_CHOICE, self.OnChoiceMonitoreoChoice,
              id=wxID_FRAME2CHOICEMONITOREO)

        self.textCtrlCAArchivos = wx.TextCtrl(id=wxID_FRAME2TEXTCTRLCAARCHIVOS,
              name='textCtrlCAArchivos', parent=self.NBCasosAdm,
              pos=wx.Point(176, 288), size=wx.Size(472, 80),
              style=wx.TE_MULTILINE, value='')
        self.textCtrlCAArchivos.Bind(wx.EVT_TEXT, self.OnTextCtrlCAArchivosText,
              id=wxID_FRAME2TEXTCTRLCAARCHIVOS)

        self.LC9 = wx.StaticText(id=wxID_FRAME2LC9, label='Caso:', name='LC9',
              parent=self.NBCasosAdm, pos=wx.Point(16, 8), size=wx.Size(30, 13),
              style=0)
        self.LC9.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))
        self.LC9.SetToolTipString('Caso actual')

        self.staticText75 = wx.StaticText(id=wxID_FRAME2STATICTEXT75,
              label='Proyecto local', name='staticText75',
              parent=self.NBCasosAdm, pos=wx.Point(16, 58), size=wx.Size(88,
              13), style=0)

        self.staticText76 = wx.StaticText(id=wxID_FRAME2STATICTEXT76,
              label='Proyecto conjunto RedTDT', name='staticText76',
              parent=self.NBCasosAdm, pos=wx.Point(16, 90), size=wx.Size(152,
              13), style=0)

        self.staticText77 = wx.StaticText(id=wxID_FRAME2STATICTEXT77,
              label='Proyecto SE', name='staticText77', parent=self.NBCasosAdm,
              pos=wx.Point(16, 122), size=wx.Size(72, 13), style=0)
        self.staticText77.Show(False)

        self.staticText78 = wx.StaticText(id=wxID_FRAME2STATICTEXT78,
              label='Comentarios', name='staticText78', parent=self.NBCasosAdm,
              pos=wx.Point(16, 160), size=wx.Size(80, 13), style=0)

        self.staticText79 = wx.StaticText(id=wxID_FRAME2STATICTEXT79,
              label='Estatus del caso', name='staticText79',
              parent=self.NBCasosAdm, pos=wx.Point(24, 264), size=wx.Size(112,
              13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME2STATICTEXT4,
              label='Archivos', name='staticText4', parent=self.NBCasosAdm,
              pos=wx.Point(24, 288), size=wx.Size(56, 13), style=0)

        self.NBActos = wx.lib.flatnotebook.FlatNotebook(id=wxID_FRAME2NBACTOS,
              name='NBActos', parent=self.NBMain, pos=wx.Point(0, 0),
              size=wx.Size(844, 593), style=0)
        self.NBActos.Enable(True)
        self.NBActos.Bind(wx.lib.flatnotebook.EVT_FLATNOTEBOOK_PAGE_CHANGED,
              self.OnNBActosFlatnotebookPageChanged, id=wxID_FRAME2NBACTOS)

        self.NBActosGral = wx.Panel(id=wxID_FRAME2NBACTOSGRAL,
              name='NBActosGral', parent=self.NBActos, pos=wx.Point(0, 0),
              size=wx.Size(844, 567), style=wx.TAB_TRAVERSAL)

        self.NBActosPerp = wx.Panel(id=wxID_FRAME2NBACTOSPERP,
              name='NBActosPerp', parent=self.NBActos, pos=wx.Point(0, 0),
              size=wx.Size(844, 567), style=wx.TAB_TRAVERSAL)

        self.LC3 = wx.StaticText(id=wxID_FRAME2LC3, label='Caso:', name='LC3',
              parent=self.NBActosGral, pos=wx.Point(16, 8), size=wx.Size(776,
              13), style=wx.ST_NO_AUTORESIZE)
        self.LC3.SetToolTipString('Caso actual')

        self.staticText6 = wx.StaticText(id=wxID_FRAME2STATICTEXT6,
              label='Actos registrados', name='staticText6',
              parent=self.NBActosGral, pos=wx.Point(120, 56), size=wx.Size(85,
              13), style=0)

        self.listActos = wx.ListBox(choices=[], id=wxID_FRAME2LISTACTOS,
              name='listActos', parent=self.NBActosGral, pos=wx.Point(8, 72),
              size=wx.Size(312, 152), style=wx.HSCROLL)
        self.listActos.Bind(wx.EVT_LISTBOX, self.OnListActosListbox,
              id=wxID_FRAME2LISTACTOS)
        self.listActos.Bind(wx.EVT_LISTBOX_DCLICK, self.OnListActosDclick,
              id=wxID_FRAME2LISTACTOS)
        self.listActos.Bind(wx.EVT_KEY_DOWN, self.OnListActosKeyDown)

        self.buttonNuevoActo = wx.Button(id=wxID_FRAME2BUTTONNUEVOACTO,
              label='Agregar acto', name='buttonNuevoActo',
              parent=self.NBActosGral, pos=wx.Point(8, 240), size=wx.Size(88,
              23), style=0)
        self.buttonNuevoActo.SetToolTipString('Acto nuevo')
        self.buttonNuevoActo.Bind(wx.EVT_BUTTON, self.OnButtonNuevoActoButton,
              id=wxID_FRAME2BUTTONNUEVOACTO)

        self.staticText44 = wx.StaticText(id=wxID_FRAME2STATICTEXT44,
              label='Tipo de acto o VDH', name='staticText44',
              parent=self.NBActosGral, pos=wx.Point(344, 48), size=wx.Size(112,
              13), style=0)

        self.staticText39 = wx.StaticText(id=wxID_FRAME2STATICTEXT39,
              label='Exportar acto', name='staticText39',
              parent=self.NBActosGral, pos=wx.Point(16, 472), size=wx.Size(88,
              13), style=0)

        self.staticText13 = wx.StaticText(id=wxID_FRAME2STATICTEXT13,
              label='V\xedctima', name='staticText13', parent=self.NBActosGral,
              pos=wx.Point(344, 93), size=wx.Size(88, 13), style=0)

        self.staticText40 = wx.StaticText(id=wxID_FRAME2STATICTEXT40,
              label='Fecha inicial', name='staticText40',
              parent=self.NBActosGral, pos=wx.Point(344, 136), size=wx.Size(112,
              13), style=0)

        self.staticText41 = wx.StaticText(id=wxID_FRAME2STATICTEXT41,
              label='Fecha final', name='staticText41', parent=self.NBActosGral,
              pos=wx.Point(344, 160), size=wx.Size(104, 13), style=0)

        self.staticText45 = wx.StaticText(id=wxID_FRAME2STATICTEXT45,
              label='Caracter\xedsticas \nrelevantes', name='staticText45',
              parent=self.NBActosGral, pos=wx.Point(344, 184), size=wx.Size(88,
              26), style=0)

        self.staticText49 = wx.StaticText(id=wxID_FRAME2STATICTEXT49,
              label='Tipo de lugar', name='staticText49',
              parent=self.NBActosGral, pos=wx.Point(344, 232), size=wx.Size(112,
              13), style=0)

        self.staticText46 = wx.StaticText(id=wxID_FRAME2STATICTEXT46,
              label='Estatus VDH', name='staticText46', parent=self.NBActosGral,
              pos=wx.Point(344, 263), size=wx.Size(112, 13), style=0)

        self.staticText47 = wx.StaticText(id=wxID_FRAME2STATICTEXT47,
              label='Estatus de la v\xedctima', name='staticText47',
              parent=self.NBActosGral, pos=wx.Point(344, 287), size=wx.Size(120,
              13), style=0)

        self.staticText48 = wx.StaticText(id=wxID_FRAME2STATICTEXT48,
              label='Observaciones', name='staticText48',
              parent=self.NBActosGral, pos=wx.Point(344, 370), size=wx.Size(144,
              13), style=0)

        self.FAObservaciones = wx.TextCtrl(id=wxID_FRAME2FAOBSERVACIONES,
              name='FAObservaciones', parent=self.NBActosGral, pos=wx.Point(344,
              384), size=wx.Size(448, 72), style=wx.TE_MULTILINE, value='')
        self.FAObservaciones.Bind(wx.EVT_TEXT, self.OnFAObservacionesText,
              id=wxID_FRAME2FAOBSERVACIONES)

        self.ActualizarActo = wx.Button(id=wxID_FRAME2ACTUALIZARACTO,
              label='Guardar', name='ActualizarActo', parent=self.NBActosGral,
              pos=wx.Point(400, 464), size=wx.Size(75, 23), style=0)
        self.ActualizarActo.Bind(wx.EVT_BUTTON, self.OnActualizarActo,
              id=wxID_FRAME2ACTUALIZARACTO)

        self.btnInfoActo = wx.Button(id=wxID_FRAME2BTNINFOACTO, label='I',
              name='btnInfoActo', parent=self.NBActosGral, pos=wx.Point(296,
              240), size=wx.Size(24, 23), style=0)
        self.btnInfoActo.SetToolTipString('Informacion de actualizacion')
        self.btnInfoActo.Bind(wx.EVT_BUTTON, self.OnBtnInfoActo,
              id=wxID_FRAME2BTNINFOACTO)

        self.BTNAgregarcaracrelevantes = wx.Button(id=wxID_FRAME2BTNAGREGARCARACRELEVANTES,
              label='+', name='BTNAgregarcaracrelevantes',
              parent=self.NBActosGral, pos=wx.Point(464, 176), size=wx.Size(24,
              23), style=0)
        self.BTNAgregarcaracrelevantes.Bind(wx.EVT_BUTTON,
              self.OnBTNAgregarCaracRelevante,
              id=wxID_FRAME2BTNAGREGARCARACRELEVANTES)

        self.buttonSelecTipodelugar = wx.Button(id=wxID_FRAME2BUTTONSELECTIPODELUGAR,
              label='+', name='buttonSelecTipodelugar', parent=self.NBActosGral,
              pos=wx.Point(465, 224), size=wx.Size(24, 23), style=0)
        self.buttonSelecTipodelugar.Bind(wx.EVT_BUTTON,
              self.OnButtonSelecTipodelugar,
              id=wxID_FRAME2BUTTONSELECTIPODELUGAR)

        self.buttonSelectEstatusVDH = wx.Button(id=wxID_FRAME2BUTTONSELECTESTATUSVDH,
              label='+', name='buttonSelectEstatusVDH', parent=self.NBActosGral,
              pos=wx.Point(465, 255), size=wx.Size(24, 23), style=0)
        self.buttonSelectEstatusVDH.Bind(wx.EVT_BUTTON,
              self.OnButtonSelectEstatusVDHButton,
              id=wxID_FRAME2BUTTONSELECTESTATUSVDH)

        self.buttonEstatusdelavictima = wx.Button(id=wxID_FRAME2BUTTONESTATUSDELAVICTIMA,
              label='+', name='buttonEstatusdelavictima',
              parent=self.NBActosGral, pos=wx.Point(465, 279), size=wx.Size(24,
              23), style=0)
        self.buttonEstatusdelavictima.Bind(wx.EVT_BUTTON,
              self.OnButtonEstatusdelavictimaButton,
              id=wxID_FRAME2BUTTONESTATUSDELAVICTIMA)

        self.FACaracRelevante = wx.ListBox(choices=[],
              id=wxID_FRAME2FACARACRELEVANTE, name='FACaracRelevante',
              parent=self.NBActosGral, pos=wx.Point(528, 176), size=wx.Size(257,
              48), style=wx.HSCROLL)
        self.FACaracRelevante.Bind(wx.EVT_LISTBOX, self.OnListBox3Listbox,
              id=wxID_FRAME2FACARACRELEVANTE)
        self.FACaracRelevante.Bind(wx.EVT_KEY_DOWN,
              self.OnFACaracRelevanteKeyDown)

        self.FATipofechainicio = wx.Choice(choices=[],
              id=wxID_FRAME2FATIPOFECHAINICIO, name='FATipofechainicio',
              parent=self.NBActosGral, pos=wx.Point(528, 128), size=wx.Size(145,
              21), style=0)
        self.FATipofechainicio.Bind(wx.EVT_CHOICE,
              self.OnFATipofechainicioChoice, id=wxID_FRAME2FATIPOFECHAINICIO)

        self.FATipofechafin = wx.Choice(choices=[],
              id=wxID_FRAME2FATIPOFECHAFIN, name='FATipofechafin',
              parent=self.NBActosGral, pos=wx.Point(528, 152), size=wx.Size(145,
              21), style=0)
        self.FATipofechafin.Bind(wx.EVT_CHOICE, self.OnFATipofechafinChoice,
              id=wxID_FRAME2FATIPOFECHAFIN)

        self.FAConfidencialidad = wx.CheckBox(id=wxID_FRAME2FACONFIDENCIALIDAD,
              label='', name='FAConfidencialidad', parent=self.NBActosGral,
              pos=wx.Point(137, 472), size=wx.Size(16, 13), style=0)
        self.FAConfidencialidad.SetValue(True)
        self.FAConfidencialidad.Bind(wx.EVT_CHECKBOX,
              self.OnFAConfidencialidadCheckbox,
              id=wxID_FRAME2FACONFIDENCIALIDAD)

        self.FATipodelugar = wx.StaticText(id=wxID_FRAME2FATIPODELUGAR,
              label='__________________________________________\n______',
              name='FATipodelugar', parent=self.NBActosGral, pos=wx.Point(529,
              226), size=wx.Size(311, 30), style=wx.ST_NO_AUTORESIZE)
        self.FATipodelugar.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.FAVictima = wx.StaticText(id=wxID_FRAME2FAVICTIMA,
              label='________________________', name='FAVictima',
              parent=self.NBActosGral, pos=wx.Point(529, 93), size=wx.Size(295,
              27), style=wx.ST_NO_AUTORESIZE)
        self.FAVictima.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))

        self.FATipoacto = wx.StaticText(id=wxID_FRAME2FATIPOACTO,
              label='________________________ _____________________________ \n________________________ ____________________________ \n_____________________',
              name='FATipoacto', parent=self.NBActosGral, pos=wx.Point(529, 40),
              size=wx.Size(296, 51), style=wx.ST_NO_AUTORESIZE)
        self.FATipoacto.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))

        self.FAEstatusvdh = wx.StaticText(id=wxID_FRAME2FAESTATUSVDH,
              label='________________________', name='FAEstatusvdh',
              parent=self.NBActosGral, pos=wx.Point(529, 263), size=wx.Size(311,
              13), style=wx.ST_NO_AUTORESIZE)
        self.FAEstatusvdh.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.FAEstatusvictima = wx.StaticText(id=wxID_FRAME2FAESTATUSVICTIMA,
              label='________________________', name='FAEstatusvictima',
              parent=self.NBActosGral, pos=wx.Point(529, 287), size=wx.Size(311,
              13), style=wx.ST_NO_AUTORESIZE)
        self.FAEstatusvictima.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.LC4 = wx.StaticText(id=wxID_FRAME2LC4, label='Caso:', name='LC4',
              parent=self.NBActosPerp, pos=wx.Point(16, 8), size=wx.Size(792,
              13), style=wx.ST_NO_AUTORESIZE)
        self.LC4.SetToolTipString('Caso actual')

        self.statixText50 = wx.StaticText(id=wxID_FRAME2STATIXTEXT50,
              label='Perpetradores', name='statixText50',
              parent=self.NBActosPerp, pos=wx.Point(72, 72), size=wx.Size(70,
              13), style=0)

        self.listBoxPerpetradores = wx.ListBox(choices=[],
              id=wxID_FRAME2LISTBOXPERPETRADORES, name='listBoxPerpetradores',
              parent=self.NBActosPerp, pos=wx.Point(16, 96), size=wx.Size(168,
              168), style=wx.HSCROLL)
        self.listBoxPerpetradores.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnListBoxPerpetradoresDclick,
              id=wxID_FRAME2LISTBOXPERPETRADORES)
        self.listBoxPerpetradores.Bind(wx.EVT_KEY_DOWN,
              self.OnListBoxPerpetradoresKeyDown)

        self.buttonAddPerpetrador = wx.Button(id=wxID_FRAME2BUTTONADDPERPETRADOR,
              label='Agregar un \nperpetrador', name='buttonAddPerpetrador',
              parent=self.NBActosPerp, pos=wx.Point(16, 272), size=wx.Size(88,
              48), style=0)
        self.buttonAddPerpetrador.Bind(wx.EVT_BUTTON, self.OnPerpetradorADD,
              id=wxID_FRAME2BUTTONADDPERPETRADOR)

        self.staticText50 = wx.StaticText(id=wxID_FRAME2STATICTEXT50,
              label='Nombre del perpetrador', name='staticText50',
              parent=self.NBActosPerp, pos=wx.Point(192, 72), size=wx.Size(144,
              32), style=0)

        self.staticText51 = wx.StaticText(id=wxID_FRAME2STATICTEXT51,
              label='Exportar perpetrador', name='staticText51',
              parent=self.NBActosPerp, pos=wx.Point(24, 416), size=wx.Size(103,
              13), style=0)

        self.FIconfidencialidad = wx.CheckBox(id=wxID_FRAME2FICONFIDENCIALIDAD,
              label='', name='FIconfidencialidad', parent=self.NBActosPerp,
              pos=wx.Point(128, 416), size=wx.Size(16, 13), style=0)
        self.FIconfidencialidad.SetValue(True)
        self.FIconfidencialidad.Bind(wx.EVT_CHECKBOX,
              self.OnFIconfidencialidadCheckbox,
              id=wxID_FRAME2FICONFIDENCIALIDAD)

        self.staticText52 = wx.StaticText(id=wxID_FRAME2STATICTEXT52,
              label='Grado de involucramiento', name='staticText52',
              parent=self.NBActosPerp, pos=wx.Point(192, 113), size=wx.Size(144,
              13), style=0)

        self.staticText53 = wx.StaticText(id=wxID_FRAME2STATICTEXT53,
              label='Tipo de perpetrador', name='staticText53',
              parent=self.NBActosPerp, pos=wx.Point(192, 144), size=wx.Size(136,
              13), style=0)

        self.staticText54 = wx.StaticText(id=wxID_FRAME2STATICTEXT54,
              label='\xdaltimo estatus del perpetrador', name='staticText54',
              parent=self.NBActosPerp, pos=wx.Point(192, 177), size=wx.Size(152,
              24), style=0)

        self.staticText14 = wx.StaticText(id=wxID_FRAME2STATICTEXT14,
              label='Observaciones', name='staticText14',
              parent=self.NBActosPerp, pos=wx.Point(216, 200), size=wx.Size(88,
              13), style=0)

        self.textCtrlINObservaciones = wx.TextCtrl(id=wxID_FRAME2TEXTCTRLINOBSERVACIONES,
              name='textCtrlINObservaciones', parent=self.NBActosPerp,
              pos=wx.Point(216, 216), size=wx.Size(400, 104),
              style=wx.TE_MULTILINE, value='')
        self.textCtrlINObservaciones.Bind(wx.EVT_TEXT,
              self.OnTextCtrlINObservacionesText,
              id=wxID_FRAME2TEXTCTRLINOBSERVACIONES)
        self.textCtrlINObservaciones.Bind(wx.EVT_KILL_FOCUS,
              self.OnTextCtrlINObservacionesKillFocus)

        self.btnInfoInvol = wx.Button(id=wxID_FRAME2BTNINFOINVOL, label='I',
              name='btnInfoInvol', parent=self.NBActosPerp, pos=wx.Point(192,
              272), size=wx.Size(24, 23), style=0)
        self.btnInfoInvol.Bind(wx.EVT_BUTTON, self.OnBtnInfoInvol,
              id=wxID_FRAME2BTNINFOINVOL)

        self.buttonSelGradoInvol = wx.Button(id=wxID_FRAME2BUTTONSELGRADOINVOL,
              label='+', name='buttonSelGradoInvol', parent=self.NBActosPerp,
              pos=wx.Point(344, 105), size=wx.Size(24, 23), style=0)
        self.buttonSelGradoInvol.Bind(wx.EVT_BUTTON, self.OnButtonSelGradoInvol,
              id=wxID_FRAME2BUTTONSELGRADOINVOL)

        self.buttonSelTipoPerp = wx.Button(id=wxID_FRAME2BUTTONSELTIPOPERP,
              label='+', name='buttonSelTipoPerp', parent=self.NBActosPerp,
              pos=wx.Point(344, 136), size=wx.Size(24, 23), style=0)
        self.buttonSelTipoPerp.Bind(wx.EVT_BUTTON,
              self.OnButtonSelTipoPerpButton, id=wxID_FRAME2BUTTONSELTIPOPERP)

        self.buttonSelUltStatusPerp = wx.Button(id=wxID_FRAME2BUTTONSELULTSTATUSPERP,
              label='+', name='buttonSelUltStatusPerp', parent=self.NBActosPerp,
              pos=wx.Point(344, 169), size=wx.Size(24, 23), style=0)
        self.buttonSelUltStatusPerp.Bind(wx.EVT_BUTTON,
              self.OnButtonSelUltStatusPerp,
              id=wxID_FRAME2BUTTONSELULTSTATUSPERP)

        self.FIultimostatusperpetrador = wx.StaticText(id=wxID_FRAME2FIULTIMOSTATUSPERPETRADOR,
              label='____', name='FIultimostatusperpetrador',
              parent=self.NBActosPerp, pos=wx.Point(401, 177), size=wx.Size(431,
              13), style=wx.ST_NO_AUTORESIZE)
        self.FIultimostatusperpetrador.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL,
              wx.BOLD, False, 'Tahoma'))

        self.FItipoperpetrador = wx.StaticText(id=wxID_FRAME2FITIPOPERPETRADOR,
              label='____', name='FItipoperpetrador', parent=self.NBActosPerp,
              pos=wx.Point(400, 144), size=wx.Size(432, 13),
              style=wx.ST_NO_AUTORESIZE)
        self.FItipoperpetrador.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.FIgradoinvolucramiento = wx.StaticText(id=wxID_FRAME2FIGRADOINVOLUCRAMIENTO,
              label='____', name='FIgradoinvolucramiento',
              parent=self.NBActosPerp, pos=wx.Point(400, 105), size=wx.Size(432,
              31), style=wx.ST_NO_AUTORESIZE)
        self.FIgradoinvolucramiento.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL,
              wx.BOLD, False, 'Tahoma'))

        self.FIperpetrador = wx.StaticText(id=wxID_FRAME2FIPERPETRADOR,
              label='____', name='FIperpetrador', parent=self.NBActosPerp,
              pos=wx.Point(400, 72), size=wx.Size(432, 13),
              style=wx.ST_NO_AUTORESIZE)
        self.FIperpetrador.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.buttonActualizarInvol = wx.Button(id=wxID_FRAME2BUTTONACTUALIZARINVOL,
              label='Guardar', name='buttonActualizarInvol',
              parent=self.NBActosPerp, pos=wx.Point(360, 352), size=wx.Size(75,
              23), style=0)
        self.buttonActualizarInvol.Bind(wx.EVT_BUTTON,
              self.OnButtonActualizarInvol,
              id=wxID_FRAME2BUTTONACTUALIZARINVOL)

        self.NBPersonas = wx.lib.flatnotebook.FlatNotebook(id=wxID_FRAME2NBPERSONAS,
              name='NBPersonas', parent=self.NBMain, pos=wx.Point(0, 0),
              size=wx.Size(844, 593), style=0)
        self.NBPersonas.Bind(wx.lib.flatnotebook.EVT_FLATNOTEBOOK_PAGE_CHANGED,
              self.OnNBPersonasFlatnotebookPageChanged,
              id=wxID_FRAME2NBPERSONAS)

        self.NBPersonasGral = wx.Panel(id=wxID_FRAME2NBPERSONASGRAL,
              name='NBPersonasGral', parent=self.NBPersonas, pos=wx.Point(0, 0),
              size=wx.Size(0, 0), style=wx.TAB_TRAVERSAL)

        self.NBPersonasDetalles = wx.Panel(id=wxID_FRAME2NBPERSONASDETALLES,
              name='NBPersonasDetalles', parent=self.NBPersonas, pos=wx.Point(0,
              0), size=wx.Size(844, 567), style=wx.TAB_TRAVERSAL)

        self.NBPersonasAdm = wx.Panel(id=wxID_FRAME2NBPERSONASADM,
              name='NBPersonasAdm', parent=self.NBPersonas, pos=wx.Point(0, 0),
              size=wx.Size(844, 567), style=wx.TAB_TRAVERSAL)

        self.NBPersonasBio = wx.Panel(id=wxID_FRAME2NBPERSONASBIO,
              name='NBPersonasBio', parent=self.NBPersonas, pos=wx.Point(0, 0),
              size=wx.Size(844, 567), style=wx.TAB_TRAVERSAL)
        self.NBPersonasBio.SetToolTipString('')
        self.NBPersonasBio.Bind(wx.EVT_SYS_COLOUR_CHANGED,
              self.OnNBPersonasBioSysColourChanged)

        self.listBoxPersonaBrowser = wx.ListBox(choices=[],
              id=wxID_FRAME2LISTBOXPERSONABROWSER, name='listBoxPersonaBrowser',
              parent=self.NBPersonasGral, pos=wx.Point(40, 160),
              size=wx.Size(296, 192), style=wx.HSCROLL)
        self.listBoxPersonaBrowser.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnListBoxPersonaBrowserDclick,
              id=wxID_FRAME2LISTBOXPERSONABROWSER)
        self.listBoxPersonaBrowser.Bind(wx.EVT_KEY_DOWN,
              self.OnListBoxPersonaBrowserKeyDown)
        self.listBoxPersonaBrowser.Bind(wx.EVT_LISTBOX,
              self.OnListBoxPersonaBrowserListbox,
              id=wxID_FRAME2LISTBOXPERSONABROWSER)

        self.CPNombre = wx.StaticText(id=wxID_FRAME2CPNOMBRE, label='Nombre(s)',
              name='CPNombre', parent=self.NBPersonasGral, pos=wx.Point(352,
              128), size=wx.Size(112, 13), style=0)

        self.CPApellido = wx.StaticText(id=wxID_FRAME2CPAPELLIDO,
              label='Apellido(s)', name='CPApellido',
              parent=self.NBPersonasGral, pos=wx.Point(352, 152),
              size=wx.Size(112, 13), style=0)

        self.CPSexo = wx.StaticText(id=wxID_FRAME2CPSEXO, label='Sexo',
              name='CPSexo', parent=self.NBPersonasGral, pos=wx.Point(352, 208),
              size=wx.Size(96, 13), style=0)

        self.CPfechanac = wx.StaticText(id=wxID_FRAME2CPFECHANAC,
              label='Fecha de nacimiento', name='CPfechanac',
              parent=self.NBPersonasGral, pos=wx.Point(352, 232),
              size=wx.Size(128, 13), style=0)

        self.CPPais = wx.StaticText(id=wxID_FRAME2CPPAIS,
              label=u'Pa\xeds de origen', name='CPPais',
              parent=self.NBPersonasGral, pos=wx.Point(352, 256),
              size=wx.Size(68, 13), style=0)

        self.CPMunicipio = wx.StaticText(id=wxID_FRAME2CPMUNICIPIO,
              label=u'Municipio de origen', name='CPMunicipio',
              parent=self.NBPersonasGral, pos=wx.Point(352, 305),
              size=wx.Size(92, 13), style=0)

        self.CPLocalidad = wx.StaticText(id=wxID_FRAME2CPLOCALIDAD,
              label=u'Localidad de origen', name='CPLocalidad',
              parent=self.NBPersonasGral, pos=wx.Point(352, 329),
              size=wx.Size(93, 13), style=0)

        self.CPCiudadania = wx.StaticText(id=wxID_FRAME2CPCIUDADANIA,
              label='Ciudadan\xeda', name='CPCiudadania',
              parent=self.NBPersonasGral, pos=wx.Point(352, 355),
              size=wx.Size(152, 13), style=0)

        self.CPEscolaridad = wx.StaticText(id=wxID_FRAME2CPESCOLARIDAD,
              label='Escolaridad', name='CPEscolaridad',
              parent=self.NBPersonasGral, pos=wx.Point(352, 379),
              size=wx.Size(160, 29), style=wx.ST_NO_AUTORESIZE)

        self.FPNombre = wx.TextCtrl(id=wxID_FRAME2FPNOMBRE, name='FPNombre',
              parent=self.NBPersonasGral, pos=wx.Point(520, 128),
              size=wx.Size(288, 21), style=0, value='')
        self.FPNombre.SetMaxLength(200)
        self.FPNombre.Bind(wx.EVT_KILL_FOCUS, self.OnFPNombreKillFocus)

        self.FPApellido = wx.TextCtrl(id=wxID_FRAME2FPAPELLIDO,
              name='FPApellido', parent=self.NBPersonasGral, pos=wx.Point(520,
              152), size=wx.Size(288, 21), style=0, value='')
        self.FPApellido.SetMaxLength(200)
        self.FPApellido.Bind(wx.EVT_KILL_FOCUS, self.OnFPApellidoKillFocus)

        self.FPSexo = wx.Choice(choices=[], id=wxID_FRAME2FPSEXO, name='FPSexo',
              parent=self.NBPersonasGral, pos=wx.Point(520, 200),
              size=wx.Size(130, 21), style=0)

        self.FPMunicipio = wx.Choice(choices=[], id=wxID_FRAME2FPMUNICIPIO,
              name='FPMunicipio', parent=self.NBPersonasGral, pos=wx.Point(520,
              297), size=wx.Size(288, 21), style=0)
        self.FPMunicipio.Bind(wx.EVT_CHOICE, self.OnFPMunicipioChoice,
              id=wxID_FRAME2FPMUNICIPIO)

        self.FPLocalidad = wx.TextCtrl(id=wxID_FRAME2FPLOCALIDAD,
              name='FPLocalidad', parent=self.NBPersonasGral, pos=wx.Point(520,
              321), size=wx.Size(288, 21), style=0, value='')
        self.FPLocalidad.SetMaxLength(100)

        self.FPEscolaridad = wx.Choice(choices=[], id=wxID_FRAME2FPESCOLARIDAD,
              name='FPEscolaridad', parent=self.NBPersonasGral,
              pos=wx.Point(520, 371), size=wx.Size(288, 21), style=0)

        self.CPEstado = wx.StaticText(id=wxID_FRAME2CPESTADO,
              label=u'Estado de origen', name='CPEstado',
              parent=self.NBPersonasGral, pos=wx.Point(352, 280),
              size=wx.Size(82, 13), style=0)

        self.buttonPGuardar = wx.Button(id=wxID_FRAME2BUTTONPGUARDAR,
              label='Guardar', name='buttonPGuardar',
              parent=self.NBPersonasGral, pos=wx.Point(520, 400),
              size=wx.Size(75, 23), style=0)
        self.buttonPGuardar.Bind(wx.EVT_BUTTON, self.OnButtonPGuardar,
              id=wxID_FRAME2BUTTONPGUARDAR)

        self.FPTipodefecha = wx.Choice(choices=[], id=wxID_FRAME2FPTIPODEFECHA,
              name='FPTipodefecha', parent=self.NBPersonasGral,
              pos=wx.Point(520, 224), size=wx.Size(176, 21), style=0)
        self.FPTipodefecha.Bind(wx.EVT_CHOICE, self.OnFPTipodefechaChoice,
              id=wxID_FRAME2FPTIPODEFECHA)

        self.FPEstado = wx.Choice(choices=[], id=wxID_FRAME2FPESTADO,
              name='FPEstado', parent=self.NBPersonasGral, pos=wx.Point(520,
              272), size=wx.Size(288, 21), style=0)
        self.FPEstado.Bind(wx.EVT_CHOICE, self.OnFPEstadoChoice,
              id=wxID_FRAME2FPESTADO)

        self.btnInfoPersona = wx.Button(id=wxID_FRAME2BTNINFOPERSONA, label='I',
              name='btnInfoPersona', parent=self.NBPersonasGral,
              pos=wx.Point(312, 361), size=wx.Size(24, 23), style=0)
        self.btnInfoPersona.Bind(wx.EVT_BUTTON, self.OnBtnInfoPersona,
              id=wxID_FRAME2BTNINFOPERSONA)

        self.FPIdioma = wx.ListBox(choices=[], id=wxID_FRAME2FPIDIOMA,
              name='FPIdioma', parent=self.NBPersonasDetalles, pos=wx.Point(168,
              66), size=wx.Size(368, 48), style=wx.HSCROLL)
        self.FPIdioma.Bind(wx.EVT_KEY_DOWN, self.OnFPIdiomaKeyDown)

        self.FPLengua = wx.ListBox(choices=[], id=wxID_FRAME2FPLENGUA,
              name='FPLengua', parent=self.NBPersonasDetalles, pos=wx.Point(168,
              144), size=wx.Size(368, 48), style=wx.HSCROLL)
        self.FPLengua.Bind(wx.EVT_KEY_DOWN, self.OnFPLenguaKeyDown)

        self.FPOrigenEtnico = wx.ListBox(choices=[],
              id=wxID_FRAME2FPORIGENETNICO, name='FPOrigenEtnico',
              parent=self.NBPersonasDetalles, pos=wx.Point(168, 200),
              size=wx.Size(368, 48), style=0)
        self.FPOrigenEtnico.Bind(wx.EVT_KEY_DOWN, self.OnFPOrigenEtnicoKeyDown)

        self.FPReligion = wx.Choice(choices=[], id=wxID_FRAME2FPRELIGION,
              name='FPReligion', parent=self.NBPersonasDetalles,
              pos=wx.Point(168, 256), size=wx.Size(368, 21), style=0)

        self.FPEstadocivil = wx.Choice(choices=[], id=wxID_FRAME2FPESTADOCIVIL,
              name='FPEstadocivil', parent=self.NBPersonasDetalles,
              pos=wx.Point(168, 288), size=wx.Size(368, 21), style=0)

        self.FPAddOrigenEtnico = wx.Button(id=wxID_FRAME2FPADDORIGENETNICO,
              label='+', name='FPAddOrigenEtnico',
              parent=self.NBPersonasDetalles, pos=wx.Point(544, 200),
              size=wx.Size(24, 23), style=0)
        self.FPAddOrigenEtnico.Bind(wx.EVT_BUTTON,
              self.OnFPAddOrigenEtnicoButton, id=wxID_FRAME2FPADDORIGENETNICO)

        self.FPAddLengua = wx.Button(id=wxID_FRAME2FPADDLENGUA, label='+',
              name='FPAddLengua', parent=self.NBPersonasDetalles,
              pos=wx.Point(544, 144), size=wx.Size(24, 23), style=0)
        self.FPAddLengua.Bind(wx.EVT_BUTTON, self.OnFPAddLenguaButton,
              id=wxID_FRAME2FPADDLENGUA)

        self.FPAddIdioma = wx.Button(id=wxID_FRAME2FPADDIDIOMA, label='+',
              name='FPAddIdioma', parent=self.NBPersonasDetalles,
              pos=wx.Point(544, 67), size=wx.Size(24, 23), style=0)
        self.FPAddIdioma.Bind(wx.EVT_BUTTON, self.OnFPAddIdiomaButton,
              id=wxID_FRAME2FPADDIDIOMA)

        self.CPOcupacion = wx.StaticText(id=wxID_FRAME2CPOCUPACION,
              label='Ocupaci\xf3n', name='CPOcupacion',
              parent=self.NBPersonasDetalles, pos=wx.Point(24, 48),
              size=wx.Size(50, 13), style=0)

        self.CPIdioma = wx.StaticText(id=wxID_FRAME2CPIDIOMA,
              label='Idioma que habla', name='CPIdioma',
              parent=self.NBPersonasDetalles, pos=wx.Point(24, 66),
              size=wx.Size(136, 32), style=wx.ST_NO_AUTORESIZE)

        self.CPHablayentiendeespanol = wx.StaticText(id=wxID_FRAME2CPHABLAYENTIENDEESPANOL,
              label='Habla y entiende espa\xf1ol',
              name='CPHablayentiendeespanol', parent=self.NBPersonasDetalles,
              pos=wx.Point(24, 120), size=wx.Size(128, 13), style=0)

        self.CPLengua = wx.StaticText(id=wxID_FRAME2CPLENGUA,
              label='Lengua que habla', name='CPLengua',
              parent=self.NBPersonasDetalles, pos=wx.Point(24, 144),
              size=wx.Size(136, 32), style=wx.ST_NO_AUTORESIZE)

        self.CPOrigenEtnico = wx.StaticText(id=wxID_FRAME2CPORIGENETNICO,
              label='Origen \xe9tnico', name='CPOrigenEtnico',
              parent=self.NBPersonasDetalles, pos=wx.Point(24, 200),
              size=wx.Size(136, 32), style=wx.ST_NO_AUTORESIZE)

        self.CPReligion = wx.StaticText(id=wxID_FRAME2CPRELIGION,
              label='Religi\xf3n', name='CPReligion',
              parent=self.NBPersonasDetalles, pos=wx.Point(24, 264),
              size=wx.Size(136, 13), style=0)

        self.CPEstadocivil = wx.StaticText(id=wxID_FRAME2CPESTADOCIVIL,
              label='Estado civil', name='CPEstadocivil',
              parent=self.NBPersonasDetalles, pos=wx.Point(24, 288),
              size=wx.Size(112, 13), style=0)

        self.CPNodependientes = wx.StaticText(id=wxID_FRAME2CPNODEPENDIENTES,
              label='No. de dependientes', name='CPNodependientes',
              parent=self.NBPersonasDetalles, pos=wx.Point(24, 324),
              size=wx.Size(136, 28), style=wx.ST_NO_AUTORESIZE)

        self.CPDescripciondelgrupo = wx.StaticText(id=wxID_FRAME2CPDESCRIPCIONDELGRUPO,
              label='Descripci\xf3n del grupo', name='CPDescripciondelgrupo',
              parent=self.NBPersonasDetalles, pos=wx.Point(24, 360),
              size=wx.Size(136, 13), style=0)

        self.staticText67 = wx.StaticText(id=wxID_FRAME2STATICTEXT67,
              label='Direcci\xf3n(es)', name='staticText67',
              parent=self.NBPersonasDetalles, pos=wx.Point(24, 384),
              size=wx.Size(88, 13), style=0)

        self.CPMonitoreo = wx.StaticText(id=wxID_FRAME2CPMONITOREO,
              label='Monitoreo', name='CPMonitoreo',
              parent=self.NBPersonasDetalles, pos=wx.Point(24, 448),
              size=wx.Size(88, 13), style=0)

        self.FPDescripciondelgrupo = wx.TextCtrl(id=wxID_FRAME2FPDESCRIPCIONDELGRUPO,
              name='FPDescripciondelgrupo', parent=self.NBPersonasDetalles,
              pos=wx.Point(168, 352), size=wx.Size(616, 21), style=0, value='')
        self.FPDescripciondelgrupo.SetMaxLength(100)

        self.FPDirecciones = wx.ListBox(choices=[], id=wxID_FRAME2FPDIRECCIONES,
              name='FPDirecciones', parent=self.NBPersonasDetalles,
              pos=wx.Point(168, 384), size=wx.Size(616, 48), style=wx.HSCROLL)
        self.FPDirecciones.Bind(wx.EVT_LISTBOX, self.OnListBox1Listbox,
              id=wxID_FRAME2FPDIRECCIONES)
        self.FPDirecciones.Bind(wx.EVT_KEY_DOWN, self.OnFPDireccionesKeyDown)
        self.FPDirecciones.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnFPDireccionesListboxDclick, id=wxID_FRAME2FPDIRECCIONES)

        self.FPMonitoreo = wx.ComboBox(choices=[], id=wxID_FRAME2FPMONITOREO,
              name='FPMonitoreo', parent=self.NBPersonasDetalles,
              pos=wx.Point(168, 440), size=wx.Size(368, 21), style=0, value='')
        self.FPMonitoreo.SetLabel('')

        self.FPAddDirecciones = wx.Button(id=wxID_FRAME2FPADDDIRECCIONES,
              label='+', name='FPAddDirecciones',
              parent=self.NBPersonasDetalles, pos=wx.Point(792, 384),
              size=wx.Size(24, 23), style=0)
        self.FPAddDirecciones.Bind(wx.EVT_BUTTON, self.OnFPAddDireccionesButton,
              id=wxID_FRAME2FPADDDIRECCIONES)

        self.FPHablayentiendeespanol = wx.CheckBox(id=wxID_FRAME2FPHABLAYENTIENDEESPANOL,
              label='', name='FPHablayentiendeespanol',
              parent=self.NBPersonasDetalles, pos=wx.Point(168, 120),
              size=wx.Size(16, 13), style=0)
        self.FPHablayentiendeespanol.SetValue(True)
        self.FPHablayentiendeespanol.Bind(wx.EVT_CHECKBOX,
              self.OnFPHablayentiendeespanolCheckbox,
              id=wxID_FRAME2FPHABLAYENTIENDEESPANOL)

        self.CPObservaciones = wx.StaticText(id=wxID_FRAME2CPOBSERVACIONES,
              label='Observaciones', name='CPObservaciones',
              parent=self.NBPersonasAdm, pos=wx.Point(296, 40), size=wx.Size(80,
              13), style=0)

        self.FPObservaciones = wx.TextCtrl(id=wxID_FRAME2FPOBSERVACIONES,
              name='FPObservaciones', parent=self.NBPersonasAdm,
              pos=wx.Point(32, 56), size=wx.Size(632, 72),
              style=wx.TE_MULTILINE, value='')
        self.FPObservaciones.Bind(wx.EVT_TEXT, self.OnFPObservacionesText,
              id=wxID_FRAME2FPOBSERVACIONES)

        self.staticText38 = wx.StaticText(id=wxID_FRAME2STATICTEXT38,
              label='Comentarios', name='staticText38',
              parent=self.NBPersonasAdm, pos=wx.Point(304, 136),
              size=wx.Size(80, 13), style=0)

        self.FPComentarios = wx.TextCtrl(id=wxID_FRAME2FPCOMENTARIOS,
              name='FPComentarios', parent=self.NBPersonasAdm, pos=wx.Point(32,
              152), size=wx.Size(632, 88), style=wx.TE_MULTILINE, value='')
        self.FPComentarios.Bind(wx.EVT_TEXT, self.OnFPComentariosText,
              id=wxID_FRAME2FPCOMENTARIOS)

        self.CPArchivos = wx.StaticText(id=wxID_FRAME2CPARCHIVOS,
              label='Archivos', name='CPArchivos', parent=self.NBPersonasAdm,
              pos=wx.Point(312, 248), size=wx.Size(48, 13), style=0)

        self.FPArchivos = wx.TextCtrl(id=wxID_FRAME2FPARCHIVOS,
              name='FPArchivos', parent=self.NBPersonasAdm, pos=wx.Point(32,
              264), size=wx.Size(632, 80), style=wx.TE_MULTILINE, value='')
        self.FPArchivos.Bind(wx.EVT_TEXT, self.OnFPArchivosText,
              id=wxID_FRAME2FPARCHIVOS)

        self.listBoxVinculos = wx.ListBox(choices=[],
              id=wxID_FRAME2LISTBOXVINCULOS, name='listBoxVinculos',
              parent=self.NBPersonasBio, pos=wx.Point(24, 56), size=wx.Size(800,
              96), style=wx.HSCROLL)
        self.listBoxVinculos.SetToolTipString('')
        self.listBoxVinculos.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnListBoxVinculosDclick, id=wxID_FRAME2LISTBOXVINCULOS)

        self.buttonVincular = wx.Button(id=wxID_FRAME2BUTTONVINCULAR,
              label='Agregar dato biogr\xe1fico', name='buttonVincular',
              parent=self.NBPersonasBio, pos=wx.Point(24, 152),
              size=wx.Size(160, 23), style=0)
        self.buttonVincular.SetToolTipString('')
        self.buttonVincular.Bind(wx.EVT_BUTTON, self.OnButtonVincular,
              id=wxID_FRAME2BUTTONVINCULAR)

        self.staticText20 = wx.StaticText(id=wxID_FRAME2STATICTEXT20,
              label='Datos biogr\xe1ficos', name='staticText20',
              parent=self.NBPersonasBio, pos=wx.Point(24, 40), size=wx.Size(84,
              13), style=0)
        self.staticText20.SetToolTipString('')

        self.NBFuentes = wx.lib.flatnotebook.FlatNotebook(id=wxID_FRAME2NBFUENTES,
              name='NBFuentes', parent=self.NBMain, pos=wx.Point(0, 0),
              size=wx.Size(844, 593), style=0)

        self.NBFuentePersonal = wx.Panel(id=wxID_FRAME2NBFUENTEPERSONAL,
              name='NBFuentePersonal', parent=self.NBFuentes, pos=wx.Point(0,
              0), size=wx.Size(844, 567), style=wx.TAB_TRAVERSAL)

        self.NBFuenteDocumental = wx.Panel(id=wxID_FRAME2NBFUENTEDOCUMENTAL,
              name='NBFuenteDocumental', parent=self.NBFuentes, pos=wx.Point(0,
              0), size=wx.Size(844, 567), style=wx.TAB_TRAVERSAL)

        self.LC6 = wx.StaticText(id=wxID_FRAME2LC6, label='Caso:', name='LC6',
              parent=self.NBFuentePersonal, pos=wx.Point(16, 8),
              size=wx.Size(600, 13), style=0)
        self.LC6.SetToolTipString('Caso actual')

        self.staticText22 = wx.StaticText(id=wxID_FRAME2STATICTEXT22,
              label='Fuentes de Informaci\xf3n     ', name='staticText22',
              parent=self.NBFuentePersonal, pos=wx.Point(8, 40),
              size=wx.Size(130, 13), style=0)

        self.listBoxFte = wx.ListBox(choices=[], id=wxID_FRAME2LISTBOXFTE,
              name='listBoxFte', parent=self.NBFuentePersonal, pos=wx.Point(8,
              64), size=wx.Size(131, 248), style=wx.HSCROLL)
        self.listBoxFte.Bind(wx.EVT_LISTBOX_DCLICK, self.OnListBoxFteDCLICK,
              id=wxID_FRAME2LISTBOXFTE)
        self.listBoxFte.Bind(wx.EVT_KEY_DOWN, self.OnListBoxFteKeyDown,
              id=wxID_FRAME2LISTBOXFTE)

        self.buttonFteNueva = wx.Button(id=wxID_FRAME2BUTTONFTENUEVA,
              label='Agregar \nfuente personal', name='buttonFteNueva',
              parent=self.NBFuentePersonal, pos=wx.Point(8, 328),
              size=wx.Size(64, 72), style=0)
        self.buttonFteNueva.Bind(wx.EVT_BUTTON, self.OnButtonFteNueva,
              id=wxID_FRAME2BUTTONFTENUEVA)

        self.staticText42 = wx.StaticText(id=wxID_FRAME2STATICTEXT42,
              label='Comentarios', name='staticText42',
              parent=self.NBFuentePersonal, pos=wx.Point(144, 304),
              size=wx.Size(88, 13), style=0)

        self.staticText37 = wx.StaticText(id=wxID_FRAME2STATICTEXT37,
              label='Confiabilidad', name='staticText37',
              parent=self.NBFuentePersonal, pos=wx.Point(144, 280),
              size=wx.Size(88, 13), style=0)

        self.staticText33 = wx.StaticText(id=wxID_FRAME2STATICTEXT33,
              label='Observaciones', name='staticText33',
              parent=self.NBFuentePersonal, pos=wx.Point(144, 224),
              size=wx.Size(96, 13), style=0)

        self.staticText28 = wx.StaticText(id=wxID_FRAME2STATICTEXT28,
              label='Lengua ind\xedgena', name='staticText28',
              parent=self.NBFuentePersonal, pos=wx.Point(144, 200),
              size=wx.Size(104, 13), style=0)

        self.staticText26 = wx.StaticText(id=wxID_FRAME2STATICTEXT26,
              label='Idioma', name='staticText26', parent=self.NBFuentePersonal,
              pos=wx.Point(144, 182), size=wx.Size(64, 13), style=0)

        self.staticText27 = wx.StaticText(id=wxID_FRAME2STATICTEXT27,
              label='Fecha de la informaci\xf3n', name='staticText27',
              parent=self.NBFuentePersonal, pos=wx.Point(144, 160),
              size=wx.Size(136, 13), style=0)

        self.staticText23 = wx.StaticText(id=wxID_FRAME2STATICTEXT23,
              label='Exportar fuente personal', name='staticText23',
              parent=self.NBFuentePersonal, pos=wx.Point(16, 416),
              size=wx.Size(136, 13), style=0)

        self.staticText25 = wx.StaticText(id=wxID_FRAME2STATICTEXT25,
              label='Conexi\xf3n con la informaci\xf3n', name='staticText25',
              parent=self.NBFuentePersonal, pos=wx.Point(144, 112),
              size=wx.Size(134, 32), style=0)

        self.staticText12 = wx.StaticText(id=wxID_FRAME2STATICTEXT12,
              label='Persona sobre quien se aporta  informaci\xf3n',
              name='staticText12', parent=self.NBFuentePersonal,
              pos=wx.Point(144, 80), size=wx.Size(112, 24), style=0)

        self.staticText24 = wx.StaticText(id=wxID_FRAME2STATICTEXT24,
              label='Nombre de la fuente personal', name='staticText24',
              parent=self.NBFuentePersonal, pos=wx.Point(144, 48),
              size=wx.Size(143, 13), style=0)

        self.staticTextFtePersona = wx.StaticText(id=wxID_FRAME2STATICTEXTFTEPERSONA,
              label='', name='staticTextFtePersona',
              parent=self.NBFuentePersonal, pos=wx.Point(368, 56),
              size=wx.Size(448, 13), style=wx.ST_NO_AUTORESIZE)

        self.staticTextRelPersona = wx.StaticText(id=wxID_FRAME2STATICTEXTRELPERSONA,
              label='', name='staticTextRelPersona',
              parent=self.NBFuentePersonal, pos=wx.Point(368, 88),
              size=wx.Size(448, 13), style=wx.ST_NO_AUTORESIZE)

        self.staticTextConexionInfo = wx.StaticText(id=wxID_FRAME2STATICTEXTCONEXIONINFO,
              label='', name='staticTextConexionInfo',
              parent=self.NBFuentePersonal, pos=wx.Point(368, 112),
              size=wx.Size(448, 13), style=wx.ST_NO_AUTORESIZE)

        self.checkBoxFteConfidencialidad = wx.CheckBox(id=wxID_FRAME2CHECKBOXFTECONFIDENCIALIDAD,
              label='', name='checkBoxFteConfidencialidad',
              parent=self.NBFuentePersonal, pos=wx.Point(159, 416),
              size=wx.Size(16, 13), style=0)
        self.checkBoxFteConfidencialidad.SetValue(False)
        self.checkBoxFteConfidencialidad.Bind(wx.EVT_CHECKBOX,
              self.OnCheckBoxFteConfidencialidadCheckbox,
              id=wxID_FRAME2CHECKBOXFTECONFIDENCIALIDAD)

        self.choiceFteTipoFecha = wx.Choice(choices=[],
              id=wxID_FRAME2CHOICEFTETIPOFECHA, name='choiceFteTipoFecha',
              parent=self.NBFuentePersonal, pos=wx.Point(287, 152),
              size=wx.Size(208, 21), style=0)
        self.choiceFteTipoFecha.Bind(wx.EVT_CHOICE, self.OnChoiceFteTipoFecha,
              id=wxID_FRAME2CHOICEFTETIPOFECHA)

        self.choiceFteIdioma = wx.Choice(choices=[],
              id=wxID_FRAME2CHOICEFTEIDIOMA, name='choiceFteIdioma',
              parent=self.NBFuentePersonal, pos=wx.Point(287, 176),
              size=wx.Size(208, 21), style=0)
        self.choiceFteIdioma.Bind(wx.EVT_CHOICE, self.OnChoiceFteIdiomaChoice,
              id=wxID_FRAME2CHOICEFTEIDIOMA)

        self.textCtrlFteObservaciones = wx.TextCtrl(id=wxID_FRAME2TEXTCTRLFTEOBSERVACIONES,
              name='textCtrlFteObservaciones', parent=self.NBFuentePersonal,
              pos=wx.Point(287, 224), size=wx.Size(392, 48),
              style=wx.TE_MULTILINE, value='')
        self.textCtrlFteObservaciones.Bind(wx.EVT_TEXT,
              self.OnTextCtrlFteObservacionesText,
              id=wxID_FRAME2TEXTCTRLFTEOBSERVACIONES)

        self.textCtrlFteComentarios = wx.TextCtrl(id=wxID_FRAME2TEXTCTRLFTECOMENTARIOS,
              name='textCtrlFteComentarios', parent=self.NBFuentePersonal,
              pos=wx.Point(287, 304), size=wx.Size(392, 48),
              style=wx.TE_MULTILINE, value='')
        self.textCtrlFteComentarios.Bind(wx.EVT_TEXT,
              self.OnTextCtrlFteComentariosText,
              id=wxID_FRAME2TEXTCTRLFTECOMENTARIOS)

        self.btnInfoFte = wx.Button(id=wxID_FRAME2BTNINFOFTE, label='I',
              name='btnInfoFte', parent=self.NBFuentePersonal, pos=wx.Point(152,
              328), size=wx.Size(24, 23), style=0)
        self.btnInfoFte.Bind(wx.EVT_BUTTON, self.OnBtnInfoFte,
              id=wxID_FRAME2BTNINFOFTE)

        self.btnAddFtePersonaRel = wx.Button(id=wxID_FRAME2BTNADDFTEPERSONAREL,
              label='+', name='btnAddFtePersonaRel',
              parent=self.NBFuentePersonal, pos=wx.Point(288, 80),
              size=wx.Size(24, 23), style=0)
        self.btnAddFtePersonaRel.Bind(wx.EVT_BUTTON, self.OnBtnAddFtePersonaRel,
              id=wxID_FRAME2BTNADDFTEPERSONAREL)

        self.buttonFteConexionInformacion = wx.Button(id=wxID_FRAME2BUTTONFTECONEXIONINFORMACION,
              label='+', name='buttonFteConexionInformacion',
              parent=self.NBFuentePersonal, pos=wx.Point(288, 104),
              size=wx.Size(24, 23), style=0)
        self.buttonFteConexionInformacion.Bind(wx.EVT_BUTTON,
              self.OnButtonFteConexionInformacion,
              id=wxID_FRAME2BUTTONFTECONEXIONINFORMACION)

        self.buttonFteActualizarDatos = wx.Button(id=wxID_FRAME2BUTTONFTEACTUALIZARDATOS,
              label='Guardar', name='buttonFteActualizarDatos',
              parent=self.NBFuentePersonal, pos=wx.Point(384, 416),
              size=wx.Size(80, 23), style=0)
        self.buttonFteActualizarDatos.Bind(wx.EVT_BUTTON,
              self.OnButtonFteActualizarDatos,
              id=wxID_FRAME2BUTTONFTEACTUALIZARDATOS)

        self.listBoxDocs = wx.ListBox(choices=[], id=wxID_FRAME2LISTBOXDOCS,
              name='listBoxDocs', parent=self.NBFuenteDocumental,
              pos=wx.Point(8, 72), size=wx.Size(160, 288), style=wx.HSCROLL)
        self.listBoxDocs.Bind(wx.EVT_LISTBOX_DCLICK, self.OnListBoxDocsDclick,
              id=wxID_FRAME2LISTBOXDOCS)
        self.listBoxDocs.Bind(wx.EVT_KEY_DOWN, self.OnListBoxDocsKeyDown1)

        self.staticText43 = wx.StaticText(id=wxID_FRAME2STATICTEXT43,
              label='Documentos', name='staticText43',
              parent=self.NBFuenteDocumental, pos=wx.Point(48, 48),
              size=wx.Size(60, 13), style=0)

        self.btnAddDoc = wx.Button(id=wxID_FRAME2BTNADDDOC,
              label='Agregar \nfuente documental', name='btnAddDoc',
              parent=self.NBFuenteDocumental, pos=wx.Point(8, 368),
              size=wx.Size(80, 80), style=0)
        self.btnAddDoc.Bind(wx.EVT_BUTTON, self.OnBtnAddDocButton,
              id=wxID_FRAME2BTNADDDOC)

        self.staticText55 = wx.StaticText(id=wxID_FRAME2STATICTEXT55,
              label='Identificaci\xf3n', name='staticText55',
              parent=self.NBFuenteDocumental, pos=wx.Point(176, 48),
              size=wx.Size(104, 13), style=0)

        self.staticText56 = wx.StaticText(id=wxID_FRAME2STATICTEXT56,
              label='Datos de la fuente', name='staticText56',
              parent=self.NBFuenteDocumental, pos=wx.Point(176, 72),
              size=wx.Size(112, 13), style=0)

        self.staticText58 = wx.StaticText(id=wxID_FRAME2STATICTEXT58,
              label='Fecha de la fuente', name='staticText58',
              parent=self.NBFuenteDocumental, pos=wx.Point(176, 120),
              size=wx.Size(112, 13), style=0)

        self.staticText59 = wx.StaticText(id=wxID_FRAME2STATICTEXT59,
              label='Nombre del sitio', name='staticText59',
              parent=self.NBFuenteDocumental, pos=wx.Point(176, 168),
              size=wx.Size(104, 13), style=0)

        self.staticText60 = wx.StaticText(id=wxID_FRAME2STATICTEXT60,
              label='Liga a la fuente', name='staticText60',
              parent=self.NBFuenteDocumental, pos=wx.Point(176, 192),
              size=wx.Size(104, 13), style=0)

        self.staticText61 = wx.StaticText(id=wxID_FRAME2STATICTEXT61,
              label='Fecha de consulta', name='staticText61',
              parent=self.NBFuenteDocumental, pos=wx.Point(176, 216),
              size=wx.Size(104, 13), style=0)

        self.staticText62 = wx.StaticText(id=wxID_FRAME2STATICTEXT62,
              label='Tipo de fuente', name='staticText62',
              parent=self.NBFuenteDocumental, pos=wx.Point(176, 144),
              size=wx.Size(112, 13), style=0)

        self.staticText63 = wx.StaticText(id=wxID_FRAME2STATICTEXT63,
              label='Idioma', name='staticText63',
              parent=self.NBFuenteDocumental, pos=wx.Point(176, 240),
              size=wx.Size(96, 13), style=0)

        self.staticText64 = wx.StaticText(id=wxID_FRAME2STATICTEXT64,
              label='Lengua ind\xedgena', name='staticText64',
              parent=self.NBFuenteDocumental, pos=wx.Point(176, 264),
              size=wx.Size(104, 13), style=0)

        self.staticText65 = wx.StaticText(id=wxID_FRAME2STATICTEXT65,
              label='Observaciones', name='staticText65',
              parent=self.NBFuenteDocumental, pos=wx.Point(176, 288),
              size=wx.Size(104, 13), style=0)

        self.staticText66 = wx.StaticText(id=wxID_FRAME2STATICTEXT66,
              label='Sobre qui\xe9n se aporta informaci\xf3n',
              name='staticText66', parent=self.NBFuenteDocumental,
              pos=wx.Point(176, 320), size=wx.Size(112, 24), style=0)

        self.staticText68 = wx.StaticText(id=wxID_FRAME2STATICTEXT68,
              label='Confiabilidad', name='staticText68',
              parent=self.NBFuenteDocumental, pos=wx.Point(176, 352),
              size=wx.Size(104, 13), style=0)

        self.staticText69 = wx.StaticText(id=wxID_FRAME2STATICTEXT69,
              label='Comentarios', name='staticText69',
              parent=self.NBFuenteDocumental, pos=wx.Point(176, 376),
              size=wx.Size(104, 13), style=0)

        self.textCtrlPubTituloParte = wx.TextCtrl(id=wxID_FRAME2TEXTCTRLPUBTITULOPARTE,
              name='textCtrlPubTituloParte', parent=self.NBFuenteDocumental,
              pos=wx.Point(296, 40), size=wx.Size(392, 21), style=0, value='')
        self.textCtrlPubTituloParte.SetMaxLength(120)

        self.textCtrlPubDatos = wx.TextCtrl(id=wxID_FRAME2TEXTCTRLPUBDATOS,
              name='textCtrlPubDatos', parent=self.NBFuenteDocumental,
              pos=wx.Point(296, 64), size=wx.Size(392, 46),
              style=wx.TE_MULTILINE, value='')
        self.textCtrlPubDatos.SetMaxLength(500)
        self.textCtrlPubDatos.Bind(wx.EVT_TEXT, self.OnTextCtrlPubTituloText,
              id=wxID_FRAME2TEXTCTRLPUBDATOS)

        self.choicePubTipoFecha = wx.Choice(choices=[],
              id=wxID_FRAME2CHOICEPUBTIPOFECHA, name='choicePubTipoFecha',
              parent=self.NBFuenteDocumental, pos=wx.Point(296, 112),
              size=wx.Size(192, 21), style=0)
        self.choicePubTipoFecha.Bind(wx.EVT_CHOICE, self.OnChoicePubTipoFecha,
              id=wxID_FRAME2CHOICEPUBTIPOFECHA)

        self.textCtrlPubNombreSitio = wx.TextCtrl(id=wxID_FRAME2TEXTCTRLPUBNOMBRESITIO,
              name='textCtrlPubNombreSitio', parent=self.NBFuenteDocumental,
              pos=wx.Point(296, 160), size=wx.Size(392, 21), style=0, value='')
        self.textCtrlPubNombreSitio.SetMaxLength(130)

        self.textCtrlPubLigaSitio = wx.TextCtrl(id=wxID_FRAME2TEXTCTRLPUBLIGASITIO,
              name='textCtrlPubLigaSitio', parent=self.NBFuenteDocumental,
              pos=wx.Point(296, 184), size=wx.Size(392, 21), style=0, value='')
        self.textCtrlPubLigaSitio.SetMaxLength(500)

        self.choicePubIdioma = wx.Choice(choices=[],
              id=wxID_FRAME2CHOICEPUBIDIOMA, name='choicePubIdioma',
              parent=self.NBFuenteDocumental, pos=wx.Point(296, 232),
              size=wx.Size(192, 21), style=0)
        self.choicePubIdioma.Bind(wx.EVT_CHOICE, self.OnChoicePubIdiomaChoice,
              id=wxID_FRAME2CHOICEPUBIDIOMA)

        self.textCtrlPubObservaciones = wx.TextCtrl(id=wxID_FRAME2TEXTCTRLPUBOBSERVACIONES,
              name='textCtrlPubObservaciones', parent=self.NBFuenteDocumental,
              pos=wx.Point(296, 280), size=wx.Size(392, 40),
              style=wx.TE_MULTILINE, value='')
        self.textCtrlPubObservaciones.Bind(wx.EVT_TEXT,
              self.OnTextCtrlPubObservacionesText,
              id=wxID_FRAME2TEXTCTRLPUBOBSERVACIONES)

        self.textCtrlPubComentarios = wx.TextCtrl(id=wxID_FRAME2TEXTCTRLPUBCOMENTARIOS,
              name='textCtrlPubComentarios', parent=self.NBFuenteDocumental,
              pos=wx.Point(296, 368), size=wx.Size(392, 40),
              style=wx.TE_MULTILINE, value='')
        self.textCtrlPubComentarios.Bind(wx.EVT_TEXT,
              self.OnTextCtrlPubComentariosText,
              id=wxID_FRAME2TEXTCTRLPUBCOMENTARIOS)

        self.btnSavePub = wx.Button(id=wxID_FRAME2BTNSAVEPUB, label='Guardar',
              name='btnSavePub', parent=self.NBFuenteDocumental,
              pos=wx.Point(392, 416), size=wx.Size(75, 23), style=0)
        self.btnSavePub.Bind(wx.EVT_BUTTON, self.onBtnSavePub,
              id=wxID_FRAME2BTNSAVEPUB)

        self.buttonPubAddPerson = wx.Button(id=wxID_FRAME2BUTTONPUBADDPERSON,
              label='+', name='buttonPubAddPerson',
              parent=self.NBFuenteDocumental, pos=wx.Point(296, 320),
              size=wx.Size(24, 23), style=0)
        self.buttonPubAddPerson.Bind(wx.EVT_BUTTON, self.OnButtonPubAddPerson,
              id=wxID_FRAME2BUTTONPUBADDPERSON)

        self.btnInfoDoc = wx.Button(id=wxID_FRAME2BTNINFODOC, label='I',
              name='btnInfoDoc', parent=self.NBFuenteDocumental,
              pos=wx.Point(167, 408), size=wx.Size(24, 23), style=0)
        self.btnInfoDoc.Bind(wx.EVT_BUTTON, self.OnBtnInfoDoc,
              id=wxID_FRAME2BTNINFODOC)

        self.staticTextPubPersona = wx.StaticText(id=wxID_FRAME2STATICTEXTPUBPERSONA,
              label='________________________________________________________',
              name='staticTextPubPersona', parent=self.NBFuenteDocumental,
              pos=wx.Point(376, 328), size=wx.Size(448, 13),
              style=wx.ST_NO_AUTORESIZE)

        self.btnDPersonaVictima = wx.Button(id=wxID_FRAME2BTNDPERSONAVICTIMA,
              label='P?', name='btnDPersonaVictima', parent=self.NBActosGral,
              pos=wx.Point(465, 92), size=wx.Size(24, 23), style=0)
        self.btnDPersonaVictima.Bind(wx.EVT_BUTTON, self.OnBtnDPersonaVictima,
              id=wxID_FRAME2BTNDPERSONAVICTIMA)

        self.btnDPersonaPerpetrador = wx.Button(id=wxID_FRAME2BTNDPERSONAPERPETRADOR,
              label='P?', name='btnDPersonaPerpetrador',
              parent=self.NBActosPerp, pos=wx.Point(368, 65), size=wx.Size(24,
              22), style=0)
        self.btnDPersonaPerpetrador.Bind(wx.EVT_BUTTON,
              self.OnBtnDPersonaPerpetrador,
              id=wxID_FRAME2BTNDPERSONAPERPETRADOR)

        self.LA1 = wx.StaticText(id=wxID_FRAME2LA1, label='Acto:', name='LA1',
              parent=self.NBActosGral, pos=wx.Point(16, 24), size=wx.Size(776,
              13), style=wx.ST_NO_AUTORESIZE)
        self.LA1.SetToolTipString('Acto actual')

        self.LA2 = wx.StaticText(id=wxID_FRAME2LA2, label='Acto:', name='LA2',
              parent=self.NBActosPerp, pos=wx.Point(16, 24), size=wx.Size(792,
              13), style=wx.ST_NO_AUTORESIZE)
        self.LA2.SetToolTipString('Acto actual')

        self.staticText73 = wx.StaticText(id=wxID_FRAME2STATICTEXT73,
              label='Localizaci\xf3n', name='staticText73',
              parent=self.NBActosGral, pos=wx.Point(344, 331), size=wx.Size(120,
              13), style=0)

        self.FALocalidad = wx.Choice(choices=[], id=wxID_FRAME2FALOCALIDAD,
              name='FALocalidad', parent=self.NBActosGral, pos=wx.Point(344,
              344), size=wx.Size(449, 21), style=0)
        self.FALocalidad.Bind(wx.EVT_CHOICE, self.OnFALocalidadChoice,
              id=wxID_FRAME2FALOCALIDAD)

        self.listBoxActoPerpetradores = wx.ListBox(choices=[],
              id=wxID_FRAME2LISTBOXACTOPERPETRADORES,
              name='listBoxActoPerpetradores', parent=self.NBActosGral,
              pos=wx.Point(16, 320), size=wx.Size(304, 136), style=wx.HSCROLL)

        self.staticText74 = wx.StaticText(id=wxID_FRAME2STATICTEXT74,
              label='Perpetradores', name='staticText74',
              parent=self.NBActosGral, pos=wx.Point(120, 304), size=wx.Size(128,
              13), style=0)

        self.staticText80 = wx.StaticText(id=wxID_FRAME2STATICTEXT80,
              label='Fecha inicial', name='staticText80',
              parent=self.NBPersonasBio, pos=wx.Point(24, 256), size=wx.Size(72,
              13), style=0)

        self.FBFechaFinalTipo = wx.Choice(choices=[],
              id=wxID_FRAME2FBFECHAFINALTIPO, name='FBFechaFinalTipo',
              parent=self.NBPersonasBio, pos=wx.Point(119, 272),
              size=wx.Size(217, 21), style=0)
        self.FBFechaFinalTipo.SetToolTipString('')
        self.FBFechaFinalTipo.Bind(wx.EVT_CHOICE, self.OnFBFechaFinalTipoChoice,
              id=wxID_FRAME2FBFECHAFINALTIPO)

        self.FBFechaInicialTipo = wx.Choice(choices=[],
              id=wxID_FRAME2FBFECHAINICIALTIPO, name='FBFechaInicialTipo',
              parent=self.NBPersonasBio, pos=wx.Point(119, 248),
              size=wx.Size(217, 21), style=0)
        self.FBFechaInicialTipo.SetToolTipString('')
        self.FBFechaInicialTipo.Bind(wx.EVT_CHOICE,
              self.OnFBFechaInicialTipoChoice,
              id=wxID_FRAME2FBFECHAINICIALTIPO)

        self.staticText82 = wx.StaticText(id=wxID_FRAME2STATICTEXT82,
              label='Observaciones', name='staticText82',
              parent=self.NBPersonasBio, pos=wx.Point(24, 344), size=wx.Size(96,
              13), style=0)

        self.FBObservaciones = wx.TextCtrl(id=wxID_FRAME2FBOBSERVACIONES,
              name='FBObservaciones', parent=self.NBPersonasBio,
              pos=wx.Point(24, 360), size=wx.Size(384, 64),
              style=wx.TE_MULTILINE, value='')
        self.FBObservaciones.SetToolTipString('')
        self.FBObservaciones.Bind(wx.EVT_TEXT, self.OnFBObservacionesText,
              id=wxID_FRAME2FBOBSERVACIONES)

        self.btnSaveVinculo = wx.Button(id=wxID_FRAME2BTNSAVEVINCULO,
              label='Guardar', name='btnSaveVinculo', parent=self.NBPersonasBio,
              pos=wx.Point(392, 472), size=wx.Size(75, 23), style=0)
        self.btnSaveVinculo.Bind(wx.EVT_BUTTON, self.OnBtnSaveVinculo,
              id=wxID_FRAME2BTNSAVEVINCULO)

        self.staticText72 = wx.StaticText(id=wxID_FRAME2STATICTEXT72,
              label='Fecha de la intervenci\xf3n', name='staticText72',
              parent=self.NBIntervenciones, pos=wx.Point(208, 160),
              size=wx.Size(144, 13), style=0)

        self.staticText83 = wx.StaticText(id=wxID_FRAME2STATICTEXT83,
              label='Qui\xe9n inicia o realiza esta intervenci\xf3n',
              name='staticText83', parent=self.NBIntervenciones,
              pos=wx.Point(208, 96), size=wx.Size(120, 32), style=0)

        self.staticText84 = wx.StaticText(id=wxID_FRAME2STATICTEXT84,
              label='Impacto de la intervenci\xf3n', name='staticText84',
              parent=self.NBIntervenciones, pos=wx.Point(208, 288),
              size=wx.Size(112, 24), style=0)

        self.staticText85 = wx.StaticText(id=wxID_FRAME2STATICTEXT85,
              label='Comentarios', name='staticText85',
              parent=self.NBIntervenciones, pos=wx.Point(208, 392),
              size=wx.Size(88, 13), style=0)

        self.staticText86 = wx.StaticText(id=wxID_FRAME2STATICTEXT86,
              label='Respuesta a la intervenci\xf3n', name='staticText86',
              parent=self.NBIntervenciones, pos=wx.Point(208, 240),
              size=wx.Size(120, 24), style=0)

        self.txtIntComentarios = wx.TextCtrl(id=wxID_FRAME2TXTINTCOMENTARIOS,
              name='txtIntComentarios', parent=self.NBIntervenciones,
              pos=wx.Point(352, 392), size=wx.Size(400, 72),
              style=wx.TE_MULTILINE, value='')
        self.txtIntComentarios.Bind(wx.EVT_TEXT, self.OnTxtIntComentariosText,
              id=wxID_FRAME2TXTINTCOMENTARIOS)

        self.txtIntObservaciones = wx.TextCtrl(id=wxID_FRAME2TXTINTOBSERVACIONES,
              name='txtIntObservaciones', parent=self.NBIntervenciones,
              pos=wx.Point(352, 336), size=wx.Size(400, 48),
              style=wx.TE_MULTILINE, value='')
        self.txtIntObservaciones.Bind(wx.EVT_TEXT,
              self.OnTxtIntObservacionesText,
              id=wxID_FRAME2TXTINTOBSERVACIONES)

        self.staticText88 = wx.StaticText(id=wxID_FRAME2STATICTEXT88,
              label='Observaciones', name='staticText88',
              parent=self.NBIntervenciones, pos=wx.Point(208, 336),
              size=wx.Size(112, 13), style=0)

        self.staticText89 = wx.StaticText(id=wxID_FRAME2STATICTEXT89,
              label='Exportar dato biogr\xe1fico', name='staticText89',
              parent=self.NBPersonasBio, pos=wx.Point(656, 208),
              size=wx.Size(117, 13), style=0)

        self.FBConfidencialidad = wx.CheckBox(id=wxID_FRAME2FBCONFIDENCIALIDAD,
              label='', name='FBConfidencialidad', parent=self.NBPersonasBio,
              pos=wx.Point(783, 208), size=wx.Size(16, 13), style=0)
        self.FBConfidencialidad.SetValue(False)
        self.FBConfidencialidad.Bind(wx.EVT_CHECKBOX,
              self.OnFBConfidencialidadCheckbox,
              id=wxID_FRAME2FBCONFIDENCIALIDAD)

        self.staticText90 = wx.StaticText(id=wxID_FRAME2STATICTEXT90,
              label='Rango', name='staticText90', parent=self.NBPersonasBio,
              pos=wx.Point(432, 432), size=wx.Size(40, 13), style=0)

        self.FBComentarios = wx.TextCtrl(id=wxID_FRAME2FBCOMENTARIOS,
              name='FBComentarios', parent=self.NBPersonasBio, pos=wx.Point(432,
              360), size=wx.Size(392, 64), style=wx.TE_MULTILINE, value='')
        self.FBComentarios.SetToolTipString('')
        self.FBComentarios.Bind(wx.EVT_TEXT, self.OnFBComentariosText,
              id=wxID_FRAME2FBCOMENTARIOS)

        self.staticText91 = wx.StaticText(id=wxID_FRAME2STATICTEXT91,
              label='Comentarios', name='staticText91',
              parent=self.NBPersonasBio, pos=wx.Point(440, 344),
              size=wx.Size(80, 13), style=0)

        self.FBRango = wx.TextCtrl(id=wxID_FRAME2FBRANGO, name='FBRango',
              parent=self.NBPersonasBio, pos=wx.Point(432, 448),
              size=wx.Size(392, 21), style=0, value='')
        self.FBRango.SetMaxLength(100)
        self.FBRango.SetToolTipString('')

        self.staticText93 = wx.StaticText(id=wxID_FRAME2STATICTEXT93,
              label='Puesto o cargo', name='staticText93',
              parent=self.NBPersonasBio, pos=wx.Point(24, 432), size=wx.Size(88,
              13), style=0)

        self.FBPuesto = wx.TextCtrl(id=wxID_FRAME2FBPUESTO, name='FBPuesto',
              parent=self.NBPersonasBio, pos=wx.Point(24, 448),
              size=wx.Size(384, 21), style=0, value='')
        self.FBPuesto.SetMaxLength(100)
        self.FBPuesto.SetToolTipString('')

        self.btnNuevaPersona = wx.Button(id=wxID_FRAME2BTNNUEVAPERSONA,
              label='Nueva persona', name='btnNuevaPersona',
              parent=self.NBPersonasGral, pos=wx.Point(40, 360),
              size=wx.Size(96, 24), style=0)
        self.btnNuevaPersona.Bind(wx.EVT_BUTTON, self.OnBtnNuevaPersona,
              id=wxID_FRAME2BTNNUEVAPERSONA)

        self.srchPersona = wx.TextCtrl(id=wxID_FRAME2SRCHPERSONA,
              name='srchPersona', parent=self.NBPersonasGral, pos=wx.Point(40,
              64), size=wx.Size(296, 21), style=0, value='')
        self.srchPersona.Bind(wx.EVT_TEXT, self.OnSrchPersonaText,
              id=wxID_FRAME2SRCHPERSONA)

        self.CPTipo = wx.StaticText(id=wxID_FRAME2CPTIPO, label='Tipo de grupo',
              name='CPTipo', parent=self.NBPersonasGral, pos=wx.Point(352, 104),
              size=wx.Size(128, 13), style=0)

        self.btnPantAnterior = wx.Button(id=wxID_FRAME2BTNPANTANTERIOR,
              label='<-- Pantalla anterior', name='btnPantAnterior',
              parent=self.NBPersonasGral, pos=wx.Point(648, 8),
              size=wx.Size(115, 23), style=0)
        self.btnPantAnterior.Show(False)
        self.btnPantAnterior.Bind(wx.EVT_BUTTON, self.OnBtnPantAnterior,
              id=wxID_FRAME2BTNPANTANTERIOR)

        self.btnDPersonaFuente = wx.Button(id=wxID_FRAME2BTNDPERSONAFUENTE,
              label='P?', name='btnDPersonaFuente',
              parent=self.NBFuentePersonal, pos=wx.Point(288, 48),
              size=wx.Size(24, 23), style=0)
        self.btnDPersonaFuente.Bind(wx.EVT_BUTTON,
              self.OnBtnDPersonaFuenteButton, id=wxID_FRAME2BTNDPERSONAFUENTE)

        self.btnDPersonaRel = wx.Button(id=wxID_FRAME2BTNDPERSONAREL,
              label='P?', name='btnDPersonaRel', parent=self.NBFuentePersonal,
              pos=wx.Point(336, 80), size=wx.Size(24, 23), style=0)
        self.btnDPersonaRel.Bind(wx.EVT_BUTTON, self.OnBtnDPersonaRel,
              id=wxID_FRAME2BTNDPERSONAREL)

        self.btnDPersonaRel2 = wx.Button(id=wxID_FRAME2BTNDPERSONAREL2,
              label='P?', name='btnDPersonaRel2',
              parent=self.NBFuenteDocumental, pos=wx.Point(344, 320),
              size=wx.Size(24, 23), style=0)
        self.btnDPersonaRel2.Bind(wx.EVT_BUTTON, self.OnBtnDPersonaRel2,
              id=wxID_FRAME2BTNDPERSONAREL2)

        self.btnDPersonaSobre = wx.Button(id=wxID_FRAME2BTNDPERSONASOBRE,
              label='P?', name='btnDPersonaSobre', parent=self.NBIntervenciones,
              pos=wx.Point(400, 176), size=wx.Size(24, 23), style=0)
        self.btnDPersonaSobre.Bind(wx.EVT_BUTTON, self.OnBtnDPersonaSobre,
              id=wxID_FRAME2BTNDPERSONASOBRE)

        self.btnDPersonaAquien = wx.Button(id=wxID_FRAME2BTNDPERSONAAQUIEN,
              label='P?', name='btnDPersonaAquien',
              parent=self.NBIntervenciones, pos=wx.Point(400, 201),
              size=wx.Size(24, 23), style=0)
        self.btnDPersonaAquien.Bind(wx.EVT_BUTTON, self.OnBtnDPersonaAquien,
              id=wxID_FRAME2BTNDPERSONAAQUIEN)

        self.CasoIsearch = wx.TextCtrl(id=wxID_FRAME2CASOISEARCH,
              name='CasoIsearch', parent=self.NBCasosGral, pos=wx.Point(16, 72),
              size=wx.Size(312, 21), style=0, value='')
        self.CasoIsearch.Bind(wx.EVT_TEXT, self.OnCasoIsearchEnter,
              id=wxID_FRAME2CASOISEARCH)

        self.FPPais = wx.StaticText(id=wxID_FRAME2FPPAIS,
              label='______________________', name='FPPais',
              parent=self.NBPersonasGral, pos=wx.Point(584, 256),
              size=wx.Size(112, 13), style=0)

        self.FPCiudadania = wx.StaticText(id=wxID_FRAME2FPCIUDADANIA,
              label='_________________________________________________',
              name='FPCiudadania', parent=self.NBPersonasGral, pos=wx.Point(584,
              355), size=wx.Size(248, 13), style=0)

        self.btnFPPais = wx.Button(id=wxID_FRAME2BTNFPPAIS, label='+',
              name='btnFPPais', parent=self.NBPersonasGral, pos=wx.Point(520,
              248), size=wx.Size(24, 23), style=0)
        self.btnFPPais.Bind(wx.EVT_BUTTON, self.OnBtnFPPais,
              id=wxID_FRAME2BTNFPPAIS)

        self.btnFPCiudadania = wx.Button(id=wxID_FRAME2BTNFPCIUDADANIA,
              label='+', name='btnFPCiudadania', parent=self.NBPersonasGral,
              pos=wx.Point(520, 347), size=wx.Size(24, 23), style=0)
        self.btnFPCiudadania.Bind(wx.EVT_BUTTON, self.OnBtnFPCiudadaniaButton,
              id=wxID_FRAME2BTNFPCIUDADANIA)

        self.staticText94 = wx.StaticText(id=wxID_FRAME2STATICTEXT94,
              label='Fecha de recepci\xf3n', name='staticText94',
              parent=self.NBCasosAdm, pos=wx.Point(16, 32), size=wx.Size(104,
              13), style=0)

        self.staticTextEdadOcurreActo = wx.StaticText(id=wxID_FRAME2STATICTEXTEDADOCURREACTO,
              label='Edad cuando ocurri\xf3 el acto',
              name='staticTextEdadOcurreActo', parent=self.NBActosGral,
              pos=wx.Point(344, 313), size=wx.Size(176, 13), style=0)

        self.staticText101 = wx.StaticText(id=wxID_FRAME2STATICTEXT101,
              label='Fecha de recepci\xf3n', name='staticText101',
              parent=self.NBPersonasAdm, pos=wx.Point(80, 355),
              size=wx.Size(136, 13), style=0)

        self.staticText103 = wx.StaticText(id=wxID_FRAME2STATICTEXT103,
              label='Proyecto local', name='staticText103',
              parent=self.NBPersonasAdm, pos=wx.Point(80, 376), size=wx.Size(80,
              13), style=0)

        self.staticText100 = wx.StaticText(id=wxID_FRAME2STATICTEXT100,
              label='Proyecto conjunto RedTDT', name='staticText100',
              parent=self.NBPersonasAdm, pos=wx.Point(80, 408),
              size=wx.Size(136, 24), style=0)

        self.staticText102 = wx.StaticText(id=wxID_FRAME2STATICTEXT102,
              label='Proyecto SE', name='staticText102',
              parent=self.NBPersonasAdm, pos=wx.Point(80, 432), size=wx.Size(80,
              13), style=0)
        self.staticText102.Show(False)

        self.FPproyecto_se = wx.TextCtrl(id=wxID_FRAME2FPPROYECTO_SE,
              name='FPproyecto_se', parent=self.NBPersonasAdm, pos=wx.Point(216,
              424), size=wx.Size(432, 21), style=0, value='')
        self.FPproyecto_se.Show(False)

        self.FPproyecto_conjunto = wx.TextCtrl(id=wxID_FRAME2FPPROYECTO_CONJUNTO,
              name='FPproyecto_conjunto', parent=self.NBPersonasAdm,
              pos=wx.Point(216, 400), size=wx.Size(432, 21), style=0, value='')

        self.FPproyecto_grupo = wx.TextCtrl(id=wxID_FRAME2FPPROYECTO_GRUPO,
              name='FPproyecto_grupo', parent=self.NBPersonasAdm,
              pos=wx.Point(216, 376), size=wx.Size(432, 21), style=0, value='')

        self.staticText104 = wx.StaticText(id=wxID_FRAME2STATICTEXT104,
              label='Exportar persona', name='staticText104',
              parent=self.NBPersonasGral, pos=wx.Point(40, 392),
              size=wx.Size(84, 13), style=0)

        self.FPconfidencialidad = wx.CheckBox(id=wxID_FRAME2FPCONFIDENCIALIDAD,
              label='', name='FPconfidencialidad', parent=self.NBPersonasGral,
              pos=wx.Point(208, 392), size=wx.Size(24, 13), style=0)
        self.FPconfidencialidad.SetValue(False)
        self.FPconfidencialidad.Bind(wx.EVT_CHECKBOX,
              self.OnFPconfidencialidadCheckbox,
              id=wxID_FRAME2FPCONFIDENCIALIDAD)

        self.staticText105 = wx.StaticText(id=wxID_FRAME2STATICTEXT105,
              label='B\xfasqueda r\xe1pida', name='staticText105',
              parent=self.NBCasosGral, pos=wx.Point(16, 59), size=wx.Size(80,
              13), style=0)

        self.btnSearch = wx.Button(id=wxID_FRAME2BTNSEARCH,
              label='B\xfasqueda exhaustiva', name='btnSearch',
              parent=self.NBCasosGral, pos=wx.Point(16, 96), size=wx.Size(136,
              23), style=0)
        self.btnSearch.SetToolTipString('Busqueda exhaustiva de casos')
        self.btnSearch.Bind(wx.EVT_BUTTON, self.OnBtnSearchButton,
              id=wxID_FRAME2BTNSEARCH)

        self.btnSerachExecute = wx.Button(id=wxID_FRAME2BTNSERACHEXECUTE,
              label='Aplicar', name='btnSerachExecute', parent=self.NBCasosGral,
              pos=wx.Point(160, 96), size=wx.Size(64, 23), style=0)
        self.btnSerachExecute.SetToolTipString('Aplicar busqueda')
        self.btnSerachExecute.Bind(wx.EVT_BUTTON, self.OnBtnSearchExecuteButton,
              id=wxID_FRAME2BTNSERACHEXECUTE)

        self.btnShowAll = wx.Button(id=wxID_FRAME2BTNSHOWALL,
              label='Mostrar todo', name='btnShowAll', parent=self.NBCasosGral,
              pos=wx.Point(232, 96), size=wx.Size(96, 23), style=0)
        self.btnShowAll.SetToolTipString('Desaplicar busqueda')
        self.btnShowAll.Bind(wx.EVT_BUTTON, self.OnBtnShowAllButton,
              id=wxID_FRAME2BTNSHOWALL)

        self.NBCasosRelaciones = wx.Panel(id=wxID_FRAME2NBCASOSRELACIONES,
              name='NBCasosRelaciones', parent=self.NBCasos, pos=wx.Point(0, 0),
              size=wx.Size(844, 567), style=wx.TAB_TRAVERSAL)
        self.NBCasosRelaciones.SetLabel('NBCasosRelaciones')

        self.listBoxCasoRel = wx.ListBox(choices=[],
              id=wxID_FRAME2LISTBOXCASOREL, name='listBoxCasoRel',
              parent=self.NBCasosRelaciones, pos=wx.Point(24, 72),
              size=wx.Size(784, 120), style=wx.HSCROLL)
        self.listBoxCasoRel.SetLabel('')
        self.listBoxCasoRel.SetToolTipString('Casos relacionados.\nSelecciona con doble clic para alterar sus caracter\xedscticas')
        self.listBoxCasoRel.SetAutoLayout(True)
        self.listBoxCasoRel.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnListBoxCasoRelListboxDclick, id=wxID_FRAME2LISTBOXCASOREL)

        self.staticText71 = wx.StaticText(id=wxID_FRAME2STATICTEXT71,
              label='Caso relacionado', name='staticText71',
              parent=self.NBCasosRelaciones, pos=wx.Point(24, 338),
              size=wx.Size(82, 30), style=0)

        self.btnAddRelacion = wx.Button(id=wxID_FRAME2BTNADDRELACION,
              label='Nueva relaci\xf3n', name='btnAddRelacion',
              parent=self.NBCasosRelaciones, pos=wx.Point(24, 200),
              size=wx.Size(96, 23), style=0)
        self.btnAddRelacion.SetToolTipString('')
        self.btnAddRelacion.Bind(wx.EVT_BUTTON, self.OnBtnAddRelacionButton,
              id=wxID_FRAME2BTNADDRELACION)

        self.FRCCasoRelComentarios = wx.TextCtrl(id=wxID_FRAME2FRCCASORELCOMENTARIOS,
              name='FRCCasoRelComentarios', parent=self.NBCasosRelaciones,
              pos=wx.Point(368, 344), size=wx.Size(440, 80),
              style=wx.TE_MULTILINE, value='')
        self.FRCCasoRelComentarios.Bind(wx.EVT_TEXT,
              self.OnFRCCasoRelComentariosText,
              id=wxID_FRAME2FRCCASORELCOMENTARIOS)
        self.FRCCasoRelComentarios.Bind(wx.EVT_KILL_FOCUS,
              self.OnFRCCasoRelComentariosKillFocus)

        self.FRCCasoRelObservaciones = wx.TextCtrl(id=wxID_FRAME2FRCCASORELOBSERVACIONES,
              name='FRCCasoRelObservaciones', parent=self.NBCasosRelaciones,
              pos=wx.Point(368, 216), size=wx.Size(440, 80),
              style=wx.TE_MULTILINE, value='')
        self.FRCCasoRelObservaciones.Bind(wx.EVT_TEXT,
              self.OnFRCCasoRelObservacionesText,
              id=wxID_FRAME2FRCCASORELOBSERVACIONES)
        self.FRCCasoRelObservaciones.Bind(wx.EVT_KILL_FOCUS,
              self.OnFRCCasoRelObservacionesKillFocus)

        self.staticText106 = wx.StaticText(id=wxID_FRAME2STATICTEXT106,
              label='Comentarios', name='staticText106',
              parent=self.NBCasosRelaciones, pos=wx.Point(368, 328),
              size=wx.Size(120, 13), style=0)

        self.staticText107 = wx.StaticText(id=wxID_FRAME2STATICTEXT107,
              label='Relacionado con', name='staticText107',
              parent=self.NBCasosRelaciones, pos=wx.Point(24, 56),
              size=wx.Size(78, 13), style=0)

        self.staticText108 = wx.StaticText(id=wxID_FRAME2STATICTEXT108,
              label='Observaciones', name='staticText108',
              parent=self.NBCasosRelaciones, pos=wx.Point(368, 200),
              size=wx.Size(128, 13), style=0)

        self.staticText109 = wx.StaticText(id=wxID_FRAME2STATICTEXT109,
              label='Relaci\xf3n entre casos', name='staticText109',
              parent=self.NBCasosRelaciones, pos=wx.Point(24, 248),
              size=wx.Size(99, 32), style=0)

        self.btnCasoRel = wx.Button(id=wxID_FRAME2BTNCASOREL, label='+',
              name='btnCasoRel', parent=self.NBCasosRelaciones,
              pos=wx.Point(136, 328), size=wx.Size(24, 23), style=0)
        self.btnCasoRel.SetToolTipString('Asignar el caso relacionado')
        self.btnCasoRel.Bind(wx.EVT_BUTTON, self.OnBtnCasoRelButton,
              id=wxID_FRAME2BTNCASOREL)

        self.btnTipoRelCaso = wx.Button(id=wxID_FRAME2BTNTIPORELCASO, label='+',
              name='btnTipoRelCaso', parent=self.NBCasosRelaciones,
              pos=wx.Point(136, 240), size=wx.Size(24, 23), style=0)
        self.btnTipoRelCaso.SetToolTipString(u'Asignar tipo de relaci\xf3n')
        self.btnTipoRelCaso.Bind(wx.EVT_BUTTON, self.OnBtnTipoRelCasoButton,
              id=wxID_FRAME2BTNTIPORELCASO)

        self.FRCCasoRelTipo = wx.StaticText(id=wxID_FRAME2FRCCASORELTIPO,
              label='_________________', name='FRCCasoRelTipo',
              parent=self.NBCasosRelaciones, pos=wx.Point(176, 240),
              size=wx.Size(176, 40), style=wx.ST_NO_AUTORESIZE)

        self.FRCCasoRel = wx.StaticText(id=wxID_FRAME2FRCCASOREL,
              label='_________________', name='FRCCasoRel',
              parent=self.NBCasosRelaciones, pos=wx.Point(176, 328),
              size=wx.Size(176, 40), style=wx.ST_NO_AUTORESIZE)

        self.FPOtroNombre = wx.TextCtrl(id=wxID_FRAME2FPOTRONOMBRE,
              name='FPOtroNombre', parent=self.NBPersonasGral, pos=wx.Point(520,
              176), size=wx.Size(288, 21), style=0, value='')
        self.FPOtroNombre.SetMaxLength(200)
        self.FPOtroNombre.Bind(wx.EVT_KILL_FOCUS, self.OnFPOtroNombreKillFocus)

        self.staticText110 = wx.StaticText(id=wxID_FRAME2STATICTEXT110,
              label='Otro nombre', name='staticText110',
              parent=self.NBPersonasGral, pos=wx.Point(352, 184),
              size=wx.Size(112, 13), style=0)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME2STATICLINE1,
              name='staticLine1', parent=self.NBActosPerp, pos=wx.Point(17, 64),
              size=wx.Size(895, 2), style=0)

        self.NBNormatividad = wx.Panel(id=wxID_FRAME2NBNORMATIVIDAD,
              name='NBNormatividad', parent=self.NBActos, pos=wx.Point(0, 0),
              size=wx.Size(844, 567), style=wx.TAB_TRAVERSAL)
        self.NBNormatividad.SetToolTipString('')

        self.btnActoLegislacion = wx.Button(id=wxID_FRAME2BTNACTOLEGISLACION,
              label='+', name='btnActoLegislacion', parent=self.NBNormatividad,
              pos=wx.Point(8, 120), size=wx.Size(32, 23), style=0)
        self.btnActoLegislacion.SetToolTipString('Agregar una legislacion')
        self.btnActoLegislacion.Bind(wx.EVT_BUTTON, self.OnBtnActoLegislacion,
              id=wxID_FRAME2BTNACTOLEGISLACION)
        self.btnActoLegislacion.Bind(wx.EVT_KEY_DOWN,
              self.OnBtnActoLegislacionKeyDown)

        self.btnActoInstrInt = wx.Button(id=wxID_FRAME2BTNACTOINSTRINT,
              label='+', name='btnActoInstrInt', parent=self.NBNormatividad,
              pos=wx.Point(8, 232), size=wx.Size(32, 23), style=0)
        self.btnActoInstrInt.SetToolTipString('Agregar un instrumento internacional')
        self.btnActoInstrInt.Bind(wx.EVT_BUTTON, self.OnBtnActoInstrInt,
              id=wxID_FRAME2BTNACTOINSTRINT)

        self.FAInstr = wx.ListBox(choices=[], id=wxID_FRAME2FAINSTR,
              name='FAInstr', parent=self.NBNormatividad, pos=wx.Point(48, 232),
              size=wx.Size(392, 72), style=wx.HSCROLL)
        self.FAInstr.SetToolTipString('')
        self.FAInstr.Bind(wx.EVT_LISTBOX_DCLICK, self.OnFAInstrListboxDclick,
              id=wxID_FRAME2FAINSTR)
        self.FAInstr.Bind(wx.EVT_KEY_DOWN, self.OnFAInstrKeyDown)

        self.FALegis = wx.ListBox(choices=[], id=wxID_FRAME2FALEGIS,
              name='FALegis', parent=self.NBNormatividad, pos=wx.Point(48, 120),
              size=wx.Size(392, 72), style=wx.HSCROLL)
        self.FALegis.SetToolTipString('')
        self.FALegis.Bind(wx.EVT_LISTBOX_DCLICK, self.OnFALegisListboxDclick,
              id=wxID_FRAME2FALEGIS)
        self.FALegis.Bind(wx.EVT_KEY_DOWN, self.OnBtnActoLegislacionKeyDown)

        self.staticText95 = wx.StaticText(id=wxID_FRAME2STATICTEXT95,
              label='Legislaci\xf3n nacional', name='staticText95',
              parent=self.NBNormatividad, pos=wx.Point(48, 104),
              size=wx.Size(272, 13), style=0)

        self.staticText97 = wx.StaticText(id=wxID_FRAME2STATICTEXT97,
              label='Instrumentos internacionales', name='staticText97',
              parent=self.NBNormatividad, pos=wx.Point(48, 216),
              size=wx.Size(256, 13), style=0)

        self.FAinstrumentos_int_notas = wx.TextCtrl(id=wxID_FRAME2FAINSTRUMENTOS_INT_NOTAS,
              name='FAinstrumentos_int_notas', parent=self.NBNormatividad,
              pos=wx.Point(456, 232), size=wx.Size(376, 72),
              style=wx.TE_MULTILINE, value='')
        self.FAinstrumentos_int_notas.SetMaxLength(0)
        self.FAinstrumentos_int_notas.SetToolTipString('')
        self.FAinstrumentos_int_notas.Bind(wx.EVT_KILL_FOCUS,
              self.OnFAinstrumentos_internacionales_notasKillFocus)
        self.FAinstrumentos_int_notas.Bind(wx.EVT_TEXT,
              self.OnFAinstrumentos_int_notasText,
              id=wxID_FRAME2FAINSTRUMENTOS_INT_NOTAS)

        self.FAlegislacion_nacional_notas = wx.TextCtrl(id=wxID_FRAME2FALEGISLACION_NACIONAL_NOTAS,
              name='FAlegislacion_nacional_notas', parent=self.NBNormatividad,
              pos=wx.Point(456, 120), size=wx.Size(376, 72),
              style=wx.TE_MULTILINE, value='')
        self.FAlegislacion_nacional_notas.SetMaxLength(0)
        self.FAlegislacion_nacional_notas.SetToolTipString('')
        self.FAlegislacion_nacional_notas.Bind(wx.EVT_KILL_FOCUS,
              self.OnFAlegislacion_nacional_notasKillFocus)
        self.FAlegislacion_nacional_notas.Bind(wx.EVT_TEXT,
              self.OnFAlegislacion_nacional_notasText,
              id=wxID_FRAME2FALEGISLACION_NACIONAL_NOTAS)

        self.staticText98 = wx.StaticText(id=wxID_FRAME2STATICTEXT98,
              label='Notas', name='staticText98', parent=self.NBNormatividad,
              pos=wx.Point(456, 104), size=wx.Size(40, 13), style=0)

        self.staticText96 = wx.StaticText(id=wxID_FRAME2STATICTEXT96,
              label='Notas', name='staticText96', parent=self.NBNormatividad,
              pos=wx.Point(456, 216), size=wx.Size(40, 13), style=0)

        self.staticLine2 = wx.StaticLine(id=wxID_FRAME2STATICLINE2,
              name='staticLine2', parent=self.NBNormatividad, pos=wx.Point(32,
              56), size=wx.Size(792, 2), style=0)

        self.btnTipodeacto = wx.Button(id=wxID_FRAME2BTNTIPODEACTO, label='+',
              name='btnTipodeacto', parent=self.NBActosGral, pos=wx.Point(465,
              40), size=wx.Size(24, 23), style=0)
        self.btnTipodeacto.Bind(wx.EVT_BUTTON, self.OnBtnTipodeactoButton,
              id=wxID_FRAME2BTNTIPODEACTO)

        self.FAedad_victima = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAME2FAEDAD_VICTIMA,
              name='FAedad_victima', parent=self.NBActosGral, pos=wx.Point(665,
              309), size=wx.Size(32, 21), style=0, value='')
        self.FAedad_victima.SetMask('###')
        self.FAedad_victima.SetAutoformat('')
        self.FAedad_victima.SetDatestyle('MDY')
        self.FAedad_victima.SetFormatcodes('')
        self.FAedad_victima.SetDescription('')
        self.FAedad_victima.SetExcludeChars('')
        self.FAedad_victima.SetValidRegex('')

        self.FPNodependientes = wx.lib.intctrl.IntCtrl(allow_long=True,
              allow_none=True, default_color=wx.BLACK,
              id=wxID_FRAME2FPNODEPENDIENTES, limited=False, max=10000000000L,
              min=0, name='FPNodependientes', oob_color=wx.RED,
              parent=self.NBPersonasDetalles, pos=wx.Point(168, 320),
              size=wx.Size(136, 21), style=0, value=0)

        self.buttonRemoveTipodelugar = wx.Button(id=wxID_FRAME2BUTTONREMOVETIPODELUGAR,
              label='X', name='buttonRemoveTipodelugar',
              parent=self.NBActosGral, pos=wx.Point(489, 224), size=wx.Size(24,
              23), style=0)
        self.buttonRemoveTipodelugar.Bind(wx.EVT_BUTTON,
              self.OnButtonRemoveTipodelugarButton,
              id=wxID_FRAME2BUTTONREMOVETIPODELUGAR)

        self.buttonRemoveEstatusdelavictima = wx.Button(id=wxID_FRAME2BUTTONREMOVEESTATUSDELAVICTIMA,
              label='X', name='buttonRemoveEstatusdelavictima',
              parent=self.NBActosGral, pos=wx.Point(489, 279), size=wx.Size(24,
              23), style=0)
        self.buttonRemoveEstatusdelavictima.Bind(wx.EVT_BUTTON,
              self.OnButtonRemoveEstatusdelavictimaButton,
              id=wxID_FRAME2BUTTONREMOVEESTATUSDELAVICTIMA)

        self.buttonRemoveEstatusVDH = wx.Button(id=wxID_FRAME2BUTTONREMOVEESTATUSVDH,
              label='X', name='buttonRemoveEstatusVDH', parent=self.NBActosGral,
              pos=wx.Point(489, 255), size=wx.Size(24, 23), style=0)
        self.buttonRemoveEstatusVDH.Bind(wx.EVT_BUTTON,
              self.OnButtonRemoveEstatusVDHButton,
              id=wxID_FRAME2BUTTONREMOVEESTATUSVDH)

        self.buttonRemoveDequien = wx.Button(id=wxID_FRAME2BUTTONREMOVEDEQUIEN,
              label='X', name='buttonRemoveDequien',
              parent=self.NBIntervenciones, pos=wx.Point(376, 176),
              size=wx.Size(24, 23), style=0)
        self.buttonRemoveDequien.Bind(wx.EVT_BUTTON,
              self.OnButtonRemoveDequienButton,
              id=wxID_FRAME2BUTTONREMOVEDEQUIEN)

        self.buttonRemoveAquien = wx.Button(id=wxID_FRAME2BUTTONREMOVEAQUIEN,
              label='X', name='buttonRemoveAquien',
              parent=self.NBIntervenciones, pos=wx.Point(376, 201),
              size=wx.Size(24, 23), style=0)
        self.buttonRemoveAquien.Bind(wx.EVT_BUTTON,
              self.OnButtonRemoveAquienButton,
              id=wxID_FRAME2BUTTONREMOVEAQUIEN)

        self.buttonRemoveFteConexionInf = wx.Button(id=wxID_FRAME2BUTTONREMOVEFTECONEXIONINF,
              label='X', name='buttonRemoveFteConexionInf',
              parent=self.NBFuentePersonal, pos=wx.Point(312, 104),
              size=wx.Size(24, 23), style=0)
        self.buttonRemoveFteConexionInf.Bind(wx.EVT_BUTTON,
              self.OnButtonRemoveFteConexionInformacionButton,
              id=wxID_FRAME2BUTTONREMOVEFTECONEXIONINF)

        self.btnRemoveFtePersonaRel = wx.Button(id=wxID_FRAME2BTNREMOVEFTEPERSONAREL,
              label='X', name='btnRemoveFtePersonaRel',
              parent=self.NBFuentePersonal, pos=wx.Point(312, 80),
              size=wx.Size(24, 23), style=0)
        self.btnRemoveFtePersonaRel.Bind(wx.EVT_BUTTON,
              self.OnBtnRemoveFtePersonaRelButton,
              id=wxID_FRAME2BTNREMOVEFTEPERSONAREL)

        self.buttonPubRemovePerson = wx.Button(id=wxID_FRAME2BUTTONPUBREMOVEPERSON,
              label='X', name='buttonPubRemovePerson',
              parent=self.NBFuenteDocumental, pos=wx.Point(320, 320),
              size=wx.Size(24, 23), style=0)
        self.buttonPubRemovePerson.Bind(wx.EVT_BUTTON,
              self.OnButtonPubRemovePersonButton,
              id=wxID_FRAME2BUTTONPUBREMOVEPERSON)

        self.buttonRemoveUltStatusPerp = wx.Button(id=wxID_FRAME2BUTTONREMOVEULTSTATUSPERP,
              label='X', name='buttonRemoveUltStatusPerp',
              parent=self.NBActosPerp, pos=wx.Point(368, 169), size=wx.Size(24,
              23), style=0)
        self.buttonRemoveUltStatusPerp.Bind(wx.EVT_BUTTON,
              self.OnButtonRemoveUltStatusPerpButton,
              id=wxID_FRAME2BUTTONREMOVEULTSTATUSPERP)

        self.buttonRemoveTipoPerp = wx.Button(id=wxID_FRAME2BUTTONREMOVETIPOPERP,
              label='X', name='buttonRemoveTipoPerp', parent=self.NBActosPerp,
              pos=wx.Point(368, 136), size=wx.Size(24, 23), style=0)
        self.buttonRemoveTipoPerp.Bind(wx.EVT_BUTTON,
              self.OnButtonRemoveTipoPerpButton,
              id=wxID_FRAME2BUTTONREMOVETIPOPERP)

        self.buttonRemoveGradoInvol = wx.Button(id=wxID_FRAME2BUTTONREMOVEGRADOINVOL,
              label='X', name='buttonRemoveGradoInvol', parent=self.NBActosPerp,
              pos=wx.Point(368, 105), size=wx.Size(24, 23), style=0)
        self.buttonRemoveGradoInvol.Bind(wx.EVT_BUTTON,
              self.OnButtonRemoveGradoInvolButton,
              id=wxID_FRAME2BUTTONREMOVEGRADOINVOL)

        self.btnRemoveFPPais = wx.Button(id=wxID_FRAME2BTNREMOVEFPPAIS,
              label='X', name='btnRemoveFPPais', parent=self.NBPersonasGral,
              pos=wx.Point(544, 248), size=wx.Size(24, 23), style=0)
        self.btnRemoveFPPais.Bind(wx.EVT_BUTTON, self.OnBtnRemoveFPPaisButton,
              id=wxID_FRAME2BTNREMOVEFPPAIS)

        self.btnRemoveFPCiudadania = wx.Button(id=wxID_FRAME2BTNREMOVEFPCIUDADANIA,
              label='X', name='btnRemoveFPCiudadania',
              parent=self.NBPersonasGral, pos=wx.Point(544, 347),
              size=wx.Size(24, 23), style=0)
        self.btnRemoveFPCiudadania.Bind(wx.EVT_BUTTON,
              self.OnBtnRemoveFPCiudadaniaButton,
              id=wxID_FRAME2BTNREMOVEFPCIUDADANIA)

        self.choiceTipoEdad = wx.Choice(choices=['', 'Edad aproximada',
              'Edad precisa'], id=wxID_FRAME2CHOICETIPOEDAD,
              name='choiceTipoEdad', parent=self.NBActosGral, pos=wx.Point(529,
              309), size=wx.Size(112, 21), style=0)
        self.choiceTipoEdad.Bind(wx.EVT_CHOICE, self.OnChoiceTipoEdadChoice,
              id=wxID_FRAME2CHOICETIPOEDAD)

        self.listPersonaVinculosDB = wx.ListBox(choices=[],
              id=wxID_FRAME2LISTPERSONAVINCULOSDB, name='listPersonaVinculosDB',
              parent=self.NBPersonasGral, pos=wx.Point(40, 432),
              size=wx.Size(792, 56), style=wx.HSCROLL)
        self.listPersonaVinculosDB.SetToolTipString('Haz doble clic para brincar al caso relacionado')
        self.listPersonaVinculosDB.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnListPersonaVinculosDBListboxDclick,
              id=wxID_FRAME2LISTPERSONAVINCULOSDB)

        self.staticPersonaActual1 = wx.StaticText(id=wxID_FRAME2STATICPERSONAACTUAL1,
              label='___', name='staticPersonaActual1',
              parent=self.NBPersonasDetalles, pos=wx.Point(24, 8),
              size=wx.Size(776, 32), style=wx.ST_NO_AUTORESIZE)
        self.staticPersonaActual1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL,
              wx.BOLD, False, 'Tahoma'))
        self.staticPersonaActual1.SetToolTipString('Persona actual')

        self.staticPersonaActual2 = wx.StaticText(id=wxID_FRAME2STATICPERSONAACTUAL2,
              label='___', name='staticPersonaActual2',
              parent=self.NBPersonasAdm, pos=wx.Point(24, 8), size=wx.Size(768,
              28), style=wx.ST_NO_AUTORESIZE)
        self.staticPersonaActual2.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL,
              wx.BOLD, False, 'Tahoma'))
        self.staticPersonaActual2.SetToolTipString('Persona actual')

        self.staticPersonaActual3 = wx.StaticText(id=wxID_FRAME2STATICPERSONAACTUAL3,
              label='___', name='staticPersonaActual3',
              parent=self.NBPersonasBio, pos=wx.Point(24, 8), size=wx.Size(776,
              27), style=wx.ST_NO_AUTORESIZE)
        self.staticPersonaActual3.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL,
              wx.BOLD, False, 'Tahoma'))
        self.staticPersonaActual3.SetToolTipString('Persona actual')

        self.staticPersonaActual0 = wx.StaticText(id=wxID_FRAME2STATICPERSONAACTUAL0,
              label='______________________________________________________________',
              name='staticPersonaActual0', parent=self.NBPersonasGral,
              pos=wx.Point(352, 40), size=wx.Size(456, 53),
              style=wx.ST_NO_AUTORESIZE)
        self.staticPersonaActual0.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL,
              wx.BOLD, False, 'Tahoma'))
        self.staticPersonaActual0.SetToolTipString('Persona actual')

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self.NBPersonasGral,
              pos=wx.Point(792, 8), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.contextHelpButton1.SetToolTipString('Ayuda contextual')
        self.contextHelpButton1.Bind(wx.EVT_HELP, self.OnContextHelpButton1Help,
              id=wxID_FRAME2CONTEXTHELPBUTTON1)

        self.contextHelpButton2 = wx.ContextHelpButton(parent=self.NBCasosGral,
              pos=wx.Point(800, 8), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.contextHelpButton2.SetToolTipString('Ayuda contextual')

        self.contextHelpButton3 = wx.ContextHelpButton(parent=self.NBCasosNarrativa,
              pos=wx.Point(800, 8), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.contextHelpButton3.SetToolTipString('Ayuda contextual')

        self.contextHelpButton4 = wx.ContextHelpButton(parent=self.NBCasosAdm,
              pos=wx.Point(744, 8), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.contextHelpButton4.SetToolTipString('Ayuda contextual')

        self.contextHelpButton5 = wx.ContextHelpButton(parent=self.NBCasosTipifica,
              pos=wx.Point(800, 5), size=wx.Size(24, 27), style=wx.BU_AUTODRAW)
        self.contextHelpButton5.SetToolTipString('Ayuda contextual')

        self.contextHelpButton6 = wx.ContextHelpButton(parent=self.NBCasosRelaciones,
              pos=wx.Point(816, 8), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.contextHelpButton6.SetToolTipString('Ayuda contextual')

        self.contextHelpButton7 = wx.ContextHelpButton(parent=self.NBNormatividad,
              pos=wx.Point(808, 8), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.contextHelpButton7.SetToolTipString('Ayuda contextual')

        self.contextHelpButton8 = wx.ContextHelpButton(parent=self.NBActosGral,
              pos=wx.Point(816, 8), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.contextHelpButton8.SetToolTipString('Ayuda contextual')

        self.contextHelpButton9 = wx.ContextHelpButton(parent=self.NBActosPerp,
              pos=wx.Point(816, 0), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.contextHelpButton9.SetToolTipString('Ayuda contextual')

        self.contextHelpButton10 = wx.ContextHelpButton(parent=self.NBIntervenciones,
              pos=wx.Point(800, 8), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.contextHelpButton10.SetToolTipString('Ayuda contextual')

        self.contextHelpButton13 = wx.ContextHelpButton(parent=self.NBPersonasDetalles,
              pos=wx.Point(808, 0), size=wx.Size(28, 27), style=wx.BU_AUTODRAW)
        self.contextHelpButton13.SetToolTipString('Ayuda contextual')

        self.contextHelpButton14 = wx.ContextHelpButton(parent=self.NBPersonasAdm,
              pos=wx.Point(808, 8), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.contextHelpButton14.SetToolTipString('Ayuda contextual')

        self.contextHelpButton15 = wx.ContextHelpButton(parent=self.NBPersonasBio,
              pos=wx.Point(808, 8), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.contextHelpButton15.SetToolTipString('Ayuda contextual')

        self.txtIntParte = wx.StaticText(id=wxID_FRAME2TXTINTPARTE,
              label='___________________________________________________________',
              name='txtIntParte', parent=self.NBIntervenciones,
              pos=wx.Point(424, 92), size=wx.Size(354, 52),
              style=wx.ST_NO_AUTORESIZE)

        self.btnIntPInt = wx.Button(id=wxID_FRAME2BTNINTPINT, label='+',
              name='btnIntPInt', parent=self.NBIntervenciones, pos=wx.Point(352,
              92), size=wx.Size(24, 23), style=0)
        self.btnIntPInt.Bind(wx.EVT_BUTTON, self.OnBtnIntPIntButton,
              id=wxID_FRAME2BTNINTPINT)

        self.txtIntRespuesta = wx.TextCtrl(id=wxID_FRAME2TXTINTRESPUESTA,
              name='txtIntRespuesta', parent=self.NBIntervenciones,
              pos=wx.Point(352, 240), size=wx.Size(400, 48),
              style=wx.TE_MULTILINE, value='')
        self.txtIntRespuesta.Bind(wx.EVT_TEXT, self.OnTxtIntRespuestaText,
              id=wxID_FRAME2TXTINTRESPUESTA)

        self.txtIntImpacto = wx.TextCtrl(id=wxID_FRAME2TXTINTIMPACTO,
              name='txtIntImpacto', parent=self.NBIntervenciones,
              pos=wx.Point(352, 288), size=wx.Size(400, 48),
              style=wx.TE_MULTILINE, value='')
        self.txtIntImpacto.Bind(wx.EVT_TEXT, self.OnTxtIntImpactoText,
              id=wxID_FRAME2TXTINTIMPACTO)

        self.staticText10 = wx.StaticText(id=wxID_FRAME2STATICTEXT10,
              label='Fecha final', name='staticText10',
              parent=self.NBPersonasBio, pos=wx.Point(24, 280), size=wx.Size(64,
              13), style=0)

        self.staticText70 = wx.StaticText(id=wxID_FRAME2STATICTEXT70,
              label='Fecha de vigencia', name='staticText70',
              parent=self.NBPersonasBio, pos=wx.Point(24, 304), size=wx.Size(96,
              32), style=0)

        self.FBFechaInfo_vigenteTipo = wx.Choice(choices=[],
              id=wxID_FRAME2FBFECHAINFO_VIGENTETIPO,
              name='FBFechaInfo_vigenteTipo', parent=self.NBPersonasBio,
              pos=wx.Point(119, 297), size=wx.Size(217, 21), style=0)
        self.FBFechaInfo_vigenteTipo.SetToolTipString('')
        self.FBFechaInfo_vigenteTipo.Bind(wx.EVT_CHOICE,
              self.OnFBFechaInfo_vigenteTipoChoice,
              id=wxID_FRAME2FBFECHAINFO_VIGENTETIPO)

        self.staticText92 = wx.StaticText(id=wxID_FRAME2STATICTEXT92,
              label='Descripci\xf3n', name='staticText92',
              parent=self.NBPersonasBio, pos=wx.Point(24, 181), size=wx.Size(72,
              13), style=0)

        self.FBDescripcion = wx.TextCtrl(id=wxID_FRAME2FBDESCRIPCION,
              name='FBDescripcion', parent=self.NBPersonasBio, pos=wx.Point(120,
              177), size=wx.Size(704, 20), style=0, value='')
        self.FBDescripcion.SetMaxLength(200)

        self.txtPubTipoPub = wx.StaticText(id=wxID_FRAME2TXTPUBTIPOPUB,
              label='_________________________________________________________',
              name='txtPubTipoPub', parent=self.NBFuenteDocumental,
              pos=wx.Point(368, 142), size=wx.Size(464, 13),
              style=wx.ST_NO_AUTORESIZE)

        self.btnRemovePubTipoPub = wx.Button(id=wxID_FRAME2BTNREMOVEPUBTIPOPUB,
              label='X', name='btnRemovePubTipoPub',
              parent=self.NBFuenteDocumental, pos=wx.Point(320, 132),
              size=wx.Size(24, 24), style=0)
        self.btnRemovePubTipoPub.Bind(wx.EVT_BUTTON,
              self.OnBtnRemovePubTipoPubButton,
              id=wxID_FRAME2BTNREMOVEPUBTIPOPUB)

        self.btnPubTipoPub = wx.Button(id=wxID_FRAME2BTNPUBTIPOPUB, label='+',
              name='btnPubTipoPub', parent=self.NBFuenteDocumental,
              pos=wx.Point(296, 132), size=wx.Size(24, 24), style=0)
        self.btnPubTipoPub.Bind(wx.EVT_BUTTON, self.OnBtnPubTipoPubButton,
              id=wxID_FRAME2BTNPUBTIPOPUB)

        self.txtTotalCasos = wx.StaticText(id=wxID_FRAME2TXTTOTALCASOS,
              label="'    '", name='txtTotalCasos', parent=self.NBCasosGral,
              pos=wx.Point(17, 26), size=wx.Size(16, 14), style=0)

        self.txtTotalPersonas = wx.StaticText(id=wxID_FRAME2TXTTOTALPERSONAS,
              label='    ', name='txtTotalPersonas', parent=self.NBPersonasGral,
              pos=wx.Point(40, 8), size=wx.Size(12, 13), style=0)
        self.txtTotalPersonas.SetToolTipString('')
        self.txtTotalPersonas.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.LC12 = wx.StaticText(id=wxID_FRAME2LC12, label='Caso:',
              name='LC12', parent=self.NBCasosRelaciones, pos=wx.Point(16, 8),
              size=wx.Size(30, 13), style=0)
        self.LC12.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))
        self.LC12.SetToolTipString('Caso actual')

        self.LC14 = wx.StaticText(id=wxID_FRAME2LC14, label='Caso:',
              name='LC14', parent=self.NBNormatividad, pos=wx.Point(16, 8),
              size=wx.Size(600, 13), style=0)
        self.LC14.SetToolTipString('Caso actual')

        self.LA14 = wx.StaticText(id=wxID_FRAME2LA14, label='Acto:',
              name='LA14', parent=self.NBNormatividad, pos=wx.Point(16, 24),
              size=wx.Size(600, 13), style=0)
        self.LA14.SetToolTipString('Acto actual')

        self.LC15 = wx.StaticText(id=wxID_FRAME2LC15, label='Caso:',
              name='LC15', parent=self.NBFuenteDocumental, pos=wx.Point(16, 8),
              size=wx.Size(600, 13), style=0)
        self.LC15.SetToolTipString('Caso actual')

        self.buttonSelPerpetrador = wx.Button(id=wxID_FRAME2BUTTONSELPERPETRADOR,
              label='+', name='buttonSelPerpetrador', parent=self.NBActosPerp,
              pos=wx.Point(344, 64), size=wx.Size(24, 23), style=0)
        self.buttonSelPerpetrador.Bind(wx.EVT_BUTTON,
              self.OnButtonSelPerpetradorButton,
              id=wxID_FRAME2BUTTONSELPERPETRADOR)

        self.txtLongNarra = wx.StaticText(id=wxID_FRAME2TXTLONGNARRA,
              label='   ', name='txtLongNarra', parent=self.NBCasosNarrativa,
              pos=wx.Point(696, 64), size=wx.Size(24, 13), style=0)

        self.txtLongResDesc = wx.StaticText(id=wxID_FRAME2TXTLONGRESDESC,
              label='   ', name='txtLongResDesc', parent=self.NBCasosNarrativa,
              pos=wx.Point(696, 184), size=wx.Size(9, 13), style=0)

        self.txtLongObs = wx.StaticText(id=wxID_FRAME2TXTLONGOBS, label='   ',
              name='txtLongObs', parent=self.NBCasosNarrativa, pos=wx.Point(696,
              288), size=wx.Size(9, 13), style=0)

        self.staticTxtPrelacionada = wx.StaticText(id=wxID_FRAME2STATICTXTPRELACIONADA,
              label='P. relacionada', name='staticTxtPrelacionada',
              parent=self.NBPersonasBio, pos=wx.Point(24, 231), size=wx.Size(80,
              13), style=0)

        self.btnTipoVinculo = wx.Button(id=wxID_FRAME2BTNTIPOVINCULO, label='+',
              name='btnTipoVinculo', parent=self.NBPersonasBio,
              pos=wx.Point(120, 199), size=wx.Size(24, 23), style=0)
        self.btnTipoVinculo.SetToolTipString('')
        self.btnTipoVinculo.Bind(wx.EVT_BUTTON, self.OnBtnTipoVinculoButton,
              id=wxID_FRAME2BTNTIPOVINCULO)

        self.txtTipoVinculo = wx.StaticText(id=wxID_FRAME2TXTTIPOVINCULO,
              label='    ', name='txtTipoVinculo', parent=self.NBPersonasBio,
              pos=wx.Point(152, 208), size=wx.Size(12, 13), style=0)

        self.btnDPersonaParteInt = wx.Button(id=wxID_FRAME2BTNDPERSONAPARTEINT,
              label='P?', name='btnDPersonaParteInt',
              parent=self.NBIntervenciones, pos=wx.Point(376, 91),
              size=wx.Size(24, 24), style=0)
        self.btnDPersonaParteInt.Bind(wx.EVT_BUTTON,
              self.OnBtnDPersonaParteIntButton,
              id=wxID_FRAME2BTNDPERSONAPARTEINT)

        self.buttonActualizarCaso3 = wx.Button(id=wxID_FRAME2BUTTONACTUALIZARCASO3,
              label='Guardar', name='buttonActualizarCaso3',
              parent=self.NBCasosAdm, pos=wx.Point(352, 424), size=wx.Size(75,
              23), style=0)
        self.buttonActualizarCaso3.SetToolTipString('Guarda informacion del caso')
        self.buttonActualizarCaso3.Bind(wx.EVT_BUTTON,
              self.OnButtonActualizarCaso3Button,
              id=wxID_FRAME2BUTTONACTUALIZARCASO3)

        self.CFIdia = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2CFIDIA, limited=False,
              max=31, min=1, name='CFIdia', oob_color=wx.RED,
              parent=self.NBCasosGral, pos=wx.Point(688, 168), size=wx.Size(24,
              21), style=0, value=0)

        self.CFIanio = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME2CFIANIO,
              limited=False, max=None, min=None, name='CFIanio',
              oob_color=wx.RED, parent=self.NBCasosGral, pos=wx.Point(752, 168),
              size=wx.Size(40, 21), style=0, value=0)
        self.CFIanio.SetInsertionPoint(0)

        self.CFImes = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2CFIMES, limited=False,
              max=None, min=None, name='CFImes', oob_color=wx.RED,
              parent=self.NBCasosGral, pos=wx.Point(720, 168), size=wx.Size(24,
              21), style=0, value=0)

        self.CFFdia = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2CFFDIA, limited=False,
              max=None, min=None, name='CFFdia', oob_color=wx.RED,
              parent=self.NBCasosGral, pos=wx.Point(688, 192), size=wx.Size(24,
              21), style=0, value=0)

        self.CFFmes = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2CFFMES, limited=False,
              max=None, min=None, name='CFFmes', oob_color=wx.RED,
              parent=self.NBCasosGral, pos=wx.Point(720, 192), size=wx.Size(24,
              21), style=0, value=0)

        self.CFFanio = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME2CFFANIO,
              limited=False, max=None, min=None, name='CFFanio',
              oob_color=wx.RED, parent=self.NBCasosGral, pos=wx.Point(752, 192),
              size=wx.Size(40, 21), style=0, value=0)
        self.CFFanio.SetInsertionPoint(0)

        self.AFIdia = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2AFIDIA, limited=False,
              max=None, min=None, name='AFIdia', oob_color=wx.RED,
              parent=self.NBActosGral, pos=wx.Point(681, 128), size=wx.Size(24,
              21), style=0, value=0)

        self.AFImes = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2AFIMES, limited=False,
              max=None, min=None, name='AFImes', oob_color=wx.RED,
              parent=self.NBActosGral, pos=wx.Point(713, 128), size=wx.Size(24,
              21), style=0, value=0)

        self.AFIanio = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME2AFIANIO,
              limited=False, max=None, min=None, name='AFIanio',
              oob_color=wx.RED, parent=self.NBActosGral, pos=wx.Point(745, 128),
              size=wx.Size(40, 21), style=0, value=0)
        self.AFIanio.SetInsertionPoint(0)

        self.AFFdia = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2AFFDIA, limited=False,
              max=None, min=None, name='AFFdia', oob_color=wx.RED,
              parent=self.NBActosGral, pos=wx.Point(681, 152), size=wx.Size(24,
              21), style=0, value=0)

        self.AFFmes = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2AFFMES, limited=False,
              max=None, min=None, name='AFFmes', oob_color=wx.RED,
              parent=self.NBActosGral, pos=wx.Point(713, 152), size=wx.Size(24,
              21), style=0, value=0)

        self.AFFanio = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME2AFFANIO,
              limited=False, max=None, min=None, name='AFFanio',
              oob_color=wx.RED, parent=self.NBActosGral, pos=wx.Point(745, 152),
              size=wx.Size(40, 21), style=0, value=0)
        self.AFFanio.SetInsertionPoint(0)

        self.IFdia = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2IFDIA, limited=False,
              max=None, min=None, name='IFdia', oob_color=wx.RED,
              parent=self.NBIntervenciones, pos=wx.Point(536, 152),
              size=wx.Size(24, 21), style=0, value=0)

        self.IFmes = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2IFMES, limited=False,
              max=None, min=None, name='IFmes', oob_color=wx.RED,
              parent=self.NBIntervenciones, pos=wx.Point(568, 152),
              size=wx.Size(24, 21), style=0, value=0)

        self.IFanio = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2IFANIO, limited=False,
              max=None, min=None, name='IFanio', oob_color=wx.RED,
              parent=self.NBIntervenciones, pos=wx.Point(600, 152),
              size=wx.Size(40, 21), style=0, value=0)
        self.IFanio.SetInsertionPoint(0)

        self.FPFdia = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2FPFDIA, limited=False,
              max=None, min=None, name='FPFdia', oob_color=wx.RED,
              parent=self.NBFuentePersonal, pos=wx.Point(528, 152),
              size=wx.Size(24, 21), style=0, value=0)

        self.FPFmes = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2FPFMES, limited=False,
              max=None, min=None, name='FPFmes', oob_color=wx.RED,
              parent=self.NBFuentePersonal, pos=wx.Point(560, 152),
              size=wx.Size(24, 21), style=0, value=0)

        self.FPFanio = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME2FPFANIO,
              limited=False, max=None, min=None, name='FPFanio',
              oob_color=wx.RED, parent=self.NBFuentePersonal, pos=wx.Point(592,
              152), size=wx.Size(40, 21), style=0, value=0)
        self.FPFanio.SetInsertionPoint(0)

        self.FDFCdia = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME2FDFCDIA,
              limited=False, max=None, min=None, name='FDFCdia',
              oob_color=wx.RED, parent=self.NBFuenteDocumental,
              pos=wx.Point(584, 208), size=wx.Size(24, 21), style=0, value=0)

        self.FDFCmes = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME2FDFCMES,
              limited=False, max=None, min=None, name='FDFCmes',
              oob_color=wx.RED, parent=self.NBFuenteDocumental,
              pos=wx.Point(616, 208), size=wx.Size(24, 21), style=0, value=0)

        self.FDFCanio = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME2FDFCANIO,
              limited=False, max=None, min=None, name='FDFCanio',
              oob_color=wx.RED, parent=self.NBFuenteDocumental,
              pos=wx.Point(648, 208), size=wx.Size(40, 21), style=0, value=0)
        self.FDFCanio.SetInsertionPoint(0)

        self.FDFdia = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2FDFDIA, limited=False,
              max=None, min=None, name='FDFdia', oob_color=wx.RED,
              parent=self.NBFuenteDocumental, pos=wx.Point(568, 112),
              size=wx.Size(24, 21), style=0, value=0)

        self.FDFmes = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2FDFMES, limited=False,
              max=None, min=None, name='FDFmes', oob_color=wx.RED,
              parent=self.NBFuenteDocumental, pos=wx.Point(600, 112),
              size=wx.Size(24, 21), style=0, value=0)

        self.FDFanio = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME2FDFANIO,
              limited=False, max=None, min=None, name='FDFanio',
              oob_color=wx.RED, parent=self.NBFuenteDocumental,
              pos=wx.Point(632, 112), size=wx.Size(40, 21), style=0, value=0)
        self.FDFanio.SetInsertionPoint(0)

        self.PFNdia = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2PFNDIA, limited=False,
              max=None, min=None, name='PFNdia', oob_color=wx.RED,
              parent=self.NBPersonasGral, pos=wx.Point(704, 224),
              size=wx.Size(24, 21), style=0, value=0)

        self.PFNmes = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2PFNMES, limited=False,
              max=None, min=None, name='PFNmes', oob_color=wx.RED,
              parent=self.NBPersonasGral, pos=wx.Point(736, 224),
              size=wx.Size(24, 21), style=0, value=0)

        self.PFNanio = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME2PFNANIO,
              limited=False, max=None, min=None, name='PFNanio',
              oob_color=wx.RED, parent=self.NBPersonasGral, pos=wx.Point(768,
              224), size=wx.Size(40, 21), style=0, value=0)
        self.PFNanio.SetInsertionPoint(0)

        self.PFRdia = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2PFRDIA, limited=False,
              max=None, min=None, name='PFRdia', oob_color=wx.RED,
              parent=self.NBPersonasAdm, pos=wx.Point(440, 352),
              size=wx.Size(24, 21), style=0, value=0)

        self.PFRmes = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2PFRMES, limited=False,
              max=None, min=None, name='PFRmes', oob_color=wx.RED,
              parent=self.NBPersonasAdm, pos=wx.Point(472, 352),
              size=wx.Size(24, 21), style=0, value=0)

        self.PFRanio = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME2PFRANIO,
              limited=False, max=None, min=None, name='PFRanio',
              oob_color=wx.RED, parent=self.NBPersonasAdm, pos=wx.Point(504,
              352), size=wx.Size(40, 21), style=0, value=0)
        self.PFRanio.SetInsertionPoint(0)

        self.BFIdia = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2BFIDIA, limited=False,
              max=None, min=None, name='BFIdia', oob_color=wx.RED,
              parent=self.NBPersonasBio, pos=wx.Point(360, 248),
              size=wx.Size(24, 21), style=0, value=0)
        self.BFIdia.SetToolTipString('')

        self.BFImes = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2BFIMES, limited=False,
              max=None, min=None, name='BFImes', oob_color=wx.RED,
              parent=self.NBPersonasBio, pos=wx.Point(392, 248),
              size=wx.Size(24, 21), style=0, value=0)
        self.BFImes.SetToolTipString('')

        self.BFIanio = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME2BFIANIO,
              limited=False, max=None, min=None, name='BFIanio',
              oob_color=wx.RED, parent=self.NBPersonasBio, pos=wx.Point(424,
              248), size=wx.Size(40, 21), style=0, value=0)
        self.BFIanio.SetInsertionPoint(0)
        self.BFIanio.SetToolTipString('')

        self.BFFdia = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2BFFDIA, limited=False,
              max=None, min=None, name='BFFdia', oob_color=wx.RED,
              parent=self.NBPersonasBio, pos=wx.Point(360, 272),
              size=wx.Size(24, 21), style=0, value=0)
        self.BFFdia.SetToolTipString('')

        self.BFFmes = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2BFFMES, limited=False,
              max=None, min=None, name='BFFmes', oob_color=wx.RED,
              parent=self.NBPersonasBio, pos=wx.Point(392, 272),
              size=wx.Size(24, 21), style=0, value=0)
        self.BFFmes.SetToolTipString('')

        self.BFFanio = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME2BFFANIO,
              limited=False, max=None, min=None, name='BFFanio',
              oob_color=wx.RED, parent=self.NBPersonasBio, pos=wx.Point(424,
              272), size=wx.Size(40, 21), style=0, value=0)
        self.BFFanio.SetInsertionPoint(0)
        self.BFFanio.SetToolTipString('')

        self.BFVdia = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2BFVDIA, limited=False,
              max=None, min=None, name='BFVdia', oob_color=wx.RED,
              parent=self.NBPersonasBio, pos=wx.Point(360, 297),
              size=wx.Size(24, 21), style=0, value=0)
        self.BFVdia.SetToolTipString('')

        self.BFVmes = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2BFVMES, limited=False,
              max=None, min=None, name='BFVmes', oob_color=wx.RED,
              parent=self.NBPersonasBio, pos=wx.Point(392, 297),
              size=wx.Size(24, 21), style=0, value=0)
        self.BFVmes.SetToolTipString('')

        self.BFVanio = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME2BFVANIO,
              limited=False, max=None, min=None, name='BFVanio',
              oob_color=wx.RED, parent=self.NBPersonasBio, pos=wx.Point(424,
              297), size=wx.Size(40, 21), style=0, value=0)
        self.BFVanio.SetInsertionPoint(0)
        self.BFVanio.SetToolTipString('')

        self.FPTipodefecharecepcion = wx.Choice(choices=[],
              id=wxID_FRAME2FPTIPODEFECHARECEPCION,
              name='FPTipodefecharecepcion', parent=self.NBPersonasAdm,
              pos=wx.Point(216, 352), size=wx.Size(192, 21), style=0)
        self.FPTipodefecharecepcion.Bind(wx.EVT_CHOICE,
              self.OnFPTipodefecharecepcionChoice,
              id=wxID_FRAME2FPTIPODEFECHARECEPCION)

        self.choiceIntTipofecha = wx.Choice(choices=[],
              id=wxID_FRAME2CHOICEINTTIPOFECHA, name='choiceIntTipofecha',
              parent=self.NBIntervenciones, pos=wx.Point(352, 152),
              size=wx.Size(184, 21), style=0)
        self.choiceIntTipofecha.Bind(wx.EVT_CHOICE,
              self.OnChoiceIntTipofechaChoice,
              id=wxID_FRAME2CHOICEINTTIPOFECHA)

        self.choicePubTipofechaconsulta = wx.Choice(choices=[],
              id=wxID_FRAME2CHOICEPUBTIPOFECHACONSULTA,
              name='choicePubTipofechaconsulta', parent=self.NBFuenteDocumental,
              pos=wx.Point(296, 208), size=wx.Size(192, 21), style=0)
        self.choicePubTipofechaconsulta.Bind(wx.EVT_CHOICE,
              self.OnChoicePubTipofechaconsultaChoice,
              id=wxID_FRAME2CHOICEPUBTIPOFECHACONSULTA)

        self.FCtipo_frecepcion = wx.Choice(choices=[],
              id=wxID_FRAME2FCTIPO_FRECEPCION, name='FCtipo_frecepcion',
              parent=self.NBCasosAdm, pos=wx.Point(176, 32), size=wx.Size(216,
              21), style=0)
        self.FCtipo_frecepcion.Bind(wx.EVT_CHOICE,
              self.OnFCtipo_frecepcionChoice, id=wxID_FRAME2FCTIPO_FRECEPCION)

        self.CFRdia = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2CFRDIA, limited=False,
              max=None, min=None, name='CFRdia', oob_color=wx.RED,
              parent=self.NBCasosAdm, pos=wx.Point(400, 32), size=wx.Size(24,
              21), style=0, value=0)

        self.CFRmes = wx.lib.intctrl.IntCtrl(allow_long=False, allow_none=False,
              default_color=wx.BLACK, id=wxID_FRAME2CFRMES, limited=False,
              max=None, min=None, name='CFRmes', oob_color=wx.RED,
              parent=self.NBCasosAdm, pos=wx.Point(432, 32), size=wx.Size(24,
              21), style=0, value=0)

        self.CFRanio = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME2CFRANIO,
              limited=False, max=None, min=None, name='CFRanio',
              oob_color=wx.RED, parent=self.NBCasosAdm, pos=wx.Point(464, 32),
              size=wx.Size(40, 21), style=0, value=0)
        self.CFRanio.SetInsertionPoint(0)

        self.btnLocMasInfo = wx.Button(id=wxID_FRAME2BTNLOCMASINFO,
              label='M\xe1s \ninformaci\xf3n', name='btnLocMasInfo',
              parent=self.NBCasosGral, pos=wx.Point(720, 320), size=wx.Size(80,
              40), style=0)
        self.btnLocMasInfo.SetToolTipString('Mas informaci\xf3n sobre una localizaci\xf3n')
        self.btnLocMasInfo.Bind(wx.EVT_BUTTON, self.OnBtnLocMasInfoButton,
              id=wxID_FRAME2BTNLOCMASINFO)

        self.btnAbrirLiga = wx.Button(id=wxID_FRAME2BTNABRIRLIGA,
              label='Abrir liga', name='btnAbrirLiga',
              parent=self.NBFuenteDocumental, pos=wx.Point(696, 184),
              size=wx.Size(75, 23), style=0)
        self.btnAbrirLiga.Bind(wx.EVT_BUTTON, self.OnBtnAbrirLigaButton,
              id=wxID_FRAME2BTNABRIRLIGA)

        self.Pguardar2 = wx.Button(id=wxID_FRAME2PGUARDAR2, label='Guardar',
              name='Pguardar2', parent=self.NBPersonasDetalles,
              pos=wx.Point(368, 472), size=wx.Size(75, 23), style=0)
        self.Pguardar2.Bind(wx.EVT_BUTTON, self.OnPguardar2Button,
              id=wxID_FRAME2PGUARDAR2)

        self.Pguardar3 = wx.Button(id=wxID_FRAME2PGUARDAR3, label='Guardar',
              name='Pguardar3', parent=self.NBPersonasAdm, pos=wx.Point(328,
              456), size=wx.Size(75, 23), style=0)
        self.Pguardar3.Bind(wx.EVT_BUTTON, self.OnPguardar3Button,
              id=wxID_FRAME2PGUARDAR3)

        self.crGuardar = wx.Button(id=wxID_FRAME2CRGUARDAR, label='Guardar',
              name='crGuardar', parent=self.NBCasosRelaciones, pos=wx.Point(440,
              448), size=wx.Size(75, 23), style=0)
        self.crGuardar.SetToolTipString('Guarda relacion del caso')
        self.crGuardar.Bind(wx.EVT_BUTTON, self.OnCrGuardarButton,
              id=wxID_FRAME2CRGUARDAR)

        self.txtLongAdmArch = wx.StaticText(id=wxID_FRAME2TXTLONGADMARCH,
              label='         ', name='txtLongAdmArch', parent=self.NBCasosAdm,
              pos=wx.Point(664, 288), size=wx.Size(27, 13), style=0)
        self.txtLongAdmArch.SetToolTipString('')

        self.txtLongAdmComent = wx.StaticText(id=wxID_FRAME2TXTLONGADMCOMENT,
              label='                                    ',
              name='txtLongAdmComent', parent=self.NBCasosAdm, pos=wx.Point(664,
              160), size=wx.Size(108, 13), style=0)
        self.txtLongAdmComent.SetToolTipString('')

        self.txtLongInObs = wx.StaticText(id=wxID_FRAME2TXTLONGINOBS,
              label='  ', name='txtLongInObs', parent=self.NBActosPerp,
              pos=wx.Point(624, 216), size=wx.Size(6, 13), style=0)

        self.txtLongIntImp = wx.StaticText(id=wxID_FRAME2TXTLONGINTIMP,
              label='   ', name='txtLongIntImp', parent=self.NBIntervenciones,
              pos=wx.Point(760, 288), size=wx.Size(9, 13), style=0)

        self.txtLongIntObs = wx.StaticText(id=wxID_FRAME2TXTLONGINTOBS,
              label='   ', name='txtLongIntObs', parent=self.NBIntervenciones,
              pos=wx.Point(760, 336), size=wx.Size(9, 13), style=0)

        self.txtLongIntComent = wx.StaticText(id=wxID_FRAME2TXTLONGINTCOMENT,
              label='   ', name='txtLongIntComent',
              parent=self.NBIntervenciones, pos=wx.Point(760, 416),
              size=wx.Size(9, 13), style=0)

        self.txtLongIntRes = wx.StaticText(id=wxID_FRAME2TXTLONGINTRES,
              label='   ', name='txtLongIntRes', parent=self.NBIntervenciones,
              pos=wx.Point(760, 240), size=wx.Size(9, 13), style=0)

        self.txtLongFDObs = wx.StaticText(id=wxID_FRAME2TXTLONGFDOBS,
              label='    ', name='txtLongFDObs', parent=self.NBFuenteDocumental,
              pos=wx.Point(696, 280), size=wx.Size(12, 13), style=0)

        self.txtLongFDComent = wx.StaticText(id=wxID_FRAME2TXTLONGFDCOMENT,
              label='    ', name='txtLongFDComent',
              parent=self.NBFuenteDocumental, pos=wx.Point(696, 368),
              size=wx.Size(12, 13), style=0)

        self.txtLongFDDatos = wx.StaticText(id=wxID_FRAME2TXTLONGFDDATOS,
              label='    ', name='txtLongFDDatos',
              parent=self.NBFuenteDocumental, pos=wx.Point(696, 64),
              size=wx.Size(12, 13), style=0)

        self.txtLongFPObs = wx.StaticText(id=wxID_FRAME2TXTLONGFPOBS,
              label='    ', name='txtLongFPObs', parent=self.NBFuentePersonal,
              pos=wx.Point(696, 224), size=wx.Size(12, 13), style=0)

        self.txtLongFPComent = wx.StaticText(id=wxID_FRAME2TXTLONGFPCOMENT,
              label='    ', name='txtLongFPComent',
              parent=self.NBFuentePersonal, pos=wx.Point(696, 304),
              size=wx.Size(12, 13), style=0)

        self.txtCasosSeleccionados = wx.StaticText(id=wxID_FRAME2TXTCASOSSELECCIONADOS,
              label="'    '", name='txtCasosSeleccionados',
              parent=self.NBCasosGral, pos=wx.Point(16, 42), size=wx.Size(18,
              13), style=0)
        self.txtCasosSeleccionados.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL,
              wx.BOLD, False, 'Tahoma'))

        self.btnReps = wx.Button(id=wxID_FRAME2BTNREPS, label='Reportes',
              name='btnReps', parent=self.NBCasosGral, pos=wx.Point(208, 280),
              size=wx.Size(80, 23), style=0)
        self.btnReps.SetToolTipString('Reportes de casos')
        self.btnReps.Bind(wx.EVT_BUTTON, self.OnBtnRepsButton,
              id=wxID_FRAME2BTNREPS)

        self.btnRepsPersona = wx.Button(id=wxID_FRAME2BTNREPSPERSONA,
              label='Reportes', name='btnRepsPersona',
              parent=self.NBPersonasGral, pos=wx.Point(240, 361),
              size=wx.Size(72, 23), style=0)
        self.btnRepsPersona.Bind(wx.EVT_BUTTON, self.OnBtnRepsButton,
              id=wxID_FRAME2BTNREPSPERSONA)

        self.txtLongFAObs = wx.StaticText(id=wxID_FRAME2TXTLONGFAOBS,
              label="'  '", name='txtLongFAObs', parent=self.NBActosGral,
              pos=wx.Point(690, 368), size=wx.Size(14, 13), style=0)

        self.staticTxtTipoderelacion = wx.StaticText(id=wxID_FRAME2STATICTXTTIPODERELACION,
              label='Tipo de relaci\xf3n', name='staticTxtTipoderelacion',
              parent=self.NBPersonasBio, pos=wx.Point(24, 208), size=wx.Size(88,
              13), style=0)

        self.btnPrelacionada = wx.Button(id=wxID_FRAME2BTNPRELACIONADA,
              label='+', name='btnPrelacionada', parent=self.NBPersonasBio,
              pos=wx.Point(120, 224), size=wx.Size(24, 23), style=0)
        self.btnPrelacionada.SetToolTipString('')
        self.btnPrelacionada.Bind(wx.EVT_BUTTON, self.OnBtnPrelacionadaButton,
              id=wxID_FRAME2BTNPRELACIONADA)

        self.txtPrelacionada = wx.StaticText(id=wxID_FRAME2TXTPRELACIONADA,
              label='    ', name='txtPrelacionada', parent=self.NBPersonasBio,
              pos=wx.Point(152, 229), size=wx.Size(672, 13),
              style=wx.ST_NO_AUTORESIZE)

        self.contextHelpButton16 = wx.ContextHelpButton(parent=self.NBFuentePersonal,
              pos=wx.Point(808, 8), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.contextHelpButton16.SetToolTipString('Ayuda contextual')

        self.contextHelpButton17 = wx.ContextHelpButton(parent=self.NBFuenteDocumental,
              pos=wx.Point(800, 8), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.contextHelpButton17.SetToolTipString('Ayuda contextual')

        self.btnAddOcupacion = wx.Button(id=wxID_FRAME2BTNADDOCUPACION,
              label='+', name='btnAddOcupacion', parent=self.NBPersonasDetalles,
              pos=wx.Point(169, 40), size=wx.Size(24, 23), style=0)
        self.btnAddOcupacion.Bind(wx.EVT_BUTTON, self.OnBtnAddOcupacionButton,
              id=wxID_FRAME2BTNADDOCUPACION)

        self.FPstrOcupacion = wx.StaticText(id=wxID_FRAME2FPSTROCUPACION,
              label='    ', name='FPstrOcupacion',
              parent=self.NBPersonasDetalles, pos=wx.Point(225, 45),
              size=wx.Size(79, 13), style=0)

        self.btnDelOcupacion = wx.Button(id=wxID_FRAME2BTNDELOCUPACION,
              label='X', name='btnDelOcupacion', parent=self.NBPersonasDetalles,
              pos=wx.Point(193, 40), size=wx.Size(24, 23), style=0)
        self.btnDelOcupacion.Bind(wx.EVT_BUTTON, self.OnBtnDelOcupacionButton,
              id=wxID_FRAME2BTNDELOCUPACION)

        self.longPerObs = wx.StaticText(id=wxID_FRAME2LONGPEROBS, label='   ',
              name='longPerObs', parent=self.NBPersonasAdm, pos=wx.Point(672,
              40), size=wx.Size(9, 13), style=0)

        self.longPerCom = wx.StaticText(id=wxID_FRAME2LONGPERCOM, label='   ',
              name='longPerCom', parent=self.NBPersonasAdm, pos=wx.Point(672,
              152), size=wx.Size(9, 13), style=0)
        self.longPerCom.Bind(wx.EVT_HELP, self.OnLongPerComHelp,
              id=wxID_FRAME2LONGPERCOM)

        self.longPerArch = wx.StaticText(id=wxID_FRAME2LONGPERARCH, label='   ',
              name='longPerArch', parent=self.NBPersonasAdm, pos=wx.Point(672,
              264), size=wx.Size(9, 13), style=0)
        self.longPerArch.Bind(wx.EVT_HELP, self.OnLongPerArchHelp,
              id=wxID_FRAME2LONGPERARCH)

        self.longPerDBObs = wx.StaticText(id=wxID_FRAME2LONGPERDBOBS,
              label='          ', name='longPerDBObs',
              parent=self.NBPersonasBio, pos=wx.Point(296, 344),
              size=wx.Size(30, 13), style=0)

        self.longPerDBCom = wx.StaticText(id=wxID_FRAME2LONGPERDBCOM,
              label='           ', name='longPerDBCom',
              parent=self.NBPersonasBio, pos=wx.Point(712, 344),
              size=wx.Size(33, 13), style=0)

        self.delCaso = wx.Button(id=wxID_FRAME2DELCASO, label='Borrar caso',
              name='delCaso', parent=self.NBCasosGral, pos=wx.Point(112, 280),
              size=wx.Size(80, 23), style=0)
        self.delCaso.SetToolTipString('Baja de caso')
        self.delCaso.Bind(wx.EVT_BUTTON, self.OnDelCasoButton,
              id=wxID_FRAME2DELCASO)

        self.delLocalizacion = wx.Button(id=wxID_FRAME2DELLOCALIZACION,
              label='Borrar localizaci\xf3n', name='delLocalizacion',
              parent=self.NBCasosGral, pos=wx.Point(392, 384), size=wx.Size(120,
              23), style=0)
        self.delLocalizacion.Enable(False)
        self.delLocalizacion.Bind(wx.EVT_BUTTON, self.OnDelLocalizacionButton,
              id=wxID_FRAME2DELLOCALIZACION)

        self.delLegislacion = wx.Button(id=wxID_FRAME2DELLEGISLACION, label='X',
              name='delLegislacion', parent=self.NBNormatividad, pos=wx.Point(8,
              144), size=wx.Size(32, 23), style=0)
        self.delLegislacion.SetToolTipString('Quitar una legislacion')
        self.delLegislacion.Bind(wx.EVT_BUTTON, self.OnDelLegislacionButton,
              id=wxID_FRAME2DELLEGISLACION)

        self.delInstrInt = wx.Button(id=wxID_FRAME2DELINSTRINT, label='X',
              name='delInstrInt', parent=self.NBNormatividad, pos=wx.Point(8,
              256), size=wx.Size(32, 23), style=0)
        self.delInstrInt.SetToolTipString('Quitar un instrumento internacional')
        self.delInstrInt.Bind(wx.EVT_BUTTON, self.OndelInstrInt,
              id=wxID_FRAME2DELINSTRINT)

        self.delActo = wx.Button(id=wxID_FRAME2DELACTO, label='Borrar acto',
              name='delActo', parent=self.NBActosGral, pos=wx.Point(104, 240),
              size=wx.Size(75, 23), style=0)
        self.delActo.SetToolTipString('Borrar acto')
        self.delActo.Bind(wx.EVT_BUTTON, self.OnDelActoButton,
              id=wxID_FRAME2DELACTO)

        self.delCaracRel = wx.Button(id=wxID_FRAME2DELCARACREL, label='X',
              name='delCaracRel', parent=self.NBActosGral, pos=wx.Point(488,
              176), size=wx.Size(24, 23), style=0)
        self.delCaracRel.Bind(wx.EVT_BUTTON, self.OnDelCaracRelButton,
              id=wxID_FRAME2DELCARACREL)

        self.delPerpetrator = wx.Button(id=wxID_FRAME2DELPERPETRATOR,
              label='Borrar un \nperpetrador', name='delPerpetrator',
              parent=self.NBActosPerp, pos=wx.Point(104, 272), size=wx.Size(80,
              48), style=0)
        self.delPerpetrator.Bind(wx.EVT_BUTTON, self.OnDelPerpetratorButton,
              id=wxID_FRAME2DELPERPETRATOR)

        self.delInterv = wx.Button(id=wxID_FRAME2DELINTERV,
              label='Borrar una \nintervenci\xf3n', name='delInterv',
              parent=self.NBIntervenciones, pos=wx.Point(96, 320),
              size=wx.Size(80, 40), style=0)
        self.delInterv.Bind(wx.EVT_BUTTON, self.OnDelIntervButton,
              id=wxID_FRAME2DELINTERV)

        self.delFuentePer = wx.Button(id=wxID_FRAME2DELFUENTEPER,
              label='Borrar \nfuente personal', name='delFuentePer',
              parent=self.NBFuentePersonal, pos=wx.Point(72, 328),
              size=wx.Size(64, 72), style=0)
        self.delFuentePer.Bind(wx.EVT_BUTTON, self.OnDelFuentePerButton,
              id=wxID_FRAME2DELFUENTEPER)

        self.delFuenteDoc = wx.Button(id=wxID_FRAME2DELFUENTEDOC,
              label='Borrar \nfuente documental', name='delFuenteDoc',
              parent=self.NBFuenteDocumental, pos=wx.Point(88, 368),
              size=wx.Size(79, 80), style=0)
        self.delFuenteDoc.Bind(wx.EVT_BUTTON, self.OnDelFuenteDocButton,
              id=wxID_FRAME2DELFUENTEDOC)

        self.delPersona = wx.Button(id=wxID_FRAME2DELPERSONA,
              label='Borrar persona', name='delPersona',
              parent=self.NBPersonasGral, pos=wx.Point(136, 360),
              size=wx.Size(104, 24), style=0)
        self.delPersona.Bind(wx.EVT_BUTTON, self.OnDelPersonaButton,
              id=wxID_FRAME2DELPERSONA)

        self.delIdioma = wx.Button(id=wxID_FRAME2DELIDIOMA, label='X',
              name='delIdioma', parent=self.NBPersonasDetalles,
              pos=wx.Point(544, 91), size=wx.Size(24, 23), style=0)
        self.delIdioma.Bind(wx.EVT_BUTTON, self.OnDelIdiomaButton,
              id=wxID_FRAME2DELIDIOMA)

        self.delLengua = wx.Button(id=wxID_FRAME2DELLENGUA, label='X',
              name='delLengua', parent=self.NBPersonasDetalles,
              pos=wx.Point(544, 168), size=wx.Size(24, 23), style=0)
        self.delLengua.Bind(wx.EVT_BUTTON, self.OnDelLenguaButton,
              id=wxID_FRAME2DELLENGUA)

        self.delOrigen = wx.Button(id=wxID_FRAME2DELORIGEN, label='X',
              name='delOrigen', parent=self.NBPersonasDetalles,
              pos=wx.Point(544, 224), size=wx.Size(24, 23), style=0)
        self.delOrigen.Bind(wx.EVT_BUTTON, self.OnDelOrigenButton,
              id=wxID_FRAME2DELORIGEN)

        self.delDireccion = wx.Button(id=wxID_FRAME2DELDIRECCION, label='X',
              name='delDireccion', parent=self.NBPersonasDetalles,
              pos=wx.Point(792, 408), size=wx.Size(24, 23), style=0)
        self.delDireccion.Bind(wx.EVT_BUTTON, self.OnDelDireccionButton,
              id=wxID_FRAME2DELDIRECCION)

        self.delDatoBio = wx.Button(id=wxID_FRAME2DELDATOBIO,
              label='Borrar dato biogr\xe1fico', name='delDatoBio',
              parent=self.NBPersonasBio, pos=wx.Point(184, 152),
              size=wx.Size(136, 23), style=0)
        self.delDatoBio.SetToolTipString('')
        self.delDatoBio.Bind(wx.EVT_BUTTON, self.OnDelDatoBioButton,
              id=wxID_FRAME2DELDATOBIO)

        self.delDerecho = wx.Button(id=wxID_FRAME2DELDERECHO,
              label='Borrar derecho', name='delDerecho',
              parent=self.NBCasosTipifica, pos=wx.Point(160, 224),
              size=wx.Size(120, 23), style=0)
        self.delDerecho.SetToolTipString('')
        self.delDerecho.Bind(wx.EVT_BUTTON, self.OnDelDerechoButton,
              id=wxID_FRAME2DELDERECHO)

        self.delTema = wx.Button(id=wxID_FRAME2DELTEMA, label='Borrar tema',
              name='delTema', parent=self.NBCasosTipifica, pos=wx.Point(136,
              448), size=wx.Size(96, 23), style=0)
        self.delTema.SetToolTipString('')
        self.delTema.Bind(wx.EVT_BUTTON, self.OnDelTemaButton,
              id=wxID_FRAME2DELTEMA)

        self.delRelacion = wx.Button(id=wxID_FRAME2DELRELACION,
              label='Borrar relaci\xf3n', name='delRelacion',
              parent=self.NBCasosRelaciones, pos=wx.Point(128, 200),
              size=wx.Size(88, 23), style=0)
        self.delRelacion.SetToolTipString('')
        self.delRelacion.Bind(wx.EVT_BUTTON, self.OnDelRelacionButton,
              id=wxID_FRAME2DELRELACION)

        self.btnAddDocLenguaIndigena = wx.Button(id=wxID_FRAME2BTNADDDOCLENGUAINDIGENA,
              label='+', name='btnAddDocLenguaIndigena',
              parent=self.NBFuenteDocumental, pos=wx.Point(296, 256),
              size=wx.Size(24, 23), style=0)
        self.btnAddDocLenguaIndigena.Bind(wx.EVT_BUTTON,
              self.OnBtnAddDocLenguaIndigenaButton,
              id=wxID_FRAME2BTNADDDOCLENGUAINDIGENA)

        self.btnDelDocLenguaIndigena = wx.Button(id=wxID_FRAME2BTNDELDOCLENGUAINDIGENA,
              label='X', name='btnDelDocLenguaIndigena',
              parent=self.NBFuenteDocumental, pos=wx.Point(320, 256),
              size=wx.Size(24, 23), style=0)
        self.btnDelDocLenguaIndigena.Bind(wx.EVT_BUTTON,
              self.OnBtnDelDocLenguaIndigenaButton,
              id=wxID_FRAME2BTNDELDOCLENGUAINDIGENA)

        self.btnAddFteLenguaIndigena = wx.Button(id=wxID_FRAME2BTNADDFTELENGUAINDIGENA,
              label='+', name='btnAddFteLenguaIndigena',
              parent=self.NBFuentePersonal, pos=wx.Point(288, 200),
              size=wx.Size(24, 23), style=0)
        self.btnAddFteLenguaIndigena.Bind(wx.EVT_BUTTON,
              self.OnBtnAddFteLenguaIndigenaButton,
              id=wxID_FRAME2BTNADDFTELENGUAINDIGENA)

        self.btnDelFteLenguaIndigena = wx.Button(id=wxID_FRAME2BTNDELFTELENGUAINDIGENA,
              label='X', name='btnDelFteLenguaIndigena',
              parent=self.NBFuentePersonal, pos=wx.Point(312, 200),
              size=wx.Size(24, 23), style=0)
        self.btnDelFteLenguaIndigena.Bind(wx.EVT_BUTTON,
              self.OnBtnDelFteLenguaIndigenaButton,
              id=wxID_FRAME2BTNDELFTELENGUAINDIGENA)

        self.staticFteLenguaIndigena = wx.StaticText(id=wxID_FRAME2STATICFTELENGUAINDIGENA,
              label='  ', name='staticFteLenguaIndigena',
              parent=self.NBFuentePersonal, pos=wx.Point(368, 208),
              size=wx.Size(32, 13), style=0)

        self.staticDocLenguaIndigena = wx.StaticText(id=wxID_FRAME2STATICDOCLENGUAINDIGENA,
              label='    ', name='staticDocLenguaIndigena',
              parent=self.NBFuenteDocumental, pos=wx.Point(352, 264),
              size=wx.Size(12, 13), style=0)

        self.btnAddFteConfiabilidad = wx.Button(id=wxID_FRAME2BTNADDFTECONFIABILIDAD,
              label='+', name='btnAddFteConfiabilidad',
              parent=self.NBFuentePersonal, pos=wx.Point(288, 280),
              size=wx.Size(24, 23), style=0)
        self.btnAddFteConfiabilidad.Bind(wx.EVT_BUTTON,
              self.OnBtnAddFteConfiabilidadButton,
              id=wxID_FRAME2BTNADDFTECONFIABILIDAD)

        self.btnDelFteConfiabilidad = wx.Button(id=wxID_FRAME2BTNDELFTECONFIABILIDAD,
              label='X', name='btnDelFteConfiabilidad',
              parent=self.NBFuentePersonal, pos=wx.Point(312, 280),
              size=wx.Size(24, 23), style=0)
        self.btnDelFteConfiabilidad.Bind(wx.EVT_BUTTON,
              self.OnBtnDelFteConfiabilidadButton,
              id=wxID_FRAME2BTNDELFTECONFIABILIDAD)

        self.staticFteConfiabilidad = wx.StaticText(id=wxID_FRAME2STATICFTECONFIABILIDAD,
              label='   ', name='staticFteConfiabilidad',
              parent=self.NBFuentePersonal, pos=wx.Point(368, 288),
              size=wx.Size(72, 13), style=0)

        self.btnAddPubConfiabilidad = wx.Button(id=wxID_FRAME2BTNADDPUBCONFIABILIDAD,
              label='+', name='btnAddPubConfiabilidad',
              parent=self.NBFuenteDocumental, pos=wx.Point(296, 344),
              size=wx.Size(24, 23), style=0)
        self.btnAddPubConfiabilidad.Bind(wx.EVT_BUTTON,
              self.OnBtnAddPubConfiabilidadButton,
              id=wxID_FRAME2BTNADDPUBCONFIABILIDAD)

        self.btnDelPubConfiabilidad = wx.Button(id=wxID_FRAME2BTNDELPUBCONFIABILIDAD,
              label='X', name='btnDelPubConfiabilidad',
              parent=self.NBFuenteDocumental, pos=wx.Point(320, 344),
              size=wx.Size(24, 23), style=0)
        self.btnDelPubConfiabilidad.Bind(wx.EVT_BUTTON,
              self.OnBtnDelPubConfiabilidadButton,
              id=wxID_FRAME2BTNDELPUBCONFIABILIDAD)

        self.staticPubConfiabilidad = wx.StaticText(id=wxID_FRAME2STATICPUBCONFIABILIDAD,
              label='        ', name='staticPubConfiabilidad',
              parent=self.NBFuenteDocumental, pos=wx.Point(376, 352),
              size=wx.Size(24, 13), style=0)

        self.btnDelFPTipo = wx.Button(id=wxID_FRAME2BTNDELFPTIPO, label='x',
              name='btnDelFPTipo', parent=self.NBPersonasGral, pos=wx.Point(544,
              96), size=wx.Size(24, 23), style=0)
        self.btnDelFPTipo.Bind(wx.EVT_BUTTON, self.OnBtnDelFPTipoButton,
              id=wxID_FRAME2BTNDELFPTIPO)

        self.btnAddFPTipo = wx.Button(id=wxID_FRAME2BTNADDFPTIPO, label='+',
              name='btnAddFPTipo', parent=self.NBPersonasGral, pos=wx.Point(520,
              96), size=wx.Size(24, 23), style=0)
        self.btnAddFPTipo.Bind(wx.EVT_BUTTON, self.OnBtnAddFPTipoButton,
              id=wxID_FRAME2BTNADDFPTIPO)

        self.staticFPTipo = wx.StaticText(id=wxID_FRAME2STATICFPTIPO,
              label='       ', name='staticFPTipo', parent=self.NBPersonasGral,
              pos=wx.Point(584, 104), size=wx.Size(21, 13), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME2STATICTEXT1,
              label='Exportar relaciones', name='staticText1',
              parent=self.NBCasosGral, pos=wx.Point(16, 456), size=wx.Size(93,
              13), style=0)

        self.checkBoxCasoExportarRelaciones = wx.CheckBox(id=wxID_FRAME2CHECKBOXCASOEXPORTARRELACIONES,
              label='', name='checkBoxCasoExportarRelaciones',
              parent=self.NBCasosGral, pos=wx.Point(128, 456), size=wx.Size(24,
              13), style=0)
        self.checkBoxCasoExportarRelaciones.SetValue(False)
        self.checkBoxCasoExportarRelaciones.Bind(wx.EVT_CHECKBOX,
              self.OnCheckBoxCasoExportarRelacionesCheckbox,
              id=wxID_FRAME2CHECKBOXCASOEXPORTARRELACIONES)

        self.staticText5 = wx.StaticText(id=wxID_FRAME2STATICTEXT5,
              label='Exportar normatividad', name='staticText5',
              parent=self.NBNormatividad, pos=wx.Point(24, 416),
              size=wx.Size(107, 13), style=0)

        self.FAExportar = wx.CheckBox(id=wxID_FRAME2FAEXPORTAR, label='',
              name='FAExportar', parent=self.NBNormatividad, pos=wx.Point(144,
              416), size=wx.Size(24, 13), style=0)
        self.FAExportar.SetValue(False)
        self.FAExportar.Bind(wx.EVT_CHECKBOX, self.OnFAExportarCheckbox,
              id=wxID_FRAME2FAEXPORTAR)

        self.staticText15 = wx.StaticText(id=wxID_FRAME2STATICTEXT15,
              label='Exportar intervenci\xf3n', name='staticText15',
              parent=self.NBIntervenciones, pos=wx.Point(32, 416),
              size=wx.Size(120, 13), style=0)

        self.checkBoxIntExportar = wx.CheckBox(id=wxID_FRAME2CHECKBOXINTEXPORTAR,
              label='', name='checkBoxIntExportar',
              parent=self.NBIntervenciones, pos=wx.Point(160, 416),
              size=wx.Size(24, 13), style=0)
        self.checkBoxIntExportar.SetValue(False)
        self.checkBoxIntExportar.Bind(wx.EVT_CHECKBOX,
              self.OnCheckBoxIntExportarCheckbox,
              id=wxID_FRAME2CHECKBOXINTEXPORTAR)

        self.staticText57 = wx.StaticText(id=wxID_FRAME2STATICTEXT57,
              label='Exportar fuente documental', name='staticText57',
              parent=self.NBFuenteDocumental, pos=wx.Point(16, 456),
              size=wx.Size(160, 13), style=0)

        self.checkBoxPubExportar = wx.CheckBox(id=wxID_FRAME2CHECKBOXPUBEXPORTAR,
              label='', name='checkBoxPubExportar',
              parent=self.NBFuenteDocumental, pos=wx.Point(183, 456),
              size=wx.Size(16, 13), style=0)
        self.checkBoxPubExportar.SetValue(False)
        self.checkBoxPubExportar.Bind(wx.EVT_CHECKBOX,
              self.OnCheckBoxPubExportarCheckbox,
              id=wxID_FRAME2CHECKBOXPUBEXPORTAR)

        self.btnInfoCasoRel = wx.Button(id=wxID_FRAME2BTNINFOCASOREL, label='I',
              name='btnInfoCasoRel', parent=self.NBCasosRelaciones,
              pos=wx.Point(240, 200), size=wx.Size(24, 23), style=0)
        self.btnInfoCasoRel.Bind(wx.EVT_BUTTON, self.OnBtnInfoCasoRelButton,
              id=wxID_FRAME2BTNINFOCASOREL)

        self.btnInfoInter = wx.Button(id=wxID_FRAME2BTNINFOINTER, label='I',
              name='btnInfoInter', parent=self.NBNormatividad, pos=wx.Point(8,
              280), size=wx.Size(32, 23), style=0)
        self.btnInfoInter.Bind(wx.EVT_BUTTON, self.OnBtnInfoInterButton,
              id=wxID_FRAME2BTNINFOINTER)

        self.btnInfoLegis = wx.Button(id=wxID_FRAME2BTNINFOLEGIS, label='I',
              name='btnInfoLegis', parent=self.NBNormatividad, pos=wx.Point(8,
              168), size=wx.Size(32, 23), style=0)
        self.btnInfoLegis.Bind(wx.EVT_BUTTON, self.OnBtnInfoLegisButton,
              id=wxID_FRAME2BTNINFOLEGIS)

        self.GuardarNormatividad = wx.Button(id=wxID_FRAME2GUARDARNORMATIVIDAD,
              label='Guardar', name='GuardarNormatividad',
              parent=self.NBNormatividad, pos=wx.Point(376, 336),
              size=wx.Size(75, 23), style=0)

        self.btnInfoBio = wx.Button(id=wxID_FRAME2BTNINFOBIO, label='I',
              name='btnInfoBio', parent=self.NBPersonasBio, pos=wx.Point(320,
              152), size=wx.Size(24, 23), style=0)
        self.btnInfoBio.Bind(wx.EVT_BUTTON, self.OnBtnInfoBioButton,
              id=wxID_FRAME2BTNINFOBIO)

        self.staticText81 = wx.StaticText(id=wxID_FRAME2STATICTEXT81,
              label='B\xfasqueda r\xe1pida', name='staticText81',
              parent=self.NBPersonasGral, pos=wx.Point(40, 48), size=wx.Size(80,
              13), style=0)

        self.staticText87 = wx.StaticText(id=wxID_FRAME2STATICTEXT87,
              label='Casos relacionados con esta persona', name='staticText87',
              parent=self.NBPersonasGral, pos=wx.Point(40, 416),
              size=wx.Size(304, 13), style=0)

        self.btnBusquedaExhausticaPersona = wx.Button(id=wxID_FRAME2BTNBUSQUEDAEXHAUSTICAPERSONA,
              label='B\xfasqueda exhaustiva',
              name='btnBusquedaExhausticaPersona', parent=self.NBPersonasGral,
              pos=wx.Point(40, 88), size=wx.Size(128, 23), style=0)
        self.btnBusquedaExhausticaPersona.Bind(wx.EVT_BUTTON,
              self.OnBtnBusquedaExhausticaPersonaButton,
              id=wxID_FRAME2BTNBUSQUEDAEXHAUSTICAPERSONA)

        self.btnBuscarPersona = wx.Button(id=wxID_FRAME2BTNBUSCARPERSONA,
              label='Aplicar', name='btnBuscarPersona',
              parent=self.NBPersonasGral, pos=wx.Point(168, 88),
              size=wx.Size(72, 23), style=0)
        self.btnBuscarPersona.Bind(wx.EVT_BUTTON, self.OnBtnBuscarPersonaButton,
              id=wxID_FRAME2BTNBUSCARPERSONA)

        self.btnMostarTodasPersonas = wx.Button(id=wxID_FRAME2BTNMOSTARTODASPERSONAS,
              label='Mostrar todas', name='btnMostarTodasPersonas',
              parent=self.NBPersonasGral, pos=wx.Point(240, 88),
              size=wx.Size(96, 23), style=0)
        self.btnMostarTodasPersonas.Bind(wx.EVT_BUTTON,
              self.OnBtnMostarTodasPersonasButton,
              id=wxID_FRAME2BTNMOSTARTODASPERSONAS)

        self.staticLine3 = wx.StaticLine(id=wxID_FRAME2STATICLINE3,
              name='staticLine3', parent=self.NBCasosGral, pos=wx.Point(16,
              488), size=wx.Size(816, 2), style=0)

        self.choiceGrupo = wx.Choice(choices=[], id=wxID_FRAME2CHOICEGRUPO,
              name='choiceGrupo', parent=self.NBCasosGral, pos=wx.Point(56,
              528), size=wx.Size(200, 21), style=0)
        self.choiceGrupo.Bind(wx.EVT_CHOICE, self.OnChoiceGrupoChoice,
              id=wxID_FRAME2CHOICEGRUPO)

        self.choiceContenedor = wx.Choice(choices=['', '1', '2', '3'],
              id=wxID_FRAME2CHOICECONTENEDOR, name='choiceContenedor',
              parent=self.NBCasosGral, pos=wx.Point(336, 528), size=wx.Size(48,
              21), style=0)
        self.choiceContenedor.Bind(wx.EVT_CHOICE, self.OnChoiceContenedorChoice,
              id=wxID_FRAME2CHOICECONTENEDOR)

        self.staticGrupo = wx.StaticText(id=wxID_FRAME2STATICGRUPO,
              label='Grupo', name='staticGrupo', parent=self.NBCasosGral,
              pos=wx.Point(16, 536), size=wx.Size(29, 13), style=0)

        self.staticContenedor = wx.StaticText(id=wxID_FRAME2STATICCONTENEDOR,
              label='Contenedor', name='staticContenedor',
              parent=self.NBCasosGral, pos=wx.Point(272, 536), size=wx.Size(57,
              13), style=0)

        self.staticText99 = wx.StaticText(id=wxID_FRAME2STATICTEXT99,
              label='Grupo', name='staticText99', parent=self.NBPersonasGral,
              pos=wx.Point(8, 544), size=wx.Size(29, 13), style=0)

        self.choiceGrupoP = wx.Choice(choices=[], id=wxID_FRAME2CHOICEGRUPOP,
              name='choiceGrupoP', parent=self.NBPersonasGral, pos=wx.Point(40,
              536), size=wx.Size(208, 21), style=0)
        self.choiceGrupoP.Bind(wx.EVT_CHOICE, self.OnChoiceGrupoPChoice,
              id=wxID_FRAME2CHOICEGRUPOP)

        self.staticText111 = wx.StaticText(id=wxID_FRAME2STATICTEXT111,
              label='Contenedor', name='staticText111',
              parent=self.NBPersonasGral, pos=wx.Point(264, 544),
              size=wx.Size(57, 13), style=0)

        self.choiceContenedorP = wx.Choice(choices=['', '1', '2', '3'],
              id=wxID_FRAME2CHOICECONTENEDORP, name='choiceContenedorP',
              parent=self.NBPersonasGral, pos=wx.Point(328, 536),
              size=wx.Size(48, 21), style=0)
        self.choiceContenedorP.Bind(wx.EVT_CHOICE,
              self.OnChoiceContenedorPChoice, id=wxID_FRAME2CHOICECONTENEDORP)

        self.staticText112 = wx.StaticText(id=wxID_FRAME2STATICTEXT112,
              label='Estatus C3', name='staticText112', parent=self.NBCasosGral,
              pos=wx.Point(16, 496), size=wx.Size(52, 13), style=0)

        self.txtStatusC3 = wx.StaticText(id=wxID_FRAME2TXTSTATUSC3,
              label='status', name='txtStatusC3', parent=self.NBCasosGral,
              pos=wx.Point(80, 496), size=wx.Size(30, 13), style=0)

        self.chkRelevante = wx.CheckBox(id=wxID_FRAME2CHKRELEVANTE,
              label='No relevante?', name='chkRelevante',
              parent=self.NBCasosGral, pos=wx.Point(184, 496), size=wx.Size(88,
              13), style=0)
        self.chkRelevante.SetValue(False)
        self.chkRelevante.Bind(wx.EVT_CHECKBOX, self.OnChkRelevanteCheckbox,
              id=wxID_FRAME2CHKRELEVANTE)

        self.btnCopiarC3 = wx.Button(id=wxID_FRAME2BTNCOPIARC3,
              label='Copiar a C3', name='btnCopiarC3', parent=self.NBCasosGral,
              pos=wx.Point(320, 493), size=wx.Size(96, 23), style=0)
        self.btnCopiarC3.Enable(False)
        self.btnCopiarC3.Bind(wx.EVT_BUTTON, self.OnBtnCopiarC3Button,
              id=wxID_FRAME2BTNCOPIARC3)

        self.btnCopiarC3P = wx.Button(id=wxID_FRAME2BTNCOPIARC3P,
              label='Copiar a C3', name='btnCopiarC3P',
              parent=self.NBPersonasGral, pos=wx.Point(448, 493),
              size=wx.Size(75, 23), style=0)
        self.btnCopiarC3P.Bind(wx.EVT_BUTTON, self.OnBtnCopiarC3PButton,
              id=wxID_FRAME2BTNCOPIARC3P)

        self.longObsRelCasos = wx.StaticText(id=wxID_FRAME2LONGOBSRELCASOS,
              label='--', name='longObsRelCasos', parent=self.NBCasosRelaciones,
              pos=wx.Point(688, 200), size=wx.Size(8, 13), style=0)

        self.longComRelCasos = wx.StaticText(id=wxID_FRAME2LONGCOMRELCASOS,
              label='        ', name='longComRelCasos',
              parent=self.NBCasosRelaciones, pos=wx.Point(688, 320),
              size=wx.Size(80, 13), style=0)

        self.MP2 = wx.CheckBox(id=wxID_FRAME2MP2,
              label='Relacionadas con el caso', name='MP2',
              parent=self.NBPersonasGral, pos=wx.Point(48, 144),
              size=wx.Size(160, 13), style=0)
        self.MP2.SetValue(False)
        self.MP2.SetToolTipString('Mostar personas relacionadas con un caso')
        self.MP2.Bind(wx.EVT_CHECKBOX, self.OnMP1Checkbox, id=wxID_FRAME2MP2)

        self.MP3 = wx.CheckBox(id=wxID_FRAME2MP3, label='Colectiva', name='MP3',
              parent=self.NBPersonasGral, pos=wx.Point(208, 128),
              size=wx.Size(96, 13), style=0)
        self.MP3.SetValue(False)
        self.MP3.SetToolTipString('Mostrar perdonas colectivas')
        self.MP3.Bind(wx.EVT_CHECKBOX, self.OnMP1Checkbox, id=wxID_FRAME2MP3)

        self.MP4 = wx.CheckBox(id=wxID_FRAME2MP4, label='Todas', name='MP4',
              parent=self.NBPersonasGral, pos=wx.Point(208, 144),
              size=wx.Size(70, 13), style=0)
        self.MP4.SetValue(True)
        self.MP4.SetToolTipString('Mostrar todas las personas')
        self.MP4.Bind(wx.EVT_CHECKBOX, self.OnMP1Checkbox, id=wxID_FRAME2MP4)

        self.MP0 = wx.StaticBox(id=wxID_FRAME2MP0, label='Mostrar', name='MP0',
              parent=self.NBPersonasGral, pos=wx.Point(40, 112),
              size=wx.Size(296, 48), style=0)
        self.MP0.SetToolTipString('Tipo de persona a mostrar')

        self.MP1 = wx.CheckBox(id=wxID_FRAME2MP1, label='Individual',
              name='MP1', parent=self.NBPersonasGral, pos=wx.Point(48, 128),
              size=wx.Size(104, 13), style=0)
        self.MP1.SetValue(False)
        self.MP1.SetToolTipString('')
        self.MP1.SetHelpText('')
        self.MP1.Bind(wx.EVT_CHECKBOX, self.OnMP1Checkbox, id=wxID_FRAME2MP1)

        self.txtLongNorLeg = wx.StaticText(id=wxID_FRAME2TXTLONGNORLEG,
              label='   ', name='txtLongNorLeg', parent=self.NBNormatividad,
              pos=wx.Point(737, 104), size=wx.Size(9, 13), style=0)

        self.txtLongNorIns = wx.StaticText(id=wxID_FRAME2TXTLONGNORINS,
              label='   ', name='txtLongNorIns', parent=self.NBNormatividad,
              pos=wx.Point(737, 215), size=wx.Size(9, 13), style=0)

        self.txtTotalPersonasSeleccionadas = wx.StaticText(id=wxID_FRAME2TXTTOTALPERSONASSELECCIONADAS,
              label='   ', name='txtTotalPersonasSeleccionadas',
              parent=self.NBPersonasGral, pos=wx.Point(40, 32), size=wx.Size(9,
              13), style=0)

        self.pantAnterior = wx.Button(id=wxID_FRAME2PANTANTERIOR,
              label='Pantalla anterior ->', name='pantAnterior',
              parent=self.NBCasosGral, pos=wx.Point(712, 32), size=wx.Size(115,
              23), style=0)
        self.pantAnterior.Show(False)
        self.pantAnterior.Bind(wx.EVT_BUTTON, self.OnPantAnteriorButton,
              id=wxID_FRAME2PANTANTERIOR)

        self.btnCambiaTipoPersona = wx.Button(id=wxID_FRAME2BTNCAMBIATIPOPERSONA,
              label='Cambiar tipo a individual', name='btnCambiaTipoPersona',
              parent=self.NBPersonasGral, pos=wx.Point(664, 400),
              size=wx.Size(144, 23), style=0)
        self.btnCambiaTipoPersona.Bind(wx.EVT_BUTTON,
              self.OnBtnCambiaTipoPersonaButton,
              id=wxID_FRAME2BTNCAMBIATIPOPERSONA)

        self.staticText113 = wx.StaticText(id=wxID_FRAME2STATICTEXT113,
              label='Estatus C3', name='staticText113',
              parent=self.NBPersonasGral, pos=wx.Point(40, 496),
              size=wx.Size(53, 13), style=0)

        self.txtStatusC3P = wx.StaticText(id=wxID_FRAME2TXTSTATUSC3P,
              label='status', name='txtStatusC3P', parent=self.NBPersonasGral,
              pos=wx.Point(112, 496), size=wx.Size(96, 13), style=0)

        self.chkRelevanteP = wx.CheckBox(id=wxID_FRAME2CHKRELEVANTEP,
              label='No relevante?', name='chkRelevanteP',
              parent=self.NBPersonasGral, pos=wx.Point(232, 496),
              size=wx.Size(96, 13), style=0)
        self.chkRelevanteP.SetValue(False)
        self.chkRelevanteP.Bind(wx.EVT_CHECKBOX, self.OnChkRelevantePCheckbox,
              id=wxID_FRAME2CHKRELEVANTEP)

        self._init_coll_NBMain_Pages(self.NBMain)
        self._init_coll_NBCasos_Pages(self.NBCasos)
        self._init_coll_NBActos_Pages(self.NBActos)
        self._init_coll_NBPersonas_Pages(self.NBPersonas)
        self._init_coll_NBFuentes_Pages(self.NBFuentes)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.Move(wx.Point(0, 0))
        
        
        s=self
        self.parent = parent
        for NB in [s.NBMain, s.NBCasos, s.NBActos, s.NBPersonas, s.NBFuentes]:
            NB.SetWindowStyleFlag(wx.lib.flatnotebook.FNB_NO_X_BUTTON|wx.lib.flatnotebook.FNB_NODRAG)
            
            screenconfig.ScreenConfig(self, 'NBMain')
            NB.Layout()
            NB.SetSelection(0)
        l = session.query(Grupo).all()
        misGrupos = [(None, ' ')]+[(i,i.Descriptor()) for i in session.query(Grupo)]
        LlenaCtrl3(self.choiceGrupo, misGrupos)
        LlenaCtrl3(self.choiceGrupoP, misGrupos)
        if cnf.OSlinux:
            module2.choiceFix(self, __name__)

 
    def OnFrame2Close(self, event):
        for i in range(0,5):
            self.save_data(i)
        session.close()
        self.MakeModal(False) 
        self.parent.Close()
            
        self.Destroy()
        event.Skip()

    def OnFrame2Activate(self, event):
        
        
        event.Skip()

    def OnEstadoChoice(self, event):

        i = self.Estado.Selection
        Edo  = self.Estado.GetClientData(i)
        LlenaCtrlChildren(self.Municipio, Edo)
        event.Skip()


    def OnListaCasosDclick(self, event):
        self.pantAnterior.Show(False)
        saveDataCaso(self)
        
        status.casoActual = MyClientData(event)
        
        
        LoadDataCaso(self)
        self.NBPersonas.SetSelection(0)
        self.NBActos.SetSelection(0)
        
        
        self.listBoxPerpetradores.Clear()
        #self.btnCopiarC3.Enable()

        # keep the focus!
        c = event.GetEventObject()
        c.SetFocus()
        #if status.casoActual:
        #    self.btnCopiarC3.Enable(status.casoActual.clavestatus == 2)
        
        
        
        
        
        LoadDataPersona(self)
        
        
        event.Skip()

    def OnTextDescripcionTextEnter(self, event):

        event.Skip()

    def OnBtnActualizarCaso(self, event):
        n=self.listaCasos.GetStringSelection()
        saveDataCaso(self)        
        

        self.CasoIsearch.ChangeValue('')
        LlenaCtrlCasos(self.listaCasos)
        
        self.listaCasos.SetFocus()
        
        self.txtTotalCasos.SetLabel("%i casos registrados"%(status.TotalCasos))
        self.txtCasosSeleccionados.SetLabel('')
        self.listaCasos.SetStringSelection(n)
        
        event.Skip()

    def OnTextDescripcionText(self, event):
        
        
        
        event.Skip()

    def OnMunicipioChoice(self, event):
        status.casoActual.Pmpio = self.Municipio.GetClientData(self.Municipio.Selection)
        event.Skip()

    def OnAltaCaso(self, event):
        status.creacionReciente = True
        saveDataCaso(self)
        descrip = MyDescrip(self, titulo='Nombre del caso')
        yaexiste = ExisteCaso(descrip)
        if yaexiste:
            MError(self, u"Ya existe un caso con este nombre")
            return
        if descrip:
              status.casoActual = Caso(descrip)
              status.objdehoy.add(status.casoActual)
              LimpiaCamposCaso(self)
            
              self.textDescripcion.SetValue(descrip)
            
              session.add(status.casoActual)
              saveDataCaso(self)
              FlushInfo(id=104)
              status.TotalCasos = NoRegistros(Caso)
              self.CasoIsearch.ChangeValue('')
              self.txtTotalCasos.SetLabel("%i casos registrados"%(status.TotalCasos))
              self.txtCasosSeleccionados.SetLabel('')
              LoadDataCaso(self)
              LlenaCtrlCasos(self.listaCasos, selected=status.casoActual)
              setLabelActoActual(self, label=' ')

              
        event.Skip()



    def OnNBMainNotebookPageChanging(self, event):
         
    
        select = self.NBMain.GetSelection()
        if select == 0:
           status.nuevoacto = False
           if status.casoActual:
                 #LlenaCtrl2(self.listActos, status.casoActual.actos) 
                 LlenaActos(self)
                 LlenaIntervenciones(self)

                 
                 #LlenaCtrlTipificacion(self.listBox1,153, status.casoActual)
                 #LlenaCtrlTipificacion(self.listBox2,154, status.casoActual)
                 
            
            
            
            
        event.Skip()
#eventocambiatab
    def OnNBMainNotebookPageChanged(self, event):

        
        paginaPrev = event.GetOldSelection()
        pagina = self.NBMain.GetSelection()
        TitPagina = self.NBMain.GetPageText(pagina)
        TitOldPage = self.NBMain.GetPageText(paginaPrev)
        
        

        if paginaPrev == -1:
            
            LlenaPantallasGenerales(self)
            LlenaCtrlCasos(self.listaCasos)
            self.CasoIsearch.ChangeValue('')
            status.TotalCasos = NoRegistros(Caso)
            self.txtTotalCasos.SetLabel("%i casos registrados"%(status.TotalCasos))
            self.txtCasosSeleccionados.SetLabel('')
            
            #status.personaIndividual=True
            CambiaTitulos(self, False)
            CambiaTitulos(self, True)
            
            LlenaCasoInicial(self)
            
            self.listaCasos.SetFocus()
            
            
        self.save_data(paginaPrev)
        
         
        if TitPagina == "Casos":
            self.NBCasos.SetSelection(0)
            
        if TitPagina == "Tipificacion":
        
           if status.casoActual:
                 LlenaCtrlTipificacion(self.listBoxDerechosafectados,153, status.casoActual)
                 LlenaCtrlTipificacion(self.listBoxTemas,154, status.casoActual)
# fuentes
        if TitPagina == "Fuentes":
           if status.casoActual:
            
               LlenaCtrlFuentes(self)
               LlenaCtrlPubs(self)
        #if TitPagina == "Actos":
        #    if status.actoActual:
        #        CtrlSelect(self.listActos, status.actoActual.Descriptor())
        

        
               
# Personas            
        if TitPagina == "Personas":
            
            self.NBPersonas.SetSelection(0) # para que regrese a la 1a pestania cada vez que entramos a personas
            
            s= status.tipoPersona
            status.totalPersonas = NoRegistros(Persona)
            t=LlenaPersonas(self.listBoxPersonaBrowser, filtro=s)
            setPersonasSeleccionadas(self, t) #(NoRegistros(Persona))
            self.txtTotalPersonas.SetLabel("%i personas registradas"%status.totalPersonas) #(NoRegistros(Persona))
            
            if status.personaActual:
                CtrlSelect(self.listBoxPersonaBrowser, status.personaActual.Descriptor())
            
            if t:
                self.listBoxPersonaBrowser.SetSelection(0)
            status.personaActual = MyClientData(self.listBoxPersonaBrowser)
            LoadDataPersona(self)         
        
        
        event.Skip()
# aun no:        SaveData(self, TitOldPage)
    def OnTextActoDescText(self, event):
        event.Skip()

    def save_data(self, pag):
        
#        session.bind.echo = True
        if pag  == 0:
            saveDataCaso(self)
            SaveDataCasoRel(self)
        if pag  == 1:
            SaveDataActo(self)
            SaveDataInvol(self)
            #SaveDataInstr(self)
            #SaveDataLegis(self)
        if pag  == 2:
            SaveDataIntervencion(self)
        if pag  == 3:
            SaveDataPub(self)
            SaveDataFuente(self)
        if pag  == 4:
            SaveDataPersona(self)
            SaveDataVinculo(self)

#        session.bind.echo = False



    def OnActualizarActo(self, event):
        n=self.listActos.GetSelection()
        SaveDataActo(self)
        
        
        FlushInfo(id=106)
        LlenaActos(self)
        #LlenaCtrl2(self.listActos, status.casoActual.actos)
        self.listActos.SetSelection(n)
        event.Skip()

    def OnListActosListbox(self, event):
        event.Skip()

    def OnListActosDclick(self, event):
        SaveDataActo(self)
        status.actoActual = MyClientData(event)
        #status.actoActual = self.listActos.GetClientData(self.listActos.Selection)
        LoadDataActo(self)
        

        
        LlenaPerpetradores(self, self.listBoxPerpetradores)
        LlenaPerpetradores(self, self.listBoxActoPerpetradores)
        panels['Involucramientos'].Enable()
        Enable_panel(self, 'Involucramientos', enable=False)
        
        # hack for this strange bug which hijacks events
        c = event.GetEventObject()
        c.SetFocus()
        
        event.Skip()

    def OnButtonCasoDerechoafectado(self, event):
        
        DialogTipifica(self, u'T03',153, desc='Derecho afectado', help=u'DerechoAfectado')
#        self.NBMain.ChangeSelection(1) 
        LlenaCtrlTipificacion(self.listBoxDerechosafectados,153, status.casoActual)
        event.Skip()

    def OnButton2Button(self, event):
        
        DialogTipifica(self, u'T01',154,desc='Temas', help=u'Temas')
        
#        self.NBMain.ChangeSelection(1) 
        LlenaCtrlTipificacion(self.listBoxTemas,154, status.casoActual)
        
        event.Skip()

    def selectIntervDeQuien(self, event):
        P=PersonaDlg(self, help=u'dlgpersonaDeQuien')
        if P:
            status.intervencionActual.solicitante = P
            self.staticText17.SetLabel(P.Descriptor())
            
        event.Skip()

    def OnVictimSelect(self, event):

        P=PersonaDlg(self)
        if P:
            status.actoActual.Pvictima= P
            self.FAVictima.SetLabel(status.actoActual.Pvictima.Descriptor())
        event.Skip()

    def OnPerpetradorADD(self, event):
        P=PersonaDlg(self, help=u'dlgpersonaperpetrador')
        if P:
            I=Involucramiento()
#            I.acto_id=status.actoActual.id
            
            I.persona=P
            I.tipo_id=2
            status.actoActual.RolPerpetradores.append(I)
            
            
            session.add(I)
            
            FlushInfo(id=109)
            session.refresh(status.actoActual)
            print 4,I.acto_id
            
            status.involActual = I
            ##SaveDataInvol(self)
#            status.actoActual = session.query(Acto).filter_by(id=status.actoActual.id)[0]
            LlenaPerpetradores(self, self.listBoxPerpetradores)
            LoadDataInvol(self)
            
            
        event.Skip()

    def OnAddIntervencion(self, event):
        intervencionActual = Intervencion()
        event.Skip()

    def OnSelectTipoIntervencion(self, event):
        
        tipoint = getTaxonomyTree(self, u"T20", u"Tipo de intervenci\xf3n", help=u'getTaxTipoIntervencion')
        if tipoint:
            status.intervencionActual.tipo = tipoint
            self.staticText18.SetLabel(status.intervencionActual.tipo.descripcion)
            
            
        event.Skip()

    def selectIntervAQuien(self, event):
        P=PersonaDlg(self, help=u'dlgpersonaAQuien')
        if P:
            status.intervencionActual.contraparte = P
            self.staticText19.SetLabel(P.Descriptor())
            
        event.Skip()


    def OnListBoxIntervencionesDclick(self, event):
        SaveDataIntervencion(self)
        #i = self.listBoxIntervenciones.Selection
        #status.intervencionActual = self.listBoxIntervenciones.GetClientData(i)
        status.intervencionActual = MyClientData(event)
        LoadDataIntervencion(self)
        event.Skip()

    def OnButtonIntervencionADD(self, event):
        SaveDataIntervencion(self)
        P,T = DialogIntervencion(self)
        if P and T:
           status.intervencionActual = Intervencion(P,T,status.casoActual)
           session.add(status.intervencionActual)
           
           #status.debug=True
           FlushInfo(id=112)
           #status.debug=False
           
           LoadDataIntervencion(self)
           
           LlenaIntervenciones(self)
           
        else:
           MError(self, u"No se cre\xf3 la intervenci\xf3n")
        

        event.Skip()

    def OnButtonIntervencionActualizar(self, event):
        if status.intervencionActual:
            n=self.listBoxIntervenciones.GetSelection()
            SaveDataIntervencion(self)
            
            LlenaIntervenciones(self)
            self.listBoxIntervenciones.SetSelection(n)
            
        event.Skip()

    def OnButtonVincular(self, event):
        SaveDataVinculo(self)
        dlg=DlgVincular.Dialog1(self)
        dlg.ShowModal()
        
        P = status.personaActual
        
        
        


        expr = status.vinculoActual.Descriptor() if status.vinculoActual else None
        LlenaCtrlVinculos(self, self.listBoxVinculos, P, selected=expr)
        if status.vinculoActual:
            LoadDataVinculo(self)
            Enable_panel(self, 'Personas 4', enable=True)
        
        
        
        event.Skip()

    def OnListBoxPersonaBrowserListbox(self, event):
        

        event.Skip()



    def OnListBoxIntervencionesListbox(self, event):
        event.Skip()



    def OnListBoxFteDCLICK(self, event):
        SaveDataFuente(self)
        #i = self.listBoxFte.Selection
        #status.fuenteActual = self.listBoxFte.GetClientData(i)
        status.fuenteActual = MyClientData(event)
        loadDataFuente(self)
        event.Skip()

    def OnButtonFteNueva(self, event):
        SaveDataFuente(self)
        LimpiaCamposFuente(self)
        
        P=PersonaDlg(self, help=u'FuentePersonal')
        if P:
           
           status.fuenteActual = Fuente(P)
           status.fuenteActual.idioma = VDefault['T14']
           
           session.add(status.fuenteActual)
           FlushInfo(id=113)
           #status.fuenteActual = None
           LlenaCtrlFuentes(self)
           loadDataFuente(self)
           
           





        event.Skip()


            
            


    def OnButtonFteActualizarDatos(self, event):
         SaveDataFuente(self)


         event.Skip()

    def OnButtonFteConexionInformacion(self, event):
        T = getTaxonomyTree(self, u"T19", u"Conexi\xf3n de la fuente con la informaci\xf3n", help=u'getTaxConexionInformacion')
        if T:
            status.fuenteActual.PConexion_info = T
            self.staticTextConexionInfo.SetLabel(T.descripcion)
            
        event.Skip()

    def OnButtonActualizarCaso2(self, event):
        self.OnBtnActualizarCaso1Button(event)
        event.Skip()

    def OnListBoxPersonaBrowserDclick(self, event):
        
        SaveDataPersona(self)
        print "ya SaveDataPersona"
        SaveDataVinculo(self)
        print "ya SaveDataVinculo"
        
        status.personaActual = MyClientData(event)
        #status.personaActual = self.listBoxPersonaBrowser.GetClientData(self.listBoxPersonaBrowser.Selection)
        
        P = status.personaActual
        
        LoadDataPersona(self)
        #self.btnCopiarC3P.Enable(status.personaActual.clavestatus == 2)
        
        
        event.Skip()

    def OnFPEstadoChoice(self, event):
        i = self.FPEstado.Selection
        Edo  = self.FPEstado.GetClientData(i)
        
        #LlenaCtrlChildren(self.FPMunicipio, Edo, orden="descripcion")
        LlenaCtrlMunicipios(self.FPMunicipio, Edo) 
        
        
        event.Skip()

    def OnButtonPGuardar(self, event):
        
        n=self.listBoxPersonaBrowser.GetStringSelection()
        P = status.personaActual
        SaveDataPersona(self)
        self.srchPersona.Clear()
        Iexpr = Sortable(self.srchPersona.GetValue(), trans=module2.transWildChar)
        t=LlenaPersonas(self.listBoxPersonaBrowser, filtro=status.tipoPersona, filtro2=Iexpr, Pselected=status.personaActual)
        #t=LlenaPersonas(self.listBoxPersonaBrowser, filtro=status.tipoPersona, Pselected=status.personaActual)
        self.txtTotalPersonas.SetLabel("%i personas registradas"%t)
        self.listBoxPersonaBrowser.SetStringSelection(n)
        self.listBoxPersonaBrowser.SetFocus()
        
        status.personaActual = P
        LoadDataPersona(self)
        CtrlSelect(self.listBoxPersonaBrowser ,P)
        
        event.Skip()

    def OnListBox3Listbox(self, event):
        self.delCaracRel.Enable(status.canEditCaso)
        event.Skip()



    def OnBTNAgregarCaracRelevante(self, event):
        a=status.actoActual
        t=getTaxonomyTree(self, u"T23", u"Caracter\xedsticas relevantes", help=u'getTaxCaracRelevante')
# validar que no se agregue el mismo DV mas de una ves
# ojo que se convienter en cacarteriticas relevantes
        if t:
            id = t.id
            if id in [i.Pcaracteristicarelevante.id for i in a.PCaracRelevantes]:
                 MError(self, u"Ya existe esta caracter\xedstica relevante en el acto")
            else:
                dv=Caracrelevantes()
                dv.Pacto = a
                dv.Pcaracteristicarelevante = t
                session.add(dv)
                FlushInfo(id=115)
                LlenaCtrl3(self.FACaracRelevante, [(i,i.Pcaracteristicarelevante.descripcion) for i in a.PCaracRelevantes])
        event.Skip()

    def OnButtonSelectEstatusVDHButton(self, event):
        t=None
        t=getTaxonomyTree(self, u"T41", "Estatus de la VDH", help=u'getTaxonomyTreeEstatusVDH')
        if t:
            status.actoActual.PEstatusvdh = t
            self.FAEstatusvdh.SetLabel(t.descripcion)
        event.Skip()

    def OnButtonEstatusdelavictimaButton(self, event):
        t=getTaxonomyTree(self, u"T25", u"Estatus de la v\xedctima", help=u'getTaxonomyTreeEstatusVictima')
        if t:
            status.actoActual.PEstatusvictima = t
            self.FAEstatusvictima.SetLabel(t.descripcion)
        event.Skip()

    def OnListBoxPerpetradoresDclick(self, event):
        SaveDataInvol(self)
        #status.involActual = self.listBoxPerpetradores.GetClientData(self.listBoxPerpetradores.Selection)
        status.involActual = MyClientData(event)
        LoadDataInvol(self)
        event.Skip()

    def onBtnSavePub(self, event):
        n=self.listBoxDocs.GetSelection()
        SaveDataPub(self)
        
        
        FlushInfo(id=116)
        LlenaCtrlPubs(self)
        self.listBoxDocs.SetSelection(n)
        
        event.Skip()

    def OnButtonSelGradoInvol(self, event):
        t= getTaxonomyTree(self, u"T18", "Grado de involucramiento",help=u'getTaxonomyTreeGradoInvol')
        if t:
            status.involActual.Pgradoinvolucramiento = t
            self.FIgradoinvolucramiento.SetLabel(t.descripcion)
            

        event.Skip()

    def OnButtonSelTipoPerpButton(self, event):
        t  = getTaxonomyTree(self, u"T24", "Tipo de perpetrador", help=u'getTaxonomyTreeTipoPerp')
        if t:
            status.involActual.Ptipoperpetrador = t
            self.FItipoperpetrador.SetLabel(t.descripcion)
            
            
        event.Skip()

    def OnButtonSelUltStatusPerp(self, event):
        t  = getTaxonomyTree(self, u"T26", u"\xdaltimo estatus de perpetrador", help=u'getTaxUltimoStatusPerp')
        if t:
            status.involActual.Pultimostatusperpetrador = t
            self.FIultimostatusperpetrador.SetLabel(t.descripcion)
            
        event.Skip()

    def OnButtonActualizarInvol(self, event):
        SaveDataInvol(self)
        event.Skip()

    def OnButtonSelecTipodelugar(self, event):
        tipo = None
        tipo = getTaxonomyTree(self, u"T17", "Tipo de lugar", help=u'getTaxonomyTreeTipodeLugar')
        if tipo:
            self.FATipodelugar.SetLabel(tipo.descripcion)
            status.actoActual.PTipodelugar = tipo
        
        event.Skip()


    def OnListBoxDerechosafectadosKeyDown(self, event):
        Aborrar = True
        if event.GetKeyCode() == wx.WXK_DELETE:
            #tipificacion = self.listBoxDerechosafectados.GetClientData(self.listBoxDerechosafectados.Selection)
            tipificacion = MyClientData(event)
            name = '^'+tipificacion.tipificacion.name
            Pattern = re.compile(name)
            for i in status.casoActual.actos:
                if Aborrar and Pattern.match(i.PTipodeacto.name):
                        MError(self, u"Este derecho no puede ser borrado, ya que tiene actos relacionados")
                        Aborrar = False
            if Aborrar and Borrar(self, u"\xbfBorrar este dato?"):            
                DelTipificacion(tipificacion)
                LlenaCtrlTipificacion(self.listBoxDerechosafectados,153, status.casoActual)
            

            
        event.Skip()

    def OnListBoxTemasKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            if Borrar(self, u"\xbfBorrar este dato?"):            
                #tipificacion = self.listBoxTemas.GetClientData(self.listBoxTemas.Selection)
                tipificacion= MyClientData(event)
                DelTipificacion(tipificacion)
                LlenaCtrlTipificacion(self.listBoxTemas,154, status.casoActual)

        event.Skip()

    def OnListActosKeyDown(self, event):
       if event.GetKeyCode() == wx.WXK_DELETE:
            
            #ActoBorrar = self.listActos.GetClientData(self.listActos.Selection)
            ActoBorrar = MyClientData(event)
            if ActoSepuedeBorrar(self, ActoBorrar):
                session.delete(ActoBorrar)
                status.casoActual.actos.remove(ActoBorrar)
                FlushInfo(id=117)
                status.actoActual = None
                LlenaActos(self)
                #LlenaCtrl2(self.listActos, status.casoActual.actos) 
       event.Skip()

    def OnListBoxIntervencionesKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            
            #IntervBorrar = self.listBoxIntervenciones.GetClientData(self.listBoxIntervenciones.Selection)
            IntervBorrar = MyClientData(event)
            if Borrar(self, u"\xbfBorrar esta intervenci\xf3n?"):
                session.delete(IntervBorrar)
                status.casoActual.intervenciones.remove(IntervBorrar)
                status.intervencionActual = None
                FlushInfo(id=118)
                LlenaIntervenciones(self)
                
        event.Skip()

    def OnListBoxFteKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            FuenteBorrar = MyClientData(event)
            #FuenteBorrar = self.listBoxFte.GetClientData(self.listBoxFte.Selection)
            if Borrar(self, u"\xbfBorrar esta fuente personal?"):
                session.delete(FuenteBorrar)
                status.casoActual.fuentes.remove(FuenteBorrar)
                status.fuenteActual = None
                FlushInfo(id=119)
                LimpiaCamposFuente(self)
                LlenaCtrlFuentes(self)
        event.Skip()

    def OnListaCasosKeyDown1(self, event):
        
        if event.GetKeyCode() == wx.WXK_DELETE:
            CasoBorrar = MyClientData(event)
            #CasoBorrar = MyClientData(self.listaCasos)
            if CasoSepuedeBorrar(self, CasoBorrar):
                session.delete(CasoBorrar)
                del CasoBorrar
                status.casoActual = None

                FlushInfo(id=120)
                self.CasoIsearch.ChangeValue('')
                LlenaCtrlCasos(self.listaCasos)
                status.TotalCasos = NoRegistros(Caso)
                self.txtTotalCasos.SetLabel("%i casos registrados"%(status.TotalCasos))
                self.txtCasosSeleccionados.SetLabel('')
                

        event.Skip()

    

    def OnChoiceTipoFechaInicialChoice(self, event):
        #TipoFecha = self.choiceTipoFechaInicial.GetClientData(self.choiceTipoFechaInicial.Selection)
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        TipoFecha = MyClientData(event)
        ActivaCtrlFecha2(TipoFecha, self.CasoFechaInicial)
        event.Skip()

    def OnChoiceTipoFechaFinal(self, event):
        #TipoFecha = self.choiceTipoFechaFinal.GetClientData(self.choiceTipoFechaFinal.Selection)
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        TipoFecha = MyClientData(event)
        ActivaCtrlFecha2(TipoFecha, self.CasoFechaFinal)
        event.Skip()

    def OnFATipofechainicioChoice(self, event):
        #TipoFecha = self.FATipofechainicio.GetClientData(self.FATipofechainicio.Selection)
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        TipoFecha = MyClientData(event)
        ActivaCtrlFecha2(TipoFecha, self.ActoFechaInicial)
        event.Skip()

    def OnFATipofechafinChoice(self, event):
        #TipoFecha = self.FATipofechafin.GetClientData(self.FATipofechafin.Selection)
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        TipoFecha = MyClientData(event)
        ActivaCtrlFecha2(TipoFecha, self.ActoFechaFinal)
        event.Skip()

    def OnFPMunicipioChoice(self, event):
        if not CanEditPersona(status.personaActual): 
            ErrorSoloLectura(self)
            return
        status.personaActual.Pmpio_nac_u_origen = self.FPMunicipio.GetClientData(self.FPMunicipio.Selection)
        
        event.Skip()

    def OnRadioBoxPersonaChange(self, event):
        s= status.tipoPersona

        t=LlenaPersonas(self.listBoxPersonaBrowser, filtro=s)
        self.txtTotalPersonas.SetLabel("%i personas registradas"%t)
        #limpiaCamposPersona(self)

            
        event.Skip()


    def OnListBoxVinculosKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            v = self.listBoxVinculos.GetClientData(self.listBoxVinculos.Selection)
            p1 = v.vinculo1
            p2 = v.vinculo2
            
            if Borrar(self, u"\xbfBorrar este dato biogr\xe1fico?"):
                
                session.delete(v)
                
                print "p1.LaOtra2 /1", p1.LaOtra2
                p1.LaOtra2.remove(v)
                print "p1.LaOtra2 /2 ", p1.LaOtra2
                if p2:
                    print "p2 ",p2
                    print "p2.LaOtra1 /1 ",p2.LaOtra1
                    p2.LaOtra1.remove(v)
                    print "p2.LaOtra1 /2 ",p2.LaOtra1
                FlushInfo(id=121)
                status.vinculoActual = None

                LlenaCtrlVinculos(self, self.listBoxVinculos, status.personaActual)
        event.Skip()

    
      

    def OnListLocalizacionDclick(self, event):
        #i=self.listLocalizacion.Selection
        #L = self.listLocalizacion.GetClientData(i)
        L = MyClientData(event)
        LocalidadMaint(self, L)
        LlenaCtrlLocalizacion(self, self.listLocalizacion, status.casoActual)
        
        LlenaCtrlLocalizacion(self, self.FALocalidad, status.casoActual, renglonInicial=True)
        if status.actoActual:
            
            if status.actoActual.PLocalidad: 
                CtrlSelect(self.FALocalidad, status.actoActual.PLocalidad.Descriptor())
                
        event.Skip()

    def OnListLocalizacionKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
        
            LocBorrar = self.listLocalizacion.GetClientData(self.listLocalizacion.Selection)
            if Borrar(self, u"\xbfBorrar esta localizaci\xf3n?"):
                status.casoActual.localidades.remove(LocBorrar)
                session.delete(LocBorrar)
                FlushInfo(id=122)
                LlenaCtrlLocalizacion(self, self.listLocalizacion, status.casoActual)
                LlenaCtrlLocalizacion(self, self.FALocalidad, status.casoActual, renglonInicial=True)
                a=status.actoActual
                s=self
                if a:
                    if a.PLocalidad: CtrlSelect(s.FALocalidad, a.PLocalidad.Descriptor())


        event.Skip()

    def OnFACaracRelevanteKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            CaracBorrar = self.FACaracRelevante.GetClientData(self.FACaracRelevante.Selection)
            if Borrar(self, u"\xbfBorrar esta caracter\xedstica relevante?"):
                status.actoActual.PCaracRelevantes.remove(CaracBorrar)
                session.delete(CaracBorrar)
                FlushInfo(id=123)
                
                
                LlenaCtrl3(self.FACaracRelevante, [(i,i.Pcaracteristicarelevante.descripcion) for i in status.actoActual.PCaracRelevantes])
        
        
        
        
        
        event.Skip()

    def OnListBoxPerpetradoresKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            status.involActual = self.listBoxPerpetradores.GetClientData(self.listBoxPerpetradores.Selection)
            if Borrar(self, u"\xbfBorrar este perpetrador?"):
                status.actoActual.RolPerpetradores.remove(status.involActual)
                session.delete(status.involActual)
                FlushInfo(id=124)
                status.involActual = None

                LlenaPerpetradores(self, self.listBoxPerpetradores)
        event.Skip()

    def OnBtnActualizarCaso1Button(self, event):
        n=self.listaCasos.GetStringSelection()
        self.OnBtnActualizarCaso(event)
        self.listaCasos.SetStringSelection(n)
        self.listaCasos.SetFocus()
        event.Skip()

    def OnBtnAddFtePersonaRel(self, event):
        P=PersonaDlg(self, help=u'dlgpersFtePersonaRelacionada')
        if P:
            status.fuenteActual.PPersona = P
            self.staticTextRelPersona.SetLabel(P.Descriptor())
            

        event.Skip()

    def OnBtnAddDoc(self, event):
        
  
        
        event.Skip()
    def OnListBoxDocsDclick(self, event):
        
        SaveDataPub(self)
        status.pubActual = MyClientData(event)
        LoadDataPub(self)
        event.Skip()

    def OnButtonPubAddPerson(self, event):
        P=PersonaDlg(self, help=u'PersonaDlgPubPersona')
        if P:
            status.pubActual.PPersonareferenciada = P
            
            
            self.staticTextPubPersona.SetLabel(P.Descriptor())
        
        
        
        event.Skip()

    def OnButtonCambiaTitulosButton(self, event):
        CambiaTitulos(self)
        event.Skip()

    def OnListBox1Listbox(self, event):
        event.Skip()

    def OnBtnFPPais(self, event):
        pais = getTaxonomyTree(self, u"T15", u"Pa\xeds de origen o nacimiento",help=u'getTaxonomyTreePaisOrigen')
        if pais:
            
             status.personaActual.Ppais_nac_u_origen = pais
             self.FPPais.SetLabel(TesNotNull(status.personaActual.Ppais_nac_u_origen))
             
             mostrarEdo = pais.descripcion == localCountry
             AjustaLocalidadSegunPais(self, mostrarEdo)
             
        event.Skip()

    def OnListBox5Listbox(self, event):
        event.Skip()

    def OnAddLocalizacionButton(self, event):
        L=Localidad(status.casoActual.id)
        retcode = LocalidadMaint(self, L, nuevo=True)
        if retcode:
            if L.localidad or L.Municipio or L.Pais:
    
                status.casoActual.localidades.append(L)
                LlenaCtrlLocalizacion(self, self.listLocalizacion, status.casoActual)
                LlenaCtrlLocalizacion(self, self.FALocalidad, status.casoActual, renglonInicial=True)
                a=status.actoActual
                s=self
                if a:
                    if a.PLocalidad: CtrlSelect(s.FALocalidad, a.PLocalidad.Descriptor())
        event.Skip()

    def OnFPAddIdiomaButton(self, event):
        DialogTipificaPersona(status.personaActual, self, u'T14', 'PIdiomas', 945, desc='Idioma', help=u'DialogTipificaPersonaIdioma')
        LlenaCtrlPersonaTipificacion(self.FPIdioma, status.personaActual.PIdiomas)
        event.Skip()

    def OnFPAddDireccionesButton(self, event):
        D = PersonaTipificacion(910, status.personaActual, None)
        MaintDireccion(self, D)
        
        
        if D.masinformacion or D.telefono or D.correo_e or D.celular or D.web:
            session.add(D)
            FlushInfo(id=128)
            status.personaActual.PDirecciones.append(D)
            LlenaDireccionesPersona(self)
        else:
            del D
        
        event.Skip()

    def OnFPAddLenguaButton(self, event):
        DialogTipificaPersona(status.personaActual, self, u'T66', 'PLenguas', 946, desc=u'Lengua ind\xedgena', help=u'DialogTipificaPersonaLIndigena')
        LlenaCtrlPersonaTipificacion(self.FPLengua, status.personaActual.PLenguas)
        event.Skip()

    def OnFPAddOrigenEtnicoButton(self, event):
        DialogTipificaPersona(status.personaActual, self, u'T13', 'POrigenEtnico', 942, desc="Origen etnico", help=u'DialogTipificaPersonaOEtnico')
        LlenaCtrlPersonaTipificacion(self.FPOrigenEtnico, status.personaActual.POrigenEtnico)
        event.Skip()

    def OnFPAddCaracsButton(self, event):
        # no se usa....
        DialogTipificaPersona(status.personaActual, self, u'T23', 'PCaracteristicasRelevantes', 944)
        LlenaCtrlPersonaTipificacion(self.PFCaracs, status.personaActual.PCaracteristicasRelevantes)
        event.Skip()

    def OnFPIdiomaKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            #c = event.GetEventObject()
            #t = c.GetClientData(c.Selection)
            t = MyClientData(event)
            if Borrar(self, u"\xbfBorrar este idioma?"):
                session.delete(t)
                status.personaActual.PIdiomas.remove(t)
                FlushInfo(id=129)
                LlenaCtrlPersonaTipificacion(c, status.personaActual.PIdiomas)
                


        event.Skip()

    def OnFPLenguaKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            #c = event.GetEventObject()
            #t = c.GetClientData(c.Selection)
            t = MyClientData(event)
            if Borrar(self, u"\xbfBorrar esta lengua?"):
                session.delete(t)
                status.personaActual.PLenguas.remove(t)
                FlushInfo(id=130)
                LlenaCtrlPersonaTipificacion(c, status.personaActual.PLenguas)        
        event.Skip()

    def OnFPOrigenEtnicoKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            #c = event.GetEventObject()
            #t = c.GetClientData(c.Selection)
            t = MyClientData(event)
            if Borrar(self, u"\xbfBorrar este origen etnico?"):
                session.delete(t)
                status.personaActual.POrigenEtnico.remove(t)
                FlushInfo(id=131)
                LlenaCtrlPersonaTipificacion(c, status.personaActual.POrigenEtnico)
        event.Skip()

    def OnPFCaracsKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            c = event.GetEventObject()
            t = c.GetClientData(c.Selection)
            if Borrar(self, u"\xbfBorrar esta caracteristica?"):
                session.delete(t)
                status.personaActual.PCaracteristicasRelevantes.remove(t)
                FlushInfo(id=132)
                LlenaCtrlPersonaTipificacion(c, status.personaActual.PCaracteristicasRelevantes)
        
        event.Skip()

    def OnFPDireccionesKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            if Borrar(self, u"\xbfBorrar esta direcci\xf3n?"):
                #D = self.FPDirecciones.GetClientData(self.FPDirecciones.Selection)
                D = MyClientData(event)
                session.delete(D)
                status.personaActual.PDirecciones.remove(D)
                FlushInfo(id=133)
                LlenaDireccionesPersona(self)
                
        event.Skip()

    def OnFPDireccionesListboxDclick(self, event):
        #D = self.FPDirecciones.GetClientData(self.FPDirecciones.Selection)
        D = MyClientData(event)
        MaintDireccion(self, D)
        session.add(D)
        LlenaDireccionesPersona(self)
        
        event.Skip()

    def OnBtnInfoCaso(self, event):
        DlgInfo(self, status.casoActual)
        event.Skip()

    def OnBtnInfoActo(self, event):
        DlgInfo(self, status.actoActual)
        event.Skip()

    def OnBtnInfoInvol(self, event):
        DlgInfo(self, status.involActual)
        event.Skip()

    def OnBtnInfoInterv(self, event):
        DlgInfo(self, status.intervencionActual)
        event.Skip()

    def OnBtnInfoFte(self, event):
        DlgInfo(self, status.fuenteActual)
        event.Skip()

    def OnBtnInfoDoc(self, event):
        DlgInfo(self, status.pubActual)

        event.Skip()

    def OnBtnInfoPersona(self, event):
        DlgInfo(self, status.personaActual)
        event.Skip()

    def OnBtnDPersonaVictima(self, event):
        PersonaDetalles(self, status.actoActual.Pvictima)

        event.Skip()

    def OnBtnDPersonaPerpetrador(self, event):
        PersonaDetalles(self, status.involActual.persona)
        event.Skip()

    def OnListBoxVinculosDclick(self, event):
        SaveDataVinculo(self)
        status.vinculoActual = MyClientData(event)
        if status.vinculoActual:
            LoadDataVinculo(self)
            Enable_panel(self, 'Personas 4', enable=True)
            print "loaded ",status.vinculoActual
        event.Skip()

    def OnNBPersonasBioSysColourChanged(self, event):
        event.Skip()

    def OnBtnSaveVinculo(self, event):
        SaveDataVinculo(self)
        LoadDataVinculo(self)
        Enable_panel(self, 'Personas 4', enable=True)
        
        expr = status.vinculoActual.Descriptor() if status.vinculoActual else None
        
        LlenaCtrlVinculos(self, self.listBoxVinculos, status.personaActual, selected=expr)
        event.Skip()

    def OnBtnIntImpacto(self, event):
        t = getTaxonomyTree(self, u"T44", "Impacto", ctrl=self.txtIntImpacto, help=u'getTaxonomyTreeImpacto')
        if t:
            status.intervencionActual.Pimpacto = t
            
            
        event.Skip()

    def OnBtnIntEstatus(self, event):
        t = getTaxonomyTree(self, u"T46", "Estatus", ctrl=self.txtIntEstatus, help=u'getTaxonomyTreeEstatus')
        if t:
            status.intervencionActual.Pestatus = t        
        event.Skip()

    def OnBtnIntRespuesta(self, event):
        t = getTaxonomyTree(self, u"T27", "Respuesta", ctrl=self.txtIntRespuesta, help=u'getTaxonomyTreeRespuesta')
        if t:
            status.intervencionActual.Prespuesta = t        
        event.Skip()

    def OnSrchPersonaText(self, event):
        SaveDataPersona(self)
        clearFiltroPersona(self)
        aBuscar = self.srchPersona.GetValue()
        aBuscar = aBuscar.strip()
        expr = Sortable(aBuscar, trans=module2.transWildChar)
        
        limpiaCamposPersona(self)
        t=LlenaPersonas(self.listBoxPersonaBrowser, filtro2=expr)
        #self.txtTotalPersonas.SetLabel("%i personas registradas"%t)
        setPersonasSeleccionadas(self, t)
        self.txtTotalPersonasSeleccionadas.Enable()
        
        if status.panelPersonasEnabled:
            Enable_panel(self,'Personas 1', enable=False)
            Enable_panel(self,'Personas 2', enable=False)
            Enable_panel(self,'Personas 3', enable=False)
            Enable_panel(self, 'Personas 4', enable=False)
            status.panelPersonasEnabled=False
            self.srchPersona.SetFocus()
            
        event.Skip()

    def OnBtnNuevaPersona(self, event):
        nombre, apellido, indiv, res = DatosAltaPersona(self)
        if res:
            if ExistePersona(nombre, apellido, indiv):
                MError(self, u"Ya existe una persona con este nombre")
            else:
                SaveDataPersona(self)
                SaveDataVinculo(self)
                if apellido != '':
                    P=Persona(nombre, apellido, indiv=indiv)
                    session.add(P)
                    FlushInfo(id=134)
                    self.srchPersona.Clear()
                    status.personaActual = P
                    LoadDataPersona(self)
                    s= status.tipoPersona
                    
                    t=LlenaPersonas(self.listBoxPersonaBrowser, filtro=s)
                    self.txtTotalPersonas.SetLabel("%i personas registradas"%t) # (NoRegistros(Persona))
                    if status.EdoDef and False: #ojo
                        CtrlSelect(self.FPEstado, status.EdoDef)
                        MpoDesc = status.MpoDef.descripcion if status.MpoDef else ""
                        
                        LlenaCtrlMunicipios(self.FPMunicipio,status.EdoDef, selected=MpoDesc)
                status.totalPersonas = NoRegistros(Persona)
                
        event.Skip()

    def OnBtnPantAnterior(self, event):
        SaveDataPersona(self)
        a=status.actoActual
        i=status.involActual
        
        s=self
        if status.PantAnterior:
                ant = status.PantAnterior
                
                if ant == 1:  # acto o perpetrador
                  if a:
                      LlenaActos(self)
                      setLabelActoActual(self)
                      if a.Pvictima:
                           s.FAVictima.SetLabel(a.Pvictima.Descriptor(perm=CanEdit(status.casoActual)))
                  if i:
                      if i.persona: 
                          self.FIperpetrador.SetLabel(i.persona.Descriptor())
                          n = self.listBoxPerpetradores.GetSelection()
                          self.listBoxPerpetradores.SetString(n, i.persona.Descriptor())
                          
                          
                if ant == 2: # intervencion
                    if status.intervencionActual:
                        This=status.intervencionActual
                        if This.solicitante:
                            self.staticText17.SetLabel(This.solicitante.Descriptor())
                        if This.contraparte:
                            self.staticText19.SetLabel(This.contraparte.Descriptor())
                        if This.Pinterviniente:
                            self.txtIntParte.SetLabel(This.Pinterviniente.Descriptor())
                if ant == 3: # fuentes
                    
                    if status.fuenteActual:
                        f = status.fuenteActual
                        if f.PPersona_como_fuente: 
                            self.staticTextFtePersona.SetLabel(f.PPersona_como_fuente.Descriptor(perm=CanEdit(status.casoActual)))
                        if f.persona_referenciada_id:
                            s.staticTextRelPersona.SetLabel(f.PPersona.Descriptor())
                        LlenaCtrlFuentes(self)
                        
                    if status.pubActual:
                        f = status.pubActual
                        if f.PPersonareferenciada:
                            f = status.pubActual
                            s.staticTextPubPersona.SetLabel(f.PPersonareferenciada.Descriptor())
                        
            
                self.NBMain.SetSelection(status.PantAnterior)
        status.PantAnterior = None
        self.btnPantAnterior.Show(False)
        event.Skip()

    def OnBtnDPersonaFuente(self, event):
        
        event.Skip()

    def OnBtnDPersonaRel(self, event):
        PersonaDetalles(self, status.fuenteActual.PPersona)
        event.Skip()

    def OnBtnDPersonaRel2(self, event):
        PersonaDetalles(self, status.pubActual.PPersonareferenciada)
        event.Skip()

    def OnBtnDPersonaSobre(self, event):
        PersonaDetalles(self, status.intervencionActual.solicitante)
        event.Skip()

    def OnBtnDPersonaAquien(self, event):
        PersonaDetalles(self, status.intervencionActual.contraparte)
        event.Skip()

    def OnCasoIsearchEnter(self, event):
        aBuscar = self.CasoIsearch.GetValue()
        aBuscar = aBuscar.strip()
        W = Sortable(aBuscar, trans=module2.transWildChar)
        print "-- ", W.encode('latin_1','replace')
        
        N=LlenaCtrlCasos(self.listaCasos, filtroIsearch=W)
        if W != '':
             self.txtTotalCasos.SetLabel("%i casos registrados"%(status.TotalCasos))
             self.txtCasosSeleccionados.SetLabel("%i casos seleccionados"%N)
        else:
             self.txtTotalCasos.SetLabel("%i casos registrados"%(status.TotalCasos))
             self.txtCasosSeleccionados.SetLabel('')
        
        event.Skip()

    def OnFBFechaFinalTipoChoice(self, event):
        if not CanEditPersona(status.personaActual): 
            ErrorSoloLectura(self)
            return
        TipoFecha = MyClientData(event)
        ActivaCtrlFecha2(TipoFecha, self.BioFechaFinal)
        
        event.Skip()

    def OnFBFechaInicialTipoChoice(self, event):
        if not CanEditPersona(status.personaActual): 
            ErrorSoloLectura(self)
            return
        TipoFecha = MyClientData(event)
        ActivaCtrlFecha2(TipoFecha, self.BioFechaInicial)        
        event.Skip()

    def OnChoiceFteTipoFecha(self, event):
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        TipoFecha = MyClientData(event)
        ActivaCtrlFecha2(TipoFecha, self.FuenPerFecha)        

        event.Skip()

    def OnChoicePubTipoFecha(self, event):
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        TipoFecha = MyClientData(event)
        ActivaCtrlFecha2(TipoFecha, self.FuenDocFecha)
        event.Skip()

    def OnListBoxPersonaBrowserKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            P = MyClientData(event)
            n = self.listBoxPersonaBrowser.Selection
            #P = self.listBoxPersonaBrowser.GetClientData(n)
            if P:
                d= P.Roles()
                Razones = ', '.join([i for i in d.keys() if d[i]])
                if Razones:
                    MError(self, 'Esta persona no puede ser borrada ya que figura como '+Razones)
                else:    
                    if Borrar(self, u"\xbfBorrar esta persona?"):
                    
                        try:
                             
                             session.delete(P)
                             FlushInfo(id=135)
                             self.listBoxPersonaBrowser.Delete(n)
                             limpiaCamposPersona(self)
                             status.personaActual = None
                             status.totalPersonas = NoRegistros(Persona)
                             self.txtTotalPersonas.SetLabel("%i personas registradas"%(status.totalPersonas))
                             Enable_panel(self, 'Personas 4', enable=False)
                             
                        except:
                             MError(self, 'Esta persona no pudo ser dada de baja')
                             print "Unexpected error:", sys.exc_info()
            else:
                MError(self, "Debes seleccionar primero una persona")    
        event.Skip()

    def OnFPTipodefechaChoice(self, event):
        if not CanEditPersona(status.personaActual): 
            ErrorSoloLectura(self)
            return
        TipoFecha = MyClientData(event)
        ActivaCtrlFecha2(TipoFecha, self.PerFechaNac)
        event.Skip()

    def OnButton1Button(self, event):
        event.Skip()

    def OnBtnFPCiudadaniaButton(self, event):
        pais = getTaxonomyTree(self, u"T15", u"Ciudadan\xeda o pa\xeds sede", help=u'getTaxonomyTreeCiudadania')
        if pais:
            
             status.personaActual.Pciudadania_o_sede = pais
             self.FPCiudadania.SetLabel(TesNotNull(status.personaActual.Pciudadania_o_sede))
        event.Skip()

    def OnBtnActoLegislacion(self, event):
        
        R = DialogTipifica(self, u'T62',2154, status.actoActual.id, desc=u'Legislaci\xf3n nacional', help=u'DialogTipificaLegisNac')
        if R:
            LlenaCtrlNormatividad(self, self.FALegis, 2154)
            CtrlSelect(self.FALegis, status.legisActual)
            self.FAlegislacion_nacional_notas.Enable()
            self.staticText98.Enable()
            self.txtLongNorLeg.Enable()
            
            

        event.Skip()

    def OnBtnActoInstrInt(self, event):
        R = DialogTipifica(self, u'T06',2155, status.actoActual.id, desc='Instrumentos internacionales', help=u'DialogTipificaInstInt')
        if R:
            LlenaCtrlNormatividad(self, self.FAInstr, 2155)
            CtrlSelect(self.FAInstr, status.instrActual)
            self.FAinstrumentos_int_notas.Enable()
            self.txtLongNorIns.Enable()
            self.staticText96.Enable()
        event.Skip()

    def OnBtnSearchButton(self, event):
        if not status.filtroCaso:
            status.filtroCaso = QueryCaso(self)
            
        status.filtroCaso.edit()
        
            
        

        
        
            
        event.Skip()

    def OnBtnSearchExecuteButton(self, event):
        self.CasoIsearch.ChangeValue('')
        # limpia busqueda rapida
        self.txtTotalCasos.SetLabel("%i casos registrados"%(status.TotalCasos))
        self.txtCasosSeleccionados.SetLabel('')
        if status.filtroCaso:
            status.applySearch=True
            
            R=status.filtroCaso.execute()
            #ojo
            print "condiciones",status.filtroCaso.MisCondiciones

            
            status.casosSeleccionados=R.all()
            
            status.casoIdseleccionados = [i.id for i in status.casosSeleccionados] 
            #print status.casosSeleccionados
            totalSeleccionados = 0
            totalSeleccionados=LlenaCtrlCasos(self.listaCasos, dataset=status.casosSeleccionados)

            self.txtTotalCasos.SetLabel("%i casos registrados"%(status.TotalCasos))
            self.txtCasosSeleccionados.SetLabel("%i casos seleccionados"%totalSeleccionados)
            if totalSeleccionados:
                status.casoActual = status.casosSeleccionados[0]
                LoadDataCaso(self)
            else:
                status.casoActual = None
                LimpiaCamposCaso(self)

        event.Skip()

    def OnBtnShowAllButton(self, event):
        
        s = self.listaCasos.GetStringSelection()
        blanqueaCasoIsearch(self)
        
        
        self.listaCasos.SetStringSelection(s)
        
        event.Skip()

    def OnBtnAddRelacionButton(self, event):
        SaveDataCasoRel(self)
        otroCaso = None
        otroCaso,tipoRel,cancelar = GetCaso(self, NoMyself=True)
        if cancelar:
            return
        if otroCaso and tipoRel:
            if status.casoActual != otroCaso:
                if otroCaso not in status.casoRelaciones:
                    cr = Caso_vinculo(status.casoActual, otroCaso, tipoRel)
                    session.add(cr)
                    FlushInfo(id=136)
                    status.casoRelActual = cr
                else:
                    MError(self, u"Ya existe una relaci\xf3n con ese caso")
            else:
                MError(self, "Un caso no puede ser relacionado consigo mismo")
            LlenaCtrlCasoRel(self)
            if otroCaso:
                self.listBoxCasoRel.SetStringSelection(otroCaso.Descriptor())
            LoadDataCasoRel(self)
        else:
            #if otroCaso or tipoRel: #ojo!!!!!
                MError(self, u"No hay datos suficientes para establecer la relaci\xf3n. Verifica que asignaste el Tipo de relaci\xf3n y que seleccionaste un caso")    
        event.Skip()

    def OnBtnCasoRelButton(self, event):
        if status.casoRelActual:
            c = GetCaso(self, SoloCaso=True , NoMyself=True)
            if c in status.casoRelaciones:
                MError(self, u"Ya existe una relaci\xf3n entre estos casos")
                return
            if c:
                if status.casoRelActual.reciproco:
                    if c != status.casoRelActual.Pcaso_2:
                        status.casoRelActual.Pcaso_1=c
                        self.FRCCasoRel.SetLabel(c.descripcion)
                    else:
                        MError(self, "Un caso no puede ser relacionado consigo mismo")
                else:
                    if c != status.casoRelActual.Pcaso_1:
                        status.casoRelActual.Pcaso_2=c
                        self.FRCCasoRel.SetLabel(c.descripcion)
                    else:
                        MError(self, "Un caso no puede ser relacionado consigo mismo")
                
                LlenaCtrlCasoRel(self)
            
        event.Skip()

    def OnBtnTipoRelCasoButton(self, event):
        if status.casoRelActual:
           t = getTaxonomyTree(self, u"T22", u"Relaci\xfan entre casos", help=u'getTaxonomyTreeRelacionEntreCasos')
           if t:
               status.casoRelActual.Ptipo = t
               self.FRCCasoRelTipo.SetLabel(status.casoRelActual.Ptipo.descripcion)
               LlenaCtrlCasoRel(self)
        event.Skip()

    def OnListBox1Help(self, event):

        event.Skip()

    def OnListBoxCasoRelListboxDclick(self, event):
        s=self
        
        SaveDataCasoRel(self)
        
        status.casoRelActual = MyClientData(event)

        LoadDataCasoRel(self)
        #LlenaCtrlCasoRel(self) # por que??


    def OnListBoxCasoRelKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            if Borrar(self, u"\xbfBorrar este dato?"):
                rel = MyClientData(self.listBoxCasoRel)
                session.delete(rel)
                if rel in status.casoActual.PelCaso2:
                    status.casoActual.PelCaso2.remove(rel)
                if rel in status.casoActual.PelCaso1:
                    status.casoActual.PelCaso1.remove(rel)
                status.casoRelActual = None

                LlenaCtrlCasoRel(self)
        event.Skip()

    def OnNBPersonasFlatnotebookPageChanged(self, event):
        obj = event.GetEventObject()
        paginaPrev = event.GetOldSelection()
        pagina = event.GetSelection()
        TitPagina = obj.GetPageText(pagina)
        TitPaginaPrev = obj.GetPageText(paginaPrev)
        
        if TitPaginaPrev == 'Datos biograficos':
            SaveDataVinculo(self)
        if TitPagina == 'Datos generales':
            if status.ReloadPersona:
                s= status.tipoPersona
                t=LlenaPersonas(self.listBoxPersonaBrowser, filtro=s)
                self.txtTotalPersonas.SetLabel("%i personas registradas"%t)
                status.ReloadPersona = False
            


        
        event.Skip()

    def OnFAInstrListboxDclick(self, event):
        #SaveDataInstr(self)
        status.instrActual = MyClientData(event)
        
        self.FAinstrumentos_int_notas.SetValue(status.instrActual.notas)
        self.FAinstrumentos_int_notas.Enable()
        self.txtLongNorIns.Enable()
        self.staticText96.Enable()
        self.delInstrInt.Enable(status.canEditCaso)
        self.btnInfoInter.Enable()
        event.Skip()

    def OnFALegisListboxDclick(self, event):
        #SaveDataLegis(self)
        status.legisActual = MyClientData(event)
        
        self.FAlegislacion_nacional_notas.SetValue(status.legisActual.notas)
        self.FAlegislacion_nacional_notas.Enable()
        self.FAlegislacion_nacional_notas.SetEditable(status.canEditCaso)
        self.staticText98.Enable()
        self.txtLongNorLeg.Enable()
        self.delLegislacion.Enable(status.canEditCaso)
        self.btnInfoLegis.Enable()
        
        event.Skip()

    def OnBtnTipodeactoButton(self, event):
        pattern=derechosafectadosPattern(status.casoActual, u'T04')
        t=getTaxonomyTree(self, u"T04", "Tipo de acto o VDH", Pattern=pattern, help=u'getTaxonomyTreeTipodeActo')
        if t:
          status.actoActual.PTipodeacto = t
          self.FATipoacto.SetLabel(t.descripcion)
        event.Skip()

    def OnIntCtrlXInt(self, event):
        ctrl = event.GetEventObject()
        valor = ctrl.GetValue()
        if valor != None:
            if not ctrl.IsInBounds():
                (min, max) = ctrl.GetBounds()
                
                MError(self, u"El valor %i esta fuera de rango. El rango permitido es de %i a %i"%(valor, min, max))
        
        event.Skip()

    def OnTextCtrl1TextEnter(self, event):
        
        event.Skip()

    def OnTextCtrl1Text(self, event):
        
        event.Skip()

    def OnTextCtrl2Text(self, event):
        
        
        
        event.Skip()

    def OnButtonRemoveTipodelugarButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            self.FATipodelugar.SetLabel('')
            status.actoActual.PTipodelugar = None
        event.Skip()

    def OnButtonRemoveEstatusdelavictimaButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.actoActual.PEstatusvictima = None
            self.FAEstatusvictima.SetLabel('')
        event.Skip()

    def OnButtonRemoveEstatusVDHButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.actoActual.PEstatusvdh = None
            self.FAEstatusvdh.SetLabel('')
        event.Skip()

    def OnButtonRemoveDequienButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.intervencionActual.solicitante = None
            self.staticText17.SetLabel('')
        event.Skip()

    def OnButtonRemoveTipoIntervencionButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.intervencionActual.tipo = None
            self.staticText18.SetLabel('')
        event.Skip()

    def OnButtonRemoveAquienButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.intervencionActual.contraparte = None
            self.staticText19.SetLabel('')
        event.Skip()

    def OnButtonRemoveIntRespuestaButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            self.txtIntRespuesta.SetLabel('')
            status.intervencionActual.Prespuesta = None
        event.Skip()

    def OnButtonRemoveIntImpactoButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            self.txtIntImpacto.SetLabel('')
            status.intervencionActual.Pimpacto = None
        event.Skip()

    def OnButtonRemoveIntEstatusButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            self.txtIntEstatus.SetLabel('')
            status.intervencionActual.Pestatus = None
        event.Skip()

    def OnButtonRemoveFteConexionInformacionButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.fuenteActual.PConexion_info = None
            self.staticTextConexionInfo.SetLabel('')
        event.Skip()

    def OnBtnRemoveFtePersonaRelButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.fuenteActual.PPersona = None
            self.staticTextRelPersona.SetLabel('')
        event.Skip()

    def OnButtonPubRemovePersonButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.pubActual.PPersonareferenciada=None
            self.staticTextPubPersona.SetLabel('')
        event.Skip()

    def OnButtonRemoveUltStatusPerpButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.involActual.Pultimostatusperpetrador = None
            self.FIultimostatusperpetrador.SetLabel('')
        event.Skip()

    def OnButtonRemoveTipoPerpButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.involActual.Ptipoperpetrador = None
            self.FItipoperpetrador.SetLabel('')
        event.Skip()

    def OnButtonRemoveGradoInvolButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.involActual.Pgradoinvolucramiento = None
            self.FIgradoinvolucramiento.SetLabel('')
        event.Skip()

    def OnBtnRemoveFPPaisButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.personaActual.Ppais_nac_u_origen = None
            self.FPPais.SetLabel('')
            mostrarEdo = False
            AjustaLocalidadSegunPais(self, mostrarEdo)
        event.Skip()

    def OnBtnRemoveFPCiudadaniaButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.personaActual.Pciudadania_o_sede = None
            self.FPCiudadania.SetLabel('')
        event.Skip()



    def OnBtnPrintCasoButton(self, event):
        if status.casoActual:
            printObj([status.casoActual], 'HTML', "Caso")
            MError(self, u"Se gener\xf3 archivo de impresi\xf3n...")
        event.Skip()

    def OnContextHelpButton1Help(self, event):
        event.Skip()


    def OnListBoxDocsKeyDown1(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            ObjBorrar = MyClientData(event)
            #ObjBorrar = self.listBoxDocs.GetClientData(self.listBoxDocs.Selection)
            if Borrar(self,u"\xbBorrar esta publicaci\xf3n?"):
                session.delete(ObjBorrar)
                status.casoActual.PPublicaciones.remove(ObjBorrar)
                status.pubActual = None
                FlushInfo(id=137)
                LlenaCtrlPubs(self)
        
        event.Skip()

    def OnBtnIntPIntButton(self, event):
        P=PersonaDlg(self, help=u'dlgpersonaParteInt')
        if P:
            status.intervencionActual.Pinterviniente = P
            

            self.txtIntParte.SetLabel(P.Descriptor())
        event.Skip()

    def OnBtnRemoveIntPIntButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.intervencionActual.Pinterviniente = None
            self.txtIntParte.SetLabel('')
        event.Skip()

    def OnListPersonaVinculosDBListboxDclick(self, event):
        SaveDataPersona(self)
        
        status.casoActual = MyClientData(event)
        LoadDataCaso(self)
        self.NBMain.SetSelection(0)
        self.NBCasos.SetSelection(0)
        self.pantAnterior.Show()
        blanqueaCasoIsearch(self)
        
        if status.casoActual:
            nombre = status.casoActual.Descriptor()
            self.listaCasos.SetStringSelection(nombre)
        event.Skip()

    def OnFBFechaInfo_vigenteTipoChoice(self, event):
        if not CanEditPersona(status.personaActual): 
            ErrorSoloLectura(self)
            return
        TipoFecha = MyClientData(event)
        ActivaCtrlFecha2(TipoFecha, self.BioFechaVig)
        event.Skip()

    def OnBtnPubTipoPubButton(self, event):
        T = getTaxonomyTree(self, u"T16", u"Tipo de fuente", help=u'getTaxTipodeFuente')
        if T:
            status.pubActual.PTipopublicacion = T
            self.txtPubTipoPub.SetLabel(T.descripcion)
        event.Skip()

    def OnBtnRemovePubTipoPubButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.pubActual.PTipopublicacion = None
            self.txtPubTipoPub.SetLabel('')
        event.Skip()

# patron de borrado

    def OnFAInstrKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            ctrl = event.GetEventObject()
            lista = status.casoActual.tipificaciones
            ItemBorrar = MyClientData(event)
            if Borrar(self, u"\xbBorrar este instrumento?"):
                lista.remove(ItemBorrar)
                session.delete(ItemBorrar)
                FlushInfo(id=139)
                status.instrActual = None
                self.FAinstrumentos_int_notas.Enable(False)
                
                LlenaCtrlNormatividad(self, ctrl, 2155)
                
        
        event.Skip()

    def OnBtnActoLegislacionKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            ctrl = event.GetEventObject()
            lista = status.casoActual.tipificaciones
            ItemBorrar = MyClientData(event)
            if Borrar(self, u"\xbfBorrar esta legislaci\xf3n?"):
                lista.remove(ItemBorrar)
                session.delete(ItemBorrar)
                status.legisActual = None
                

                FlushInfo(id=140)
                self.FAlegislacion_nacional_notas.Enable(False)
                LlenaCtrlNormatividad(self, ctrl, 2154)
        
        
        
        
        event.Skip()

    def OnBtnPrintPersonaButton(self, event):
        if status.personaActual:
            printObj([status.personaActual], 'HTML', "Persona")
            MError(self, u"se genero archivo de impresion...")
        event.Skip()

    def OnButtonSelPerpetradorButton(self, event):
        P=PersonaDlg(self)
        if P:
            status.involActual.persona = P
            
            
            self.FIperpetrador.SetLabel(P.Descriptor())
            LlenaPerpetradores(self, self.listBoxPerpetradores)
            LlenaPerpetradores(self, self.listBoxActoPerpetradores)
        event.Skip()

    def OnTextCtrlDescripcionNarrativaText(self, event):
        cuentaEspacios(self.txtLongNarra, event)

        event.Skip()

    def OnTextCtrlResumenText(self, event):
        cuentaEspacios(self.txtLongResDesc, event)
        event.Skip()

    def OnTextCtrlObservacionesText(self, event):
        cuentaEspacios(self.txtLongObs, event)
        event.Skip()

    def OnBtnTipoVinculoButton(self, event):
        t=getTaxonomyTree(self, u"T21", u"Tipo de relacion",help=u'getTaxonomyTreeTipodeVinculo')
        if t:
            status.vinculoActual.tipo = t
            self.txtTipoVinculo.SetLabel(t.descripcion)
            SaveDataVinculo(self)
        event.Skip()

    def OnNBActosFlatnotebookPageChanged(self, event):
        obj = event.GetEventObject()
        paginaPrev = event.GetOldSelection()
        pagina = event.GetSelection()
        TitPagina = obj.GetPageText(pagina)
        TitPaginaPrev = obj.GetPageText(paginaPrev)
        
        if paginaPrev == 1:
            SaveDataInvol(self)
        
        if paginaPrev == 0:
           SaveDataActo(self)


    def OnNBCasosFlatnotebookPageChanged(self, event):
        saveDataCaso(self)
        
        event.Skip()

    def OnBtnDPersonaParteIntButton(self, event):
        PersonaDetalles(self, status.intervencionActual.Pinterviniente)
        event.Skip()

    def OnButtonActualizarCaso3Button(self, event):
        self.OnBtnActualizarCaso1Button(event)
        event.Skip()

    def OnChoiceIntTipofechaChoice(self, event):
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        TipoFecha = MyClientData(event)
        ActivaCtrlFecha2(TipoFecha, self.InterFecha)
        event.Skip()

    def OnChoicePubTipofechaconsultaChoice(self, event):
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        TipoFecha = MyClientData(event)
        ActivaCtrlFecha2(TipoFecha, self.FuenDocFechaConsulta)
        event.Skip()

    def OnFPTipodefecharecepcionChoice(self, event):
        if not CanEditPersona(status.personaActual): 
            ErrorSoloLectura(self)
            return
        TipoFecha = MyClientData(event)
        ActivaCtrlFecha2(TipoFecha, self.PerFechaRec)
        event.Skip()

    def OnFCtipo_frecepcionChoice(self, event):
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        TipoFecha = MyClientData(event)
        ActivaCtrlFecha2(TipoFecha, self.CasoFechaRecepcion)
        event.Skip()

    def OnBtnLocMasInfoButton(self, event):
        n = self.listLocalizacion.Selection
        if n > -1:
            loc = self.listLocalizacion.GetClientData(n)
            if loc:
                
                Locldetalles.LocDetalles(self, tesDesc(loc.Pais), tesDesc(loc.Estado), tesDesc(loc.Municipio), loc.localidad, loc.notas_municipio, loc.notas_localidad)
        event.Skip()

    def OnListLocalizacionListbox(self, event):
        n = self.listLocalizacion.Selection
        if n > -1:
            self.delLocalizacion.Enable(CanEdit(status.casoActual))
            loc = self.listLocalizacion.GetClientData(n)
            if loc:
                if loc.notas_municipio or  loc.notas_localidad:
                    self.btnLocMasInfo.Show()
                else:
                    self.btnLocMasInfo.Show(False)
                    
        
        event.Skip()

    def OnBtnAbrirLigaButton(self, event):
        nombre = self.textCtrlPubLigaSitio.GetValue()
        if nombre:
            try:
                webbrowser.open(nombre)
            except:
                MError(self, u"No es posible abrir esta liga")
        event.Skip()

    def OnBtnDPersonaFuenteButton(self, event):
        PersonaDetalles(self, status.fuenteActual.PPersona_como_fuente)
        event.Skip()

    def OnPguardar2Button(self, event):
        self.OnButtonPGuardar(event)
        event.Skip()

    def OnPguardar3Button(self, event):
        self.OnButtonPGuardar(event)
        event.Skip()

    def OnCrGuardarButton(self, event):
        SaveDataCasoRel(self)
        event.Skip()

    def OnTextCtrlCAComentariosText(self, event):
        cuentaEspacios(self.txtLongAdmComent, event)
        event.Skip()

    def OnTextCtrlCAArchivosText(self, event):
        cuentaEspacios(self.txtLongAdmArch, event)
        event.Skip()

    def OnTextCtrlINObservacionesText(self, event):
        cuentaEspacios(self.txtLongInObs, event)
        event.Skip()

    def OnTxtIntComentariosText(self, event):
        cuentaEspacios(self.txtLongIntComent, event)
        event.Skip()

    def OnTxtIntObservacionesText(self, event):
        cuentaEspacios(self.txtLongIntObs, event)
        event.Skip()

    def OnTxtIntRespuestaText(self, event):
        cuentaEspacios(self.txtLongIntRes, event)
        event.Skip()

    def OnTxtIntImpactoText(self, event):
        cuentaEspacios(self.txtLongIntImp, event)
        event.Skip()

    def OnTextCtrlFteObservacionesText(self, event):
        cuentaEspacios(self.txtLongFPObs    , event)
        
        event.Skip()

    def OnTextCtrlFteComentariosText(self, event):
        cuentaEspacios(self.txtLongFPComent   , event)
        event.Skip()

    def OnTextCtrlPubTituloText(self, event):
        cuentaEspacios(self.txtLongFDDatos    , event)
        event.Skip()

    def OnTextCtrlPubObservacionesText(self, event):
        cuentaEspacios(self.txtLongFDObs, event)
        event.Skip()

    def OnTextCtrlPubComentariosText(self, event):
        cuentaEspacios(self.txtLongFDComent   , event)
        event.Skip()

    def OnBtnRepsButton(self, event):
        if not status.casosSeleccionados:
            status.casosSeleccionados = session.query(Caso).all()
        dlg=frameRep5.Frame3(self)
        dlg.MakeModal()
        dlg.Show()
        #dlg.Destroy()
        event.Skip()

    def OnFAObservacionesText(self, event):
        cuentaEspacios(self.txtLongFAObs, event)
        event.Skip()

    def OnBtnPrelacionadaButton(self, event):
        P=PersonaDlg(self, excepto=status.personaActual, help="Prelacionada")
        if P:
            status.vinculoActual.vinculo2 = P
            self.txtPrelacionada.SetLabel(P.Descriptor() )
            SaveDataVinculo(self)
            LlenaCtrlVinculos(self, self.listBoxVinculos, status.personaActual)
        event.Skip()

    def OnBtnAddOcupacionButton(self, event):
        ocupacion = getTaxonomyTree(self, u"T10", u'Ocupaci\xf3n', help=u'getTaxonomyTreeOcupacion')
        if ocupacion:
            status.personaActual.Pocupacion = ocupacion
            self.FPstrOcupacion.SetLabel(TesNotNull(ocupacion))
        event.Skip()

    def OnBtnDelOcupacionButton(self, event):
        if Borrar(self, u"\xbfBorrar esta ocupaci\xf3n?"):
            status.personaActual.Pocupacion = None
            self.FPstrOcupacion.SetLabel('')
        
        event.Skip()

    def OnFPObservacionesText(self, event):
        cuentaEspacios(self.longPerObs, event)
        event.Skip()

    def OnFPComentariosText(self, event):
        cuentaEspacios(self.longPerCom, event)
        event.Skip()

    def OnFPArchivosText(self, event):
        cuentaEspacios(self.longPerArch, event)
        event.Skip()

    def OnLongPerComHelp(self, event):
        event.Skip()

    def OnLongPerArchHelp(self, event):
        event.Skip()

    def OnFBObservacionesText(self, event):
        cuentaEspacios(self.longPerDBObs, event)
        event.Skip()

    def OnFBComentariosText(self, event):
        cuentaEspacios(self.longPerDBCom, event)
        event.Skip()

    def OnButton3Button(self, event):
        
        #p=self.__getattribute__('NBActosPerp')
        #res=self.NBActos.RemovePage(1)
        #print res
        screenconfig.ScreenConfig(self, 'NBMain')
        self.NBMain.Layout()
        event.Skip()

    def OnChoiceMonitoreoChoice(self, event):
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        event.Skip()

    def OnFAConfidencialidadCheckbox(self, event):
        checaRO(self, event, status.canEditCaso)
        event.Skip()

    def OnFIconfidencialidadCheckbox(self, event):
        checaRO(self, event, status.canEditCaso)
        event.Skip()

    def OnChoiceFteIdiomaChoice(self, event):
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        event.Skip()

    def OnChoiceFteLenguaIndigenaChoice(self, event):
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        event.Skip()

    def OnChoiceFteConfiabilidadChoice(self, event):
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        event.Skip()

    def OnChoicePubIdiomaChoice(self, event):
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        event.Skip()

    def OnChoicePubLenguaIndigenaChoice(self, event):
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        event.Skip()

    def OnChoicePubConfiabilidadChoice(self, event):
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        event.Skip()

    def OnFALocalidadChoice(self, event):
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        event.Skip()

    def OnFBConfidencialidadCheckbox(self, event):
        if not CanEditPersona(status.personaActual): 
            ErrorSoloLectura(self)
            return
        event.Skip()

    def OnChoiceTipoEdadChoice(self, event):
        if not CanEdit(status.casoActual): 
            ErrorSoloLectura(self)
            return
        else:
            s=self.choiceTipoEdad.Selection
            if s < 1: self.FAedad_victima.SetValue('')
            
        event.Skip()

    def OnDelCasoButton(self, event):
            CasoEnC2 = None
            
            CasoBorrar = MyClientData(self.listaCasos)
            if CasoBorrar:
                if CasoSepuedeBorrar(self, CasoBorrar):
                    if cnf.baseCentral:
                        id = CasoBorrar.id
                        if CasoBorrar.clavestatus == 3:
                            CasoEnC2 = CasoBorrar.id
                    for tipificacion in CasoBorrar.tipificaciones:
                        session.delete(tipificacion)
                        del tipificacion
                    session.delete(CasoBorrar.PLoginfo)
                    session.delete(CasoBorrar)
                    del CasoBorrar
                    status.casoActual = None
    
                    FlushInfo(id=120)
                    self.CasoIsearch.ChangeValue('')
                    LlenaCtrlCasos(self.listaCasos)
                    status.TotalCasos = NoRegistros(Caso)
                    self.txtTotalCasos.SetLabel("%i casos registrados"%(status.TotalCasos))
                    self.txtCasosSeleccionados.SetLabel('')
                    
                    LimpiaCamposCaso(self)
                    Enable_panel(self, 'Datos Generales', enable=False)
                    setEtiquetaCasoActual(self, '', enable=False)
                    # ahora buscamos casos en C2 que hayan estado referidos a C3
                    if CasoEnC2:
                        print "buscando caso ", CasoEnC2 , " en C2"
                        q = session.query(Caso).filter(Caso.casorelacionadoc3 == CasoEnC2).all()
                        for C in q:
                            C.casorelacionadoc3 = None
                            C.clavestatusc3 = 0 if C.clavestatusc3 != 1 else 1
                            session.add(C)
                            print 'actualizado ',C
                        session.flush()
        #event.Skip()

    def OnDelLocalizacionButton(self, event):
        #LocBorrar = self.listLocalizacion.GetClientData(self.listLocalizacion.Selection)
        LocBorrar = MyClientData(self.listLocalizacion)
        if LocBorrar:
            if LocBorrar in [i.PLocalidad for i in status.casoActual.actos]:
                MError(self, u"Esta localizaci\xf3n no puede ser borrada ya que est\xe1 presente en un acto de este caso")
                return
            if Borrar(self, u"\xbfBorrar esta localizaci\xf3n?"):
                status.casoActual.localidades.remove(LocBorrar)
                session.delete(LocBorrar)
                FlushInfo(id=122)
                LlenaCtrlLocalizacion(self, self.listLocalizacion, status.casoActual)
                LlenaCtrlLocalizacion(self, self.FALocalidad, status.casoActual, renglonInicial=True)
                a=status.actoActual
                s=self
                if a:
                    if a.PLocalidad: CtrlSelect(s.FALocalidad, a.PLocalidad.Descriptor())
    

    def OnDelLegislacionButton(self, event):
        ctrl = self.FALegis
        lista = status.casoActual.tipificaciones
        ItemBorrar = MyClientData(ctrl)
        
        if ItemBorrar:
            mensaje = u"Esta legislaci\xf3n contiene notas. \xbfEst\xe1 seguro que desea borrarla?" if ItemBorrar.notas else u"\xbfBorrar esta legislaci\xf3n?"
            if Borrar(self, mensaje):
                lista.remove(ItemBorrar)
                session.delete(ItemBorrar)
                status.legisActual = None
                self.FAlegislacion_nacional_notas.Enable(False)
                FlushInfo(id=140)
                LlenaCtrlNormatividad(self, ctrl, 2154)
        event.Skip()

    def OndelInstrInt(self, event):
        ctrl = self.FAInstr
        lista = status.casoActual.tipificaciones
        ItemBorrar = MyClientData(ctrl)
        if ItemBorrar:
            mensaje = u"Este instrumento contiene notas. \xbfEst\xe1 seguro que desea borrarlo?" if ItemBorrar.notas else "\xbfBorrar este instrumento?"
            if Borrar(self, mensaje):
                lista.remove(ItemBorrar)
                session.delete(ItemBorrar)
                FlushInfo(id=139)
                status.instrActual = None
                self.FAinstrumentos_int_notas.Enable(False)
                LlenaCtrlNormatividad(self, ctrl, 2155)
        event.Skip()

    def OnDelActoButton(self, event):
        ActoBorrar = MyClientData(self.listActos)
        if ActoSepuedeBorrar(self, ActoBorrar):
            ActoBorrar.borrar()
            #for carac in ActoBorrar.PCaracRelevantes:
            #    if carac.PLoginfo:
            #        session.delete(carac.PLoginfo)
            #    session.delete(carac)
            #    del carac
            #session.delete(ActoBorrar)
            
            
            status.casoActual.actos.remove(ActoBorrar)
            
            FlushInfo(id=117)
            status.actoActual = None
            LimpiaCampos(self, camposEntidad['acto'])
            Enable_panel(self, 'Actos', enable=False)

            LlenaActos(self)
        event.Skip()

    def OnDelCaracRelButton(self, event):
        CaracBorrar = self.FACaracRelevante.GetClientData(self.FACaracRelevante.Selection)
        if Borrar(self, u"\xbfBorrar esta caracter\xedstica?"):
            status.actoActual.PCaracRelevantes.remove(CaracBorrar)
            if CaracBorrar.PLoginfo:
                session.delete(CaracBorrar.PLoginfo)
            session.delete(CaracBorrar)
            FlushInfo(id=123)
            
            LlenaCtrl3(self.FACaracRelevante, [(i,i.Pcaracteristicarelevante.descripcion) for i in status.actoActual.PCaracRelevantes])
        
        event.Skip()

    def OnDelPerpetratorButton(self, event):
        status.involActual = self.listBoxPerpetradores.GetClientData(self.listBoxPerpetradores.Selection)
        if Borrar(self, u"\xbfBorrar este perpetrador?"):
            status.actoActual.RolPerpetradores.remove(status.involActual)
            session.delete(status.involActual)
            FlushInfo(id=124)
            session.refresh(status.actoActual)
            status.involActual = None
            LimpiaCampos(self, camposEntidad['involucramiento'])
            LlenaPerpetradores(self, self.listBoxPerpetradores)
            


    def OnDelIntervButton(self, event):
        IntervBorrar = MyClientData(self.listBoxIntervenciones)
        if Borrar(self, u"\xbfBorrar esta intervenci\xf3n?"):
            session.delete(IntervBorrar)
            status.casoActual.intervenciones.remove(IntervBorrar)
            status.intervencionActual = None
            FlushInfo(id=118)
            LimpiaCamposIntervencion(self)
            LlenaIntervenciones(self)
        event.Skip()

    def OnDelFuentePerButton(self, event):
        FuenteBorrar = MyClientData(self.listBoxFte)
        if Borrar(self, u"\xbfBorrar esta fuente personal?"):
            session.delete(FuenteBorrar)
            status.casoActual.fuentes.remove(FuenteBorrar)
            status.fuenteActual = None
            FlushInfo(id=119)
            LimpiaCamposFuente(self)
            LlenaCtrlFuentes(self)
        event.Skip()

    def OnBtnAddDocButton(self, event):
        SaveDataPub(self)
        status.pubActual = None
        LimpiaCamposPub(self)
        descrip = MyDescrip(self, titulo=u'Identificaci\xf3n', long=120, help=u'MyDescripDoc')
        if descrip:
           status.pubActual = Publicacion(status.casoActual, descrip)
           status.pubActual.PIdioma = getDefault('T14')
           session.add(status.pubActual)
           
           FlushInfo(id=126)
           LlenaCtrlPubs(self)
           
           LoadDataPub(self)
        


    def OnDelFuenteDocButton(self, event):
            ObjBorrar = MyClientData(self.listBoxDocs)
            
            if Borrar(self,u"\xbfBorrar esta fuente documental?"):
                session.delete(ObjBorrar)
                status.casoActual.PPublicaciones.remove(ObjBorrar)
                status.pubActual = None
                FlushInfo(id=137)
                LimpiaCamposPub(self)
                LlenaCtrlPubs(self)        


    def OnDelIdiomaButton(self, event):
        ctrl = self.FPIdioma
        t = MyClientData(ctrl)
        if Borrar(self, u"\xbfBorrar este idioma?"):
            session.delete(t)
            status.personaActual.PIdiomas.remove(t)
            FlushInfo(id=129)
            LlenaCtrlPersonaTipificacion(ctrl, status.personaActual.PIdiomas)
        event.Skip()

    def OnDelLenguaButton(self, event):
        ctrl= self.FPLengua
        t = MyClientData(ctrl)
        if Borrar(self, u"\xbfBorrar esta lengua?"):
            session.delete(t)
            status.personaActual.PLenguas.remove(t)
            FlushInfo(id=130)
            LlenaCtrlPersonaTipificacion(ctrl, status.personaActual.PLenguas)    
        event.Skip()

    def OnDelOrigenButton(self, event):
        ctrl = self.FPOrigenEtnico
        t = MyClientData(ctrl)
        if Borrar(self, u"\xbfBorrar este origen \xe9tnico?"):
            session.delete(t)
            status.personaActual.POrigenEtnico.remove(t)
            FlushInfo(id=131)
            LlenaCtrlPersonaTipificacion(ctrl, status.personaActual.POrigenEtnico)
        event.Skip()

    def OnDelDireccionButton(self, event):
        D = MyClientData(self.FPDirecciones)
        if D:
            if Borrar(self, u"\xbfBorrar esta direcci\xf3n?"):
                self.FPDirecciones
                
                session.delete(D)
                status.personaActual.PDirecciones.remove(D)
                FlushInfo(id=133)
                LlenaDireccionesPersona(self)
        else:
            MError(self, u"A\xfan no hay una direcci\xf3n seleccionada")
        event.Skip()

    def OnDelDatoBioButton(self, event):
        v = self.listBoxVinculos.GetClientData(self.listBoxVinculos.Selection)
        p1 = v.vinculo1
        p2 = v.vinculo2
        
        if Borrar(self, u"\xbfBorrar este dato biogr\xe1fico?"):
            session.delete(v)
            print "p1, laotra2 ",p1, p1.LaOtra2
            
            p1.LaOtra2.remove(v)
            if v in p1.Pdetallesyvinculosbiograficos:
                p1.Pdetallesyvinculosbiograficos.remove(v)
            if v in p1.Pdetallesbiograficos:
                p1.Pdetallesbiograficos.remove(v)
            print "p1, laotra2 ",p1, p1.LaOtra2
            print "p1.Pdetallesbiograficos ",p1.Pdetallesbiograficos
            print "p1.Pdetallesyvinculosbiograficos ",p1.Pdetallesyvinculosbiograficos
            
            if p2:
                print "p2, laotra1 ", p2, p2.LaOtra1
                print "p2.Pdetallesbiograficos ",p2.Pdetallesbiograficos
                print "p2.Pdetallesyvinculosbiograficos ",p2.Pdetallesyvinculosbiograficos
                p2.LaOtra1.remove(v)
                if v in p2.Pdetallesbiograficos:
                    p2.Pdetallesbiograficos.remove(v)
                if v in p2.Pdetallesyvinculosbiograficos:
                    p2.Pdetallesyvinculosbiograficos.remove(v)
                
            FlushInfo(id=121)
            print 'session.dirty [121] ', session.dirty
            status.vinculoActual = None

            LlenaCtrlVinculos(self, self.listBoxVinculos, status.personaActual)


    def OnDelDerechoButton(self, event):
            Aborrar = True
        
            tipificacion = MyClientData(self.listBoxDerechosafectados)
            name = '^'+tipificacion.tipificacion.name
            Pattern = re.compile(name)
            for i in status.casoActual.actos:
                if Aborrar and Pattern.match(i.PTipodeacto.name):
                        MError(self, u"Este derecho no puede ser borrado, ya que tiene actos relacionados")
                        Aborrar = False
            if Aborrar and Borrar(self, u"\xbfBorrar este dato?"):            
                DelTipificacion(tipificacion)
                LlenaCtrlTipificacion(self.listBoxDerechosafectados,153, status.casoActual)
        

    def OnDelTemaButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):            
                #tipificacion = self.listBoxTemas.GetClientData(self.listBoxTemas.Selection)
                tipificacion= MyClientData(self.listBoxTemas)
                DelTipificacion(tipificacion)
                LlenaCtrlTipificacion(self.listBoxTemas,154, status.casoActual)
        event.Skip()

    def OnDelRelacionButton(self, event):
        #rel = MyClientData(self.listBoxCasoRel)
        rel = status.casoRelActual
        if rel:
            if Borrar(self, u'\xbfBorrar esta relaci\xf3n?'):
                    
                    session.delete(rel)
                    if rel in status.casoActual.PelCaso2:
                        status.casoActual.PelCaso2.remove(rel)
                    if rel in status.casoActual.PelCaso1:
                        status.casoActual.PelCaso1.remove(rel)
                    status.casoRelActual = None
    
                    LlenaCtrlCasoRel(self)
                    LimpiaCampos(self, camposEntidad['casoRel'])
        else:
            MError(self, u"A\xfan no hay una relaci\xf3n seleccionada")    
        event.Skip()

    def OnListBoxTemasListbox(self, event):
        self.delTema.Enable(status.canEditCaso)
        event.Skip()

    def OnDelPersonaButton(self, event):
        P = MyClientData(self.listBoxPersonaBrowser)
        n = self.listBoxPersonaBrowser.Selection
        
        if P:
            d= P.Roles()
            Razones = ', '.join([i for i in d.keys() if d[i]])
            DetallesBio = P.LaOtra1 + P.LaOtra2
            relacionConC3 = []
            if P.clavestatus == 3:
               relacionConC3 = session.query(Persona).filter(Persona.clavestatus == 2).filter(Persona.personarelacionadac3 == P.id).all()
            if Razones:
                MError(self, 'Esta persona no puede ser borrada ya que figura como '+Razones)
            elif DetallesBio:
                MError(self, 'Esta persona no puede ser borrada ya que tiene datos biogr\xe1ficos')
            else:    
                if Borrar(self, u"\xbfBorrar esta persona?"):
                
                    try:
                         
                         session.delete(P)
                         FlushInfo(id=135)
                         if relacionConC3:
                             for miPersona in relacionConC3:
                                 miPersona.personarelacionadac3 = None
                                 miPersona.clavestatusc3 = None
                                 session.add(miPersona)
                             session.flush()
                         
                         
                         self.listBoxPersonaBrowser.Delete(n)
                         limpiaCamposPersona(self)
                         status.personaActual = None
                         status.totalPersona = NoRegistros(Persona)
                         self.txtTotalPersonas.SetLabel("%i personas registradas"%(status.totalPersona))
                         Enable_panel(self, 'Personas 1', enable=False)
                         Enable_panel(self, 'Personas 2', enable=False)
                         Enable_panel(self, 'Personas 3', enable=False)
                         Enable_panel(self, 'Personas 4', enable=False)
                         setLabelStaticPersonaActual(self, '')
                         
                    except:
                         MError(self, 'Esta persona no pudo ser dada de baja')
                         print "Unexpected error:", sys.exc_info()
        else:
            MError(self, u"A\xfan no hay una persona seleccionada")    

    def OnFAlegislacion_nacional_notasKillFocus(self, event):
        SaveDataLegis(self)
        event.Skip()

    def OnFAinstrumentos_internacionales_notasKillFocus(self, event):
        SaveDataInstr(self)
        event.Skip()

    def OnButton5Button(self, event):
        event.Skip()

    def OnBtnAddDocLenguaIndigenaButton(self, event):
        T = getTaxonomyTree(self, u"T66", u"Lengua ind\xedgena", help=u'getTaxonomyTreeDocLengua')
        if T:
            status.pubActual.PLengua_indigena = T
            self.staticDocLenguaIndigena.SetLabel(T.descripcion)
        event.Skip()

    def OnBtnDelDocLenguaIndigenaButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.pubActual.PLengua_indigena = None
            self.staticDocLenguaIndigena.SetLabel('')
        event.Skip()

    def OnBtnAddFteLenguaIndigenaButton(self, event):
        T = getTaxonomyTree(self, u"T66", u"Lengua ind\xedgena",help=u'getTaxTreeFteLengua')
        if T:
            status.fuenteActual.PLengua_indigena = T
            self.staticFteLenguaIndigena.SetLabel(T.descripcion)

        event.Skip()

    def OnBtnDelFteLenguaIndigenaButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.fuenteActual.PLengua_indigena = None
            self.staticFteLenguaIndigena.SetLabel('')
        
        event.Skip()

    def OnBtnAddFteConfiabilidadButton(self, event):
        T = getTaxonomyTree(self, u"T42", u"Confiabilidad",help=u'getTaxFteConfiabilidad')
        if T:
            status.fuenteActual.PConfiabilidad = T
            self.staticFteConfiabilidad.SetLabel(T.descripcion)
        
        event.Skip()

    def OnBtnDelFteConfiabilidadButton(self, event):
        
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.fuenteActual.PConfiabilidad = None
            self.staticFteConfiabilidad.SetLabel('')
        event.Skip()

    def OnBtnAddPubConfiabilidadButton(self, event):
        T = getTaxonomyTree(self, u"T42", u"Confiabilidad", help=u'getTaxPubConfiabilidad')
        if T:
            status.pubActual.PConfiabilidad = T
            self.staticPubConfiabilidad.SetLabel(T.descripcion)
        event.Skip()

    def OnBtnDelPubConfiabilidadButton(self, event):
        
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.pubActual.PConfiabilidad = None
            self.staticPubConfiabilidad.SetLabel('')
        event.Skip()

    def OnBtnDelFPTipoButton(self, event):
        if Borrar(self, u"\xbfBorrar este dato?"):
            status.personaActual.Ptipo = None
            self.staticFPTipo.SetLabel('')

        event.Skip()

    def OnBtnAddFPTipoButton(self, event):
        T = getTaxonomyTree(self, u"T07", u"Tipo de persona colectiva", help=u'getTaxTipoPersonaCol')
        if T:
            status.personaActual.Ptipo = T
            self.staticFPTipo.SetLabel(T.descripcion)
        event.Skip()

    def OnBtnInfoCasoRelButton(self, event):
        DlgInfo(self, status.casoRelActual)
        event.Skip()



    def OnBtnInfoInterButton(self, event):
        DlgInfo(self, status.instrActual)
        event.Skip()

    def OnBtnInfoLegisButton(self, event):
        DlgInfo(self, status.legisActual)
        event.Skip()

    def OnBtnInfoBioButton(self, event):
        DlgInfo(self, status.vinculoActual)
        event.Skip()

    def OnCFIdiaSetFocus(self, event):
        c = event.GetEventObject()
        status.vfecha = c.GetValue()
        #c.SetValue('')
        c.SetValue(None)
        
        
        event.Skip()

    def OnButtonNuevoActoButton(self, event):
        if not status.casoActual.derechosafectados:
            MError(self, "Este caso no tiene derechos afectados asignados. No es posible agregar actos.")
            return
        patron = derechosafectadosPattern(status.casoActual, u'T04')
        
        P, T = NuevoActo(self, patron)
        #TipoActo = getTaxonomyTree(self,'T04',"Tipo de acto",Pattern=derechosafectadosPattern(status.casoActual, 'T04'))
        if T and P:
           status.actoActual = Acto(P, T, caso_id=status.casoActual.id)
           #status.actoActual.PTipodeacto = TipoActo
           
           
           status.casoActual.actos.append(status.actoActual)
           
           
           session.add(status.actoActual)
           
           FlushInfo(id=105)
           session.refresh(status.actoActual)
           
           status.nuevoacto = True
           LoadDataActo(self)
           if status.casoActual:
                 LlenaActos(self)
           panels['Involucramientos'].Enable()
           Enable_panel(self, 'Involucramientos', enable=False)
           self.listBoxActoPerpetradores.Clear()
           self.listBoxPerpetradores.Clear()
           self.statixText50.SetLabel('')
           
        event.Skip()

    def OnCFIdiaKillFocus(self, event):
        c = event.GetEventObject()
        if c.GetValue()=='' or c.GetValue()==None:
            c.SetValue(status.vfecha)
        
        event.Skip()

    def OnBtnBusquedaExhausticaPersonaButton(self, event):
        if not status.filtroPersona:
            status.filtroPersona = QueryPersona(self)
            
        status.filtroPersona.edit()
        event.Skip()

    def OnBtnBuscarPersonaButton(self, event):
        if status.filtroPersona:
            R=status.filtroPersona.execute()
            #print "R ",R
            
            # si hay algun filtro por tipo de persona, lo aplicamos...
            filtro = status.tipoPersona
            if filtro == 'Individual':
                R = R.filter(Persona.esindividual == 1)
                
            if filtro == 'Colectiva':
                R = R.filter(Persona.esindividual == 0)
                
            # si hay filtro por grupo, lo aplicamos
            if status.filtroGrupo:
                R = R.filter(Persona.clavegrupo == status.filtroGrupo)
            
            # si hay filtro por contenedor, lo aplicamos
            if status.filtroContenedor:
                R = R.filter(Persona.clavestatus == status.filtroContenedor)
            
                
            # finalmente obtenemos la lista de personas a mostrar    
                
            status.personasSeleccionadas=R.all()
            
            status.personasIdseleccionadas = [i.id for i in status.personasSeleccionadas] 
            
            totalSeleccionados=LlenaPersonas(self.listBoxPersonaBrowser, dataset=status.personasSeleccionadas)
            
            setPersonasSeleccionadas(self, totalSeleccionados)
            status.applySearchPersona=True
        
        event.Skip()

    def OnBtnMostarTodasPersonasButton(self, event):
        n = self.listBoxPersonaBrowser.GetStringSelection()
        s= status.tipoPersona
        self.srchPersona.Clear()
        #t=LlenaPersonas(self.listBoxPersonaBrowser, filtro=s)
        t=LlenaPersonas(self.listBoxPersonaBrowser)
        self.txtTotalPersonas.SetLabel("%i personas registradas"%t)
        
        self.listBoxPersonaBrowser.SetStringSelection(n)
        self.listBoxPersonaBrowser.SetFocus()
        setPersonasSeleccionadas(self, None)
        status.applySearchPersona=False
        event.Skip()

    def OnChoiceGrupoChoice(self, event):
        cambiaGrupo(self, event)
        
        

            
        event.Skip()

    def OnChoiceContenedorChoice(self, event):
        
        cambiaContenedor(self, event)
        
        
        event.Skip()

    def OnChoiceContenedorPChoice(self, event):
        cambiaContenedor(self, event)
        
        event.Skip()

    def OnChoiceGrupoPChoice(self, event):
        cambiaGrupo(self, event)
        
        
        event.Skip()

    def OnChkRelevanteCheckbox(self, event):
        if self.chkRelevante.GetValue():
            status.casoActual.clavestatusc3 = 1
        else:
            status.casoActual.clavestatusc3 = 0
        session.add(status.casoActual)
        session.flush()
        module2.updateStatusC3(self, status.casoActual)
        
        
        event.Skip()

    def OnBtnCopiarC3PButton(self, event):
        P=status.personaActual
        #import moduleClonPersona
        #moduleClonPersona.clonaPersona(self, P)
        if P:
            idRel = P.personarelacionadac3
            id = module2.adaptaId(P.id, 3)
            if False: #idRel: ojo
                if idRel == id:
                    MError(self, "La persona ya esta presente en el contenedor 3")
                else:
                    MError(self, "La persona esta relacionada con la persona "+module2.personaDescriptor(idRel)+" en el contenedor 3")
            else:
                import FrameClonPersonas2
                FrameClonPersonas2.frameClonPersona(self, P)
        else:
            MError(self, u"A\xfan no hay una persona seleccionada para copiar al contenedor 3")


    def OnBtnCopiarC3Button(self, event):
        if status.casoActual:
            idRel = status.casoActual.casorelacionadoc3
            id = module2.adaptaId(status.casoActual.id, 3)
            if False: #idRel: ojo
                if idRel == id:
                    MError(self, "El caso ya esta presente en el contenedor 3")
                else:
                    MError(self, "El caso esta relacionado con el caso "+module2.casoDescriptor(idRel)+" en el contenedor 3")
            else:
                import FrameClonPersonas
                FrameClonPersonas.frameClonCaso(self, status.casoActual, nombreDelCaso=status.nombreCasoActual)
        else:
            MError(self, u"A\xfan no hay un caso seleccionado para pasar al contenedor 3")
            

    def OnFRCCasoRelComentariosTextEnter(self, event):
        cuentaEspacios(self.longComRelCasos, event)
        event.Skip()

    def OnFRCCasoRelObservacionesTextEnter(self, event):
        cuentaEspacios(self.longObsRelCasos, event)
        event.Skip()

    def OnFRCCasoRelObservacionesText(self, event):
        cuentaEspacios(self.longObsRelCasos, event)
        event.Skip()

    def OnFRCCasoRelComentariosText(self, event):
        cuentaEspacios(self.longComRelCasos, event)
        event.Skip()

    def OnFAExportarCheckbox(self, event):
        event.Skip()

    def OnMP1Checkbox(self, event):
        ctrl = event.GetEventObject()
        
        #quitar palomas y asignar la que se haya hecho clic
        for ctrlName in ['MP1','MP2','MP3','MP4']:
            c = getattr(self, ctrlName)
            c.SetValue(False)
        ctrl.SetValue(True)
        
        status.tipoPersona = ctrl.GetLabel()
        t=LlenaPersonas(self.listBoxPersonaBrowser, filtro=status.tipoPersona)
        
        # poner el letrero con la cantidad de personas seleccionadas
        setPersonasSeleccionadas(self, t)
        
        
        event.Skip()

    def OnFRCCasoRelComentariosKillFocus(self, event):
        SaveDataCasoRel(self)
        event.Skip()

    def OnFRCCasoRelObservacionesKillFocus(self, event):
        SaveDataCasoRel(self)
        event.Skip()

    def OnFAinstrumentos_int_notasText(self, event):
        cuentaEspacios(self.txtLongNorIns, event)
        event.Skip()

    def OnFAlegislacion_nacional_notasText(self, event):
        cuentaEspacios(self.txtLongNorLeg, event)
        event.Skip()

    def OnPantAnteriorButton(self, event):
        "regresar de la pantalla de casos a personas"
        self.pantAnterior.Show(False)
        self.NBMain.SetSelection(4)
        LlenaRoles(self.listPersonaVinculosDB, status.personaActual)
        
        event.Skip()

    def OnBtnCambiaTipoPersonaButton(self, event):
        if status.personaActual.esindividual:
            tipoGrupo = getTaxonomyTree(self, u"T07", u"Tipo de persona colectiva", help=u'getTaxTipoPersonaCol')
            if tipoGrupo:
                status.personaActual.esindividual = 0
                status.personaActual.Ptipo = tipoGrupo
        else:
            status.personaActual.esindividual = 1
                
        SaveDataPersona(self)
        LoadDataPersona(self)
        setItemString(self.listBoxPersonaBrowser, status.personaActual.Descriptor())
        
        event.Skip()

    def OnTextCtrlINObservacionesKillFocus(self, event):
        status.involActual.observaciones = self.textCtrlINObservaciones.GetValue()
        event.Skip()

    def OnChkRelevantePCheckbox(self, event):
        if self.chkRelevanteP.GetValue():
            status.personaActual.clavestatusc3 = 1
        else:
            status.personaActual.clavestatusc3 = 0
        session.add(status.personaActual)
        session.flush()
        module2.updateStatusC3(self, status.personaActual)
        
        event.Skip()

    def OnCheckBoxCasoConfidencialidadCheckbox(self, event):
        checaRO(self, event, status.canEditCaso)
        event.Skip()

    def OnCheckBoxFteConfidencialidadCheckbox(self, event):
        checaRO(self, event, status.canEditCaso)
        event.Skip()

    def OnCheckBoxCasoExportarRelacionesCheckbox(self, event):
        checaRO(self, event, status.canEditCaso)
        event.Skip()

    def OnCheckBoxIntExportarCheckbox(self, event):
        checaRO(self, event, status.canEditCaso)
        event.Skip()

    def OnCheckBoxPubExportarCheckbox(self, event):
        checaRO(self, event, status.canEditCaso)
        event.Skip()

    def OnFPHablayentiendeespanolCheckbox(self, event):
        checaRO(self, event, status.canEditPersona)
        event.Skip()

    def OnFPconfidencialidadCheckbox(self, event):
        checaRO(self, event, status.canEditPersona)
        event.Skip()

    def OnListBoxDerechosafectadosListbox(self, event):
        self.delDerecho.Enable(status.canEditCaso)
        event.Skip()

    def OnFPNombreKillFocus(self, event):
        e_obj = event.GetEventObject()
        st = LimpiaString(e_obj.GetValue())
        e_obj.SetValue(st)
        event.Skip()

    def OnFPApellidoKillFocus(self, event):
        self.OnFPNombreKillFocus(event)
        

    def OnFPOtroNombreKillFocus(self, event):
        self.OnFPNombreKillFocus(event)

    def OnFrame2Paint(self, event):
        #self.Restore()
        event.Skip()
        


def checaRO(self, evt, miStatus):
    if not miStatus:  # esta en readOnly
        e_obj = evt.GetEventObject()
        e_obj.SetValue(not e_obj.GetValue())
        ErrorSoloLectura(self)
        
def clearFiltroPersona(self):
    for ctrlName in ['MP1','MP2','MP3']:
            c = getattr(self, ctrlName)
            c.SetValue(False)
    self.MP4.SetValue(True)
    status.tipoPersona = "Todas"
    
def cambiaGrupo(self, event):
    ctrl = event.GetEventObject()
    v = ctrl.GetSelection()
    # cambia controles
    self.choiceGrupo.SetSelection(v)
    self.choiceGrupoP.SetSelection(v)
    
    
    obj = MyClientData(event)
    if obj:
        status.filtroGrupo = obj.id
        print status.filtroGrupo
        
    else:
        status.filtroGrupo = None
    
    # casos
    self.CasoIsearch.ChangeValue('')
    n=LlenaCtrlCasos(self.listaCasos)
    status.TotalCasos = n
    self.txtTotalCasos.SetLabel("%i casos registrados"%(status.TotalCasos))
    self.txtCasosSeleccionados.SetLabel('')
    LimpiaTodosLosCamposCaso(self)
    
    # personas
    t=LlenaPersonas(self.listBoxPersonaBrowser)
    self.txtTotalPersonas.SetLabel("%i personas registradas"%t)
    status.totalPersonas = t
    setPersonasSeleccionadas(self, None)
    
def setItemString(listCtrl, expr):
    "reasigna la etiqueda de un item en un control de lista"
    n = listCtrl.GetSelection()
    listCtrl.SetString(n, expr)        
def cambiaContenedor(self, event):
    ctrl = event.GetEventObject()
    v = ctrl.GetSelection()

    if v:
        status.filtroContenedor = int(v)
        
    else:
        status.filtroContenedor = None
        
    self.choiceContenedorP.SetSelection(v)
    self.choiceContenedor.SetSelection(v)
    
    # boton de copiar
    self.btnCopiarC3P.Enable(status.filtroContenedor == 2)
    self.btnCopiarC3.Enable(status.filtroContenedor == 2)
    
    
    #casos
    self.CasoIsearch.ChangeValue('')
    n=LlenaCtrlCasos(self.listaCasos)
    status.TotalCasos = n
    self.txtTotalCasos.SetLabel("%i casos registrados"%(status.TotalCasos))
    self.txtCasosSeleccionados.SetLabel('')
    LimpiaTodosLosCamposCaso(self)
    
          
    # personas
    t=LlenaPersonas(self.listBoxPersonaBrowser)
    self.txtTotalPersonas.SetLabel("%i personas registradas"%t)
    status.totalPersonas = t
    setPersonasSeleccionadas(self, None)
    
    muestraControlesRelevancia(self, status.filtroContenedor == 2)
      

def DialogTipifica(parent,Tesauro, Campo, acto_id=None, desc='',help=u''):
        Tipo = getTaxonomyTree(parent, Tesauro, desc, help=help)
        
        if Tipo:
          lista = [(i.tipificacion, i.acto_id) for i in status.casoActual.tipificaciones]
          if (Tipo, acto_id) in lista:
                MError(None, u'Ya existe esta tipificaci\xf3n en el caso')
                return False
          else:
              tipificacion=EventoTipificacion(status.casoActual.id, Tipo.id, Campo, Tipo, acto_id=acto_id)
              if Campo == 2154:
                  status.legisActual = tipificacion 
              if Campo == 2155:
                  status.instrActual = tipificacion     
              status.casoActual.tipificaciones.append(tipificacion)
              status.casoActual.derechosafectados.append(tipificacion)
              FlushInfo()
              
              return True
        else:
            return False  
              
              
    
              
def DelTipificacion(tipificacion):
    if tipificacion:
        status.casoActual.tipificaciones.remove(tipificacion)
        if tipificacion.codigo == 153:
            try:
                status.casoActual.derechosafectados.remove(tipificacion)
                status.casoActual.derechosafectadosL.remove(tipificacion)
            except:
                module2.nada()
        session.delete(tipificacion)
        
        FlushInfo(id=143)


def LlenaCtrlPersonas(self, filtro='Todas', filtro2=''):        
    
    #no se usa....
        if filtro == 'Todas': 
            ListaPersonas = session.query(Persona)
        else:
            if filtro == 'Individual':
                ListaPersonas = session.query(Persona).filter_by(esindividual = 1)
            else:
                ListaPersonas = session.query(Persona).filter_by(esindividual = 0)


        LlenaCtrl3(self.listBoxPersonaBrowser, [(i,i.Descriptor()) for i in ListaPersonas])

def saveDataCaso(self):
     c = status.casoActual
    
     if c:
         descrip = self.textDescripcion.GetValue()
         descrip = descrip.strip()
         if c.descripcion != descrip:
             if ExisteCaso(descrip, casoActual=c):
                 MError(self, u"Ya existe otro caso con esta descripci\xf3n")
                 return
         
         if not descrip:
             MError(self, u"No es posible guardar un caso sin nombre")
             self.textDescripcion.SetValue(c.descripcion)
         else:
             c.descripcion = descrip
         c.Ptipo_fecha_inicio = getChoiceValue(self.choiceTipoFechaInicial)
         c.Ptipo_fecha_final = getChoiceValue(self.choiceTipoFechaFinal)
         c.Ptipo_frecepcion  = getChoiceValue(self.FCtipo_frecepcion)
         c.Pmonitoreo = getChoiceValue(self.choiceMonitoreo)
         c.no_persona_afectadas = self.textCtrlNoPersonasAfectadas.GetValue()
         
         if validDate(self.CasoFechaInicial, err=u"inicial del caso"):
            c.fecha_inicio = setDateField2(self.CasoFechaInicial)
         
         
         if validDate(self.CasoFechaFinal, err=u"final del caso"):
            c.fecha_final = setDateField2(self.CasoFechaFinal)
            
         if not moduleFechas.ctrlFechasValidas(self.CasoFechaInicial, c.Ptipo_fecha_inicio,
                                               self.CasoFechaFinal, c.Ptipo_fecha_final, status):
                    MError(self, "La fecha final del caso no puede ser anterior a la fecha inicial") 
         if not moduleFechas.ctrlFechasValidas(self.CasoFechaInicial, status.casoActual.Ptipo_fecha_inicio,
                                               self.CasoFechaRecepcion, status.casoActual.Ptipo_frecepcion, status):
            
            MError(self, u"La fecha de recepci\xf3n no puede ser anterior a la fecha inicial del caso") 
         
         if validDate(self.CasoFechaRecepcion, err=u"de recepci\xf3n"):
            c.frecepcion = setDateField2(self.CasoFechaRecepcion)
         
         
         c.descripcion_narrativa = self.textCtrlDescripcionNarrativa.GetValue()
         c.resumen_descripcion = self.textCtrlResumen.GetValue()
         c.observaciones = self.textCtrlObservaciones.GetValue()
         c.exportar = getCheckBoxValue(self.checkBoxCasoConfidencialidad)
         c.exportarrelaciones = getCheckBoxValue(self.checkBoxCasoExportarRelaciones)
         c.archivos = self.textCtrlCAArchivos.GetValue()
         c.comentarios = self.textCtrlCAComentarios.GetValue()
         c.proyecto_grupo = self.FCproyecto_grupo.GetValue()
         c.proyecto_conjunto = self.FCproyecto_conjunto.GetValue()
         c.proyecto_se = self.FCproyecto_se.GetValue()
         #session.add(c)
         session.add(c)
         FlushInfo(id=145)
         
         
def CtrlFechas(self):
    self.CasoFechaInicial=[self.CFIdia, self.CFImes, self.CFIanio]         
    self.CasoFechaFinal=[self.CFFdia, self.CFFmes, self.CFFanio]
    self.CasoFechaRecepcion=[self.CFRdia, self.CFRmes, self.CFRanio]
    self.ActoFechaInicial=[self.AFIdia, self.AFImes, self.AFIanio]     
    self.ActoFechaFinal=[self.AFFdia, self.AFFmes, self.AFFanio]  
    self.FuenDocFecha=  [self.FDFdia, self.FDFmes, self.FDFanio]  
    self.FuenDocFechaConsulta=[self.FDFCdia, self.FDFCmes, self.FDFCanio]
    self.FuenPerFecha=[self.FPFdia, self.FPFmes, self.FPFanio]
    self.InterFecha=[self.IFdia, self.IFmes, self.IFanio]
    self.PerFechaNac=[self.PFNdia, self.PFNmes, self.PFNanio]
    self.PerFechaRec=[self.PFRdia, self.PFRmes, self.PFRanio]
    self.BioFechaInicial=[self.BFIdia, self.BFImes, self.BFIanio]
    self.BioFechaFinal=[self.BFFdia, self.BFFmes, self.BFFanio]
    self.BioFechaVig=[self.BFVdia, self.BFVmes, self.BFVanio]
    ListaCtrlFechas = [self.CasoFechaInicial,
                    self.CasoFechaFinal,
                    self.CasoFechaRecepcion,
                    self.ActoFechaInicial,
                    self.ActoFechaFinal,
                    self.FuenDocFecha,
                    self.FuenDocFechaConsulta,
                    self.FuenPerFecha,
                    self.InterFecha,
                    self.PerFechaNac,
                    self.PerFechaRec,
                    self.BioFechaInicial,
                    self.BioFechaFinal,
                    self.BioFechaVig
                    ]
    for i in ListaCtrlFechas:
        i[0].SetBounds(1,31)
        #i[0].SetLimited(True)
        i[1].SetBounds(1,12)
        #i[1].SetLimited(True)
        i[2].SetMax(2050)
        i[2].SetMin(1)
        #i[2].SetLimited(True)
        
        for ctrl in i:
            ctrl.SetLimited(False)
            ctrl.SetNoneAllowed(True)
            ctrl.Bind(wx.EVT_SET_FOCUS, self.OnCFIdiaSetFocus)
            ctrl.Bind(wx.EVT_KILL_FOCUS, self.OnCFIdiaKillFocus)
            ctrl.Bind(wx.lib.intctrl.EVT_INT, self.OnIntCtrlXInt)
    
def LoadDataCasoRel(self):
    cr = status.casoRelActual
    s = self
    s.FRCCasoRelObservaciones.SetValue('')
    s.FRCCasoRelComentarios.SetValue('')
    s.FRCCasoRel.SetLabel('')
    if cr:
        try:
            s.FRCCasoRelObservaciones.SetValue(Mvs(cr.observaciones))
            s.FRCCasoRelComentarios.SetValue(Mvs(cr.comentarios))
            if cr.reciproco:
                if cr.Ptipo:
                    s.FRCCasoRelTipo.SetLabel(terminoReciproco(status.reciprocoRelacionCasos, cr.Ptipo.name, cr.Ptipo.descripcion))
                if cr.Pcaso_1:
                    s.FRCCasoRel.SetLabel(cr.Pcaso_1.descripcion)
            else:
                if cr.Ptipo:
                    s.FRCCasoRelTipo.SetLabel(cr.Ptipo.descripcion )
                    
                if cr.Pcaso_2:
                    s.FRCCasoRel.SetLabel(cr.Pcaso_2.descripcion)
            self.FRCCasoRelObservaciones.Enable(CanEdit(status.casoActual))
            self.FRCCasoRelComentarios.Enable(CanEdit(status.casoActual))
        except:
            MError(self, "No se pudo cargar el caso relacionado")
            status.casoRelActual = None
            
def SaveDataCasoRel(self):
    cr = status.casoRelActual
    s=self
    
    if cr:
        cr.observaciones = s.FRCCasoRelObservaciones.GetValue()
        cr.comentarios = s.FRCCasoRelComentarios.GetValue()
        session.add(cr)
        FlushInfo(id=146)
    
def LimpiaCamposCaso(self):
    s=self
    if u'T04' in status.dlg.keys():
        status.dlg.pop(u'T04')
        

    LimpiaCampos(self, camposEntidad['caso'])
    LimpiaCamposActo(self)
    status.casoRelActual=None
       
def LoadDataCaso(self):
#self.NBMain.EnableTab(1, False)
    
    status.legisActual = None
    status.instrActual = None
    try:
        session.refresh(status.casoActual)
    except:
        MError(self, u"Existen problemas de conexi\xf3n con el servidor")
        return
    c = status.casoActual
    if c:
        try:
            status.AlertaGrabarDatos=False
        
            status.casoActual=c
            
            s=self
            LimpiaCamposCaso(self)
            
            
            Edo = None
            RO = ''
            if not CanEdit(status.casoActual):
                RO = '(solo lectura) '

            self.textDescripcion.SetValue(status.casoActual.descripcion)
            tmp = status.casoActual.descripcion
            status.baseCentral = status.casoActual.clavegrupo != None
            if status.baseCentral:
                expresion = "Caso: ["+RO+str(status.casoActual.id)[:-4]+"/"+str(status.casoActual.clavegrupo)+"/"+str(status.casoActual.clavestatus)+"] "+status.casoActual.descripcion
            else:
                expresion = "Caso: ["+RO+str(status.casoActual.id)+"] "+status.casoActual.descripcion
            expresion = expresion[:120]
            status.nombreCasoActual = expresion
            print 1.1
            if c:
                LlenaCtrlCasoRel(self)

                t = QueryTesNode
                
                status.actoActual=None
                status.intervencionActual=None
                status.fuenteActual=None
                status.involActual=None
                
                status.pubActual=None
                
                
                
                LoadDataActo(self)

                LoadDataIntervencion(self)

                loadDataFuente(self)

                LoadDataPub(self)

                
            
                
                if c.Ptipo_fecha_inicio: CtrlSelect(self.choiceTipoFechaInicial,c.Ptipo_fecha_inicio.descripcion)
                else: CtrlSelect(self.choiceTipoFechaInicial,u'')
                if c.Ptipo_fecha_final: CtrlSelect(self.choiceTipoFechaFinal,c.Ptipo_fecha_final.descripcion) 
                else: CtrlSelect(self.choiceTipoFechaFinal,u'')
                
                if c.Ptipo_frecepcion: CtrlSelect(self.FCtipo_frecepcion,c.Ptipo_frecepcion.descripcion) 
                else: CtrlSelect(self.FCtipo_frecepcion,u'')
             
                if c.monitoreo: self.choiceMonitoreo.SetStringSelection(c.Pmonitoreo.descripcion)

                self.textCtrlNoPersonasAfectadas.SetValue(Mvs(c.no_persona_afectadas))

                if c.fecha_inicio: 
                    
                    setDateCtrl2(self.CasoFechaInicial, c.fecha_inicio, c.Ptipo_fecha_inicio)

                if c.fecha_final:  
                    
                    setDateCtrl2(self.CasoFechaFinal, c.fecha_final, c.Ptipo_fecha_final)

                if c.frecepcion:
                    setDateCtrl2(self.CasoFechaRecepcion, c.frecepcion, c.Ptipo_frecepcion)

                if c.descripcion_narrativa: self.textCtrlDescripcionNarrativa.SetValue(c.descripcion_narrativa)
                if c.resumen_descripcion: self.textCtrlResumen.SetValue(c.resumen_descripcion)
                if c.observaciones: self.textCtrlObservaciones.SetValue(c.observaciones)

                if c.exportar: self.checkBoxCasoConfidencialidad.SetValue(setCheckBoxValue(c.exportar))

                if c.exportarrelaciones: self.checkBoxCasoExportarRelaciones.SetValue(setCheckBoxValue(c.exportarrelaciones))

                if c.comentarios: self.textCtrlCAComentarios.SetValue(c.comentarios)
                if c.archivos: self.textCtrlCAArchivos.SetValue(c.archivos)
                if c.proyecto_grupo: s.FCproyecto_grupo.SetValue(c.proyecto_grupo)
                if c.proyecto_conjunto: s.FCproyecto_conjunto.SetValue(c.proyecto_conjunto)
                if c.proyecto_se: s.FCproyecto_se.SetValue(c.proyecto_se)
                
                LlenaCtrlLocalizacion(self, self.listLocalizacion, status.casoActual, perm=CanEdit(status.casoActual))
                
                
                LlenaCtrlLocalizacion(self, self.FALocalidad, status.casoActual, renglonInicial=True, perm=CanEdit(status.casoActual))
                self.btnLocMasInfo.Show(False)
                panels['Tipificacion'].Enable()
                panels['Inf. Narrativa'].Enable()
                panels['Casos Adm'].Enable()
                panels['Actos'].Enable()
                panels['Intervenciones'].Enable()
                panels['Fuentes'].Enable()
                panels['Documentos'].Enable()
                panels['Involucramientos'].Disable()
                
                
                
                Enable_panel(self, 'Fuentes', enable=False)
                Enable_panel(self, 'Actos', enable=False)
                Enable_panel(self, 'ActosNormatividad', enable=False)
                Enable_panel(self, 'Datos Generales')
                Enable_panel(self, 'Intervenciones', enable=False)
                Enable_panel(self, 'Documentos', enable=False)
                Enable_panel(self, 'Involucramientos', enable=False)
                self.delLocalizacion.Disable()
                self.delTema.Disable()
                self.delDerecho.Disable()
                
                
                
                
                etiquetas = ['LC1','LC2','LC3','LC4','LC5','LC6','LC7','LC9','LC12','LC14','LC15']
                for ctrlName in etiquetas:
                    ctrl = getattr(self, ctrlName)
                    ctrl.SetLabel(expresion)
                    ctrl.Enable()
                
                LlenaCtrlTipificacion(self.listBoxDerechosafectados,153, status.casoActual)
                LlenaCtrlTipificacion(self.listBoxTemas,154, status.casoActual)
                # limpiaCamposPersona(self)
                module2.updateStatusC3(self, status.casoActual)
                clavestatusc3 = status.casoActual.clavestatusc3
                
                self.chkRelevante.Enable(clavestatusc3 < 2)
                self.chkRelevante.SetValue((clavestatusc3 == 1))
                # mucho ojo!
                if status.UserLevel <=5:
                    for ctrlName in moduleCtrls.CtrlsC3Caso:
                        ctrl=getattr(self, ctrlName)
                        ctrl.Show(not status.baseCentral)    
                status.canEditCaso = CanEdit(status.casoActual)
                #setCamposSololectura(self, CanEdit(status.casoActual))
        except:
            MError(self, "No se pudo cargar el caso ("+str(sys.exc_info())+")")
            status.casoActual = None
                

def blanqueaCasoIsearch(self):
    status.applySearch=False
    LlenaCtrlCasos(self.listaCasos)
    self.CasoIsearch.ChangeValue('')
    self.txtTotalCasos.SetLabel("%i casos registrados"%(status.TotalCasos))
    self.txtCasosSeleccionados.SetLabel('')
    status.casosSeleccionados = None
    
def Reciproco(name, dict):
    if name in dict:
        return dict[name]
def LlenaCtrlCasoRel(self):
    try:
        self.FRCCasoRelObservaciones.Enable(False)
        self.FRCCasoRelComentarios.Enable(False)
        #listaDirecta = [(i, i.Pcaso_2.descripcion + ':'+terminoReciproco(status.reciprocoRelacionCasos, i.Ptipo.name, i.Ptipo.descripcion)) for i in status.casoActual.PelCaso2 if i.Ptipo and i.Pcaso_2]
        listaDirecta = [(i, i.Pcaso_2.descripcion ) for i in status.casoActual.PelCaso2 if i.Ptipo and i.Pcaso_2]
        for j in listaDirecta:
            j[0].reciproco=False
        #listaReciproca = [(i, i.Pcaso_1.descripcion + ':'+TesNotNull(i.Ptipo)) for i in status.casoActual.PelCaso1 if i.Ptipo and i.Pcaso_1]    
        listaReciproca = [(i, i.Pcaso_1.descripcion ) for i in status.casoActual.PelCaso1 if i.Ptipo and i.Pcaso_1]
        for j in listaReciproca:
            j[0].reciproco=True
        LlenaCtrl3(self.listBoxCasoRel, listaDirecta, append=None, orden="name")
        
        
        LlenaCtrl3(self.listBoxCasoRel, listaReciproca, append=True, orden="name")
        status.casoRelaciones=set([])
        for c in listaDirecta:
            status.casoRelaciones.add(c[0].Pcaso_2)
        for c in listaReciproca:
            status.casoRelaciones.add(c[0].Pcaso_1)
        #print status.casoRelaciones
        
             
    except:
        print "problemas casos relacionados"
        print "Unexpected error:", sys.exc_info()
        pass        


def LoadDataPersona(self):
    p = status.personaActual
    s=self
    limpiaCamposPersona(self)
    status.personaActual = p
    
    if p:
        try:
            status.AlertaGrabarDatos=False
            status.canEditPersona = CanEditPersona(status.personaActual)
            s.FPApellido.SetValue(Mvs(p.apellido))
            s.FPNombre.SetValue(Mvs(p.nombre))
            s.FPOtroNombre.SetValue(Mvs(p.otro_nombre))
            s.FPproyecto_grupo.SetValue(Mvs(p.proyecto_grupo))
            s.FPproyecto_conjunto.SetValue(Mvs(p.proyecto_conjunto))
            s.FPproyecto_se.SetValue(Mvs(p.proyecto_se))
            s.FPDescripciondelgrupo.SetValue(Mvs(p.descripcion_del_grupo))
            s.FPObservaciones.SetValue(Mvs(p.observaciones))
            s.FPComentarios.SetValue(Mvs(p.comentarios))
            s.FPArchivos.SetValue(Mvs(p.archivos))
            PutDesc(self.staticFPTipo, p.Ptipo)
            
            s.FPLocalidad.SetValue(Mvs(p.localidad_nac_u_origen))
            s.FPHablayentiendeespanol.SetValue(setCheckBoxValue(p.habla_lengua_local))
            
            s.FPNodependientes.SetValue(p.no_dependientes)
            
            s.FPconfidencialidad.SetValue(setCheckBoxValue(p.exportar))
            
            CtrlSelect(s.FPSexo,p.Psexo)
            CtrlSelect(s.FPTipodefecha, p.Ptipodefecha)
            CtrlSelect(s.FPTipodefecharecepcion, p.Ptipo_frecepcion)            
            
            s.FPPais.SetLabel(TesNotNull(p.Ppais_nac_u_origen))
            
            mostrarEdo = False
            if p.Ppais_nac_u_origen:
                mostrarEdo = p.Ppais_nac_u_origen.descripcion == localCountry
            AjustaLocalidadSegunPais(self, mostrarEdo)
            
            CtrlSelect(s.FPEstado, p.Pestado_nac_u_origen)
        #    CtrlSelect(s.FPMunicipio, p.Pmpio_nac_u_origen)
            s.FPCiudadania.SetLabel(TesNotNull(p.Pciudadania_o_sede))
            #CtrlSelect(s.FPCiudadania, p.Pciudadania_o_sede)
            CtrlSelect(s.FPEscolaridad, p.Pescolaridad)
            s.FPstrOcupacion.SetLabel(TesNotNull(p.Pocupacion))
            #CtrlSelect(s.FPOcupacion, p.Pocupacion)
            
            CtrlSelect(s.FPReligion, p.Preligion)
            CtrlSelect(s.FPEstadocivil, p.Pestado_civil)
            
            CtrlSelect(s.FPMonitoreo, p.Pmonitoreo)
            #CtrlSelect(s.FPTipo, p.Ptipo)    
            setDateCtrl2(s.PerFechaNac, p.fecha_nac_o_fund, p.Ptipodefecha)
            setDateCtrl2(s.PerFechaRec, p.frecepcion      , p.Ptipo_frecepcion)
            MpioDesc = ''
            s.FPMunicipio.Clear()
            if p.Pmpio_nac_u_origen:
                MpioDesc = p.Pmpio_nac_u_origen.descripcion
            if p.Pestado_nac_u_origen:
                LlenaCtrlMunicipios(s.FPMunicipio,p.Pestado_nac_u_origen, selected=MpioDesc)   
            LlenaCtrlPersonaTipificacion(self.FPIdioma, status.personaActual.PIdiomas)
            LlenaCtrlPersonaTipificacion(self.FPLengua, status.personaActual.PLenguas)
            LlenaCtrlPersonaTipificacion(self.FPOrigenEtnico, status.personaActual.POrigenEtnico)
            #LlenaCtrlPersonaTipificacion(self.PFCaracs, status.personaActual.PCaracteristicasRelevantes)
            
            CambiaTitulos(self, p.esindividual == 1)
            s1= status.tipoPersona
            if s1=='Personas relacionadas con el caso':
                t=LlenaPersonas(self.listBoxPersonaBrowser, filtro=s)
                setPersonasSeleccionadas(self, t)
            
        
            Enable_panel(self,'Personas 1')
            Enable_panel(self,'Personas 2')
            Enable_panel(self,'Personas 3')
            LlenaCtrlVinculos(self, self.listBoxVinculos, p)
            Enable_panel(self, 'Personas 4', enable=False)
            self.buttonVincular.Enable(status.canEditPersona)
            self.listBoxVinculos.Enable()
            LlenaRoles(self.listPersonaVinculosDB, status.personaActual)
            LlenaDireccionesPersona(self)
            status.baseCentral = status.personaActual.clavegrupo != None
            if status.baseCentral:
                readOnly = '(Solo lectura) ' if not CanEditPersona(status.personaActual) else ''
                desc= readOnly + \
                '['+str(status.personaActual.id)[:-4]+"/"+\
                str(status.personaActual.clavegrupo)+"/"+\
                str(status.personaActual.clavestatus)+\
                '] '+ status.personaActual.Descriptor()
                module2.updateStatusC3(self, status.personaActual)
                
            else:
                readOnly = '' if status.canEditPersona else '(Solo lectura) '
                desc= '['+str(status.personaActual.id)+'] '+ readOnly + status.personaActual.Descriptor()
            setLabelStaticPersonaActual(self, desc)
            
            s.staticPersonaActual3.Enable()
            etiqueta = "Cambiar a colectiva" if p.esindividual else "Cambiar a individual" 
            s.btnCambiaTipoPersona.SetLabel(etiqueta)
            
        except: 
            MError(self, "No fue posible cargar el dato de esta persona("+str(sys.exc_info())+')')
            tb=sys.exc_info()[2]
            traceback.print_tb(tb)

            sys.exc_info()
            status.personaActual = None
            
              
        
def setLabelStaticPersonaActual(self, desc):
    self.staticPersonaActual0.SetLabel(desc)
    self.staticPersonaActual1.SetLabel(desc)
    self.staticPersonaActual2.SetLabel(desc)
    self.staticPersonaActual3.SetLabel(desc)
    
def SaveDataPersona(self):
    p = status.personaActual
    if not CanEditPersona(p):
        return False
    s=self
    if p:
        apellido = s.FPApellido.GetValue()
        if apellido:
            apellido = apellido.strip()
        nombre = s.FPNombre.GetValue() 
        if nombre:
            nombre = nombre.strip()
        if (p.apellido != apellido) and (p.nombre != nombre):
            if ExistePersona(s.FPNombre.GetValue(), s.FPApellido.GetValue(), p.esindividual):
                MError(self, "Ya existe una persona con este nombre")
                return
        
        
        if not apellido:
            MError(self, u"Falta poner el %s a esta persona"%('apellido' if p.esindividual else 'nombre'))
            return
        p.apellido = apellido
        p.nombre = nombre
        p.otro_nombre = s.FPOtroNombre.GetValue() 
        p.otro_nombre = p.otro_nombre.strip()
        p.proyecto_grupo = self.FPproyecto_grupo.GetValue()
        p.proyecto_conjunto = self.FPproyecto_conjunto.GetValue()
        p.proyecto_se = self.FPproyecto_se.GetValue()
        if validDate(s.PerFechaRec, err=u"de recepci\xf3n"):
             p.frecepcion = setDateField2(s.PerFechaRec, err=u"Fecha de recepci\xf3n")
        #else:
        #     MError(self, u"Fecha de recepci\xf3n de persona inv\xe1lida")  
        p.exportar = getCheckBoxValue(s.FPconfidencialidad)
        p.descripcion_del_grupo = s.FPDescripciondelgrupo.GetValue()
        p.observaciones = s.FPObservaciones.GetValue()
        p.comentarios = s.FPComentarios.GetValue()
        p.archivos = s.FPArchivos.GetValue()
        p.localidad_nac_u_origen = s.FPLocalidad.GetValue()
        
        p.no_dependientes = s.FPNodependientes.GetValue()
        
        p.Psexo = getChoiceValue(s.FPSexo)
        p.Ptipodefecha = getChoiceValue(s.FPTipodefecha)
        
        p.Ptipo_frecepcion = getChoiceValue(s.FPTipodefecharecepcion)
        if validDate(s.PerFechaNac, err=u"de nacimiento o fundaci\xf3n"):
             p.fecha_nac_o_fund = setDateField2(s.PerFechaNac) 
        #else:
        #     MError(self, u"Fecha de nacimiento o fundaci\xf3n inv\xe1lida")     
        
        p.Pestado_nac_u_origen = getChoiceValue(s.FPEstado)
        
        p.Pescolaridad = getChoiceValue(s.FPEscolaridad)
        #p.Pocupacion = getChoiceValue(s.FPOcupacion)
        
        p.Preligion = getChoiceValue(s.FPReligion)
        p.Pestado_civil = getChoiceValue(s.FPEstadocivil)
        
        p.Pmonitoreo = getChoiceValue(s.FPMonitoreo)
        #p.Ptipo = getChoiceValue(s.FPTipo)
        p.habla_lengua_local = getCheckBoxValue(s.FPHablayentiendeespanol)
        session.add(p)
        print 'session.dirty [147] ', session.dirty
        FlushInfo(id=147)
    
def LimpiaCamposActo(s):
    s.FATipoacto.SetLabel('')
    s.FATipodelugar.SetLabel('')
    s.FAEstatusvdh.SetLabel('')
    s.FAVictima.SetLabel('')
    s.FAEstatusvictima.SetLabel('')
    s.FALocalidad.SetSelection(-1)
    s.choiceTipoEdad.SetSelection(0)
    s.FATipofechafin.SetSelection(-1)
    s.FATipofechainicio.SetSelection(-1)
    HideCtrlFecha(s.ActoFechaInicial)
    HideCtrlFecha(s.ActoFechaFinal)
    
def LoadDataActo(self):
    status.legisActual = None
    status.instrActual = None
    a=status.actoActual
    s=self
    LimpiaCamposActo(s)
    
    

    if a:
        try:
            
            if status.actoActual.Pvictima:
                s.FAVictima.SetLabel(a.Pvictima.Descriptor(perm= CanEdit(status.casoActual)))
                #s.btnDPersonaVictima.Show(CanEdit(status.casoActual))
                s.delCaracRel.Show( CanEdit(status.casoActual) )
                mostrarIndividual = a.Pvictima.esindividual == 1
                self.staticTextEdadOcurreActo.Show(mostrarIndividual)
                self.choiceTipoEdad.Show(mostrarIndividual)
                self.FAedad_victima.Show(mostrarIndividual)
               
            s.FAConfidencialidad.SetValue(setCheckBoxValue(a.exportar))
            s.FAExportar.SetValue(setCheckBoxValue(a.exportarnormatividad))
            
            s.FAedad_victima.SetValue(MviMask(a.edad_victima))
            if a.edad_victima_tipo:
                s.choiceTipoEdad.SetSelection(a.edad_victima_tipo)
            
            if a.PEstatusvdh: s.FAEstatusvdh.SetLabel(a.PEstatusvdh.descripcion)
            if a.PEstatusvictima: s.FAEstatusvictima.SetLabel(a.PEstatusvictima.descripcion)
            s.FAObservaciones.SetValue(Mvs(a.observaciones))
            LlenaCtrl3(self.FACaracRelevante, [(i,i.Pcaracteristicarelevante.descripcion) for i in a.PCaracRelevantes])
            
            if a.PTipodeacto: s.FATipoacto.SetLabel(a.PTipodeacto.descripcion )
            if a.PTipodelugar: s.FATipodelugar.SetLabel(a.PTipodelugar.descripcion )
            
            if a.fechainicio: setDateCtrl2(s.ActoFechaInicial, a.fechainicio, a.PTipodefechainicio)
            if a.fechafin: setDateCtrl2(s.ActoFechaFinal, a.fechafin, a.PTipodefechafin)
            CtrlSelect(s.FATipofechainicio,a.PTipodefechainicio)
            CtrlSelect(s.FATipofechafin,a.PTipodefechafin)
            if a.PLocalidad: CtrlSelect(s.FALocalidad, a.PLocalidad.Descriptor())
            
           
            
            ActivaCtrlFecha2(a.PTipodefechainicio, self.ActoFechaInicial)    
            ActivaCtrlFecha2(a.PTipodefechafin, self.ActoFechaFinal)    
        
            Enable_panel(self, 'Involucramientos', enable=False)
            Enable_panel(self, 'Actos')
            Enable_panel(self, 'ActosNormatividad', noTodos=True)
            setLabelActoActual(self)
            LlenaCtrlNormatividad(self, self.FALegis , 2154)
            LlenaCtrlNormatividad(self, self.FAInstr , 2155)
            
            self.FAinstrumentos_int_notas.Enable(False)
            self.FAlegislacion_nacional_notas.Enable(False)
            self.GuardarNormatividad.Enable()
            self.staticText5.Enable(CanEdit(status.casoActual))
            self.FAExportar.Enable(CanEdit(status.casoActual))
            self.delCaracRel.Enable(False)
            
        except:
            print "Unexpected error:", sys.exc_info()
            MError(self, "No se pudo cargar el acto ("+str(sys.exc_info())+")")
            status.actoActual = None

def setLabelActoActual(self, label=''):
    if not label:
        label = 'Acto: '+status.actoActual.Descriptor()
    self.LA1.SetLabel(label)
    self.LA2.SetLabel(label)
    self.LA14.SetLabel(label)

def SaveDataActo(self):
    if not CanEdit(status.casoActual):
        return None
    a=status.actoActual
    s=self
    if a:

        a.exportar = getCheckBoxValue(s.FAConfidencialidad)
        a.exportarnormatividad = getCheckBoxValue(s.FAExportar)
    
        a.observaciones = s.FAObservaciones.GetValue()
        edad = ToIntegerField(s.FAedad_victima.GetValue())
        if edad <= 120:
             a.edad_victima = edad
        else:
            MError(self, u"La edad de la v\xedctima no puede superar los 120 a\xf1os")
        a.edad_victima_tipo = s.choiceTipoEdad.GetSelection()
            
        if validDate(s.ActoFechaInicial, err="inicial del acto"):
            a.fechainicio = setDateField2(s.ActoFechaInicial) 
        if validDate(s.ActoFechaFinal, err="final del acto"):
            a.fechafin = setDateField2(s.ActoFechaFinal)
        
          
        
        a.PTipodefechainicio = getChoiceValue(s.FATipofechainicio)
        a.PLocalidad = getChoiceValue(s.FALocalidad)
        a.PTipodefechafin = getChoiceValue(s.FATipofechafin)
        
        if not moduleFechas.ctrlFechasValidas(s.ActoFechaInicial, a.PTipodefechainicio,
                                              s.ActoFechaFinal, a.PTipodefechafin, status):
                    MError(self, "La fecha final del acto no puede ser anterior a la fecha inicial")
        if not moduleFechas.ctrlFechasValidas(s.CasoFechaInicial, status.casoActual.Ptipo_fecha_inicio,
                                              s.ActoFechaInicial, a.PTipodefechainicio, status):
                    MError(self, "La fecha inicial del acto no puede ser anterior a la fecha inicial del caso")
                    
        if not moduleFechas.ctrlFechasValidas(s.ActoFechaFinal, a.PTipodefechafin, 
                                              s.CasoFechaFinal, status.casoActual.Ptipo_fecha_final,
                                              status):
                    MError(self, "La fecha final del acto no puede ser posterior a la fecha final del caso")        
        if not moduleFechas.ctrlFechasValidas(s.ActoFechaInicial, a.PTipodefechainicio, 
                                              s.CasoFechaFinal, status.casoActual.Ptipo_fecha_final,
                                              status):
                    MError(self, "La fecha inicial del acto no puede ser posterior a la fecha final del caso")                
        
        
        session.add(a)
        FlushInfo(id=148)
def LoadDataInvol(self):
    
    i=status.involActual
    s=self
    self.FIconfidencialidad.SetValue(False)
    self.FIgradoinvolucramiento.SetLabel('')
    self.FItipoperpetrador.SetLabel('')
    self.FIultimostatusperpetrador.SetLabel('')
    self.textCtrlINObservaciones.SetValue('')
    if i:
        try:
        
        
            if i.persona: 
                self.FIperpetrador.SetLabel(i.persona.Descriptor(perm=CanEdit(status.casoActual)))
                #self.btnDPersonaPerpetrador.Show(CanEdit(status.casoActual))
                
            
            if i.exportar: self.FIconfidencialidad.SetValue(setCheckBoxValue(i.exportar))
            if i.Pgradoinvolucramiento: self.FIgradoinvolucramiento.SetLabel(i.Pgradoinvolucramiento.descripcion)
            if i.Ptipoperpetrador: self.FItipoperpetrador.SetLabel(i.Ptipoperpetrador.descripcion)
            if i.Pultimostatusperpetrador: self.FIultimostatusperpetrador.SetLabel(Mvs(i.Pultimostatusperpetrador.descripcion))
            self.textCtrlINObservaciones.SetValue(Mvs(i.observaciones))
            Enable_panel(self, 'Involucramientos')
        except:
            
            MError(self, "No se pudo cargar el perpetrador"  +str(sys.exc_info())+")")
            status.involActual = None
    
def SaveDataInvol(self):
    i=status.involActual
    s=self
    if i:
        i.exportar = getCheckBoxValue(s.FIconfidencialidad)
        i.observaciones=s.textCtrlINObservaciones.GetValue()
        session.add(status.involActual)
        FlushInfo(id=149)
    
    
    
    
    
    
    
def Mvi(value):
    if value:
        return value
    else: 
        return 0

def ToIntegerField(value):
    try:
        i=int(value)
    except:
        i=None
    return i


def ActoSepuedeBorrar(self, acto):
    borrar = False
    if acto.RolPerpetradores:
        borrar = False
        MError(self, u"Este acto no puede ser borrado ya que tiene perpetradores involucrados")
        return borrar
    #if acto.PCaracRelevantes:
    #    borrar = False
    #    MError(self, u"El acto tiene caracter\xedsticas registradas")
    #    return borrar
    if Borrar(self, u"\xbfBorrar este acto?"):
        borrar = True
    return borrar
def CasoSepuedeBorrar(self, CasoBorrar):
    borrar = False
    if CasoBorrar.actos:
        MError(self, u"Este caso no puede ser borrado ya que contiene actos")
        return borrar
    if CasoBorrar.intervenciones:
        MError(self, "Este caso no puede ser borrado ya que contiene intervenciones")
        return borrar
    if CasoBorrar.fuentes:
        MError(self, u"Este caso no puede ser borrado ya que contiene fuentes de informaci\xf3n")
        return borrar
    if CasoBorrar.Pvinculos or CasoBorrar.PvinculosInversos:
        MError(self, u"Este caso no puede ser borrado ya que est\xe1 relacionado con otros casos")
        return borrar
    if CasoBorrar.localidades:
        MError(self, u"Este caso no puede ser borrado ya que contiene localidades")
        return borrar
    if Borrar(self, u"\xbfBorrar el caso?"):
        borrar = True
    return borrar

def ActivaCtrlFecha(item,ctrl):
    if item:
        if hasattr(item, 'name'):
            if not(item.name == status.UnknownDate) :
                ctrl.Show(True)
        else:
            ctrl.Show(False)
    else:
        ctrl.Show(False)

    
    

        
    
def LlenaIntervenciones(self):
    t = LlenaCtrl3(self.listBoxIntervenciones,
               [(i,i.Descriptor()) for i in status.casoActual.intervenciones])
    if status.intervencionActual:
        CtrlSelect(self.listBoxIntervenciones, status.intervencionActual.Descriptor())
    self.staticText11.SetLabel("%i Intervenciones "%t)
    self.staticText11.Enable()
def LlenaPantallasGenerales(self):  
            s=self  
            
            LlenaCtrlCategoria(self.choiceTipoFechaInicial, u"T48")
        
            LlenaCtrlCategoria(self.choiceTipoFechaFinal, u"T48")
            LlenaCtrlCategoria(self.choicePubTipofechaconsulta, u"T48")
            LlenaCtrlCategoria(self.FCtipo_frecepcion, u"T48")
            LlenaCtrlCategoria(self.choiceMonitoreo,u"T46")
            #LlenaCtrlCategoria(self.choicePais,"T15")
            
            #LlenaCtrlCategoria(self.FPTipo,u"T07")
            LlenaCtrlCategoria(self.FPMonitoreo,u"T43")
            LlenaCtrlCategoria(self.FPTipodefecha ,u"T48" )
            LlenaCtrlCategoria(self.FPTipodefecharecepcion ,u"T48" )
            LlenaCtrlCategoria(self.FBFechaInicialTipo ,u"T48" )
            LlenaCtrlCategoria(self.FBFechaFinalTipo ,u"T48" )
            LlenaCtrlCategoria(self.FBFechaInfo_vigenteTipo ,u"T48" )
            LlenaCtrlCategoria(self.FPEscolaridad  ,u"T09" )
            #LlenaCtrlCategoria(self.FPOcupacion  ,u"T10" )
            
            LlenaCtrlCategoria(self.FPReligion  ,u"T12" )
            LlenaCtrlCategoria(self.FPMonitoreo   ,u"T43" )
            LlenaCtrlCategoria(self.FPEstadocivil   ,u"T08" )
            
            LlenaCtrlCategoria(self.FPSexo   ,u"T39" )
            LlenaCtrlCategoria(self.FPEstado, u'T63')

            
            LlenaCtrlCategoria(self.FATipofechainicio, u'T48')
            LlenaCtrlCategoria(self.FATipofechafin, u'T48')
            LlenaCtrlCategoria(s.choicePubTipoFecha, u'T48')
            LlenaCtrlCategoria(s.choiceIntTipofecha, u'T48')
            LlenaCtrlCategoria(s.choicePubIdioma, u'T14')
            #LlenaCtrlCategoria(s.choicePubLenguaIndigena, u'T66')
            #LlenaCtrlCategoria(s.choicePubConfiabilidad, u'T42')
            
            LlenaCtrlCategoria(s.choiceFteTipoFecha, u'T48')
            LlenaCtrlCategoria(s.choiceFteIdioma, u'T14')
            #LlenaCtrlCategoria(s.choiceFteLenguaIndigena, u'T66')
            #LlenaCtrlCategoria(s.choiceFteConfiabilidad, u'T42')
            status.reciprocoRelacionCasos = DictReciproco(u'R22')
            status.reciprocoRelacionPersonas = DictReciproco(u'R21')
            
            
            
            CtrlFechas(self)
            init_panels(self)
            
            ajustesSE(self, status.SE)
            
            if not status.cnfBaseCentral:
                for ctrlName in moduleCtrls.CtrlsBaseCentral:
                    ctrl=getattr(self, ctrlName)
                    ctrl.Show(False)
            self.btnCopiarC3P.Enable(False)
            self.btnCopiarC3.Enable(False)
                
            
panels={}
def init_panels(self):
     
     panels['Datos Generales'] = self.NBCasosGral
     panels['Tipificacion'] = self.NBCasosTipifica
     panels['Inf. Narrativa']=self.NBCasosNarrativa
     panels['Casos Adm']=self.NBCasosAdm
     
     panels['Actos']=self.NBActosGral
     panels['Involucramientos']=self.NBActosPerp
     panels['Intervenciones']=self.NBIntervenciones
     panels['Fuentes']=self.NBFuentePersonal
     panels['Documentos']=self.NBFuenteDocumental
     panels['Personas 1']=self.NBPersonasGral
     panels['Personas 2']=self.NBPersonasDetalles
     panels['Personas 3']=self.NBPersonasAdm
     panels['Personas 4']=self.NBPersonasBio
     panels['CasosRelaciones']=self.NBCasosRelaciones
     panels['ActosNormatividad']=self.NBNormatividad
     
     if False:
         panels['Tipificacion'].Disable()
         panels['Inf. Narrativa'].Disable()
         panels['Casos Adm'].Disable()
         panels['Actos'].Disable()
         panels['Involucramientos'].Disable()
         panels['Intervenciones'].Disable()
         panels['Fuentes'].Disable()
         panels['Personas 2'].Disable()
         panels['ActosNormatividad'].Disable()
     
     Enable_panel(self, 'Datos Generales', enable=False)
     Enable_panel(self, 'Actos', enable=False)
     Enable_panel(self, 'ActosNormatividad', enable=False)
     Enable_panel(self, 'Involucramientos', enable=False)
     Enable_panel(self, 'Intervenciones', enable=False)
     Enable_panel(self, 'Fuentes', enable=False)
     Enable_panel(self, 'Documentos', enable=False)
     Enable_panel(self, 'Personas 1', enable=False)
     Enable_panel(self, 'Personas 4', enable=False)
     Enable_panel(self, 'Personas 3', enable=False)
     #Enable_panel(self, 'CasosRelaciones', enable=False)
     
     LlenaAyuda(self, u'frame2')
     LlenaAyuda(self, u'personaInd')
     LlenaPersonas(self.listBoxPersonaBrowser)
     if cnf.baseCentral:
         self.AltaCaso.Disable()
         self.btnNuevaPersona.Disable()
         muestraControlesRelevancia(self, False)
     print >>status.log, datetime.datetime.now()
         
def setEtiquetaCasoActual(self, expr, enable=True):
    etiquetas = ['LC1','LC2','LC3','LC4','LC5','LC6','LC7','LC9','LC12','LC14','LC15']
    for ctrlName in etiquetas:
        ctrl = getattr(self, ctrlName)
        ctrl.SetLabel(expr)
        ctrl.Enable(enable)

def Enable_panel(self, winName, enable=True, noTodos=False):
    helpButtonType = type(self.contextHelpButton1)
    if winName in panels.keys():
         if enable: panels[winName].Enable()
         ctrls = panels[winName].GetChildren()
         disable = not enable
        
         for i in ctrls:
             if enable and not noTodos:
                i.Enable()
             else: 
                if type(i) != helpButtonType:
                    i.Disable()
                 
                 
         if winName== 'Datos Generales':
             
             CamposSololectura(self, camposEntidad['caso'], enable and CanEdit(status.casoActual))
             self.listaCasos.Enable()
             self.AltaCaso.Enable(CanCreateCaso())
             self.btnReps.Enable(CanReport())
             self.NBCasos.SetSelection(0)
             self.CasoIsearch.Enable()
             self.staticText105.Enable()
             
             if status.casoActual:
                 
                HabilitarCopiarC3 = status.casoActual.clavestatusc3 != 1
             self.btnCopiarC3.Enable(status.filtroContenedor == 2 and HabilitarCopiarC3)
    
         if winName== 'Actos':
             
             CamposSololectura(self, camposEntidad['acto'], enable and CanEdit(status.casoActual))
             self.listActos.Enable()
             self.buttonNuevoActo.Enable(CanEdit(status.casoActual))
             self.NBActos.SetSelection(0)
             if disable:
                 status.actoActual = None
                 LimpiaCampos(self, camposEntidad['acto'])
         if winName == 'Involucramientos':
             CamposSololectura(self, camposEntidad['involucramiento'], enable and CanEdit(status.casoActual))
             self.buttonAddPerpetrador.Enable(CanEdit(status.casoActual))
             self.listBoxPerpetradores.Enable()
             if disable: 
                 LimpiaCampos(self, camposEntidad['involucramiento'])
                 status.involActual=None
             self.LC4.Enable()
             self.statixText50.Enable()
         if winName == 'ActosNormatividad':
             #CamposSololectura(self, camposEntidad[''], enable and CanEdit(status.casoActual))
             self.FALegis.Enable()
             self.FAInstr.Enable()
             self.LA14.Enable(enable)
             self.LC14.Enable()
             self.staticText97.Enable(enable)
             self.staticText95.Enable(enable)
             self.staticText96.Enable(enable)
             self.staticText98.Enable(enable)
             self.txtLongNorLeg.Enable(enable)
             self.txtLongNorIns.Enable(enable)
             self.btnActoLegislacion.Enable(enable and CanEdit(status.casoActual))
             self.btnActoInstrInt.Enable(enable and CanEdit(status.casoActual))
             
             
             
             
         if winName == 'Intervenciones':  
             CamposSololectura(self, camposEntidad['intervenciones'], enable and CanEdit(status.casoActual))
             self.listBoxIntervenciones.Enable()
             self.buttonAddIntervencion.Enable(CanEdit(status.casoActual))
        
             
         if winName == 'Fuentes':    
             CamposSololectura(self, camposEntidad['fuentePersonal'], enable and CanEdit(status.casoActual))
             
             self.listBoxFte.Enable()
             #self.buttonFteNueva.Enable(status.canEditCaso)
             self.buttonFteNueva.Enable(CanEdit(status.casoActual))
             self.NBFuentes.SetSelection(0)
             if disable:
                status.fuenteActual = None
                LimpiaCamposFuente(self)
                
                
         if winName == 'Documentos':  
             CamposSololectura(self, camposEntidad['fuenteDocumental'], enable and CanEdit(status.casoActual)) 
             self.listBoxDocs.Enable()
             self.btnAddDoc.Enable(CanEdit(status.casoActual))
             if disable:
                status.pubActual = None
                LimpiaCamposPub(self)

             
         if winName == 'Personas 1':
             #controles que se activan solo cuando se puede editar una entidad
             status.panelPersonasEnabled = enable
             CamposSololectura(self, camposEntidad['persona'], enable and CanEditPersona(status.personaActual)) 
             
             statbutton = self.btnAddOcupacion.IsEnabled()
             
             #controles que siempre estan activos
             self.listBoxPersonaBrowser.Enable()
             self.srchPersona.Enable()
             self.btnRepsPersona.Enable(CanReport())
             self.btnNuevaPersona.Enable(CanCreate())
             #self.NBPersonas.SetSelection(0)
             # ojo!
             self.btnBusquedaExhausticaPersona.Enable()
             self.btnBuscarPersona.Enable()
             self.btnMostarTodasPersonas.Enable()
             self.MP1.Enable()
             self.MP0.Enable()
             self.MP2.Enable()
             self.MP3.Enable()
             self.MP4.Enable()
             self.choiceGrupoP.Enable()
             self.choiceContenedorP.Enable()
             self.staticText99.Enable()
             self.staticText111.Enable()
             
             self.txtTotalPersonas.Enable()
             self.staticText81.Enable()
             
            
             
             
             
             #if disable:
                 #limpiaCamposPersona(self)
         if winName == 'Personas 2':
             CamposSololectura(self, camposEntidad['persona2'], enable and CanEditPersona(status.personaActual)) 
                   
         if winName == 'Personas 4':
             self.staticText20.Enable()
             if status.vinculoActual:
                s = self
                t = status.vinculoActual.vinculo2 is not None
                s.staticText93.Show(t)
                s.staticText90.Show(t)
                s.FBPuesto.Show(t)
                s.FBRango.Show(t) 
                if status.vinculoActual.vinculo2:
                    self.FBDescripcion.Disable()
                    self.staticTxtTipoderelacion.Show()
                    self.btnTipoVinculo.Show()
                    
                    
                else:
                    self.FBDescripcion.Enable()
                    self.staticTxtTipoderelacion.Show(False)
                    self.btnTipoVinculo.Show(False)
                CamposSololectura(self, camposEntidad['DetalleBiografico'], enable and CanEditPersona(status.personaActual)) 
    else:
        print winName, " error"
         
def LimpiaCamposFuente(self):
    LimpiaCampos(self, camposEntidad['fuentePersonal'])
    EscondeCtrlFecha([self.FuenPerFecha])
    
             
def LimpiaCamposPub(self):
    LimpiaCampos(self, camposEntidad['fuenteDocumental']) 
    EscondeCtrlFecha([self.FuenDocFecha, self.FuenDocFechaConsulta])
                       
def LlenaCtrlFuentes(self):
    t=LlenaCtrl3(self.listBoxFte, [(i,i.Descriptor()) for i in status.casoActual.fuentes], selected=status.fuenteActual)   
    self.staticText22.SetLabel(u'%i Fuentes de Informaci\xf3n'%t)
    self.staticText22.Enable()

def LlenaCtrlVinculos(self, ctrl, persona, selected=None):
        P = persona


        lista = [(i,i.Descriptor()) for i in P.LaOtra2  if i.vinculo2] + \
                [(i,i.Descriptor_R()) for i in P.LaOtra1  if i.vinculo1] + \
                [(i,i.Descriptor()) for i in P.LaOtra2  if i.descripcion]
        
        
        t=LlenaCtrl3(ctrl,lista, selected=selected)
        self.staticText20.SetLabel(u'%i Datos biogr\xe1ficos'%t)
        self.staticText20.Enable()
        
def SaveData(self, page):
        if page in ['Datos Generales', 'Tipificacion', 'Inf. Narrativa', 'Casos Adm']:
            saveDataCaso(self)
            
            
        if page in ['Actos']:
            saveDataActo(self)
            
        
        if page in ['Intervenciones']:
            saveDataActo(self)
            SaveDataIntervencion(self)
            
        if page in ['Fuentes']:
            saveDataFuentes(self)
        if page in ['Documentos']:
            saveDataDocumentos(self)
        if page in ['Personas 1', 'Personas 2','Personas 3' ]:
            saveDataPersona(self)
            
        FlushInfo(id=150)    
def LlenaCtrlLocalizacion(self, ctrl, caso, renglonInicial=None, perm=True):
    Locs = caso.localidades
    if renglonInicial:
        LlenaCtrl3(ctrl, [(None, ' ')]  )
    LlenaCtrl3(ctrl, 
       [(i,   i.Descriptor(perm=perm)) for i in Locs], append=renglonInicial)
    
    
def derechosafectadosPattern(ElCaso, raiz):
    lista1 = []
    lista2 = []
    
    RegExp = raiz
    
    listaderechos = ElCaso.derechosafectados
    for i in ElCaso.derechosafectados:
        
        parentpattern = ParentsPattern(i.tipificacion.parent, u'T03')
        
        RegExp = RegExp + '|^'+i.tipificacion.name
        if parentpattern:
            RegExp = RegExp + '|' + parentpattern

    print "RegExp ", RegExp
    Pattern = re.compile(RegExp)
    
    return Pattern




def loadDataFuente(self):
    f= status.fuenteActual
    s=self
    self.staticTextFtePersona.SetLabel('')
    s.checkBoxFteConfidencialidad.SetValue(False)
    s.textCtrlFteObservaciones.SetLabel('')
    s.textCtrlFteComentarios.SetLabel('')
    s.staticTextRelPersona.SetLabel('')
    s.staticFteConfiabilidad.SetLabel('')
    s.staticFteLenguaIndigena.SetLabel('')
    s.choiceFteIdioma.SetSelection(-1)

    
    s.choiceFteTipoFecha.SetSelection(-1)

    
    
    self.staticTextConexionInfo.SetLabel('')
    if f:
        try:
            if f.PPersona_como_fuente: 
                self.staticTextFtePersona.SetLabel(f.PPersona_como_fuente.Descriptor(perm=CanEdit(status.casoActual)))
                self.btnDPersonaFuente.Show(CanEdit(status.casoActual))
        
            
            if f.PConexion_info:
                self.staticTextConexionInfo.SetLabel(f.PConexion_info.descripcion)
            if f.PPersona:
                s.staticTextRelPersona.SetLabel(f.PPersona.Descriptor())
            PutDesc(self.staticFteLenguaIndigena, f.PLengua_indigena)
            PutDesc(self.staticFteConfiabilidad, f.PConfiabilidad)
            CtrlSelect(s.choiceFteTipoFecha,f.PTipofecha)
            ActivaCtrlFecha2(f.PTipofecha, self.FuenPerFecha)    
            if f.fecha:
                module2.setDateCtrl2(self.FuenPerFecha, f.fecha, f.PTipofecha)
            if f.idioma:
                CtrlSelect(s.choiceFteIdioma, f.PIdioma)

            if f.comentarios:
                s.textCtrlFteComentarios.SetValue(f.comentarios)
            if f.observaciones:
                s.textCtrlFteObservaciones.SetValue(f.observaciones)
            if f.exportar: 
                s.checkBoxFteConfidencialidad.SetValue(setCheckBoxValue(f.exportar))
            
            
                
            Enable_panel(self, 'Fuentes')
        except:
            MError(self, "No se puedo cargar la fuente"+str(sys.exc_info())+")")
            status.fuenteActual = None
    
def SaveDataFuente(self):
        
        if status.fuenteActual:
           f= status.fuenteActual
           s=self
           if validDate(self.FuenPerFecha, "de la fuente"):
               f.fecha= module2.setDateField2(self.FuenPerFecha)
           f.observaciones = self.textCtrlFteObservaciones.GetValue()
           f.comentarios= self.textCtrlFteComentarios.GetValue()
           f.exportar = getCheckBoxValue(s.checkBoxFteConfidencialidad)
           f.PTipofecha = getChoiceValue(s.choiceFteTipoFecha)
           f.PIdioma = getChoiceValue(s.choiceFteIdioma)
           
           session.add(status.fuenteActual)
           FlushInfo(id=151)
           
def SaveDataPub(self):
        
        if status.pubActual:
           f= status.pubActual
           s=self
           if validDate(self.FuenDocFecha, "de la fuente documental"):
               f.fecha= module2.setDateField2(self.FuenDocFecha)
           if validDate(self.FuenDocFechaConsulta, "de consulta de la fuente documental"):
               f.fecha_consulta = module2.setDateField2(self.FuenDocFechaConsulta)
           f.observaciones = self.textCtrlPubObservaciones.GetValue()
           f.comentarios= self.textCtrlPubComentarios.GetValue()
           
           f.PTipofecha = getChoiceValue(s.choicePubTipoFecha)
           f.PTipofechaConsulta = getChoiceValue(s.choicePubTipofechaconsulta)
           f.PIdioma = getChoiceValue(s.choicePubIdioma)
           #f.PLengua_indigena = getChoiceValue(s.choicePubLenguaIndigena)
           #f.PConfiabilidad  = getChoiceValue(s.choicePubConfiabilidad)
           f.titulo_de_parte = s.textCtrlPubTituloParte.GetValue()
           #f.titulo = s.textCtrlPubTitulo.GetValue()
           f.datos_publicacion = s.textCtrlPubDatos.GetValue()
           f.Nombre_del_sitio = s.textCtrlPubNombreSitio.GetValue()
           f.Liga_publicacion = s.textCtrlPubLigaSitio.GetValue()
           f.exportar = getCheckBoxValue(s.checkBoxPubExportar)
        
           
           session.add(status.pubActual)
           FlushInfo(id=152)
           
def LoadDataPub(self):
    f= status.pubActual
    s=self
    self.staticTextPubPersona.SetLabel('')
    
    s.textCtrlPubObservaciones.SetValue('')
    s.textCtrlPubComentarios.SetValue('')
    s.textCtrlPubDatos.SetValue('')
    s.txtPubTipoPub.SetLabel('')
    s.staticDocLenguaIndigena.SetLabel('')
    self.staticPubConfiabilidad.SetLabel('')
    s.choicePubTipoFecha.SetSelection(-1)
    
    s.choicePubIdioma.SetSelection(-1)
    
    s.checkBoxPubExportar.SetValue(1)
    

    if f:
        try:    
            
            
            CtrlSelect(s.choicePubTipoFecha,f.PTipofecha)
            
            
            CtrlSelect(s.choicePubTipofechaconsulta,f.PTipofechaConsulta)
            
            PutDesc(self.staticDocLenguaIndigena, f.PLengua_indigena)   
            PutDesc(self.staticPubConfiabilidad, f.PConfiabilidad)
            if f.fecha:
                module2.setDateCtrl2(self.FuenDocFecha, f.fecha, f.PTipofecha)
            if f.fecha_consulta:
                module2.setDateCtrl2(self.FuenDocFechaConsulta, f.fecha_consulta, f.PTipofechaConsulta)
            if f.idioma:
                CtrlSelect(s.choicePubIdioma, f.PIdioma)
            if f.exportar:
                s.checkBoxPubExportar.SetValue(setCheckBoxValue(f.exportar))
            
            if f.comentarios:
                s.textCtrlPubComentarios.SetValue(f.comentarios)
            if f.observaciones:
                s.textCtrlPubObservaciones.SetValue(f.observaciones)
            
            if f.PTipopublicacion:
                s.txtPubTipoPub.SetLabel(f.PTipopublicacion.descripcion)
                
            
            s.textCtrlPubTituloParte.SetValue(Mvs(f.titulo_de_parte))
            
            
            if f.datos_publicacion:
                s.textCtrlPubDatos.SetValue(f.datos_publicacion)
            
            s.textCtrlPubNombreSitio.SetValue(Mvs(f.Nombre_del_sitio))
            
            s.textCtrlPubLigaSitio.SetValue(Mvs(f.Liga_publicacion))
            if f.PPersonareferenciada:
                s.staticTextPubPersona.SetLabel(f.PPersonareferenciada.Descriptor())
            Enable_panel(self, 'Documentos')
        except:
            MError(self, u"No se pudo cargar la publicaci\xf3n ("+str(sys.exc_info())+')')
            status.pubActual = None

def LlenaCtrlPubs(self):
    if status.casoActual:
        
        t=LlenaCtrl3(self.listBoxDocs,[(i, i.titulo_de_parte) for i in status.casoActual.PPublicaciones], selected=status.pubActual)
        self.staticText43.SetLabel('%i Documentos'%t)
        self.staticText43.Enable()
def AjustaLocalidadSegunPais(self, toShow):
    s = self
    for ctrl in [s.CPEstado, s.FPEstado, s.CPMunicipio, s.FPMunicipio, 
                 s.CPLocalidad, s.FPLocalidad]:
        ctrl.Show(toShow)


def CambiaTitulos(self, IND):
    s=self
    if not hasattr(s.CPApellido, 'ALT'):
        
        s.CPApellido.ALT='Nombre'
        
        s.CPNombre.ALT='Sigla'
        
        
        #s.FPNombre.IND=True
        s.CPSexo.ALT=''
        s.FPSexo.IND=True
        
        
        s.CPPais.ALT=u'Pa\xeds de origen'
        s.CPEstado.ALT=u'Estado de origen'
        s.CPMunicipio.ALT=u'Municipio de origen'
        s.CPLocalidad.ALT=u'Localidad de origen'
        s.CPCiudadania.ALT=u'Pa\xeds sede'
        s.CPEscolaridad.ALT=u'Nivel de escolaridad predominante'
        s.CPfechanac.ALT=u'Fecha de creaci\xf3n'
        s.CPReligion.ALT=u'Religi\xf3n predominate'
        s.CPEstadocivil.ALT=''
        s.FPEstadocivil.IND=True
        s.btnAddFPTipo.IND=False
        s.btnDelFPTipo.IND=False
        s.staticFPTipo.IND=False
        s.CPTipo.IND=False
        s.CPNodependientes.ALT=u'No. de personas en el grupo'
        s.CPDescripciondelgrupo.ALT=u'Descripci\xf3n del grupo'
        s.CPDescripciondelgrupo.IND=False
        s.FPDescripciondelgrupo.IND=False 
        s.CPArchivos.ALT=''
        s.CPOcupacion.ALT=u'Ocupaci\xf3n predominante'
        s.CPIdioma.ALT=u'Idioma predominante'
        s.CPLengua.ALT=u'Lengua predominante'
        s.CPOrigenEtnico.ALT=u'Origen \xe9tnico predominante'
               
    if IND:
        if status.personaIndividual:
            # nothing to change
            return
        else:
            LlenaAyuda(self, u'personaInd')
    if not IND:
        if not status.personaIndividual:
            # nothing to change
            return
        else:
            LlenaAyuda(self, u'personaCol')
    l = []
    status.personaIndividual = not status.personaIndividual
    for i in panels['Personas 1'].GetChildren():
        l.append(i)
    for i in panels['Personas 2'].GetChildren():
        l.append(i)
    
    for ctrl in l:

        if hasattr(ctrl, 'ALT'):
            tmp = ctrl.GetLabel()
            ctrl.SetLabel(ctrl.ALT)
            ctrl.ALT = tmp
        if hasattr(ctrl,'IND'):
            if ctrl.IND:
                 ctrl.Show(IND)
            else:
                 ctrl.Show(not IND)
               
def DialogTipificaPersona(P, parent,Tesauro, Tipology, codigo,desc='', help=u''):
        Tipo = getTaxonomyTree(parent, Tesauro, desc, help=help)
        collection = getattr(P, Tipology)
        
        if Tipo:
          tipificacion=PersonaTipificacion(codigo, P, Tipo )
          
          session.add(tipificacion)
          FlushInfo(id=153)
          
          collection.append(tipificacion)
def LlenaDireccionesPersona(self):
        P = status.personaActual
        LlenaCtrl3(self.FPDirecciones, DireccionesPersona(P, " - "))
        if P.PDirecciones:
            self.delDireccion.Enable(CanEditPersona(status.personaActual))
        else:
            self.delDireccion.Enable(False)

def setPersonasSeleccionadas(self, totalSeleccionadas):
    "asigna el letrero con la cantidad de personas seleccionadas"
    if totalSeleccionadas == status.totalPersonas:
        label = ''
    elif totalSeleccionadas == None:
        label = ''
    else:
        label = "%i personas seleccionadas"%totalSeleccionadas

    self.txtTotalPersonasSeleccionadas.SetLabel(label)


def PersonaDetalles(self, Persona):
    status.PantAnterior= self.NBMain.GetSelection()
    if Persona:
        SaveDataPersona(self)
        SaveDataVinculo(self)
        status.personaActual = Persona
        P = status.personaActual #???
        
        if status.personaReciente:
            LlenaPersonas(self.listBoxPersonaBrowser)
            
        LoadDataPersona(self)
        CtrlSelect(self.listBoxPersonaBrowser, Persona)
        self.NBMain.SetSelection(4)
        self.NBPersonas.SetSelection(0)
        self.btnPantAnterior.Show()
    
def LlenaActos(self):
    t=LlenaCtrl3(self.listActos, [(i,i.Descriptor()) for i in status.casoActual.actos])
    if status.actoActual:
        s=status.actoActual.Descriptor()
        self.listActos.SetStringSelection(s) 
    self.staticText6.SetLabel("%i Actos registrados"%t)
    self.staticText6.Enable()
        
    
def LoadDataVinculo(self):
    V = status.vinculoActual
    s = self
    if V:
        try:
            tipovinculo = None
            if V.vinculo2:
                if V.vinculo1 == status.personaActual:
                    tipovinculo = 'Directo'
                if V.vinculo2 == status.personaActual:
                    tipovinculo = 'Reciproco'
            print 'tipo de vinculo', tipovinculo
            
            s.FBObservaciones.SetValue('')
            s.FBDescripcion.SetValue('')
            s.FBPuesto.SetValue('')
            s.FBRango.SetValue('')
            s.FBComentarios.SetValue('')
            s.txtPrelacionada.SetLabel('')
            s.FBConfidencialidad.SetValue(False)
            s.FBObservaciones.Enable(V.vinculo2 == None)
            #--------------------------------------------
            
            if tipovinculo == "Directo":
                s.txtTipoVinculo.SetLabel(TesNotNull(V.tipo))
            if tipovinculo == "Reciproco":
                s.txtTipoVinculo.SetLabel(terminoReciproco(status.reciprocoRelacionPersonas, V.tipo.name, V.tipo.ClaveODesc()))
            #--------------------------------------------
            if V.observaciones: s.FBObservaciones.SetValue(V.observaciones)
            if V.descripcion: s.FBDescripcion.SetValue(V.descripcion)
            if V.comentarios: s.FBComentarios.SetValue(V.comentarios)
            
            CtrlSelect(s.FBFechaInicialTipo,V.Ptipofecha_inicial)
            CtrlSelect(s.FBFechaInfo_vigenteTipo,V.Ptipofecha_info_vigente)
            
            CtrlSelect(s.FBFechaFinalTipo,V.Ptipofecha_final)
            if V.Fecha_inicial: setDateCtrl2(s.BioFechaInicial, V.Fecha_inicial, V.Ptipofecha_inicial )
            if V.fecha_info_vigente: setDateCtrl2(s.BioFechaVig, V.fecha_info_vigente, V.Ptipofecha_info_vigente)
            if V.Fecha_final:   setDateCtrl2(s.BioFechaFinal, V.Fecha_final, V.Ptipofecha_final)
            if V.exportar: self.FBConfidencialidad.SetValue(setCheckBoxValue(V.exportar))
            if V.puesto: s.FBPuesto.SetValue(V.puesto)
            if V.rango: s.FBRango.SetValue(V.rango)
            if V.vinculo2: 
            #-------------------------------------------------------
                if tipovinculo == 'Directo':
                    s.txtPrelacionada.SetLabel(V.vinculo2.Descriptor() )
                if tipovinculo == 'Reciproco':    
                    s.txtPrelacionada.SetLabel(V.vinculo1.Descriptor() )
                s.staticTxtPrelacionada.Show()
                s.btnPrelacionada.Show()
            else:
                self.staticTxtPrelacionada.Show(False)
                s.btnPrelacionada.Show(False)
            s.staticTxtTipoderelacion.Show(V.vinculo2 != None)
            s.btnTipoVinculo.Show(V.vinculo2 != None)
            s.txtTipoVinculo.Show(V.vinculo2 != None)
                
        except:
            MError(self, u"No se pudo cargar el detalle biogr\xe1fico ("+str(sys.exc_info())+')')
            status.vinculoActual = None

def SaveDataVinculo(self):
    V = status.vinculoActual
    s = self
    if V:
        try:
            V.observaciones = s.FBObservaciones.GetValue()
            V.descripcion = s.FBDescripcion.GetValue()
            V.comentarios = s.FBComentarios.GetValue()
            if validDate(s.BioFechaInicial, u"inicial del dato biogr\xe1fico"):
                V.Fecha_inicial = setDateField2(s.BioFechaInicial)
            if validDate(s.BioFechaFinal, u"final del dato biogr\xe1fico", Posterior= False):
                V.Fecha_final = setDateField2(s.BioFechaFinal)
            if validDate(s.BioFechaVig, u"de vigencia del dato biogr\xe1fico"):
                V.fecha_info_vigente = setDateField2(s.BioFechaVig)
            V.Ptipofecha_inicial = getChoiceValue(s.FBFechaInicialTipo)
            V.Ptipofecha_final = getChoiceValue(s.FBFechaFinalTipo)
            V.Ptipofecha_info_vigente = getChoiceValue(s.FBFechaInfo_vigenteTipo)
            V.exportar = getCheckBoxValue(self.FBConfidencialidad)
            V.puesto = s.FBPuesto.GetValue()
            V.rango  = s.FBRango.GetValue()
            session.add(V)
            FlushInfo(id=154)
        except:
            MError(self, u"No se puedo grabar el dato biogr\xe1fico ("+str(sys.exc_info())+')')
            status.vinculoActual = None
 
def LoadDataIntervencion(self):
    s=self
    I=status.intervencionActual
    This=I
    print 1.33
    LimpiaCamposIntervencion(self)

    if I:
        try:
            #self.textCtrlIntervencionDescrip.Value = This.descripcion
            if This.solicitante:
                self.staticText17.SetLabel(This.solicitante.Descriptor())
            if This.contraparte:
                self.staticText19.SetLabel(This.contraparte.Descriptor())
            if This.Pinterviniente:
                self.txtIntParte.SetLabel(This.Pinterviniente.Descriptor())
            if This.tipo:
                self.staticText18.SetLabel(This.tipo.descripcion)
            if I.exportar:
                print 1.31
                self.checkBoxIntExportar.SetValue(setCheckBoxValue(I.exportar))
                print 1.32
            Enable_panel(self, 'Intervenciones')
            setDateCtrl2(s.InterFecha, I.fecha, I.PTipofecha)
            CtrlSelect(s.choiceIntTipofecha,I.PTipofecha)
            
            if I.observaciones:  s.txtIntObservaciones.SetValue(I.observaciones)
            if I.respuesta:  s.txtIntRespuesta.SetValue(I.respuesta)
            if I.impacto:  s.txtIntImpacto.SetValue(I.impacto)
            
            if I.comentarios:   s.txtIntComentarios.SetValue(I.comentarios)
            
        except:
            MError(self, u"No se pudo cargar la intervenci\xf3n ("+str(sys.exc_info())+")")
            status.intervencionActual = None
    
def LimpiaCamposIntervencion(self):
    LimpiaCampos(self, camposEntidad['intervenciones'])
    EscondeCtrlFecha([self.InterFecha])

        
def SaveDataIntervencion(self):
    s=self
    I=status.intervencionActual
    errorFecha = False
    if I:
        tipofecha = getChoiceValue(s.choiceIntTipofecha)
        if validDate(s.InterFecha,u"de la intervenci\xf3n"):
            errorFecha = False
        else:
            errorFecha = True
                
            
        if not moduleFechas.ctrlFechasValidas(self.CasoFechaInicial, status.casoActual.Ptipo_fecha_inicio,
                                               self.InterFecha, tipofecha, status):
            
            MError(self, u"La fecha inicial de la intervenci\xf3n no puede ser anterior a la fecha inicial del caso")  
            errorFecha = True
        if not errorFecha:
            I.fecha = setDateField2(s.InterFecha)
            I.PTipofecha = getChoiceValue(s.choiceIntTipofecha)
        
        
        I.observaciones = s.txtIntObservaciones.GetValue()
        I.comentarios = s.txtIntComentarios.GetValue()
        I.respuesta = s.txtIntRespuesta.GetValue()
        I.impacto = s.txtIntImpacto.GetValue()
        I.exportar = getCheckBoxValue(s.checkBoxIntExportar)

        
        
        session.add(I)
        FlushInfo(id=155)
        
def SaveDataLegis(self):
    s=self
    L=status.legisActual
    if L:
        L.notas=s.FAlegislacion_nacional_notas.GetValue()
        session.add(L)
        FlushInfo(id=156)
        print "SaveDataLegis"
        
def SaveDataInstr(self):
    s=self
    L=status.instrActual
    if L:
        L.notas=s.FAinstrumentos_int_notas.GetValue()
        session.add(L)
        FlushInfo(id=157)
        print "SaveDataInstr"
        
        

def PersonaSepuedeBorrar(self, P):
    return True
def LlenaCtrlNormatividad(self, ctrl, codigo):
    lista = [(i, i.tipificacion.descripcion)  for i in status.actoActual.caso.tipificaciones if i.codigo == codigo and i.acto_id == status.actoActual.id]
    LlenaCtrl3(ctrl, lista)
    self.FAlegislacion_nacional_notas.SetValue('')
    self.FAinstrumentos_int_notas.SetValue('')

    
    
    pass
def LimpiaCampos(self, listadecampos):
    for campo in listadecampos:
        c=self.__getattribute__(campo)
        tipo_de_c = str(type(c))
        

        if type(c)==wx.ListBox:
            c.Clear()
            
                    
        elif type(c) == wx.CheckBox:
            c.SetValue(0)
            
        elif type(c)==wx.StaticText:
            c.SetLabel('')
        elif type(c)==wx.Choice:
            c.SetStringSelection('')
            c.SetSelection(-1)
            
        elif type(c)==wx.Button:
            NOP()
        
        elif type(c)==wx.lib.intctrl.IntCtrl:
             c.SetValue(None)


        elif hasattr(c, 'Value'):

            c.SetValue('')
            
            
        else: print "!!!!!"
        

def limpiaCamposPersona(self):
    
    
    status.personaActual = None
    status.vinculoActual = None
    LimpiaCampos(self, camposEntidad['persona'])
    
          
def LlenaRoles(ctrl, P):
    R = P.Roles()
    ctrl.Clear()
    for rol in R.keys():
        
            LlenaCtrl3(ctrl, [(i, i.descripcion +' / '+ rol) for i in R[rol] if i], append=True)
def LlenaCasoInicial(self):
    n = self.listaCasos.GetCount()
    if n:
        self.listaCasos.SetSelection(0)
        status.casoActual=MyClientData(self.listaCasos)
        LoadDataCaso(self)    
        self.listaCasos.SetFocus()     
def ajustesSE(self, activar):
    "ajustes para secretaria ejecutiva"
    if activar:
        for ctrlName in ['staticText77',
                        'FCproyecto_se',
                        'staticText102',
                        'FPproyecto_se']:
            ctrl = getattr(self, ctrlName)
            ctrl.Show()
            


def EscondeCtrlFecha(ctrlList):
    for ctrls in ctrlList:
        for ctrl in ctrls:
            ctrl.Show(False)
        
def LimpiaTodosLosCamposCaso(self):
                status.casoActual=None
                status.actoActual=None
                status.intervencionActual=None
                status.fuenteActual=None
                status.involActual=None
                
                status.pubActual=None
                
                
                for entidad in ['caso','acto','casoRel','involucramiento',\
                                'fuentePersonal','fuenteDocumental',\
                                'intervenciones']:
                    LimpiaCampos(self, camposEntidad[entidad])
                    if entidad in boxEntidad:
                        LimpiaCampos(self, boxEntidad[entidad])


def muestraControlesRelevancia(self, mostrar=False):
    controlesRelevancia = [self.chkRelevante,
self.txtStatusC3,
self.staticText112,
self.staticText113,
self.txtStatusC3P,
self.chkRelevanteP]
    for ctrl in controlesRelevancia:
        ctrl.Show(mostrar)
                
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
