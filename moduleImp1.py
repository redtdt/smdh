#-----------------------------------------------------------------------------
# Name:        moduleImp1.py
#
#
# RCS-ID:      $Id: moduleImp1.py $
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
import xml.dom.minidom

from codecs import encode
import re
nl=re.compile(r'(\r)')

#pendiente: 
# determinar los ID de cada entidad a importar y hacer un recuento de ID existentes.
# con eso borrar entidades que desaparecieron del set de entidades a importar


cloning = False




if __name__ == '__main__':
    import cnf
    cnf.user='admin'
    cnf.passwd='redtdt'

import module2

session = module2.session
Caso = module2.Caso
Persona = module2.Persona
User = module2.User
class obj1(object):
    pass
localstatus = obj1()
localstatus.overwo = True
localstatus.overwf = True
localstatus.usuarios = []

import datetime

from camposexp import camposExp


def reportaError(st):
    print "error **************", st
def get_a_document(name="someFile.xml"):
    return xml.dom.minidom.parse(name)

def columnType(name, table):
    tabla = table
    colType = tabla.columns[name].type
    r = str(colType)
    
    return r.split('(')[0]

def idCond(id, grupo, status):
    "ifCondensado: id -> id+status+grupo"
    if cloning:
       Sid=str(id)
       s=Sid[:-4]+str(status)+Sid[-3:] 
       return int(s)
    else:
       miId = id * 10000
       miStatus = status * 1000
       return miId + miStatus + grupo
   
def existePersona(id):
    if  (id in module2.status.idPersonas): return True
    q=session.query(Persona).filter(Persona.id == id).all()
    if q: return True
    return False

def ajustaRef(childs, campo, grupo, status):
    "ajuste para referencias de personas"
    if campo in childs.keys():
        ref = myNodeValue(childs[campo], 'Integer')
        
        
        
        if ref:
            
            if cloning: # si estoy copiando persona
                p=module2.getPersona(ref) # la referencia original es valida en el contenedor 2?
                print "examinando ",p
                if p:
                    print "examinando personarelacionadac3", p.personarelacionadac3
                    if p.personarelacionadac3: # esta como reemplazo de otra persona....
                        ref=p.personarelacionadac3 #ajusto la referencia con la persona reemplazada
                    else:
                        reportaError(str(ref)+":referencia pendiente. persona no resuelta")
                        return False # aun no podemos hacer el ajuste
                else:
                    reportaError(str(ref)+":referencia pendiente. persona faltante")
                    return False
                    # la referencia original no es valida. 
                
                    
            
            else: #estoy importando persona
            
                ref = idCond(ref, grupo, status)
            
        
            
            if childs[campo].hasAttribute('REFID'):
                childs[campo].setAttribute('REFID', str(ref))
            else:
                childs[campo].childNodes[0].data = str(ref)
            return True
    return False    
                

def ajustaRef2(childs, campo, grupo, status):
    "para referencias que no son personas (sino usuarios)"
    if campo in childs.keys():
        ref = myNodeValue(childs[campo], 'Integer')
        if ref:
            ref = idCond(ref, grupo, status)
            if childs[campo].hasAttribute('REFID'):
                childs[campo].setAttribute('REFID', str(ref))
            
            
def ajustaRef3(childs, campo, grupo, status):
    "para referencias que no son personas (sino localizaciones)" 
    ref = None
    if campo in childs.keys():
        ref = myNodeValue(childs[campo], 'Integer')   
        if ref:
            ref = idCond(ref, grupo, status)  
            if childs[campo].hasAttribute('REFID'):
                childs[campo].setAttribute('REFID', str(ref))
            else:
                childs[campo].childNodes[0].data = str(ref)
        else:
            print "*** localizacion: no hay ref"
    else:
        print "*** localizacion no esta en childs"
                
def ajustaRefCaso(childs, campo, grupo, status):
    "para referencias que no son personas (sino casos)"
    if campo in childs.keys():
        ref = myNodeValue(childs[campo], 'Integer')
        if ref:
            ref = idCond(ref, grupo, status)
            # ahora veamos si ya existe el caso
            
            C = session.query(Caso).filter(Caso.id == ref).first()
            if C:
                if childs[campo].hasAttribute('REFID'):
                    childs[campo].setAttribute('REFID', str(ref))
                    return True
                else:
                    return False
    
def existeObjeto(objeto, id):
    q=session.query(objeto).filter(objeto.id == id).all()
    if q: 
        return q[0]
    return None


valorNulo={'Integer':0,'Text':u'','Unicode':u'','Nombre':''}


def myNodeValue(nodo, tipo):
    valor=None
    if tipo == 'Integer':
        
        if nodo.hasAttribute('REFID'):
            valorStr = nodo.getAttribute('REFID')
            valor= None if valorStr == "None" else int(valorStr)
        else:
            if nodo.childNodes:
                
                exp = nodo.childNodes[0].nodeValue
                if exp:
                    valor = int(exp)
                
    if tipo in ['Text','Unicode']:
        if nodo.childNodes:
            valor = nodo.childNodes[0].nodeValue

            valor = nl.sub('\n',valor)
        else:
            valor = ''
        
    if tipo == 'Date':
        if nodo.childNodes:
            anio,mes,dia=nodo.childNodes[0].nodeValue.split('-')
            dia = dia[:2]
            valor = datetime.date(int(anio),int(mes),int(dia))
    if tipo in ['Nombre']:
        if nodo.childNodes:
            valor = nodo.childNodes[0].childNodes[0].nodeValue

            valor = nl.sub('\n',valor)
        else:
            valor = ''

        
    
    return valor

def AsignaAtributos(obj, childs, tabla, nombre, grupo, status):
    
    for col in camposExp[nombre][0]+camposExp[nombre][1]:
        
        if col in childs.keys():
           esteNodo=childs[col]
           valor, valoranterior = None, None
            
           if esteNodo:
             
              tipo  = columnType(col, tabla)
              valor = myNodeValue(esteNodo, tipo)
              
              valoranterior = None
              if hasattr(obj, col):
                  valoranterior = getattr(obj, col)
              if localstatus.overwf and valoranterior != valor:
                  
                  
                  setattr(obj, col, valor)  
              
        else:
              if hasattr(obj, col):
                  valoranterior = getattr(obj, col)
                  if valoranterior:
                     setattr(obj, col, None)      
        

                      
    
    if hasattr(obj, 'clavegrupo'):
        obj.clavegrupo=grupo
    if hasattr(obj, 'clavestatus'):
        obj.clavestatus=status
    #obj.PLoginfo = None      ???
    if 'loginfo' in childs.keys():
        esteNodo = childs['loginfo']
         
        if esteNodo:
            id = int(esteNodo.getAttribute('id'))
            miID = idCond(id, grupo, status)
            
            LogObj = loginfoImport(esteNodo, grupo, status, miID)
            session.add(LogObj)
            #session.bind.echo=True
             
             
            obj.PLoginfo = LogObj    
            session.flush()
            
            #session.bind.echo=False
            ###setattr(obj, 'loginfo', miID)
             
            obj.PLoginfo = LogObj    
                  
            
def loginfoImport(nodo, grupo, status, miID):
    tabla = module2.loginfo
    objeto = module2.Loginfo
    nombre = 'Loginfo'
    
    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i
    userCreacion, userActualizacion = None, None
    if 'userCreacion' in childs.keys():
        userCreacion = myNodeValue(childs['userCreacion'], 'Integer')
        userCreacion = idCond(userCreacion, grupo, status)
        userCreacionNombre = myNodeValue(childs['userCreacion'], 'Nombre')
        ajustaRef2(childs, 'userCreacion', grupo, status)
    if 'userActualizacion' in childs.keys():
        userActualizacion = myNodeValue(childs['userActualizacion'], 'Integer')
        userActualizacion = idCond(userActualizacion, grupo, status)
        userActualizacionNombre = myNodeValue(childs['userActualizacion'], 'Nombre')
        ajustaRef2(childs, 'userActualizacion', grupo, status)
     
    if userCreacion not in localstatus.usuarios:
        objUserCreacion = existeObjeto(User, userCreacion)
        if not objUserCreacion:
               objUserCreacion = User('%s [%i]'%(userCreacionNombre,grupo), 0, id=userCreacion)
               session.add(objUserCreacion)
               session.flush()
               localstatus.usuarios.append(userCreacion)
    if userActualizacion not in localstatus.usuarios:
        objUserActualizacion = existeObjeto(User, userActualizacion)
        if not objUserActualizacion:
               objUserActualizacion = User('%s [%i]'%(userActualizacionNombre,grupo), 0, id=userActualizacion)
               session.add(objUserActualizacion)
               session.flush()
               localstatus.usuarios.append(userActualizacion)
    
    obj = existeObjeto(objeto, miID)
    if not obj:
        obj=objeto(id=miID, userCreacion=userCreacion, userActualizacion=userActualizacion)
    
    AsignaAtributos(obj, childs, tabla, nombre, grupo, status)
    
    return obj            
            

def getElements(nodo, tag):
     elementos=nodo.getElementsByTagName(tag)
     if elementos:
         return elementos[0].childNodes
     else:
         return []
def sobrantes(nodo, objColeccion, nodoColeccion, grupo, status):
    Xcoleccion = getElements(nodo, nodoColeccion)
    Xids = set([ idCond(int(x.getAttribute('id')), grupo, status) for x in Xcoleccion])
    Ocoleccion = objColeccion
    Oids = set([o.id for o in Ocoleccion])
    diferencia = Oids - Xids
    if diferencia:
        
        aBorrar = [o for o in Ocoleccion if o.id in diferencia]
        for obj in aBorrar:
            print "borrando sobrante",obj
            obj.borrar()
        session.flush()
    return diferencia
     
    
def tipificacionImport(nodo, grupo, status, codigo, caso_id, acto_id=None):
    tabla = module2.evento_tipificacion
    objeto = module2.EventoTipificacion
    nombre = 'EventoTipificacion'
    
    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i
    id = int(nodo.getAttribute('id'))
    miID = idCond(id, grupo, status)
    obj = existeObjeto(objeto, miID)
    if not obj:
    
        obj=objeto(caso_id, None, codigo, None, acto_id=acto_id, id=miID, Log=True)
    
    AsignaAtributos(obj, childs, tabla, nombre, grupo, status)
    #session.add(obj)
    
    return obj

def involucramientoImport(nodo, grupo, status):
    tabla = module2.involucramiento
    objeto = module2.Involucramiento
    nombre = 'Involucramiento'
    
    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i
    id = int(nodo.getAttribute('id'))
    miID = idCond(id, grupo, status)
    persona_id = myNodeValue(childs['persona_id'], 'Integer')
    miPersona =  idCond(persona_id, grupo, status)
    if not existePersona(miPersona):
        print "involucramiento ", id , " incompleto: no se encuenta la persona ", persona_id
        return
    
    
    obj = existeObjeto(objeto, miID)
    if not obj:
        obj=objeto(id=miID, Log=True)
    AsignaAtributos(obj, childs, tabla, nombre, grupo, status)
    
    
    obj.persona_id = idCond(persona_id, grupo, status)
    
    
    
    return obj

def CaracteristicasRelevantesImport(nodo, grupo, status):
    tabla = module2.caracrelevantes
    objeto = module2.Caracrelevantes
    nombre = 'Caracrelevantes'
    
    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i
    id = int(nodo.getAttribute('id'))
    miID = idCond(id, grupo, status)
    obj = existeObjeto(objeto, miID)
    if not obj:
        obj=objeto(id=miID)
    AsignaAtributos(obj, childs, tabla, nombre, grupo, status)
    return obj

def localidadImport(nodo, grupo, status, caso_id):
    tabla = module2.localidad
    objeto = module2.Localidad
    nombre = 'Localidad'
    
    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i
    id = int(nodo.getAttribute('id'))
    miID = idCond(id, grupo, status)
    obj = existeObjeto(objeto, miID)
    if not obj:
        obj=objeto(caso_id, id=miID, Log=True)
    
    AsignaAtributos(obj, childs, tabla, nombre, grupo, status)
    return obj





def intervencionImport(nodo, grupo, status, caso_id):
    tabla = module2.intervencion
    objeto = module2.Intervencion
    nombre = 'Intervencion'
    
    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i
    id = int(nodo.getAttribute('id'))
    miID = idCond(id, grupo, status)
    
    ajustaRef(childs, 'Pinterviniente', grupo, status)
    ajustaRef(childs, 'solicitante', grupo, status)
    ajustaRef(childs, 'contraparte', grupo, status)
    
    
    Pinterviniente_id = None
    if 'Pinterviniente' in childs.keys():
        Pinterviniente_id = myNodeValue(childs['Pinterviniente'], 'Integer')
        if not existePersona(Pinterviniente_id):
            print nombre, id , " incompleto"
            return None
        
    else:
        return None
    
    obj = existeObjeto(objeto, miID)
    if not obj:
        obj=objeto(Pinterviniente_id, 0, caso_id, id=miID, Log=True) 
    
    AsignaAtributos(obj, childs, tabla, nombre, grupo, status)
    
    
    setattr(obj, 'persona_id_interviniente', Pinterviniente_id)
    if 'solicitante' in childs.keys():
        solicitante_id = myNodeValue(childs['solicitante'], 'Integer')
        if not existePersona(solicitante_id):
            print nombre, id , " incompleto"
            return 
         
        setattr(obj, 'persona_id_dequien', solicitante_id)
    if 'contraparte' in childs.keys():    
        contraparte_id = myNodeValue(childs['contraparte'], 'Integer')
        if not existePersona(contraparte_id):
            print "intervencion ", id , " incompleto"
            return
        
        setattr(obj, 'persona_id_aquien', contraparte_id)
    
    return obj

def fuenteImport(nodo, grupo, status):
    "importa fuente personal"
    tabla = module2.fuente
    objeto = module2.Fuente
    nombre = 'FuentePersonal'
    
    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i
        
    # valores para __init__ y creacion del objeto
    id = int(nodo.getAttribute('id'))
    miID = idCond(id, grupo, status)
    
    ajustaRef(childs, 'PersonaFuente', grupo, status)
    ajustaRef(childs, 'PersonaReferenciada', grupo, status)
    persona_fuente, persona_referenciada = None, None
    
    
    
    if 'PersonaFuente' in childs.keys():    
        persona_fuente  = myNodeValue(childs['PersonaFuente'], 'Integer')
        if not existePersona(persona_fuente):
            print nombre, id , " incompleto"
            return 
        #persona_fuente = idCond(persona_fuente, grupo, status) 
        
    if 'PersonaReferenciada' in childs.keys():    
        persona_referenciada  = myNodeValue(childs['PersonaReferenciada'], 'Integer')
        if not existePersona(persona_referenciada):
            print nombre, id , " incompleto"
            return
        
        #persona_referenciada = idCond(persona_referenciada, grupo, status) 
        
    obj = existeObjeto(objeto, miID)
    if not obj:
        obj = objeto(persona_fuente,persona_referenciada, id=miID, Log=True)
      
    AsignaAtributos(obj, childs, tabla, nombre, grupo, status)
    session.add(obj)
    session.flush()
    
    return obj



def publicacionImport(nodo, grupo, status, caso_id):
    "importa fuente personal"
    tabla = module2.publicacion
    objeto = module2.Publicacion
    nombre = 'Publicacion'
    
    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i
        
    # valores para __init__ y creacion del objeto
    id = int(nodo.getAttribute('id'))
    miID = idCond(id, grupo, status)
    
    persona_referenciada_id = None
    ajustaRef(childs, 'PersonaReferenciada', grupo, status)
    if 'PersonaReferenciada' in childs.keys():    
        persona_referenciada_id  = myNodeValue(childs['PersonaReferenciada'], 'Integer')
        if not existePersona(persona_referenciada_id):
            print nombre, id , " incompleto"
            return
    
    obj = existeObjeto(objeto, miID)
    if not obj:
        obj = objeto(caso_id, u'', id=miID, Log=True)
        
    AsignaAtributos(obj, childs, tabla, nombre, grupo, status)
    setattr(obj, 'persona_referenciada_id', persona_referenciada_id)
    
    return obj
def importarReferenciasDeCasos(nodo, grupo, status, forzar=True):
    id = int(nodo.getAttribute('id'))
    miID = idCond(id, grupo, status)
    
    
    # validamos que el caso 1 exista....
    C= session.query(Caso).filter(Caso.id == miID).all()
    if not C:
        print "El caso1" , miID , " no es consistente"
        return
    
    
    nombre = 'Caso'
    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i
    if 'CasosRelacionados' in childs.keys():
        referencias = childs['CasosRelacionados']
        if referencias:
            for referencia in referencias.childNodes:
                casoRefImport(referencia, grupo, status, miID, forzar=forzar)
                

        
def casoRefImport(nodo, grupo, status, caso1, forzar=True):
    tabla = module2.caso_vinculo
    objeto = module2.Caso_vinculo
    nombre = 'RefCaso'
    
    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i
        
    # valores para __init__ y creacion del objeto
    id = int(nodo.getAttribute('id'))
    miID = idCond(id, grupo, status)
    
    obj = existeObjeto(objeto, miID)
    if obj and not forzar:
        return
    

    
    
    caso2, tipoRel = None, None
    ajuste= ajustaRefCaso(childs, 'CasoRelacionado', grupo, status)
    if not ajuste: # se econtro el otro caso?
        return
    if 'CasoRelacionado' in childs.keys():    
        caso2  = myNodeValue(childs['CasoRelacionado'], 'Integer')
        print "caso 2:",caso2
        
    C= session.query(Caso).filter(Caso.id == caso2).all()
    if not C:
        print "el caso2 ", caso2 ," no es consistente"
        return
    if 'tipo_id' in childs.keys():    
        tipoRel  = myNodeValue(childs['tipo_id'], 'Integer')
    
    if caso1 and caso2 and tipoRel and C:
        if not obj:
            obj = objeto(caso1, caso2, tipoRel, id=miID, Log=True)
            obj.loginfo = None

    
        # atributos escalares
        AsignaAtributos(obj, childs, tabla, nombre, grupo, status)
        session.add(obj)
        obj.caso_2_id = caso2
        session.add(obj)
         
        session.flush()
        

def vinculosBiograficosImport(nodo, grupo, status, forzar=True):

    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i
    persona_id = int(nodo.getAttribute('id'))
    persona_id = idCond(persona_id, grupo, status)
    if not existePersona(persona_id):
        print "aun no existe persona ", persona_id
        return # aun no es hora de esta importacion
    
    if 'VinculosBiograficos' in childs.keys():
        vinculos = childs['VinculosBiograficos']
        for VB in vinculos.childNodes:
            
            vinculoBiograficoImport(VB, grupo, status, persona_id, forzar=forzar)
def vinculoBiograficoImport(nodo, grupo, status, persona, forzar=True):
    tabla  = module2.persona_vinculo
    objeto = module2.Persona_Vinculo
    nombre = 'VinculoBiografico'
    
    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i
        
    # valores para __init__ y creacion del objeto
    id = int(nodo.getAttribute('id'))
    miID = idCond(id, grupo, status)
    
    obj = existeObjeto(objeto, miID)
    if obj and not forzar:
        print "importacion no forzada"
        return

    persona2 = None
    exito=ajustaRef(childs, 'PersonaVinculada', grupo, status)
    if not exito:
        print "sin exito, persona aun no presente"
        return # la persona vinculada aun no esta presente
    if 'PersonaVinculada' in childs.keys():
        persona2 = myNodeValue(childs['PersonaVinculada'], 'Integer')
        miPersona = existeObjeto(Persona, persona2)
        if not miPersona:
            print "vinculo ", id , " incompleto"
            return    # el campo no esta presente
        
    if not obj:
        obj = objeto(persona, id=miID, Log=True)
        obj.loginfo = None
    # / valores para __init__

    # atributos escalares
    AsignaAtributos(obj, childs, tabla, nombre, grupo, status)
    
    obj.persona_2_id = persona2  #creo que no hace falta
    
    session.add(obj)
    session.flush()
    

def detalleBiograficoImport(nodo, grupo, status, persona):
    tabla  = module2.persona_vinculo
    objeto = module2.Persona_Vinculo
    nombre = 'DetalleBiografico'
    
    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i
        
    # valores para __init__ y creacion del objeto
    id = int(nodo.getAttribute('id'))
    miID = idCond(id, grupo, status)
    
    obj = existeObjeto(objeto, miID)
    if not obj:
        obj = objeto(persona, id=miID, Log=True)
        obj.loginfo = None
    # / valores para __init__

    # atributos escalares
    AsignaAtributos(obj, childs, tabla, nombre, grupo, status)
    return obj




def casoImport(nodo, grupo, status):
    tabla = module2.caso
    objeto = module2.Caso
    nombre = 'Caso'
    
    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i
        
    # valores para __init__ y creacion del objeto
    id = int(nodo.getAttribute('id'))
    print "importando caso ",id
    miID = idCond(id, grupo, status)
    descripcion = myNodeValue(childs['descripcion'], 'Text')
    
    obj = existeObjeto(objeto, miID)
    if obj:
        session.refresh(obj)
    
    
    
    if not obj:
        obj = objeto(descripcion, id=miID, Log=True)
    # / valores para __init__

    # atributos escalares
    AsignaAtributos(obj, childs, tabla, nombre, grupo, status)
    session.add(obj)
    session.flush()
    
    


    #localidades
    localidades = getElements(nodo,'Localidades')
    for nodoLoc in localidades:
        Loc = localidadImport(nodoLoc, grupo, status, miID)
        obj.localidades.append(Loc)
        session.add(Loc)
    sobrantes(nodo, obj.localidades, 'Localidades', grupo, status)
    
    session.flush()
    # actos
    actos = getElements(nodo, 'Actos')
    
    for nodoActo in actos:
        
        objActo = actoImport(nodoActo, grupo, status, miID, obj)
        if objActo:
            obj.actos.append(objActo)
            session.add(objActo)
    sobrantes(nodo, obj.actos, 'Actos', grupo, status)
    # tipificaciones
    derechos_afectados = getElements(nodo,'DerechosAfectados')
    for nodoTip in derechos_afectados:
        Tip = tipificacionImport(nodoTip, grupo, status, 153, miID)
        #obj.Pderechosafectados.append(Tip)
        session.add(Tip)
    
    sobrantes(nodo, obj.derechosafectados, 'DerechosAfectados', grupo, status)
        
    temas = getElements(nodo,'Temas')
    for nodoTip in temas:
        Tip = tipificacionImport(nodoTip, grupo, status, 154, miID)
        if Tip:
            #obj.Pderechosafectados.append(Tip)
            session.add(Tip)
    
    sobrantes(nodo, obj.temas, 'Temas', grupo, status)
        
        

    intervenciones = getElements(nodo, 'Intervenciones')
    for nodoInter in intervenciones:
        Inter = intervencionImport(nodoInter, grupo, status, miID)
        if Inter:
            session.add(Inter)
            obj.intervenciones.append(Inter)
    session.flush()
    sobrantes(nodo, obj.intervenciones, 'Intervenciones', grupo, status)
    
    
    fuentes = getElements(nodo, 'FuentesPersonales')
    for nodoFuente in fuentes:
        Fuente = fuenteImport(nodoFuente, grupo, status)
        if Fuente:
            obj.fuentes.append(Fuente)
            session.add(Fuente)
    session.flush()
    
    sobrantes(nodo, obj.fuentes, 'FuentesPersonales', grupo, status)
    
    publicaciones = getElements(nodo, 'Publicaciones')
    for nodoPub in publicaciones:
        Pub = publicacionImport(nodoPub, grupo, status, miID)
        if Pub:
            obj.PPublicaciones.append(Pub)
            session.add(Pub)
    session.flush()
    
    sobrantes(nodo, obj.PPublicaciones, 'Publicaciones', grupo, status)
        
            
    return obj

def actoImport(nodo, grupo, status, caso_id, miCaso):
    tabla = module2.acto
    objeto = module2.Acto
    nombre = 'Acto'
    
    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i
        
    # valores para __init__ y creacion del objeto
    id = int(nodo.getAttribute('id'))
    
    miID = idCond(id, grupo, status)
    ajustaRef(childs, 'Victima', grupo, status)
    # deberia checarse si la victima ya esta en C3.... en caso contrario abortar la importacion
    ajustaRef3(childs, 'localizacion_id', grupo, status)
    
    victima = myNodeValue(childs['Victima'], 'Integer')
    miPersona = existeObjeto(Persona, victima)
    if not miPersona:
        print "acto ", id , " incompleto"
        return    
    
    
    tipodeacto = myNodeValue(childs['tipodeacto'], 'Integer')
    
    obj = existeObjeto(objeto, miID)
    if obj:
        session.refresh(obj)
    if not obj:
        obj = objeto(victima,None,id=miID, Log=True)
    # / valores para __init__

    # atributos escalares
    #if 'localizacion_id' in childs.keys():
    #    localizacion_id = myNodeValue(childs['localizacion_id'], 'Integer')
    #    localizacion_id = idCond(localizacion_id, grupo, status)
    #    childs['localizacion_id'].childNodes[0].data = str(localizacion_id)
    obj.edad_victima_tipo = 0
    AsignaAtributos(obj, childs, tabla, nombre, grupo, status)
    session.add(obj)
    session.flush()
    if cloning:
        session.refresh(obj)
    # excepciones - localidad
    
    #if obj.localizacion_id:
    #    obj.localizacion_id = idCond(obj.localizacion_id, grupo, status)
    
    # tipificaciones
    legisNac = getElements(nodo, 'LegislacionNacional')
    for nodoTip in legisNac:
        Tip = tipificacionImport(nodoTip, grupo, status, 2154, caso_id, acto_id=miID)
        if Tip:
            #obj.Pderechosafectados.append(Tip)
            session.add(Tip)
     
    #ojo   
    #sobrantes(nodo, miCaso.PLegisNac, 'LegislacionNacional', grupo, status)
        
    instrInt = getElements(nodo, 'InstrumentosInternacionales')
    for nodoTip in instrInt:
        Tip = tipificacionImport(nodoTip, grupo, status, 2155, caso_id, acto_id=miID)
        if Tip:
            #obj.Pderechosafectados.append(Tip)
            session.add(Tip)
        
    #sobrantes(nodo, miCaso.PLegisInt, 'InstrumentosInternacionales', grupo, status)
    #ojo
    perpetradores = getElements(nodo, 'Perpetradores')

    
    for nodoInvol in perpetradores:
        objInvol = involucramientoImport(nodoInvol, grupo, status)
        if objInvol:
            obj.RolPerpetradores.append(objInvol)
            session.add(objInvol)
    sobrantes(nodo, obj.RolPerpetradores, 'Perpetradores', grupo, status)
        
        
    session.flush()        
    caracRelevantes = getElements(nodo, 'CaracteristicasRelevantes')

    
    for nodoCarRel in caracRelevantes:
        objCarRel = CaracteristicasRelevantesImport(nodoCarRel, grupo, status, )
        if objCarRel:
            obj.PCaracRelevantes.append(objCarRel)
    
            session.add(objCarRel)
    
    session.flush()
    sobrantes(nodo, obj.PCaracRelevantes, 'CaracteristicasRelevantes', grupo, status)
    
    
    
    
            
    return obj
# fin de actoImport
def personaTipificacionesImport(nodo, grupo, status, persona_id):
    P = session.query(Persona).filter(Persona.id == persona_id).first()
    
    for (campo,codigo, prop) in [("Idiomas", 945, "PIdiomas"), ("Lenguas", 946, "PLenguas"), ("OrigenEtnico", 942, "POrigenEtnico"),("Direcciones",910, "PDirecciones")]:
        coleccion = getElements(nodo, campo)

    
        for nodoTip in coleccion:
            objTip = personaTipificacionImport(nodoTip, grupo, status, codigo, campo, persona_id)
            

            session.add(objTip)
        session.flush()
        objetos = getattr(P, prop)
        sobrantes(nodo, objetos, campo, grupo, status)
 
        


def personaTipificacionImport(nodo, grupo, status, codigo, campo, persona_id):
    tabla = module2.persona_tipificacion
    objeto = module2.PersonaTipificacion
    nombre = 'PersonaTipificacion'
    
    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i

    id = int(nodo.getAttribute('id'))
    miID = idCond(id, grupo, status)
    tesauro_id = None
    if 'tesauro_id' in childs.keys():
          tesauro_id = myNodeValue(childs['tesauro_id'], 'Integer')
          
    obj = existeObjeto(objeto, miID)
    if not obj:
        obj=objeto( codigo, persona_id, tesauro_id,  id=miID, Log=True)
    
    AsignaAtributos(obj, childs, tabla, nombre, grupo, status)
    
    return obj
    

def personaImport(nodo, grupo, status, id=None):
    tabla = module2.persona
    objeto = module2.Persona
    nombre = 'Persona'
    
    childs={}
    for i in nodo.childNodes:
        childs[i.nodeName]=i
    if not id:
        id = int(nodo.getAttribute('id'))
    
    
    
    miID = idCond(id, grupo, status)
    

    
    obj = existeObjeto(objeto, miID)
    
    
    if not obj:
        obj=objeto(u'', u'', indiv=0, id=miID, Log=True)
    
    AsignaAtributos(obj, childs, tabla, nombre, grupo, status)
    
    session.add(obj)
    session.flush()
    
    module2.status.idPersonas.add(miID)
    
    personaTipificacionesImport(nodo, grupo, status, miID)
    detallesBio = getElements(nodo, 'DetallesBiograficos')
    for nodoDet in detallesBio:
        Det = detalleBiograficoImport(nodoDet, grupo, status, miID)
        #obj.Pderechosafectados.append(Tip)
        session.add(Det)
    session.flush()
    
    sobrantes(nodo, obj.Pdetallesbiograficos, 'DetallesBiograficos', grupo, status)
    

    return obj

    
#
#d= get_a_document(name="someFile.xml")
#envio = d.childNodes[0]
#
#casos = envio.childNodes[1].childNodes
#if casos:
#    caso1 = casos[0]
#    for i in casos:
#        v=i.getAttribute('id')
#        if v == '7':
#            caso7 = i 
#    
#personas = envio.childNodes[2].childNodes
#if personas:
#    persona1 = personas[0]
#    persona2 = personas[1]


#for i in caso1.childNodes:
#    print i.nodeName
#    print i.childNodes[0].nodeValue.encode("latin_1", 'replace')
#o = casoImport(caso1, 8, 1)

# type(caso.columns['archivos'].type) == sqlalchemy.types.Text

# type(caso.columns['exportar'].type) == sqlalchemy.types.Integer

# id -> grupo+status+id
