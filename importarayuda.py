#-----------------------------------------------------------------------------
# Name:        importarayuda.py
#
#
# RCS-ID:      $Id: importarayuda.py $
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
#
# Esta rutina no es parte formal del sistema SMDH
# es un auxiliar para importar ayudas contextuales desde un archivo de hoja de calculo
# los campos deben estar separados por TABs
# ejemplo de renglon:
# Casos/Datos generales	Busqueda Exhaustiva	53	xxxxxxxxxxxx Borrar todas		frameBusqueda	delAll	i   Haz clic aqui para borrar todas las condiciones que se encuentren en la ventana.
# seccion               subseccion              consec  coment.                                 frame           ctrlName    Texto de ayuda
# Los unicos campos significativos son: Frame (6o), CtrlName (7o) y Texto de ayuda(8o) contando a partir de 1
#
# antes de ejecutar verificar que el valor de la secuencia del id de tesauro tenga
# un valor adecuado



import codecs
if __name__ == '__main__':
    import cnf
    cnf.user='admin'
    cnf.passwd='redtdt'
    #cnf.host='tdtdb.dyndns.org'
    cnf.host='localhost'
    cnf.db='redtdt'
    
    

from module2 import *
filein = codecs.open('libro.txt','r','latin-1')
l = filein.readline()
nopresente = set([])
print "ejecutando..."
linea=0
while l:
   linea +=1

   campos = l.split('\t')
   campos[6]=campos[6].replace('"','')
   #campos[6]=campos[6].split(',')
   txt=campos[7]
   if txt:
     if txt[0]=='"':
         txt = txt[1:]
         txt = txt[:-1]
         txt = txt.replace('""','"')
     #print txt
   descrip = campos[0]+"/"+campos[1]+"/"+campos[3]
   if campos[4]: descrip = descrip +" / " +campos[4]

   ctrls = campos[6] 
   
   textoayuda = txt
   seccion = campos[5]

   if seccion == '':
       print linea, " seccion vacia!!"
       l = filein.readline()
       continue
   padre = session.query(TesNode.id).filter(TesNode.name == seccion).all()
   

   if padre:
      
        padreID = padre[0][0]
        for myCtrl in ctrls.split(','):
            myCtrl = myCtrl.strip()
            if len(myCtrl) > 30: 
                print linea, "******* "+myCtrl+" excede longitud"
            else:
                nodo = session.query(TesNode).filter(TesNode.name == myCtrl).filter(TesNode.parent_id == padreID).first()
                if not nodo:
                   print linea, "padreID ",padreID, "name ", myCtrl
                   print linea, "agregando "+myCtrl + " en seccion "+seccion
                   nodo = TesNode(myCtrl, descrip, notas=textoayuda, parent_id=padreID)
                   session.add(nodo)
                   session.flush()
                   
                else:
                   actualizando=False
                   if nodo.notas != textoayuda:
                       
                       actualizando=True
                       
                   nodo.notas = textoayuda
                   session.add(nodo)
                   if actualizando: 
                        print linea," actualizando "+myCtrl + " en seccion "+seccion
                        print session.dirty
                   session.bind.echo = actualizando 
                   session.flush()
                   session.bind.echo = False 
                   
   else:
        if seccion not in nopresente:
            nopresente.add(seccion)
            print linea, "********** la seccion "+seccion +" no esta presente"
   
   l = filein.readline()
