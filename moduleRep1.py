#-----------------------------------------------------------------------------
# Name:        moduleRep1.py
#
#
# RCS-ID:      $Id: moduleRep1.py $
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


Title = "Hello world"
pageinfo = "Informe de Caso"



from module2 import Caso, Acto, status, TesNode, EventoTipificacion
from module2 import Involucramiento, Intervencion, Persona, Derechoviolado
from module2 import Fuente, Localidad, Publicacion, tesDesc, Loginfo
from module2 import Caracrelevantes, PersonaTipificacion

from module2 import strDate, MError

from codecs import encode
from string import replace
import codecs

from moduleRep2 import *
from moduleRep6 import por_imprimir, campos
import webbrowser
from printconfig import matflag


#from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
#from reportlab.lib.styles import getSampleStyleSheet
#from reportlab.rl_config import defaultPageSize
#from reportlab.lib.units import inch
#from reportlab.lib import colors
#from reportlab.platypus import Table, TableStyle

session = status.session


#PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
#styles = getSampleStyleSheet()

def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold',8)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Primera pagina / %s" % pageinfo)
    canvas.restoreState()

def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Pag. %d %s" % (doc.page, pageinfo))
    canvas.restoreState()


            
               
               
               
            



def printObj(objetos, Formato, TipoObj, filename='salida.htm', titulo='', tipoRep='normal'):
    global fileout
    global PDF
    global HTML
    PDF = Formato=='PDF'
    HTML = not PDF
    
    
    
    if HTML:
            
            try:
                fileout = codecs.open(filename,'w','utf-8')
            except:
                MError(None, u"No pudo abrirse el reporte. Es probable que alguna aplicaci\xf3n (Word, excel) ya tenga abierto ese archivo con el nombre de salida. Intenta cerrar estas aplicaciones")
                return None
            
            fileout.write(HTMLHeader(titulo=titulo))

    for obj in objetos:
        session.refresh(obj)
        
        
        if PDF:
            doc = SimpleDocTemplate("salida.pdf", allowSplitting=1)
            
            Story = []
            style = styles["Normal"]
            pageinfo = obj.Descriptor()
        
            PrtObj(TipoObj,[obj], style,TipoObj, Formato=Formato, por_imprimir=por_imprimir, tipoRep=tipoRep)
            #renglones = [ [1,2,3,4] ]
            t=Table(renglones, colWidths=(1* inch, 6* inch), splitByRow=1)
            estiloTabla = TableStyle([('VALIGN',(0,0),(-1, -1),'TOP'),
                                      ('INNERGRID',(0,0),(-1,-1),0.25,colors.black),
                                      ('BOX',(0,0),(-1,-1),0.25,colors.black),
        
                                                                  ])
            t.setStyle(estiloTabla)
            
            Story.append(t)
            Pbreak = PageBreak()
            Story.append(Pbreak)
            
            doc.build(Story)#, onFirstPage=myLaterPages, onLaterPages=myLaterPages)
        if HTML:
            

            PrtObj(TipoObj,[obj], None,TipoObj, fileout=fileout, Formato=Formato, por_imprimir=por_imprimir, tipoRep=tipoRep)
            fileout.write('<tr><td colspan = 2><hr></td></tr>')
            
    if HTML:
        fileout.write(HTMLFooter())
        fileout.close()
        return filename

if __name__ == '__main__':
    c= session.query(Caso).filter(Caso.id == 23)[0]
    p = session.query(Persona)[0]

    printObj([p], 'HTML','Persona')

