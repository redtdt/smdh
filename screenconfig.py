#-----------------------------------------------------------------------------
# Name:        screenconfig.py
#
#
# RCS-ID:      $Id: screenconfig.py $
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

# XXX ojo aun no funciona si la tabla de config no existe previamente
from  module2 import ConfigTdt, status, MError
import wx
import wx.gizmos
import pickle
import sys

session = status.session


def create(parent):
    return Frame3(parent)

[wxID_FRAME3, wxID_FRAME3BUTTON1, wxID_FRAME3PANEL1, wxID_FRAME3STATICTEXT1, 
 wxID_FRAME3TREE1, 
] = [wx.NewId() for _init_ctrls in range(5)]

tablapestania = {}
itemsNoModificables = ['NBCasos','NBCasosGral','NBCasosNarrativa', 'NBActosGral', 'NBPersonasGral']
NBconfig =[('NBCasos','Casos',-1),   [('NBCasosGral', 'Datos generales',-1), 
                                      ('NBCasosNarrativa',u'Informaci\xf3n narrativa',2),
                                      ('NBCasosAdm',u'Informaci\xf3n administrativa',3), 
                                      ('NBCasosTipifica', 'Tipificaciones',1), 
                                      ('NBCasosRelaciones','Relaciones',4)], 
        ('NBActos','Actos',1),       [('NBActosGral',u'Informaci\xf3n general',-1), 
                                      ('NBActosPerp','Perpetradores',1), 
                                      ('NBNormatividad','Normatividad',2)], 
        ('NBIntervenciones', 'Intervenciones',2), 
        ('NBFuentes','Fuentes',3),   [('NBFuentePersonal','Fuente personal',0), 
                                      ('NBFuenteDocumental','Fuente documental',1)], 
        ('NBPersonas','Personas',4), [('NBPersonasGral',u'Datos generales',-1), 
                                      ('NBPersonasDetalles','Detalles',1),
                                      ('NBPersonasAdm',u'Informaci\xf3n administrativa',2), 
                                      ('NBPersonasBio',u'Datos biogr\xe1ficos',3)]
                                     ]

# la llave general representa la pestania de la cual cuelgan los otros objetos
# la llave es el primer objeto a ocultar y es usada tambien para gauardar la opcion en el objeto de opciones
# la lista contiene en primer termino la descripcion de la opcion. luego siguen otros objetos a ocultar
        
tablaCampos={

        'NBPersonasGral':{
            'staticText104':[u'Exportar persona','FPconfidencialidad'],
            'staticText110':[u'Otro nombre','FPOtroNombre'],
            'CPfechanac':[u'Fecha de nacimiento / Creaci\xf3n','FPTipodefecha','PFNdia','PFNmes','PFNanio'],
            'CPCiudadania':[u'Ciudadan\xeda / Pa\xeds sede','btnFPCiudadania','btnRemoveFPCiudadania','FPCiudadania'],
            'CPEscolaridad':[u'Escolaridad / Nivel de escolaridad predominante','FPEscolaridad'],
            
            },
        


        'NBPersonasDetalles':{
        
        
        
            'CPOcupacion': [u'Ocupaci\xf3n','btnAddOcupacion', 'btnDelOcupacion', 'FPstrOcupacion'],
            'CPIdioma': ['Idioma','FPIdioma', 'FPAddIdioma','delIdioma'],
            'CPHablayentiendeespanol':[u'Habla y entiende espa\xf1ol', 'FPHablayentiendeespanol'],
            'CPLengua': [u'Lengua ind\xedgena','FPLengua', 'FPAddLengua','delLengua'],
            'CPOrigenEtnico': [u'Origen \xe9tnico','FPOrigenEtnico', 'FPAddOrigenEtnico','delOrigen'],
            'CPReligion': [u'Religi\xf3n','FPReligion'],
            'CPEstadocivil': [u'Estado civil','FPEstadocivil'],
            'CPNodependientes': [u'No. de dependientes / No. de personas en el grupo','FPNodependientes'],
            'CPDescripciondelgrupo': [u'Descripci\xf3n del grupo','FPDescripciondelgrupo'],
            'staticText67':[u'Direcciones', 'FPDirecciones', 'FPAddDirecciones','delDireccion'],
            'CPMonitoreo':[u'Monitoreo','FPMonitoreo'],
            
        },
        'NBPersonasAdm':{
            'CPObservaciones':[u'Observaciones','FPObservaciones'],
            'staticText38':[u'Comentarios','FPComentarios'],
            'CPArchivos':[u'Archivos','FPArchivos'],
            'staticText101':[u'Fecha de recepci\xf3n','FPTipodefecharecepcion','PFRdia','PFRmes','PFRanio'],
            'staticText103':[u'Proyecto local','FPproyecto_grupo'],
            'staticText100':[u'Proyecto conjunto RedTDT','FPproyecto_conjunto'],
            'staticText102':[u'Proyecto SE','FPproyecto_se'],
            },
        'NBPersonasBio':{
            'staticText89':[u'Exportar dato biogr\xe1fico','FBConfidencialidad'],
            'staticText82':[u'Observaciones','FBObservaciones','longPerDBObs'],
            'staticText91':[u'Comentarios','FBComentarios', 'longPerDBCom'],
            'staticText93':[u'Puesto o cargo','FBPuesto'],
            'staticText90':[u'Rango','FBRango'],
            },
        
        'NBCasosNarrativa':{
            'staticText34': [u'Descripci\xf3n narrativa', 'textCtrlDescripcionNarrativa', 'txtLongNarra'],
            #'staticText35': [u'Resumen de la descripci\xf3n', 'textCtrlResumen'],
            'staticText36': [u'Observaciones', 'textCtrlObservaciones', 'txtLongObs'],
            },
        'NBCasosGral':{
            'staticText29': [u'Exportar caso','checkBoxCasoConfidencialidad'],
            'staticText1': [u'Exportar relaciones','checkBoxCasoExportarRelaciones'],
            'staticText32':['No. de personas afectadas', 'textCtrlNoPersonasAfectadas'],
        
            },
        'NBCasosAdm':{
            'staticText94': [u'Fecha de recepci\xf3n', 'FCtipo_frecepcion', 'CFRdia', 'CFRmes', 'CFRanio'],
            'staticText75': [u'Proyecto local', 'FCproyecto_grupo'],
            'staticText76': [u'Proyecto conjunto RedTDT', 'FCproyecto_conjunto'],
            'staticText77': [u'Proyecto SE', 'FCproyecto_se'],
            'staticText78': [u'Comentarios', 'textCtrlCAComentarios','txtLongAdmComent'],
            'staticText79': [u'Estatus del caso', 'choiceMonitoreo'],
            'staticText4': [u'Archivos', 'textCtrlCAArchivos','txtLongAdmArch'],
            },
        'NBCasosTipifica':{
            'staticText7': [u'Derechos afectados', 'listBoxDerechosafectados', 'buttonCasoDerechoafectado','delDerecho'],
            'staticText8': [u'Temas', 'listBoxTemas', 'button2','delTema'],
            },
        'NBCasosRelaciones':{
            'staticText108':[u'Observaciones', 'FRCCasoRelObservaciones'],
            'staticText106':[u'Comentarios','FRCCasoRelComentarios'],
            },
            
        'NBActosGral':{
            'staticText39': [u'Exportar acto' , 'FAConfidencialidad'],  
            'staticText45': [u'Caracter\xedsticas relevantes','BTNAgregarcaracrelevantes','delCaracRel', 'FACaracRelevante'],
             
            'staticText49': [u'Tipo de lugar', 'buttonSelecTipodelugar', 'buttonRemoveTipodelugar', 'FATipodelugar'],
            'staticText46': [u'Estatus VDH', 'buttonSelectEstatusVDH', 'buttonRemoveEstatusVDH', 'buttonRemoveEstatusVDH', 'FAEstatusvdh'],
            'staticText47': [u'Estatus de la v\xedctima', 'buttonEstatusdelavictima', 'buttonRemoveEstatusdelavictima', 'FAEstatusvictima'],
            'staticTextEdadOcurreActo': [u'Edad cuando ocurri\xf3 el acto', 'choiceTipoEdad', 'FAedad_victima'],
            #'staticText73': [u'Localizaci\xf3n', 'FALocalidad'],
            'staticText48': [u'Observaciones', 'FAObservaciones'],
            },
            
        'NBActosPerp':{
            'staticText51': [u'Exportar perpetrador','FIconfidencialidad'],
            'staticText52': [u'Grado de involucramiento', 'buttonSelGradoInvol', 'buttonRemoveGradoInvol', 'FIgradoinvolucramiento'],
            #'staticText53': [u'Tipo de perpetrador', 'buttonSelTipoPerp', 'buttonRemoveTipoPerp', 'FItipoperpetrador'],
            'staticText54': [u'\xdaltimo estatus del perpetrador', 'buttonSelUltStatusPerp', 'buttonRemoveUltStatusPerp', 
            'buttonRemoveUltStatusPerp'],
            'staticText14': [u'Observaciones', 'textCtrlINObservaciones', 'txtLongInObs'],
            },
        'NBNormatividad':{
            'staticText95':[u'Legislaci\xf3n nacional','btnActoLegislacion','delLegislacion', 'FALegis', 'staticText98', 'FAlegislacion_nacional_notas', 'txtLongNorLeg' ],
            'staticText97':[u'Instrumentos internacionales','btnActoInstrInt', 'delInstrInt', 'FAInstr', 'staticText96', 'FAinstrumentos_int_notas','txtLongNorIns'],
            'staticText5':[u'Exportar normatividad','FAExportar'],

            },
        'NBIntervenciones':{
            'staticText21':[u'Sobre qui\xe9n se interviene','buttonDeQuien','buttonRemoveDequien', 'btnDPersonaSobre', 'staticText17'],
            'staticText9' :[u'A qui\xe9n se le dirigi\xf3 esta intervenci\xf3n', 'buttonAQuien', 'buttonRemoveAquien','btnDPersonaAquien','staticText19'],
            'staticText86':[u'Respuesta a la intervenci\xf3n', 'txtIntRespuesta', 'txtLongIntRes'],
            'staticText84':[u'Impacto de la intervenci\xf3n', 'txtIntImpacto', 'txtLongIntImp'],
            'staticText88':[u'Observaciones', 'txtIntObservaciones','txtLongIntObs'],
            
            'staticText85':[u'Comentarios','txtIntComentarios','txtLongIntComent'],
            "staticText15":[u"Exportar intervenci\xf3n","staticText15", "checkBoxIntExportar"]
    
            },
        'NBFuentePersonal':{
            'staticText12':[u'Persona sobre qui\xe9n se aporta informaci\xf3n','btnAddFtePersonaRel','btnRemoveFtePersonaRel','btnDPersonaRel','staticTextRelPersona' ],
            'staticText25':[u'Conexi\xf3n con la informaci\xf3n','buttonFteConexionInformacion','buttonRemoveFteConexionInf','staticTextConexionInfo'],
            
            'staticText23':[u'Exportar fuente personal','checkBoxFteConfidencialidad'],
            'staticText26':[u'Idioma','choiceFteIdioma'],
            'staticText28':[u'Lengua ind\xedgena','btnAddFteLenguaIndigena', 'btnDelFteLenguaIndigena','staticFteLenguaIndigena'],
            'staticText33':[u'Observaciones','textCtrlFteObservaciones','txtLongFPObs'],
            'staticText37':[u'Confiabilidad','btnAddFteConfiabilidad','btnDelFteConfiabilidad','staticFteConfiabilidad'],
            'staticText42':[u'Comentarios','textCtrlFteComentarios','txtLongFPComent'],
            },
        'NBFuenteDocumental':{
            'staticText62':[u'Tipo de fuente','btnPubTipoPub','btnRemovePubTipoPub','txtPubTipoPub'],
            'staticText59':[u'Nombre del sitio','textCtrlPubNombreSitio'],
            'staticText60':[u'Liga a la fuente','textCtrlPubLigaSitio','btnAbrirLiga'],
            'staticText61':[u'Fecha de consulta','choicePubTipofechaconsulta','FDFCdia','FDFCmes','FDFCanio'],
            'staticText63':[u'Idioma','choicePubIdioma'],
            'staticText64':[u'Lengua ind\xedgena','btnAddDocLenguaIndigena','btnDelDocLenguaIndigena','staticDocLenguaIndigena'],
            'staticText65':[u'Observaciones','textCtrlPubObservaciones','txtLongFDObs'],
            'staticText66':[u'Sobre qui\xe9n se aporta informaci\xf3n','buttonPubAddPerson','buttonPubRemovePerson','btnDPersonaRel2','staticTextPubPersona'],
            'staticText68':[u'Confiabilidad','btnAddPubConfiabilidad','btnDelPubConfiabilidad','staticPubConfiabilidad'],
            'staticText69':[u'Comentarios','textCtrlPubComentarios','txtLongFDComent'],
            'staticText57':[u'Exportar fuente documental','checkBoxPubExportar'],

            }

    }

llaveCamposBaseLocal = ['staticText77', 'staticText102']
if status.cnfBaseCentral:
    llaveCamposBaseLocal = []

llaves = {
       'NBPersonasGral':[
            'staticText104', 
            'staticText110', 
            'CPfechanac' ,
            'CPCiudadania', 
            'CPEscolaridad'],

        'NBPersonasDetalles':[
            'CPOcupacion',
            'CPIdioma' ,
            'CPHablayentiendeespanol' ,
            'CPLengua' ,
            'CPOrigenEtnico' ,
            'CPReligion' ,
            'CPEstadocivil' ,
            'CPNodependientes', 
            'CPDescripciondelgrupo', 
            'staticText67', 
            'CPMonitoreo', 
        ],
        'NBPersonasAdm':[
            'CPObservaciones', 
            'staticText38', 
            'CPArchivos', 
            'staticText101', 
            'staticText103', 
            'staticText100', 
            'staticText102', 
            ],
        'NBPersonasBio':[
            'staticText89', 
            'staticText82', 
            'staticText91', 
            'staticText93', 
            'staticText90', 
            ],
        
        'NBCasosNarrativa':[
            'staticText34',    
            'staticText36',  
            ],
        'NBCasosGral':[
            'staticText29',  
            'staticText1',  
            'staticText32', 
            ],
        'NBCasosAdm':[
            'staticText94',  
            'staticText75',  
            'staticText76',  
            'staticText77',  
            'staticText78', 
            'staticText79',  
            'staticText4',  
            ],
        'NBCasosTipifica':[
            'staticText7',  
            'staticText8',  
            ],
        'NBCasosRelaciones':[
            'staticText108', 
            'staticText106', 
            ],
            
        'NBActosGral':[
            'staticText39',  
            'staticText45',  
             
            'staticText49',  
            'staticText46',  
            'staticText47',  
            'staticTextEdadOcurreActo', 
           
            'staticText48',  
            ],
            
        'NBActosPerp':[
            'staticText51',  
            'staticText52', 
            'staticText54', 
 
            'staticText14',  
            ],
        'NBNormatividad':[
            'staticText95', 
            'staticText97', 
            'staticText5'

            ],
        'NBIntervenciones':[
            "staticText15",
            'staticText21', 
            'staticText9' , 
            'staticText86', 
            'staticText84', 
            'staticText88', 
            'staticText85', 
            ],
        'NBFuentePersonal':[
            'staticText23',
            'staticText12', 
            'staticText25', 
 
            'staticText26', 
            'staticText28', 
            'staticText33', 
            'staticText37', 
            'staticText42', 
            ],
        'NBFuenteDocumental':[
            'staticText57',
            'staticText62', 
            'staticText59', 
            'staticText60', 
            'staticText61', 
            'staticText63',
            'staticText64',
            'staticText65',
            'staticText66',
            'staticText68',
            'staticText69',

            ]
            
            
            
            
}


    
tablaObjetos = {}
#tablaObjetos es la misma tablaCampos, pero sin la jerarquia de la pestania
for i in tablaCampos.keys():
    for j in tablaCampos[i].keys():
        tablaObjetos[j] = tablaCampos[i][j]
        

opcionmenu={}
opcionmenudescrip={}
opciones = {}
l = None

def ScreenConfig(self, parentname):
    NB = self.NBMain
    NB1 = self.NBCasos
    verdad = NB._windows[0] == NB1
    for i in NBconfig:
        if type(i) == tuple:
            tablapestania[i[0]] = (i[2],parentname)
            clave = i[0]
        if type(i) == list:
            for j in i:
                tablapestania[j[0]] = (j[2],clave)
    registro=session.query(ConfigTdt).filter(ConfigTdt.tipo == u'ScreenConfig').all()
    opciones = {}
    if registro:
        l = registro[0]
        try:
            opciones = pickle.loads(str(l.contenido))
        except:
            print str(l.contenido)
            MError(self, u"No se pudieron cargar opciones de configuraci\xf3n de pantallas "+str(sys.exc_info()[1]))
        
        for i in opciones.keys():
            if not opciones[i]:
                if i in tablapestania.keys():
                    padre=self.__getattribute__(tablapestania[i][1])
                    pestania = self.__getattribute__(i)
                    for j in range(len(padre._windows)):
                        if padre._windows[j] == pestania:
                            padre.RemovePage(j)
                            
                            break
                if i in tablaObjetos.keys():
                    objetos = [i] + tablaObjetos[i][1:]
                    
                    for j in objetos:
                        campo = self.__getattribute__(j)
                        campo.Show(False)
                        
                    
        

def CargaOpcionMenu(lista=None):
    global opciones
    global l
    registro=session.query(ConfigTdt).filter(ConfigTdt.tipo == u'ScreenConfig').all()
    opciones = {}
    if registro:
        try:
            l = registro[0]
            opciones = pickle.loads(str(l.contenido))
            
            for i in opciones.keys():
                opcionmenu[i]=opciones[i]
        except:
            print "no se cargaron opciones de pantalla"
    else:
        l = None
        
        
        
    
    for i in lista:
        
        if type(i) == tuple:
                #opcionmenu[i[0]]=True
                opcionmenudescrip[i[0]]=i[1]
                 
        if type(i) == list:
                CargaOpcionMenu(i)
    
    
    
def armaTree(lista, raiz, tree):
     
    for i in lista:
        if type(i) == tuple:
            flag=''
            if i[0] in opcionmenu.keys():
                if not opcionmenu[i[0]]:
                    flag = ' [NO]'
                else:
                    flag=''
            item = tree.AppendItem(raiz, i[1]+flag)
            tree.SetPyData(item, i[0])
            
            if i[0] in tablaCampos.keys():
                pestania=i[0]
                 
                 
                armaTreeCampos(tablaCampos[pestania], llaves[pestania], item, tree)
            
            
             
        if type(i) == list:
            armaTree(i, item, tree)


def armaTreeCampos(listaCampos, llaves,  raiz, tree):
     
    #for i in listaCampos.keys():
    for i in llaves:
        if i not in llaveCamposBaseLocal:
            obj = i
            descripcion =  listaCampos[i][0]
            flag=''
            if i in opcionmenu.keys():
                if not opcionmenu[i]:
                    flag = ' [NO]'
    
            item = tree.AppendItem(raiz, descripcion+flag)
            tree.SetPyData(item, i)
            
             
        
            
def setDescrip(item, key, tree):
    flag = ''
   
    if not opcionmenu[key]:
        flag = ' [NO]'
    if key in opcionmenudescrip.keys():
        tree.SetItemText(item,opcionmenudescrip[key]+flag )
    if key in tablaObjetos.keys():
        tree.SetItemText(item,tablaObjetos[key][0]+flag )
            
class Frame3(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME3, name='', parent=prnt,
              pos=wx.Point(24, 55), size=wx.Size(530, 651),
              style=wx.DEFAULT_FRAME_STYLE, title='Configuraci\xf3n')
        self.SetClientSize(wx.Size(514, 615))
        self.Bind(wx.EVT_CLOSE, self.OnFrame3Close)

        self.panel1 = wx.Panel(id=wxID_FRAME3PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(514, 615),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(255, 174, 136))

        self.tree1 = wx.TreeCtrl(id=wxID_FRAME3TREE1, name='tree1',
              parent=self.panel1, pos=wx.Point(48, 64), size=wx.Size(424, 456),
              style=wx.TR_HAS_BUTTONS)
        self.tree1.Bind(wx.EVT_TREE_ITEM_ACTIVATED,
              self.OnTree1TreeItemActivated, id=wxID_FRAME3TREE1)

        self.button1 = wx.Button(id=wxID_FRAME3BUTTON1, label='Cerrar',
              name='button1', parent=self.panel1, pos=wx.Point(208, 560),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME3BUTTON1)

        self.staticText1 = wx.StaticText(id=wxID_FRAME3STATICTEXT1,
              label='Visibilidad de pesta\xf1as y campos de captura',
              name='staticText1', parent=self.panel1, pos=wx.Point(48, 16),
              size=wx.Size(288, 16), style=0)
        self.staticText1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)
        root = self.tree1.AddRoot(u'Configuraci\xf3n')
        CargaOpcionMenu(lista=NBconfig)
        armaTree(NBconfig, root, self.tree1)
        self.tree1.Expand(root)
        


        
        
        
    def agregaboxes(self):
        self.controles={}
        for i in range(5):
            id = wx.NewId()
            self.controles[i]= wx.CheckBox(id=id, label='checkBox'+str(i),
              name='checkBoxx'+str(i), parent=self, pos=wx.Point(96, 100 + i * 15),
                     size=wx.Size(70, 13), style=0)

    def OnButton1Button(self, event):
        self.Close()
        

        event.Skip()

    def OnTree1TreeItemActivated(self, event):
        item = event.GetItem()
        #itemData = self.tree1.GetItemData(item)
        itemData = self.tree1.GetPyData(item)
        if itemData in itemsNoModificables:
            return
        
        if itemData:
            
            if itemData in opcionmenu.keys():    
                opcionmenu[itemData] = not opcionmenu[itemData]
            else:
                opcionmenu[itemData] = False
                
            setDescrip(item, itemData, self.tree1)
        
        
        event.Skip()

    def OnFrame3Close(self, event):
        global l
        if not l:
            l = ConfigTdt(u'ScreenConfig')
            
            l.descripcion = u'Config de pantallas 1'
        
        l.contenido=pickle.dumps(opcionmenu)
        session.add(l)
        session.flush()
        self.MakeModal(False) 
        
        
        event.Skip()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)

    frame.Show()

    app.MainLoop()
