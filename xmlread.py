if __name__ == '__main__':
    import cnf
    cnf.user='admin'
    cnf.passwd='redtdt'


import module2 as m2
from module2 import TesNode, status
import xml.dom.minidom


session = status.session

def get_a_document(name="/municipio.xml"):
    return xml.dom.minidom.parse(name)

estados = m2.session.query(TesNode).filter(TesNode.name==u'T63')[0]
print "estados:",estados
edos={}
a=get_a_document()
for i in a.childNodes[0].childNodes:
	if i.nodeName == u'cat_municipio_AGO2007':
#		print i.childNodes[3].childNodes[0].nodeValue
		descrip = i.childNodes[3].childNodes[0].nodeValue
		clave = '0' + i.childNodes[1].childNodes[0].nodeValue
		edos[clave] = descrip
crear = 1
if crear:
  for i in edos.keys():
    print str(i), edos[i]
    name = ''
    estados.append(str(i),edos[i])
session.add(estados)    


#session.flush()

# crea estados


if crear:
   for i in estados.children.keys():
       #print estados.children[i].descripcion
       session.add(estados.children[i])
       print estados.children[i].name
   session.flush()

crear = 1

# crear municipio

q= m2.session.query(TesNode)
if crear:
    for i in a.childNodes[0].childNodes:
        if i.nodeName == u'cat_municipio_AGO2007':
            descripEdo = i.childNodes[3].childNodes[0].nodeValue
            claveEdo = "0" + i.childNodes[1].childNodes[0].nodeValue
            estado = q.filter_by(name=claveEdo, parent_id=40)[0]
            claveMpio = i.childNodes[7].childNodes[0].nodeValue
            descripMpio = i.childNodes[9].childNodes[0].nodeValue
            
            estado.append(str(claveEdo)+str(claveMpio), descripMpio)

if crear:
   for i in estados.children.keys():
       estado = estados.children[i]
       for j in estado.children.keys():
           municipio = estado.children[j]
           session.add(municipio)
           print municipio.name
       session.flush()
           
       

            
                
                
    
		


