#-----------------------------------------------------------------------------
# Name:        modulerep2.py
#
#
# RCS-ID:      $Id: modulerep2.py $
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

# funciones para reportes narrativos, como prtobj
#from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
#from reportlab.lib.units import inch
#from reportlab.lib import colors
#from reportlab.platypus import Table, TableStyle
#from reportlab.lib.styles import getSampleStyleSheet
from module2 import strDate, strDate2
from module2 import Caso, Acto, status,  TesNode, EventoTipificacion
from module2 import Involucramiento, Intervencion, Persona, Derechoviolado
from module2 import Fuente, Localidad, Publicacion, tesDesc, Loginfo
from module2 import Caracrelevantes, PersonaTipificacion
import module2
#from printconfig import seImprime
from moduleRep6 import campos, TituloAlternativo

session = status.session

ClassAliases = module2.ClassAliases

### faltan relaciones con perpetradores

# establecer un parametro de formato en los terminos 'por imprimir' como
# id.formato.formato.formato.....

# modificar cellformat de acuerdo al parametro de formato


#styles = getSampleStyleSheet()
#style = styles["Normal"]
style = None
PDF=False
HTML=True
RAW=False

fileout=None

cellFormats={}
# formato standard: contenido al margem y contenido
cellFormats['A']="<tr><td valign='top'><b>%(tit)s</b></td><td align=top>%(cont)s</td></tr>"
# titulo arriba y contenido a dos coumnas (para rollos)
cellFormats['B']="<tr><td colspan=2><b>%(tit)s</b></td></tr> <tr><td colspan=2 >%(cont)s</td></tr>"
# contenido como titulo, centrado a dos columnas
cellFormats['C']="<tr><td colspan=2 align=center><br><b><u>%(cont)s</u></b></td></tr>"
# contenido en segunda columna, sin titulo
cellFormats['D']="<tr><td valign='top'></td><td align=top>%(cont)s</td></tr>"
# sin contenido, sin titulo
cellFormats['E']="<tr><td valign='top'></td><td align=top></td></tr>"

cellFormat=cellFormats['A']
renglones=[]



#1.-
#campos['Caso']={'descripcion':('Descripcion del caso','PrtStr'),......
#       Entidad   Campo          Titulo                 Render
#       Primaria  Primario
#2.-
#campos['EventoTipificacion']={'derechosafectados':('Derecho afectado','PrtTes','TesNode','derechosafectados', 'descripcion'),}
#        Entidad                Campo                Titulo             Render   Entidad       ID               campo
#        Primaria               Primario                                         Secundaria                     P/render

camposCruzables={'Caso':['descripcion','no_persona_afectadas','frecepcion','fecha_inicio'],
                'EventoTipificacionDerechosAfectados':['derechosafectados'],
                'EventoTipificacionTemas':['temas'],
                'Acto':['PTipodeacto','PTipodelugar','Pvictima','Pvictima/Psexo',
                        'Pvictima/Pescolaridad','Pvictima/Ptipo'],
                'Involucramiento':['persona','Pgradoinvolucramiento',
                                    'Ptipoperpetrador','Pultimostatusperpetrador'],
                'Localidad':['strEstado','strMpio']
                }
                
                            



for i in ClassAliases.keys():
    for j in ClassAliases[i]:
        campos[j]=campos[i]



def filterNone(s):
    if s: return s
    else: return ''
    
def PrtSi(Titulo, Contenido, style, Tipo, fileout=None, Formato=None):
     if Contenido == 1:
         Contenido = 'Si'
     else:
         Contenido = 'No'
     if Formato=='HTML':
        if Contenido == 'Si': 
            salida = cellFormat%{'tit':Titulo,'cont': filterNone(Contenido)}
            fileout.write(salida)
     if Formato=='RAW':
        return filterNone(Contenido)

def PrtInt(Titulo, Contenido, style, Tipo, fileout=None, Formato=None):
    if Contenido:
        Contenido = str(Contenido)
    else:
        Contenido = ''
    if Formato=='HTML':
        salida = cellFormat%{'tit':Titulo,'cont': filterNone(Contenido)}
        fileout.write(salida)
    if Formato=='RAW':
        return filterNone(Contenido)
    
        

def PrtStr(Titulo, Contenido, style, Tipo, fileout=None, Formato=None):
    Contenido = Contenido.replace('\n','<br/>')
    #Contenido = Contenido.replace('\n',' ')
    if Formato=='PDF':
        p1= Paragraph(Contenido,style)
        p2= Paragraph(Titulo,style)
        
    
        
        lista=[]
        px = p1.split(5.8 * inch, 9 * inch)
        #print px[0]
        #if len(px) > 1:
        #    print px[1]
        while len(px) > 1:
            lista.append(px[0])
            px2 = px[1]
            px3 = px2.split(5 * inch, 9 * inch)
            px = px3
        lista.append(px)
       
        for p in lista:
            renglones.append([p2, p])
    if Formato=='HTML':
        salida = cellFormat%{'tit':Titulo, 'cont':filterNone(Contenido)}
        fileout.write(salida)
    if Formato=='RAW':
        return filterNone(Contenido)
    
    
    
    
def PrtChk(Titulo, Contenido, style, Tipo, fileout=None, Formato=None):
    
    
    if Formato=='HTML':
        if Contenido == 1:
            expr = "Si"
        else:
            expr = "No"
        
        salida = cellFormat%{'tit':Titulo,'cont': expr}
        fileout.write(salida)
    if Formato=='RAW':
        return expr   

def PrtConst(Titulo, Contenido, style, Tipo, fileout=None, Formato=None):
    if Formato=='PDF':
        p1=Paragraph('',style)
        
        p2= Paragraph(Titulo,style)
        renglones.append([p2, p1])
    if Formato=='HTML':
        salida = cellFormat%{'tit':Titulo, 'cont':filterNone(Contenido)}
        fileout.write(salida)
    if Formato=='RAW':
        return filterNone(Contenido)
        
        
    pass


def PrtDateC(Titulo, Contenido, style, Tipo, fileout=None, Formato=None):
        
        fecha, Ptipofecha=Contenido()
        if Ptipofecha:
            if Formato=='HTML':
                salida = cellFormat%{'tit':Titulo,'cont': filterNone(strDate2(fecha, Ptipofecha))}
                fileout.write(salida)
            if Formato=='RAW':
                return filterNone(strDate2(fecha, Ptipofecha))
            

def PrtTes(Titulo, Contenido, style, Tipo, fileout=None, Formato=None):
    if Contenido:
        if Formato=='PDF':
            p1= Paragraph(tesDesc(Contenido),style)
            p2= Paragraph(Titulo,style)
            renglones.append([p2, p1])
        if Formato=='HTML':
            salida = cellFormat%{'tit':Titulo,'cont': filterNone(tesDesc(Contenido))}
            fileout.write(salida)
        if Formato=='RAW':
            return filterNone(tesDesc(Contenido))
#def PrtTesL(Titulo, Contenido, style, Tipo, fileout=None, Formato=None):
#    if Contenido:
#        if Formato=='PDF':
#            p1= Paragraph(Contenido.DescriptorCompleto(),style)
#            p2= Paragraph(Titulo,style)
#            renglones.append([p2, p1])
#        if Formato=='HTML':
#            salida = cellFormat%{'tit':Titulo,'cont': filterNone("---"+Contenido.DescriptorCompleto())}
#            fileout.write(salida)
#        if Formato=='RAW':
#            return filterNone("---"+Contenido.DescriptorCompleto())
        
def PrtDate(Titulo, Contenido, style, Tipo, fileout=None, Formato=None):
    if Contenido:
        if Formato=='PDF':
            p1= strDate(Contenido)
            p2= Paragraph(Titulo,style)
            renglones.append([p2, p1])
        if Formato=='HTML':
            salida = cellFormat%{'tit':Titulo, 'cont':filterNone(strDate(Contenido))}
            fileout.write(salida)
        if Formato=='RAW':
            return filterNone(strDate(Contenido))
def PrtFun(Titulo, Contenido, style, Tipo, fileout=None, Formato=None):
    #print "contenido:",str(Contenido)
    if Contenido:
        # asumo que el contenido es el resultado de una funcion
        # entonces invoco 'contenido como si fuera una funcion'
        s=Contenido()
        if s:
            s=s.replace('\n','<br/>')
        if Formato=='PDF':
            if s:
                p1= Paragraph(s,style)
                p2= Paragraph(Titulo,style)
                renglones.append([p2, p1])
        if Formato=='HTML':
            if s:
               salida = cellFormat%{'tit':Titulo,'cont': filterNone(s)}
               fileout.write(salida)
        if Formato=='RAW':
            return filterNone(s)

def PrtObjFun(Titulo, Contenido, style, Tipo, fileout=None, Formato=None, por_imprimir=None, tipoRep="normal" ):
    if Contenido:
        # asumo que el contenido es el resultado de una funcion
        # entonces invoco 'contenido como si fuera una funcion'
        l=Contenido()
        
        PrtObj(Titulo, l, style, Tipo, fileout=fileout, Formato=Formato, por_imprimir=por_imprimir, tipoRep=tipoRep)
        
        
        
def PrtObj(Titulo,objList,  style, Tipo, fileout=None, Formato=None, por_imprimir=None, tipoRep="normal"):
    
    if hasattr(objList, 'im_func'):
        list = objList()
        objList = list  
    
    if type(objList) in [Loginfo]:
        objList = [objList]
    
    #ojo
    objList.sort(cmp=lambda x,y:int(x.id) - int(y.id))
    #objList.sort(cmp=lambda x,y:x.id - y.id)
    #ojo
    
    for obj in objList:
        #PrtConst('<b>'+Titulo+'</b>',None,style,'', fileout=fileout, Formato=Formato)
        #PrtConst('<br>',None,style,'', fileout=fileout, Formato=Formato)
        
        
        for field in por_imprimir[Tipo]:
            cond = True
            field1 = field.split('.')[0]
            cond = module2.seImprime(Tipo,field1, tipoRep)
            if cond:
                
                renderObj(obj, field, Tipo, Formato, por_imprimir=por_imprimir, fileout=fileout, tipoRep=tipoRep)
        #PrtConst('',None,style,'', fileout=fileout, Formato=Formato)  

def GetOpcionObj(obj):
    if type(obj) == Persona:
        if obj.esindividual == 1:
            return 0
        else:
            return 1
    return 0

def renderObj(obj, field, Tipo, Formato, por_imprimir=None, fileout=None, tipoRep="normal"):
        global cellFormat
        if obj:
            opcionObj = GetOpcionObj(obj)
            field1 = field.split('.')[0]
            opciones =field.split('.')[1:]
            #print field1, opciones
            formatoCelda = opciones[0] if opciones and len(opciones) > 0 else "A"
            cellFormat = cellFormats[formatoCelda]
            
            funcion = PrtFn[campos[Tipo][field1][1]] 
                            #field es el nombre de campo a imprimir, 
                            # tipo es la clase de objeto = tabla
                            # funcion es el procedimiento a invocar para renderear el contenido
                            # obj es la instancia a imprimir                                               
            #print "argumento ", campos[Tipo][field1][1] , " funcion ", str(funcion)
            titulo  = campos[Tipo][field1][0]
            if type(titulo) == tuple:
                
                titulo = titulo[opcionObj]
                
            titulo = TituloAlternativo[titulo] if titulo in TituloAlternativo else titulo
                
                
            try:
                atts = field1.split('/')
                cont = obj
                for k in atts:  # ojo. en este caso, k es un str. cont debe ser la str propiamente (mucho ojo!!!!!!!!!!!!!!!!!!!)
                    cont = cont.__getattribute__(k)
                contenido = cont
                #contenido = obj.__getattribute__(i)
            except:
                if funcion == PrtChk:
                    contenido = 0
                else:
                    contenido=None
                    #print "no se pudo determinar el contenido"
            if contenido or (funcion == PrtChk):
                # se invoca la funcion render (PrtXXX)
                if funcion in [PrtObj, PrtObjFun] :
                     r=funcion(titulo,contenido, style, field1, fileout=fileout, Formato=Formato, por_imprimir=por_imprimir, tipoRep=tipoRep)
                else:
                     r=funcion(titulo,contenido, style, field1, fileout=fileout, Formato=Formato)

                if Formato == 'RAW': return filterNone(r)
            else: return ''
        else:
            return ''        

        
        
        
PrtFn = {}
PrtFn['PrtStr']=PrtStr
PrtFn['PrtTes']=PrtTes
#PrtFn['PrtTesL']=PrtTesL
PrtFn['PrtObj']=PrtObj
PrtFn['PrtFun']=PrtFun
PrtFn['PrtDate']=PrtDate
PrtFn['PrtSi']=PrtSi
PrtFn['PrtInt']=PrtInt
PrtFn['PrtChk']=PrtChk
PrtFn['PrtDateC']=PrtDateC
PrtFn['PrtObjFun']=PrtObjFun
PrtFn['PrtConst']=PrtConst

def fileExist(name):
    try:
        f=file(name)
        return True
    except:
        return False
def Membrete(conMembrete=False):
    if not conMembrete:
        return " "
    logoName = ''
    logo = ' '
    for nombre in ['logo.gif','logo.jpg','logo.png']:
        
        if fileExist('c:/smdh2/config/'+nombre):
              logoName = nombre
              logo = """<td border=0 >
                      <img src="file://c:/smdh2/config/%s" height=200 width=200>
                      </td>"""%logoName
    
        
    txtMembrete = status.OrgMembrete.replace('\n','<br>')
    salida = """
    
    <table border=0 width=100%%>
    <tr>
    %s
    <td border=0 valign=middle>
    %s
    </td>
    </tr>
    </table>"""%(logo, txtMembrete)
    return salida


def HTMLHeader(titulo='', cols=[], border=0, conMembrete=True):
    org = status.OrgNombre
    strTitulo = "<tr><td colspan=4><b>%s</b></td></tr>"%titulo if titulo else ''
    strOrg =  u"<tr><td><b>Organizaci\xf3n&nbsp;</b></td><td>%s</td></tr>"%org if org else ''
    strFecha = u"<tr><td><b>Fecha de emisi\xf3n&nbsp;</b></td><td>%s</td></tr>"%status.strDiadehoy
    s= """
<html>
  <head>
   <title>""" + titulo + """</title>
   <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/> 
   <style type="text/css">
.nivel1 {margin-left:0px;}   
.nivel2 {margin-left:12px;}
.nivel3 {margin-left:24px;}
.nivel4 {margin-left:36px;}
.nivel5 {margin-left:48px;}
.nivel6 {margin-left:60px;}
.nivel7 {margin-left:72px;}
.nivel8 {margin-left:84px;}
.nivel9 {margin-left:96px;}

   
   </style>
</head>
<body>
%s
 <table border=%i>
  %s %s<br>%s
 </table>
 <table border=0>
 """%( Membrete(conMembrete),border,strTitulo, strOrg, strFecha)
    if cols:
       
        s = s + '<tr>' 
        for i in cols:
            s = s + '<td><b>'+i+'</b></td><td>&nbsp;&nbsp;</td>'
        s = s + '</tr>' 
    
    
    
    return s
def HTMLFooter(PieDePagina=''):
    
    s = """
    %s
    
    </table>
    </body>
    </html>
    """%("<tr></tr><tr><td colspan=6>"+PieDePagina+"</td></tr>" if PieDePagina else " ")
    return s

        
