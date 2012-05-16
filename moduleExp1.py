#-----------------------------------------------------------------------------
# Name:        moduleExp1.py
#
#
# RCS-ID:      $Id: moduleExp1.py $
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
if __name__ == '__main__':
    import cnf
    cnf.user='admin'
    cnf.passwd='redtdt'


import codecs


from module2 import *
from xml.dom.minidom import Document
from camposexp import camposExp
import os
diagnostico=[]
diagnosticos={}
exportandoCasos=False
exportandoPersonas=False
# se hace True cuando se desea que la funcion SesID convierta id's de status 2 a status 1, a efectos de comparacion
SWid=False
exportando=False

abortar=False


def GeneraEnvio(gruponombre, grupoclave,  hashcode, coleccionCasos, coleccionPersonas):
    """ genera el envio en xml de casos y personas para un grupo determinado por su clave validado
    por su codigo de hash. Coleccion de casos y personas son conjuntos de objetos a enviar"""
    global exportandoCasos
    global exportandoPersonas
    if SWid:
        try:
            camposExp['Acto'][0].remove('localizacion_id')
        except:
            nada=0
    
    envio=Document()
    
    elemento=envio.createElement("Envio")
    
    # datos del grupo
    elementoGrupo=DatosGrupo(envio, gruponombre, grupoclave,  hashcode)
    elemento.appendChild(elementoGrupo)
    
    #personas
    
    exportandoPersonas=True
    estaColeccion=ExportaColeccionPersonas(envio, coleccionPersonas)
    exportandoPersonas=False
    elemento.appendChild(estaColeccion)
    
    #casos
    
    exportandoCasos=True
    estaColeccion=ExportaColeccionCasos(envio, coleccionCasos)
    elemento.appendChild(estaColeccion)
    exportandoCasos=False
    
    envio.appendChild(elemento)
    
    return envio

def DatosGrupo(doc, gruponombre, grupoclave,  hashcode):
    Grupo=doc.createElement("Grupo")
    elemento=doc.createElement("Nombre")
    mitexto=doc.createTextNode(gruponombre.encode( "utf-8" ))
    
    

    
    
    elemento.appendChild(mitexto)
    Grupo.appendChild(elemento)
    
    elemento=doc.createElement("Clave")
    mitexto=doc.createTextNode(str(grupoclave))
    elemento.appendChild(mitexto)
    Grupo.appendChild(elemento)
    elemento=doc.createElement("Hash")
    mitexto=doc.createTextNode(hashcode.encode( "utf-8" ))
    elemento.appendChild(mitexto)
    Grupo.appendChild(elemento)
    return Grupo
    
def ExportaColeccionCasos(doc, coleccion):
    global abortar
    elemento=doc.createElement("ColeccionCasos")
    coleccion.sort(compID)
    
    for c in coleccion:
        abortar=False
        session.refresh(c)
        esteCaso=ExportaCaso(doc, c)
        if esteCaso:
            elemento.appendChild(esteCaso)
        else:
            print "el caso ",c," no fue exportado"
    return elemento

def ExportaColeccionPersonas(doc, coleccion):
    
    elemento=doc.createElement("ColeccionPersonas")
    coleccion.sort(compID)
    for p in coleccion:
        session.refresh(p)
        estaPersona=ExportaPersona(doc, p)
        if estaPersona:
            elemento.appendChild(estaPersona)
            
    
    return elemento
def ajustaID(valor):
    if valor:
        return valor[:-4]+'1'+valor[-3:]
def SetID(elemento, obj, valor=None):
    if not valor:
        valor = str(getattr(obj, 'id'))
    else:
        valor = str(valor)
    if SWid:
        valor=ajustaID(valor)
    elemento.setAttribute('id',valor)
    if hasattr(obj, 'Descriptor'):
        desc = obj.Descriptor()
        desc = desc.encode( "utf-8" )
        if desc:
            elemento.setAttribute('descriptor',desc)
    
def seExporta(miObj):
    if miObj:
        if hasattr(miObj, 'exportar'):
            valor = getattr(miObj,'exportar')
            return valor == 1
        else:
            return True
    else:
        return False
    
 
def reportaObjeto(historia, obj, tipoObj='C', mensaje='', severidad=2):
    
    global exportandoCasos
    global exportandoPersonas
    #if exportandoCasos:
    #        diagnostico.append(u"Diagn\xf3stico de casos:\n")
    #        exportandoCasos=False
            
    #if exportandoPersonas:
    #        diagnostico.append(u"Diagn\xf3stico de Personas:\n")
    #        exportandoPersonas=False
            
    tipoDeError = u"ERROR" if severidad == 2 else u"ADVERTENCIA"
    
    elMensaje= mensaje if mensaje else obj.noValido()
    tipo = type(obj)
    strTipo = objetoDescrip[tipo] if tipo in objetoDescrip.keys() else ''
    descripcion=strTipo+" ["+str(obj.id)+"] "+obj.Descriptor()
    #print "descrip","["+str(obj.id)+"] "+mensaje
    texto = tipoDeError+u'\n'+'\n'.join(historia)+'\n'+descripcion+"\n"+elMensaje
    #texto = '\n'.join(historia)+'\n'+descripcion+"\n"+elMensaje
    diagnostico.append(texto)
    diagnosticos[tipoObj][severidad].append(texto)
def ExportaCaso(doc, miCaso):
    global abortar
    if not seExporta(miCaso): return None
    
    if miCaso.noValido() and exportando:
        

        reportaObjeto([], miCaso)
        return None
    elemento=doc.createElement("Caso")
    SetID(elemento, miCaso)
    # campos normales
    for campo in camposExp['Caso'][0]:
        micampo = ExportaCampoSimple(doc, miCaso, campo)
        if micampo:
            elemento.appendChild(micampo)
    # campos tesauro        
    for campo in camposExp['Caso'][1]:
        # ['monitoreo', 'tipo_fecha_inicio', 'tipo_fecha_final', 'tipo_frecepcion']:
        micampo = ExportaCampoTesauro(doc, miCaso, campo)
        if micampo:
            elemento.appendChild(micampo)
    # loginfo
    micampo = ExportaLoginfo(doc, miCaso)
    if micampo:
            elemento.appendChild(micampo)
    # derechos afectados        
    micampo = ExportaColeccion(doc, miCaso, miCaso.derechosafectados, 'DerechosAfectados', ExportaEventoTipificacion, historia=[miCaso.tipoDescriptor()])
    if micampo:
        elemento.appendChild(micampo)
    # temas    
    micampo = ExportaColeccion(doc, miCaso, miCaso.temas, 'Temas', ExportaEventoTipificacion, historia=[miCaso.tipoDescriptor()]) 
    if micampo:
        elemento.appendChild(micampo)   
    # localidades
    micampo = ExportaColeccion(doc, miCaso, miCaso.localidades, 'Localidades', ExportaLocalidad, historia=[miCaso.tipoDescriptor()])
    if micampo:
        elemento.appendChild(micampo)  
        
    # actos
    micampo = ExportaColeccion(doc, miCaso, miCaso.actos, 'Actos', ExportaActo, historia=[miCaso.tipoDescriptor()])
    if micampo:
        elemento.appendChild(micampo) 
    # intervenciones    
    micampo = ExportaColeccion(doc, miCaso, miCaso.intervenciones, 'Intervenciones', ExportaIntervencion, historia=[miCaso.tipoDescriptor()])
    if micampo:
        elemento.appendChild(micampo) 
    # publicaciones
    micampo = ExportaColeccion(doc, miCaso, miCaso.PPublicaciones, 'Publicaciones', ExportaPublicacion, historia=[miCaso.tipoDescriptor()])
    if micampo:
        elemento.appendChild(micampo)     
    # fuentes personales
    micampo = ExportaColeccion(doc, miCaso, miCaso.fuentes, 'FuentesPersonales', ExportaFuentePersonal, historia=[miCaso.tipoDescriptor()])
    if micampo:
        elemento.appendChild(micampo)     
    # relaciones con otros casos
    micampo = ExportaColeccion(doc, miCaso, miCaso.Pvinculos, 'CasosRelacionados', ExportaRefCaso, historia=[miCaso.tipoDescriptor()])
    if micampo:
        elemento.appendChild(micampo)     
        
    if abortar:
        return None
    return elemento
def ExportaCampoSimple(doc, obj, campo, valorLocal=None):
    if valorLocal:
        valor = valorLocal
    else:
        valor=getattr(obj, campo)
    
        
    if ((not valor) and (type(valor) != int)):
        valor=''
    #if valor:
    if type(valor)==unicode:
        valor = valor.encode( "utf-8" )
    texto=str(valor)
    
    micampo=doc.createElement(campo)
    mitexto=doc.createTextNode(texto)
    micampo.appendChild(mitexto)
    
    return micampo
    #else:
    #    return None
def ExportaCampoTesauro(doc, obj, campo):
    
    valor=getattr(obj, campo)
    if not seExporta(obj): valor=''
    #if not valor: return None
    if valor:
        ID = int(valor)
    else:
        ID = 0
    micampo=doc.createElement(campo)
    micampo.setAttribute('REFID',str(valor))
    
    
    micampoDesc = doc.createElement('desc')
    if ID:
        t = TesNombre(ID)
    else:
        t = ''
    mitextoDesc=doc.createTextNode(t.encode( "utf-8" ))
    micampoDesc.appendChild(mitextoDesc)
    micampo.appendChild(mitextoDesc)
    #micampo.appendChild(micampoDesc)
    
    return micampo
def compID(a,b):
    
    return a.id - b.id

def ExportaColeccion(doc, obj, coleccion, coleccionTag, funcion, historia=[]):
    elemento = doc.createElement(coleccionTag)
    if coleccion:
        
        coleccion.sort(compID)
        for T in coleccion:
            
            elemento2 = funcion(doc, T, historia=historia)
            if elemento2:
                elemento.appendChild(elemento2)
    return elemento
    
def ExportaRefCaso(doc, obj, historia=[]):
    if not seExporta(obj): return None
    if obj.noValido() and exportando:
        reportaObjeto(historia, obj)
        return None
    
    (severidad, mensaje) = obj.noExportable()
    
    if exportando and severidad:
        print "relacion de caso no exportada"
        reportaObjeto(historia, obj, mensaje=mensaje, severidad=severidad)
        
        return None
    
    
    
    
    elemento = doc.createElement("RefCaso")
    SetID(elemento, obj)
    if obj:
        for campo in camposExp['RefCaso'][0]:
            micampo = ExportaCampoSimple(doc, obj, campo)
            if micampo:
                elemento.appendChild(micampo)
        for campo in camposExp['RefCaso'][1]:
            micampo = ExportaCampoTesauro(doc, obj, campo)
            if micampo:
                elemento.appendChild(micampo)
        casoRef = doc.createElement("CasoRelacionado")
        valor=str(obj.Pcaso_2.id)
        if SWid:
            valor = ajustaID(valor)
            
        
        casoRef.setAttribute('REFID',valor)
        #id = ExportaCampoSimple(doc, obj, 'id', valorLocal=obj.Pcaso_2.id)
        descriptor = ExportaCampoSimple(doc, obj, "Caso", valorLocal=obj.Pcaso_2.descripcion)
        #casoRef.appendChild(id)
        casoRef.appendChild(descriptor)
        elemento.appendChild(casoRef)
        
        micampo = ExportaLoginfo(doc, obj)
        if micampo:
            elemento.appendChild(micampo)
        
            
        return elemento

def ExportaRefPersona(doc, P, rol, historia=[]):
    diag = None
    if not seExporta(P):
         diag = "NE", P.Descriptor() if P else ''
         return (None, diag)
    diag =P.noValido()
    if diag:
        diag = diag,  P.Descriptor() if P else ''
        
        #print "**** referencia no exportable", P.Descriptor().encode('ascii', 'replace'), diag.encode('ascii', 'replace')
        
        return (None, diag)
    session.refresh(P)

    if P:
        elemento = doc.createElement(rol)
        valor = str(P.id)
        if SWid:
            valor = ajustaID(valor)
        elemento.setAttribute('REFID',valor)
        e = ExportaCampoSimple(doc, P, 'Nombre_de_la_persona', valorLocal=P.Descriptor())
        if e: elemento.appendChild(e)
        
        return (elemento, diag)
    else:
        return (None, diag)

def ExportaEventoTipificacion(doc, obj, historia=[]):
    if not seExporta(obj): return None
    if obj.noValido() and exportando:
        reportaObjeto(historia, obj)
        return None
    session.refresh(obj)
    elemento = doc.createElement("Tipificacion")
    SetID(elemento, obj)
    for field in ['notas']:
        e= ExportaCampoSimple(doc, obj, field)
        if e: elemento.appendChild(e)
    e=ExportaLoginfo(doc, obj)
    if e: elemento.appendChild(e)
    e=ExportaCampoTesauro(doc, obj, 'tesauro_id')
    if e: elemento.appendChild(e)
    return elemento
    
def ExportaLoginfo(doc, obj, historia=[]):
    loginfo = obj.PLoginfo
    if not loginfo: return None
    elemento = doc.createElement('loginfo')
    SetID(elemento, loginfo)
    #mitextoId=doc.createTextNode(str(loginfo.id))
    #elementoId=doc.createElement('id')
    #elementoId.appendChild(mitextoId)
    #elemento.appendChild(elementoId)
    
    fc=ExportaCampoSimple(doc, loginfo, 'fechaCreacion')
    elemento.appendChild(fc)
    fa=ExportaCampoSimple(doc, loginfo, 'fechaActualizacion')
    elemento.appendChild(fa)
    
    if loginfo.Creador:
        elementoUserC = doc.createElement('userCreacion')
        #elementoUserCid = doc.createElement('id')
        elementoUserCnom = doc.createElement('nombre')
        #elementoUserCidText = doc.createTextNode(str(loginfo.userCreacion))
        #elementoUserCid.appendChild(elementoUserCidText)
        nombreC = loginfo.Creador.nombre.encode( "utf-8" )
        elementoUserCnomText = doc.createTextNode(str(nombreC))
        elementoUserCnom.appendChild(elementoUserCnomText)
        #elementoUserC.appendChild(elementoUserCid)
        
        elementoUserC.setAttribute('REFID',str(loginfo.userCreacion))
        
        elementoUserC.appendChild(elementoUserCnom)
        elemento.appendChild(elementoUserC)
    
    if loginfo.Actualizador:
        elementoUserA = doc.createElement('userActualizacion')
        #elementoUserAid = doc.createElement('id')
        elementoUserAnom = doc.createElement('nombre')
        #elementoUserAidText = doc.createTextNode(str(loginfo.userActualizacion))
        #elementoUserAid.appendChild(elementoUserAidText)
        nombreA = loginfo.Actualizador.nombre.encode( "utf-8" )
        elementoUserAnomText = doc.createTextNode(str(nombreA))
        elementoUserAnom.appendChild(elementoUserAnomText)
        #elementoUserA.appendChild(elementoUserAid)
        elementoUserA.setAttribute('REFID',str(loginfo.userActualizacion))
        elementoUserA.appendChild(elementoUserAnom)
        elemento.appendChild(elementoUserA)
    
    return elemento
def ExportaTesauros(doc, obj, listadecampos, historia=[]):
    lista = []
    for field in listadecampos:
        e= ExportaCampoTesauro(doc, obj, field)
        if e:
            lista.append(e)
    return lista
def ExportaLocalidad(doc, obj, historia=[]):
    if not seExporta(obj): return None
    if obj.noValido() and exportando:
        reportaObjeto(historia, obj)
        return None
    session.refresh(obj)
    elemento=doc.createElement("Localidad")
    SetID(elemento, obj)
    for campo in camposExp["Localidad"][0]:
        micampo = ExportaCampoSimple(doc, obj, campo)
        if micampo:
            elemento.appendChild(micampo)
    miscampos = ExportaTesauros(doc, obj, camposExp["Localidad"][1])
    for micampo in miscampos:
        elemento.appendChild(micampo)
    micampo = ExportaLoginfo(doc, obj)
    if micampo:
            elemento.appendChild(micampo)
    return elemento
def ExportaActo(doc, obj, historia=[]):
    global abortar
    if not seExporta(obj): return None
    if obj.noValido() and exportando:
        reportaObjeto(historia, obj)
        return None
    (severidad, mensaje) = obj.noExportable()
    abortar = severidad > 1
    if exportando and severidad:
        reportaObjeto(historia, obj, mensaje=mensaje)
        return None
        
    session.refresh(obj)

    
    elemento=doc.createElement("Acto")
    SetID(elemento, obj)
    for campo in camposExp["Acto"][0]:
        micampo = ExportaCampoSimple(doc, obj, campo)
        if micampo:
            elemento.appendChild(micampo)
        else: print "no se exporto ",campo
    if SWid:
        valor=getattr(obj, 'localizacion_id')
        
        if valor: valor = ajustaID(str(valor))
        micampo = ExportaCampoSimple(doc, obj, 'localizacion_id', valorLocal=valor)
        if micampo:
            elemento.appendChild(micampo)
        
        
    
            
    miscampos = ExportaTesauros(doc, obj, camposExp["Acto"][1])
    for micampo in miscampos:
        elemento.appendChild(micampo)
    # tipificaciones actos (legislacion + instrumentos
    if  obj.exportarnormatividad == 1:
        codigo = 2154
        tipificaciones = [i for i in obj.caso.tipificaciones if i.codigo == codigo and i.acto_id == obj.id]
        micampo = ExportaColeccion(doc, obj, tipificaciones, 'LegislacionNacional', ExportaEventoTipificacion, historia=historia+[obj.tipoDescriptor()])
        if micampo:
            elemento.appendChild(micampo)  
        codigo = 2155
        tipificaciones = [i for i in obj.caso.tipificaciones if i.codigo == codigo and i.acto_id == obj.id]
        micampo = ExportaColeccion(doc, obj, tipificaciones, 'InstrumentosInternacionales', ExportaEventoTipificacion, historia=historia+[obj.tipoDescriptor()])
        if micampo:
            elemento.appendChild(micampo)  
    (micampo, diag) = ExportaRefPersona(doc, obj.Pvictima, 'Victima')
    if micampo:
        elemento.appendChild(micampo)    
    
            
    micampo = ExportaColeccion(doc, obj, obj.PCaracRelevantes, 'CaracteristicasRelevantes', ExportaCaracRelevante, historia=historia+[obj.tipoDescriptor()])
    if micampo:
        elemento.appendChild(micampo)
        
    micampo = ExportaColeccion(doc, obj, obj.RolPerpetradores, 'Perpetradores', ExportaInvolucramiento, historia=historia+[obj.tipoDescriptor()])
    if micampo:
        elemento.appendChild(micampo)  
        
    micampo = ExportaLoginfo(doc, obj)
    if micampo:
            elemento.appendChild(micampo)  
    
    return elemento
    
def ExportaInvolucramiento(doc, obj, historia=[]):
    global abortar
    if not seExporta(obj): return None
    if obj.noValido() and exportando:
        reportaObjeto(historia, obj)
        return None
    (severidad, mensaje) = obj.noExportable()
    abortar = severidad > 1
    if exportando and severidad:
        reportaObjeto(historia, obj, mensaje=mensaje)
        return None
    
    session.refresh(obj)
    elemento=doc.createElement("Involucramiento")
    SetID(elemento, obj)
    for campo in camposExp["Involucramiento"][0]:
        micampo = ExportaCampoSimple(doc, obj, campo)
        if micampo:
            elemento.appendChild(micampo)
    miscampos = ExportaTesauros(doc, obj, camposExp["Involucramiento"][1])
    for micampo in miscampos:
        elemento.appendChild(micampo)
    
   
    (micampo, diag) = ExportaRefPersona(doc, obj.persona, 'persona_id')
    if micampo:
        elemento.appendChild(micampo)    
    
    
    micampo = ExportaLoginfo(doc, obj)
    if micampo:
            elemento.appendChild(micampo)
    return elemento

def ExportaIntervencion(doc, obj, historia=[]):
    if not seExporta(obj): return None
    if obj.noValido() and exportando:
        reportaObjeto(historia, obj)
        return None
    
    
    (severidad, mensaje) = obj.noExportable()
    abortar = severidad > 1
    if exportando and severidad:
        reportaObjeto(historia, obj, mensaje=mensaje)
        return None
    
    session.refresh(obj)
    elemento=doc.createElement("Intervencion")
    SetID(elemento, obj)
    for campo in camposExp["Intervencion"][0]:
        micampo = ExportaCampoSimple(doc, obj, campo)
        if micampo:
            elemento.appendChild(micampo)
    miscampos = ExportaTesauros(doc, obj, camposExp["Intervencion"][1])
    for micampo in miscampos:
        elemento.appendChild(micampo)
    
    (micampo, diag) = ExportaRefPersona(doc, obj.solicitante, 'solicitante')
    if micampo:
        elemento.appendChild(micampo)    
    (micampo, diag) = ExportaRefPersona(doc, obj.contraparte, 'contraparte')
    if micampo:
        elemento.appendChild(micampo)   
    (micampo, diag) = ExportaRefPersona(doc, obj.Pinterviniente, 'Pinterviniente')
    if micampo:
        elemento.appendChild(micampo)    
    micampo = ExportaLoginfo(doc, obj)
    if micampo:
            elemento.appendChild(micampo)
    
                
    return elemento
def ExportaPublicacion(doc, obj, historia=[]):
    if not seExporta(obj): return None
    if obj.noValido() and exportando:
        reportaObjeto(historia, obj)
        return None
    session.refresh(obj)
    elemento=doc.createElement("Publicacion")
    
    SetID(elemento, obj)
    for campo in camposExp["Publicacion"][0]:
        micampo = ExportaCampoSimple(doc, obj, campo)
        if micampo:
            elemento.appendChild(micampo)
            
            
    miscampos = ExportaTesauros(doc, obj, camposExp["Publicacion"][1])
    for micampo in miscampos:
        elemento.appendChild(micampo)
    (micampo, diag) = ExportaRefPersona(doc, obj.PPersonareferenciada, 'PersonaReferenciada')
    if micampo:
        elemento.appendChild(micampo)    
    
    micampo = ExportaLoginfo(doc, obj)
    if micampo:
            elemento.appendChild(micampo)
    
                
    return elemento

def ExportaFuentePersonal(doc, obj, historia=[]):
    if not seExporta(obj): return None
    if obj.noValido() and exportando:
        reportaObjeto(historia, obj)
        return None
    (severidad, mensaje) = obj.noExportable()
    abortar = severidad > 1
    if exportando and severidad:
        reportaObjeto(historia, obj, mensaje=mensaje)
        return None
    session.refresh(obj)
    elemento=doc.createElement("FuentePersonal")
    SetID(elemento, obj)
    
    for campo in camposExp["FuentePersonal"][0]:
        micampo = ExportaCampoSimple(doc, obj, campo)
        if micampo:
            elemento.appendChild(micampo)
            
            
    miscampos = ExportaTesauros(doc, obj, camposExp["FuentePersonal"][1])
    for micampo in miscampos:
        elemento.appendChild(micampo)
    (micampo, diag) = ExportaRefPersona(doc, obj.PPersona, 'PersonaReferenciada')
    if micampo:
        elemento.appendChild(micampo)   
    
    (micampo, diag) = ExportaRefPersona(doc, obj.PPersona_como_fuente, 'PersonaFuente')
    if micampo:
        elemento.appendChild(micampo)        
    
    micampo = ExportaLoginfo(doc, obj)
    if micampo:
            elemento.appendChild(micampo)
    
                
    return elemento

def ExportaPersona(doc, obj, historia=[]):
    if not seExporta(obj): return None
    if obj.noValido() and exportando:
        reportaObjeto(historia, obj, tipoObj="P")
        return None
    
    elemento=doc.createElement("Persona")
    SetID(elemento, obj)
    for campo in camposExp["Persona"][0]:

        micampo = ExportaCampoSimple(doc, obj, campo)
        if micampo:
            elemento.appendChild(micampo)
            
    miscampos = ExportaTesauros(doc, obj, camposExp["Persona"][1])
    
                                          
    for micampo in miscampos:
        elemento.appendChild(micampo)
    for cr in ["Idiomas", "Lenguas", "OrigenEtnico"]:
        col=getattr(obj, "P"+cr)
        micampo = ExportaColeccion(doc, obj, col, cr, ExportaPersonaTipificacion, historia=historia+[obj.tipoDescriptor()])
        if micampo:
            elemento.appendChild(micampo)
    micampo = ExportaColeccion(doc, obj, obj.PDirecciones, "Direcciones", ExportaPersonaDireccion, historia=historia+[obj.tipoDescriptor()])
    if micampo:
        elemento.appendChild(micampo)
        
    col = [i for i in obj.LaOtra2  if i.descripcion]
    micampo = ExportaColeccion(doc, obj, col, "DetallesBiograficos", ExportaDetalleBiografico, historia=historia+[obj.tipoDescriptor()])
    if micampo:
        elemento.appendChild(micampo)
        
    col = [i for i in obj.LaOtra2  if not i.descripcion]
    micampo = ExportaColeccion(doc, obj, col, "VinculosBiograficos", ExportaVinculoBiografico, historia=historia+[obj.tipoDescriptor()])
    if micampo:
        elemento.appendChild(micampo)
    
    micampo = ExportaLoginfo(doc, obj)
    if micampo:
            elemento.appendChild(micampo)
    return elemento

def ExportaCaracRelevante(doc, obj, historia=[]):
    if not seExporta(obj): return None
    if obj.noValido() and exportando:
        reportaObjeto(historia, obj)
        return None
    session.refresh(obj)
    if obj:
        elemento=doc.createElement("CaracteristicaRelevante")
        SetID(elemento, obj)
        
        elemento.appendChild(ExportaCampoTesauro(doc, obj, 'caracrelevantes_id'))
        micampo = ExportaLoginfo(doc, obj)
        if micampo:
            elemento.appendChild(micampo)

        return elemento
    else:
        return None

def ExportaPersonaTipificacion(doc, obj, historia=[]):
    
    if not seExporta(obj): return None
    if obj.noValido() and exportando:
        reportaObjeto(historia, obj, tipoObj="P")
        return None

    session.refresh(obj)
    if obj:
        elemento=doc.createElement("PersonaTipificacion")
        SetID(elemento, obj)
        
        elemento.appendChild(ExportaCampoTesauro(doc, obj, 'tesauro_id'))
        micampo = ExportaLoginfo(doc, obj)
        if micampo:
            elemento.appendChild(micampo)

        return elemento
    else:
        return None
def ExportaPersonaDireccion(doc, obj, historia=[]):
    if not seExporta(obj): return None
    if obj.noValido() and exportando:
        reportaObjeto(historia, obj, tipoObj="P")
        return None
    session.refresh(obj)
    if obj:
        elemento=doc.createElement("Direccion")
        SetID(elemento, obj)
        for campo in camposExp["Direccion"][0]:
            micampo = ExportaCampoSimple(doc, obj, campo)
            if micampo:
                elemento.appendChild(micampo)
                
        miscampos = ExportaTesauros(doc, obj, camposExp["Direccion"][1])
        for micampo in miscampos:
            elemento.appendChild(micampo)
        
        
        
        
        micampo = ExportaLoginfo(doc, obj)
        if micampo:
            elemento.appendChild(micampo)
        return elemento
    else:
        return None
def ExportaDetalleBiografico(doc, obj, historia=[]):
    if not seExporta(obj): return None
    if obj.noValido() and exportando:
        reportaObjeto(historia, obj, tipoObj="P")
        return None
    session.refresh(obj)
    if obj:
        elemento=doc.createElement("DetalleBiografico")    
        SetID(elemento, obj)
        for campo in camposExp["DetalleBiografico"][0]:
            micampo = ExportaCampoSimple(doc, obj, campo)
            if micampo:
                elemento.appendChild(micampo)
            
        miscampos = ExportaTesauros(doc, obj, camposExp["DetalleBiografico"][1])
        for micampo in miscampos:
            elemento.appendChild(micampo)     
        micampo = ExportaLoginfo(doc, obj)
        if micampo:
            elemento.appendChild(micampo) 
        
        return elemento    
def ExportaVinculoBiografico(doc, obj, historia=[]):
    if not seExporta(obj): return None
    if obj.noValido() and exportando:
        reportaObjeto(historia, obj, tipoObj="P")
        return None
    session.refresh(obj)
    if obj:
        elemento=doc.createElement("VinculoBiografico")    
        SetID(elemento, obj)
        for campo in camposExp["VinculoBiografico"][0]:
            micampo = ExportaCampoSimple(doc, obj, campo)
            if micampo:
                elemento.appendChild(micampo)
            
        miscampos = ExportaTesauros(doc, obj, camposExp["VinculoBiografico"][1])
        for micampo in miscampos:
            elemento.appendChild(micampo)  
        (micampo, diag) = ExportaRefPersona(doc, obj.vinculo2, "PersonaVinculada")
        if micampo:
               elemento.appendChild(micampo)
            
        micampo = ExportaLoginfo(doc, obj)
        if micampo:
            elemento.appendChild(micampo)
        return elemento    
def encripta(archivo):
    comando="c:\smdh2\utils\gpg.exe --homedir c:\smdh2\utils -e -r redtdt "+archivo

    os.system(comando)
    comando="del %s"%archivo
    os.system(comando)
    pass

def PreparaEnvio(NombreOrg,ClaveOrg,HashOrg):
        global diagnostico
        global diagnosticos
        diagnostico=[]
        diagnosticos={}
        for Itipo in ['P','C']:
            diagnosticos[Itipo]={}
            for Jseveridad in [1,2]:
                diagnosticos[Itipo][Jseveridad]=[]
        coleccionCasos = session.query(Caso).filter(Caso.id <'9999').all()
        coleccionPersonas = session.query(Persona).filter(Persona.id <'9999').all()
        

        x = GeneraEnvio(NombreOrg,ClaveOrg,HashOrg,coleccionCasos, coleccionPersonas)
        
        r = x.toxml()
        fecha=datetime.datetime.now()
    
        fecha = fecha.isoformat()[:16].replace(':','')
        org = "%04i"%ClaveOrg
        nombreArchivo = "c:\smdh2\export\smdhdata"+org+"-"+fecha
        nombreArchivoXML = nombreArchivo+'.xml'
        fileObj = file( nombreArchivoXML, "w" )
        fileObj.write(r)
        fileObj.close()
        encripta(nombreArchivoXML)
        if diagnosticos['C'][1]:
            diagnosticos['C'][1] = ["------Advertencias\n"]+diagnosticos['C'][1]
        if diagnosticos['P'][1]:
            diagnosticos['P'][1] = ["------Advertencias\n"]+diagnosticos['P'][1]
        if diagnosticos['C'][2]:
            diagnosticos['C'][2] = ["------Errores\n"]+diagnosticos['C'][2]
        if diagnosticos['P'][2]:
            diagnosticos['P'][2] = ["------Errores\n"]+diagnosticos['P'][2]
        tituloC=''
        tituloP=''
        
        if diagnosticos['C'][1] or diagnosticos['C'][2]:
            tituloC = "---Casos\n"
        if diagnosticos['P'][1] or diagnosticos['P'][2]:
            tituloP = "---Personas\n"    
        res =  [tituloC] + diagnosticos['C'][1] + diagnosticos['C'][2] + \
                       [tituloP] + diagnosticos['P'][1] + diagnosticos['P'][2]
        #return diagnostico, nombreArchivo
        return res, nombreArchivo

    
#if __name__ == '__main__':
    #diag, archivo = PreparaEnvio("SEjecutiva",33,'asdfgh')
    #print diagnostico, archivo
    

