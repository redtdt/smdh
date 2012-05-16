#-----------------------------------------------------------------------------
# Name:        midataset.py
#
#
# RCS-ID:      $Id: midataset.py $
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
import cnf
if __name__ == '__main__':
    cnf.user='admin'
    cnf.passwd='redtdt'

from module2 import *
from sqlalchemy.sql import func
#global MiDatasets
#MiDataset = None


session = status.session

def GeneraQueryCaso(listaEntidad, id=True, counter=False, Entidad=Caso):
    
    global MiDataset
    def Asigna(j, incluidos):
        global MiDataset
        
        if (j not in incluidos) or (j in ['AE']):
            dep = j[:-1]
            if dep: Asigna(dep, incluidos)
            
            if j == 'A':
                MiDataset = MiDataset.outerjoin(Caso.actos)
            if j == 'AA':
                MiDataset = MiDataset.outerjoin(Acto.RolPerpetradores) # rolperpet
                
            if j == 'AAA':
                MiDataset = MiDataset.outerjoin((PerPerpetrador, Involucramiento.persona)) # rolperpet
            if j == 'AAAA':
                MiDataset = MiDataset.outerjoin((TesPerpSexo,PerPerpetrador.Psexo))    
            if j == 'AAAB':
                MiDataset = MiDataset.outerjoin((TesPerpOcupacion,PerPerpetrador.Pocupacion))
            if j == 'AAAC':
                MiDataset = MiDataset.outerjoin((PersonaTipificacionPerpEtnico, PerPerpetrador.Ptipificacion))
                MiDataset = MiDataset.outerjoin((TesPerpEtnico,PersonaTipificacionPerpEtnico.PTesauro))
            if j == 'AAB':
                MiDataset = MiDataset.outerjoin((TesTipoPerpetrador, Involucramiento.Ptipoperpetrador)) # tipo perpet    
            if j == 'AAC':
                MiDataset = MiDataset.outerjoin((LoginfoInvol, Involucramiento.PLoginfo))
                
            
            if j == 'AB':
                MiDataset = MiDataset.outerjoin((TesTipodeacto, Acto.PTipodeacto))
            if j == 'AC':
                MiDataset = MiDataset.outerjoin((TesTipodelugar, Acto.PTipodelugar))
            if j == 'AD':
                MiDataset = MiDataset.outerjoin((PerVictima, Acto.Pvictima)) #pers
            if j == 'ADA':
                MiDataset = MiDataset.outerjoin((TesVicSexo, PerVictima.Psexo))    
            if j == 'ADB':
                MiDataset = MiDataset.outerjoin((TesVicOcupacion,PerVictima.Pocupacion))
            if j == 'ADC':
                MiDataset = MiDataset.outerjoin((PersonaTipificacionVicEtnico, PerVictima.Ptipificacion))
                MiDataset = MiDataset.outerjoin((TesVicEtnico,PersonaTipificacionVicEtnico.PTesauro))
                
                
                
                
                
            if j == 'AE':
                MiDataset = MiDataset.outerjoin(Acto.PCaracRelevantes) #pers
            if j == 'AEA':
                MiDataset = MiDataset.outerjoin((TesCaracRelevante,Caracrelevantes.Pcaracteristicarelevante)) #carac. relevante T23
            
                
                
                
                
            if j == 'AF':
                MiDataset = MiDataset.outerjoin((LoginfoActo, Acto.PLoginfo)) 
            
            
            
            
            
            
            if j == 'E':
                MiDataset = MiDataset.outerjoin((EventoTipificacionDerechosAfectados, Caso.derechosafectados)) #derechos afectados
            if j == 'EA':
                MiDataset = MiDataset.outerjoin((TesDerechoAfectado,EventoTipificacionDerechosAfectados.tipificacion)) #derechos afectados
            
            if j == 'F':
                MiDataset = MiDataset.outerjoin((EventoTipificacionTemas, Caso.temas)) #temas
            if j == 'FA':
                MiDataset = MiDataset.outerjoin((TesTema,EventoTipificacionTemas.tipificacion)) #temas
            if j == 'G':
                MiDataset = MiDataset.outerjoin(Caso.localidades)
            if j == 'GA':
                MiDataset = MiDataset.outerjoin((TesPais, Localidad.Pais)) #tes
            if j == 'GB':
                MiDataset = MiDataset.outerjoin((TesEstado, Localidad.Estado)) #tes
            if j == 'GC':
                MiDataset = MiDataset.outerjoin((TesMunicipio, Localidad.Municipio)) #tes
            if j == 'H':
                MiDataset = MiDataset.outerjoin(Caso.PPublicaciones)
            if j == 'HA':
                MiDataset = MiDataset.outerjoin((PerPersonareferenciada, Publicacion.PPersonareferenciada)) #pers
            if j == 'HB':
                MiDataset = MiDataset.outerjoin((TesTipopublicacion, Publicacion.PTipopublicacion)) #tes
            if j == 'HC':
                MiDataset = MiDataset.outerjoin((TesPubIdioma, Publicacion.PIdioma)) #tes
            if j == 'HD':
                MiDataset = MiDataset.outerjoin((TesPubLengua_indigena, Publicacion.PLengua_indigena)) #tes
            if j == 'HE':
                MiDataset = MiDataset.outerjoin((TesPubConfiabilidad, Publicacion.PConfiabilidad)) #tes
            if j == 'HF':
                MiDataset = MiDataset.outerjoin((LoginfoPub, Publicacion.PLoginfo))
            if j == 'I':
                MiDataset = MiDataset.outerjoin(Caso.intervenciones)
            if j == 'IA':    
                MiDataset = MiDataset.outerjoin((PerSolicitante,Intervencion.solicitante)) #pers
            if j == 'IB':        
                MiDataset = MiDataset.outerjoin((PerContraparte, Intervencion.contraparte)) #pers
            if j == 'IC':    
                MiDataset = MiDataset.outerjoin((PerInterviniente, Intervencion.Pinterviniente)) #pers
            if j == 'ID':    
                MiDataset = MiDataset.outerjoin((TesIntervTipo, Intervencion.tipo)) #tes
            if j == 'IE':    
                MiDataset = MiDataset.outerjoin((TesIntervEstatus, Intervencion.Pestatus)) #tes
            if j == 'IF':
                MiDataset = MiDataset.outerjoin((LoginfoIntervencion, Intervencion.PLoginfo))
            if j == 'J':    
                MiDataset = MiDataset.outerjoin(Caso.fuentes)
            if j == 'JA':    
                MiDataset = MiDataset.outerjoin((PerFuenPersona, Fuente.PPersona)) #pers
            if j == 'JB':    
                MiDataset = MiDataset.outerjoin((PerPersona_como_fuente, Fuente.PPersona_como_fuente)) #pers
            if j == 'JC':    
                MiDataset = MiDataset.outerjoin((TesConexion_info, Fuente.PConexion_info)) #tes
            if j == 'JD':    
                MiDataset = MiDataset.outerjoin((TesFuenLengua_indigena, Fuente.PLengua_indigena)) #tes
            if j == 'JE':    
                
                MiDataset = MiDataset.outerjoin((TesFuenConfiabilidad, Fuente.PConfiabilidad)) #tes
            if j == 'JF':
                MiDataset = MiDataset.outerjoin((LoginfoFuente, Fuente.PLoginfo))
            if j == 'K':    
                MiDataset = MiDataset.outerjoin((LoginfoCaso, Caso.PLoginfo))
            if j == 'L':
                MiDataset = MiDataset.outerjoin((EventoTipificacionLegisNac, Caso.PLegisNac)) #legislacion nacional
            
            if j == 'M':
                MiDataset = MiDataset.outerjoin((EventoTipificacionInstInt, Caso.PLegisInt)) #instrumentos internacionales
            
            if j == 'O':
                MiDataset = MiDataset.outerjoin((EventoTipificacionNormatividadActo, Caso.Pactonormatividad))
            if j == 'OA':
                MiDataset = MiDataset.outerjoin((LoginfoEvTip, EventoTipificacionNormatividadActo.PLoginfo)) #loginfo de EventoTipificacion en acto  
            if j == 'V':
                MiDataset = MiDataset.outerjoin(Caso.Pvinculos)
            if j == 'V1':
                MiDataset = MiDataset.outerjoin((LoginfoCasoVinculo, Caso_vinculo.PLoginfo  ))     
            if j == 'V2':
                MiDataset = MiDataset.outerjoin((TesRelacionCasos,   Caso_vinculo.Ptipo ))            
            incluidos.add(j)
    #main!
    
    EntidadId = getattr(Entidad,"id")  
        
    if id: 
        MiDataset = session.query(EntidadId)
    elif counter: 
        MiDataset = session.query(func.count(EntidadId))
    else: 
        MiDataset = session.query(Entidad)
    
    incluidos = set()
    for j in listaEntidad:
        Asigna(j, incluidos)
    if id:
        MiDataset = MiDataset.filter(EntidadId > 0)
    print >>status.log, "MiDataset 1 ",MiDataset
    return MiDataset
        


def GeneraQueryPersona(listaEntidad, id=True, counter=False, Entidad=Persona):
    
    global MiDataset
    def Asigna(j, incluidos):
        global MiDataset
        
        if j not in incluidos:
            dep = j[:-1]
            if dep: Asigna(dep, incluidos)
            
            if j == 'P':
                MiDataset = MiDataset.outerjoin((TesPerPais, Persona.Ppais_nac_u_origen))
            if j == 'E':
                MiDataset = MiDataset.outerjoin((TesPerEstado, Persona.Pestado_nac_u_origen))
            if j == 'M':
                MiDataset = MiDataset.outerjoin((TesPerMpo, Persona.Pmpio_nac_u_origen))
            if j == 'C':
                MiDataset = MiDataset.outerjoin((TesPerCiudadania, Persona.Pciudadania_o_sede))    
            if j == '0':
                MiDataset = MiDataset.outerjoin((TesPerEscolaridad, Persona.Pescolaridad))    
            if j == '1':
                MiDataset = MiDataset.outerjoin((TesPerOcupacion, Persona.Pocupacion))  
            
            if j == '3':
                MiDataset = MiDataset.outerjoin((TesPerEstadoCivil, Persona.Pestado_civil)) 
            if j == '4':
                MiDataset = MiDataset.outerjoin((TesPerConfiabilidad, Persona.Pconfiabilidad))    
            if j == '5':
                MiDataset = MiDataset.outerjoin((TesPerMonitoreo, Persona.Pmonitoreo))          
            if j == 'S':
                MiDataset = MiDataset.outerjoin((TesPerSexo, Persona.Psexo))
            if j == 'R':
                MiDataset = MiDataset.outerjoin((TesPerReligion, Persona.Preligion))
            if j == 'G':
                MiDataset = MiDataset.outerjoin((TesPerTipoGrupo, Persona.Ptipo))
            if j == 'T':
                #MiDataset = MiDataset.outerjoin((PersonaTipificacionIdioma , Persona.Ptipificacion))
                MiDataset = MiDataset.outerjoin((PersonaTipificacionIdioma , Persona.PIdiomas))
            if j == 'T1':
                MiDataset = MiDataset.outerjoin((TesPerIdioma, PersonaTipificacionIdioma.PTesauro)) 
            if j == 'Q':
                #MiDataset = MiDataset.outerjoin((PersonaTipificacionLengua , Persona.Ptipificacion))   
                MiDataset = MiDataset.outerjoin((PersonaTipificacionLengua , Persona.PLenguas))   
            if j == 'Q1':
                MiDataset = MiDataset.outerjoin((TesPerLengua, PersonaTipificacionLengua.PTesauro))
            if j == 'U':
                #MiDataset = MiDataset.outerjoin((PersonaTipificacionTipoGrupo, Persona.Ptipificacion))   
                MiDataset = MiDataset.outerjoin((PersonaTipificacionTipoGrupo, Persona.POrigenEtnico))   
            if j == 'U1':
                MiDataset = MiDataset.outerjoin((TesPerTipoGrupo, PersonaTipificacionTipoGrupo.PTesauro))
            if j== "D":
                #MiDataset = MiDataset.outerjoin((DetalleBiografico, Persona.Pdetallesbiograficos))
                MiDataset = MiDataset.outerjoin((DetalleBiografico, Persona.Pdetallesyvinculosbiograficos))
            if j=="D1":
                MiDataset = MiDataset.outerjoin((LoginfoDatoBio, DetalleBiografico.PLoginfo))
            if j=="D2":
                MiDataset = MiDataset.outerjoin((TesTipoVinculo, DetalleBiografico.tipo))
            if j == 'K':    
                MiDataset = MiDataset.outerjoin((LoginfoPersona, Persona.PLoginfo))
            if j == 'V':
                MiDataset = MiDataset.outerjoin(Persona.Ptipificacion)   
            
                    
            incluidos.add(j)
            
    #main!
    EntidadId = getattr(Entidad,"id")        
    if id: 
        MiDataset = session.query(EntidadId)
    elif counter: 
        MiDataset = session.query(func.count(EntidadId))
    else: 
        MiDataset = session.query(Entidad)
    incluidos = set()
    for j in listaEntidad:
        Asigna(j, incluidos)
    if id:
        MiDataset = MiDataset.filter(EntidadId > 0)
    return MiDataset





if __name__ == '__main__':

    
    
    
    
    
    aMiDataset = GeneraQueryCaso( ['AA'], Entidad=Acto )

    
    #aMiDataset = aMiDataset.add_entity(TesDerechoAfectado).add_entity(Caso).add_entity(TesEstado).order_by(TesDerechoAfectado.id)
    print aMiDataset
    
    r= aMiDataset.all()
    print len(r)
    print r
    #for i in range(L):
    #    print aMiDataset[i]

