#-----------------------------------------------------------------------------
# Name:        Frametree.py
#
#
# RCS-ID:      $Id: Frametree.py $
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

from  module2 import  ConfigTdt, status
import wx
import wx.gizmos
import pickle

session = status.session

def create(parent):
    return Frame3(parent)

[wxID_FRAME3, wxID_FRAME3TREE1, 
] = [wx.NewId() for _init_ctrls in range(2)]

NBconfig =[('NBCasos','Casos',-1),   [('NBCasosGral', 'Datos generales',-1), ('NBCasosTipifica', 'Tipificaciones',1), ('NBCasosNarrativa','Informacion narrativa',2),
                               ('NBCasosAdm','Informacion administrativa',3), ('NBCasosRelaciones','Relaciones',4)], 
        ('NBActos','Actos',1),   [('NBActosGral','Informacion general',-1), ('NBActosPerp','Perpetradores',1), ('NBNormatividad','Normatividad',2)], 
        ('NBIntervenciones', 'Intervenciones',2), 
        ('NBFuentes','Fuentes',3), [('NBFuentePersonal','Fuente personal',0), ('NBFuenteDocumental','Fuente documental',1)], 
        
        ('NBPersonas','Personas',4), [('NBPersonasGral','Informacion general',-1), ('NBPersonasDetalles','Detalles',1),
                  ('NBPersonasAdm','Informacion administrativa',2), ('NBPersonasBio','Detalles biograficos',3)]
        ]
opcionmenu={}
opcionmenudescrip={}
opciones = {}
l = None

def CargaOpcionMenu(lista=None):
    global opciones
    global l
    registro=session.query(ConfigTdt).filter(ConfigTdt.tipo == u'ScreenConfig').filter(ConfigTdt.id == 1).all()
    opciones = {}
    if registro:
        l = registro[0]
        opciones = pickle.loads(str(l.contenido))
        print 'opciones carga', opciones
        for i in opciones.keys():
            opcionmenu[i]=opciones[i]
    else:
        l = None
        
        
        
    
    for i in lista:
        
        if type(i) == tuple:
                opcionmenu[i[0]]=True
                opcionmenudescrip[i[0]]=i[1]
                 
        if type(i) == list:
                CargaOpcionMenu(i)
    
    
def armaTree(lista, raiz, tree):
    for i in lista:
        if type(i) == tuple:
            if i[0] in opcionmenu.keys():
                if not opcionmenu[i[0]]:
                    flag = ' [NO]'
                else:
                    flag=''
            item = tree.AppendItem(raiz, i[1]+flag)
            tree.SetPyData(item, i[0])
            
             
        if type(i) == list:
            armaTree(i, item, tree)
            
def setDescrip(item, key, tree):
    flag = ''
    if not opcionmenu[key]:
        flag = ' [NO]'
    tree.SetItemText(item,opcionmenudescrip[key]+flag )
            
class Frame3(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME3, name='', parent=prnt,
              pos=wx.Point(442, 157), size=wx.Size(400, 484),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame3')
        self.SetClientSize(wx.Size(392, 457))
        self.Bind(wx.EVT_CLOSE, self.OnFrame3Close)

        self.tree1 = wx.TreeCtrl(id=wxID_FRAME3TREE1, name='tree1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(392, 457),
              style=wx.TR_HAS_BUTTONS)
        self.tree1.Bind(wx.EVT_TREE_ITEM_ACTIVATED,
              self.OnTree1TreeItemActivated, id=wxID_FRAME3TREE1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        root = self.tree1.AddRoot('Configuracion')
        CargaOpcionMenu(lista=NBconfig)
        armaTree(NBconfig, root, self.tree1)
        


        
        
        
    def agregaboxes(self):
        self.controles={}
        for i in range(5):
            id = wx.NewId()
            self.controles[i]= wx.CheckBox(id=id, label='checkBox'+str(i),
              name='checkBoxx'+str(i), parent=self, pos=wx.Point(96, 100 + i * 15),
                     size=wx.Size(70, 13), style=0)

    def OnButton1Button(self, event):
        for i in range(5):
            print self.controles[i].GetValue()
        event.Skip()

    def OnTree1TreeItemActivated(self, event):
        item = event.GetItem()
        #itemData = self.tree1.GetItemData(item)
        itemData = self.tree1.GetPyData(item)
        if itemData:
            
            opcionmenu[itemData] = not opcionmenu[itemData]
            setDescrip(item, itemData, self.tree1)
        
        
        event.Skip()

    def OnFrame3Close(self, event):
        global l
        if not l:
            l = ConfigTdt(u'ScreenConfig')
            l.id = 1
            l.descripcion = 'Config de pantallas 1'
        l.contenido=pickle.dumps(opcionmenu)
        session.add(l)
        session.flush()
        print opcionmenu
        event.Skip()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)

    frame.Show()

    app.MainLoop()
