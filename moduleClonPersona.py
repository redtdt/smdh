#-----------------------------------------------------------------------------
# Name:        moduleClonPersona.py
#
#
# RCS-ID:      $Id: moduleClonPersona.py $
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
import moduleExp1
import moduleImp1
from xml.dom.minidom import Document
import module2


def clonaPersona(self, obj):
    doc = Document()
    laPersona = obj
    
    elemento = moduleExp1.ExportaPersona(doc, laPersona)
    doc.appendChild(elemento)
    
    #r = doc.toxml()
    #nombreArchivo = "c:\smdh2\export\\test.xml"
    #fileObj = file( nombreArchivo, "w" )
    #fileObj.write(r)
    #fileObj.close()
    
    nodo = doc.childNodes[0]
    strId = nodo.getAttribute('id')
    
    nodoID    = int(strId[:-4])
    grupo = int(strId[-3:])
    print "grupo ", grupo
    print "nodoID ", nodoID
    moduleImp1.cloning=True
    p=moduleImp1.personaImport(nodo, grupo, 3)
    laPersona.personarelacionadac3 = p.id
    laPersona.clavestatusc3 = 2
    module2.session.add(laPersona)
    module2.session.flush()
    module2.session.refresh(laPersona)
    
    
    
    #clonando vinculos de esta persona a otra
    moduleImp1.vinculosBiograficosImport(nodo, grupo, 3)
    
    for otraPersona in laPersona.PpersonasRelacionadasInv:
        doc = Document()
        elemento = moduleExp1.ExportaPersona(doc, otraPersona)
        doc.appendChild(elemento)
        nodo = doc.childNodes[0]
        strId = nodo.getAttribute('id')
        nodoID    = int(strId[:-4])
        grupo = int(strId[-3:])
        moduleImp1.vinculosBiograficosImport(nodo, grupo, 3, forzar=False)
        print "vinculando tambien",otraPersona
    
        
    
    moduleImp1.cloning=False
    return p
    
    
    
def clonaCaso(self, obj):
    doc = Document()

    elemento = moduleExp1.ExportaCaso(doc, obj)
    doc.appendChild(elemento)
    
    # para debug...    
    r = doc.toxml()
    nombreArchivo = "c:\smdh2\export\\test.xml"
    fileObj = file( nombreArchivo, "w" )
    fileObj.write(r)
    fileObj.close()
    # termina para debug
    
    nodo = doc.childNodes[0]
    strId = nodo.getAttribute('id')
    
    nodoID    = int(strId[:-4])
    grupo = int(strId[-3:])
    
    print "grupo ", grupo
    print "nodoID ", nodoID
    
    moduleImp1.cloning=True
    
    p=moduleImp1.casoImport(nodo, grupo, 3)
    # importar relaciones de casos
    moduleImp1.importarReferenciasDeCasos(nodo, grupo, 3)
    
    
    for C in obj.PcasosRelacionadosReciprocos:
        doc = Document()
        
        elemento = moduleExp1.ExportaCaso(doc, C)
        doc.appendChild(elemento)
        nodo = doc.childNodes[0]
        strId = nodo.getAttribute('id')
        nodoID    = int(strId[:-4])
        grupo = int(strId[-3:])
        moduleImp1.importarReferenciasDeCasos(nodo, grupo, 3, forzar=False)
        
    
    
    
    moduleImp1.cloning=False
    return p
    
    
    
    
    