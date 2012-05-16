#-----------------------------------------------------------------------------
# Name:        reportaVocab.py
#
#
# RCS-ID:      $Id: reportaVocab.py $
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
#Boa:Frame:Frame3

import wx
import cnf
import codecs
if __name__ == '__main__':
    cnf.user='admin'
    cnf.passwd='redtdt'
from module2 import  *
from moduleRep2 import HTMLHeader
from configmodule import getVOrden

def create(parent):
    return Frame3(parent)

[wxID_FRAME3] = [wx.NewId() for _init_ctrls in range(1)]

class Frame3(wx.Frame):
    def _init_ctrls(self, prnt):
        wx.Frame.__init__(self, style=wx.DEFAULT_FRAME_STYLE, name='', parent=prnt, title='Frame3', pos=wx.Point(-1, -1), id=wxID_FRAME3, size=wx.Size(-1, -1))

    def __init__(self, parent):
        self._init_ctrls(parent)
        
def ReportaTipo(type, nombre='vocabulario.doc', noClaves=False):
    rootElement = QueryTesNode.filter_by(name=type)
    Vorden = getVOrden(type)
    try:
        rootElement = rootElement[0]
        salida=codecs.open(nombre,'w','utf-8')
        header = HTMLHeader()
        encClave,encID= 'Clave','ID'
        if noClaves:
            encClave,encID = '',''
        salida.write(header)
        expr = "<tr><td colspan=5><p class=titulo>Tesauro:%s - %s</p></td></tr>"%(rootElement.name, rootElement.descripcion)
        salida.write(expr)
        expr = "<tr border=0><td><b>%s</b></td><td width=%s><b>%s</b></td><td><b>%s</b></td><td><b>%s</b></td><td><b>%s</b></td></tr>\n"%('Nivel','70%',u'T\xe9rmino',encClave,encID,'Notas de alcance')
        salida.write(expr)
        DesarrollaTipo(rootElement, 0, salida, noClaves=noClaves, VOrden=Vorden)
        salida.close()
    except:
        print "no existe ", sys.exc_info()
    
def DesarrollaTipo(node, nivel, fileOut, noClaves=False, VOrden=None):
            if node:
                COLname, COLid = node.name, str(node.id)
                if noClaves:
                    COLname, COLid = '',''
                #expr = "<tr border=0 valign=top><td width=%s>%s%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n"%('70%','&nbsp;'*4*nivel, node.descripcion, COLname, COLid, node.notas)
                expr = "<tr border=0 valign=top><td align=right>%i</td><td width=%s><p  class=nivel%s>%s</p></td><td>%s</td><td>%s</td><td>%s</td></tr>\n"%(nivel,'70%',str(nivel),node.descripcion, COLname, COLid, node.notas)
                if nivel > 0:
                    fileOut.write(expr)    
                ColumnaOrden = TesNode.name
                if VOrden:
                    ClaveOrden = VOrden[0]        
                    if ClaveOrden == "C":
                        ColumnaOrden = TesNode.name
                    else:
                        ColumnaOrden = TesNode.descripcion
                print nivel, ColumnaOrden
                
                
                          
                #Torden =   TesNode.name
                q = session.query(TesNode).filter(TesNode.parent_id == node.id).order_by(ColumnaOrden).all()
                
                if q:
                   #fileOut.write("<ul>")
                   for i in q:
                       if VOrden:
                            if len(VOrden) > 1:
                                orden = VOrden[1:]
                            else:
                                orden = VOrden
                       else:
                            orden = None
                       
                       
                       DesarrollaTipo(i, nivel + 1, fileOut, VOrden=orden)
                   #fileOut.write("</ul>")                


if __name__ == '__main__':

  
   ReportaTipo('T04')

