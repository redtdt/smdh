
import xml.dom.minidom as minidom
import xml.dom.minidom
import diccionarios

topLevel='Caso'

def get_a_document(name="/municipio.xml"):
    return xml.dom.minidom.parse(name)

def isEqualXML(a, b):
    #da, db= minidom.parseString(a), minidom.parseString(b)
    global listaRes

    listaRes=[]
    da, db= a,b
    #x= isEqualElement(da.documentElement, db.documentElement)
    x= isEqualElement(da, db)
    #for resultado in listaRes:
    #    print resultado['campo'], resultado['accion'], resultado['contexto']
    if listaRes:
        reporte = {}
        reporte['resultado'] = listaRes
        #elemento = da.documentElement
        elemento = da
        if elemento.hasAttribute('descriptor'):
                mensaje = elemento.getAttribute('descriptor')
        else:
                mensaje = elemento.tagName
        reporte['objeto']=mensaje
        return reporte
    return None


def getIDs(nodo):
    lista=[]
    if nodo.hasChildNodes():
        for child in nodo.childNodes:

            if  child.nodeType == 1 and child.hasAttribute('id'):
                id = child.getAttribute('id')
                lista.append(id)
    return lista
def TraducirExpr(mensaje):
    if mensaje in diccionarios.expresiones.keys():
        mensaje = diccionarios.expresiones[mensaje]#.encode("latin_1", 'replace')
        

    return mensaje
def reportaNodo(nodo, accion="Dato diferente"):
            if nodo.tagName=='loginfo':return
            global listaRes
            resultado = {}
            tag = TraducirExpr(nodo.tagName)
            if nodo.hasAttribute('descriptor'):
                
                descr = nodo.getAttribute('descriptor')
                descr = descr.decode('utf-8', 'replace')
                
                mensaje = tag +u" - "+descr
                #mensaje = mensaje.decode('utf-8', 'replace')
            else:
                mensaje = tag
                
            
            resultado['campo']=mensaje
            
            resultado['accion']=accion
            resultado['contexto']=''
            
            padre = nodo.parentNode
            while padre.nodeName != topLevel:
                mensaje = ''
                tag = TraducirExpr(padre.tagName)
                if padre.hasAttribute('descriptor'):
                   descr =  padre.getAttribute('descriptor')
                   descr = descr.decode('utf-8', 'replace')
                   mensaje = tag +u": "+ descr
                else:
                   mensaje = tag
                
                if not mensaje: mensaje = '???'
                if resultado['contexto']:
                   resultado['contexto'] += ' / '+mensaje
                else:
                    resultado['contexto']=mensaje
                
                padre = padre.parentNode
            #print resultado['campo'], resultado['accion'], resultado['contexto']
            
            listaRes.append(resultado)
def nodoTexto(nodo):
    if nodo.childNodes and nodo.childNodes[0].nodeType == 3:
        return True
    return False
def nodoVacio(nodo):
    if nodo.childNodes: return False
    return True

def isEqualElement(a, b):
    nodeName = a.nodeName
    if nodeName in ['loginfo']: return True
    #print "comp ", a.nodeName, b.nodeName
    
    #if a.nodeName!=b.nodeName:
    #    print "elementos diferentes:", a.nodeName, b.nodeName
    if nodoTexto(a) and nodoVacio(b):
        reportaNodo(a, accion="Dato agregado:")
    if nodoTexto(b) and nodoVacio(a):
        reportaNodo(b, accion="Dato eliminado:")
        #return False
    # comparacion de atributos. hara falta?
    #if sorted(a.attributes.items())!=sorted(b.attributes.items()):

    #    sa = set(a.attributes.items())
    #    sb = set(b.attributes.items())
    #    print sa - sb, sb - sa
        
    #    reportaNodo(a, accion="atributos diferentes")
        #return False
    #if len(a.childNodes)!=len(b.childNodes):
    #    print  "numero de elementos diferente en ", a.tagName, ":"
    #    #return False



    #antes de invocar zip(), a,b.childNodes debe convertirse en una lista de
    # nodos cuyos id deben coincidir.
    # en todo caso reportar los nodos cuyos id quedan fuera de la lista
    na = getIDs(a)
    nb = getIDs(b)
    idComunes = set(na).intersection(set(nb))
    a_childs = a.childNodes
    b_childs = b.childNodes
    agregados = []
    eliminados = []
    if na != nb:
        #print "Vastagos diferentes"
        
        agregados = [x for x in a_childs if x.nodeType == 1 and x.hasAttribute('id') and x.getAttribute('id') not in nb]
        eliminados = [x for x in b_childs if x.nodeType == 1 and x.hasAttribute('id') and x.getAttribute('id') not in na]
        a_childs = [x for x in a_childs if x.nodeType == 1 and x.hasAttribute('id') and x.getAttribute('id') in nb]
        b_childs = [x for x in b_childs if x.nodeType == 1 and x.hasAttribute('id') and x.getAttribute('id') in na]
        #print [x.getAttribute('id') for x in a_childs]
        
    #if agregados:
        #print "agregados"
        #print "a",na
        #print "b",nb
        #print ' '
        
    for i in agregados:
            reportaNodo(i, "Entidad agregada")
            
    
    
    
    for i in eliminados:
            reportaNodo(i, "entidad eliminada")
    #qqq = [i.nodeName for i in b_childs]
    
    #print "checando ",b,qqq
    #print "childs ", a_childs, b_childs
    #if not zip(a_childs, b_childs):
    #    print "dato vacio de un lado"
    for ac, bc in zip(a_childs, b_childs):
        #print "comparando ",ac.nodeName, bc.nodeName        
        #print ac.nodeName, bc.nodeName
        if ac.nodeType!=bc.nodeType:
            #print "tipo de nodo diferente" #esto seria incoherente
            reportaNodo(a)
            #return False
        
        elif ac.nodeType==ac.TEXT_NODE  and ac.data!=bc.data:

            reportaNodo(a) 
            ## esto en caso de que sea variable escalar.
            #return False
        elif ac.nodeType==ac.ELEMENT_NODE and not isEqualElement(ac, bc):
            print "difiere en estructura? ", ac.tagName, ac.getAttribute('id')
            #return False
    return True
if __name__ == '__main__':
   
   doc1 = get_a_document(name="/pytdt2/sample1.xml")
   doc2 = get_a_document(name="/pytdt2/sample2.xml")
   caso1 = doc1.childNodes[0].childNodes[1].childNodes[0]
   caso2 = doc2.childNodes[0].childNodes[1].childNodes[0]
   
   doc3 = xml.dom.minidom.parseString("""<Envio><ColeccionCasos><b><c></c></b></ColeccionCasos></Envio>""")
   doc4 = xml.dom.minidom.parseString("""<Envio><ColeccionCasos><b><c>yy</c></b></ColeccionCasos></Envio>""")

   res = isEqualXML(caso1, caso2)
   if res:
       #print res['objeto']
       for resultado in res['resultado']:
           print resultado['accion'], resultado['campo'], resultado['contexto']


