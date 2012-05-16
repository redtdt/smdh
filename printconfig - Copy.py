#-----------------------------------------------------------------------------
# Name:        printconfig.py
#
#
# RCS-ID:      $Id: printconfig.py $
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
import wx.lib.flatnotebook

from moduleRep6 import por_imprimir
from moduleRep6 import campos
from module2 import status, LlenaAyuda
frame=None



entidad_alias={'Caso':'Caso', 
               'actos':'Actos', 
               'RolPerpetradores':'Perpetradores',
               'PPublicaciones':'Fuente documental',
               'fuentes':'Fuente personal',
               'intervenciones':u'Intervenciones',
               'Personas_relacionadas':'Personas relacionadas',
               'DetallesBio':u'Datos biogr\xe1ficos', 
               'localidades':u'Localizaci\xf3n detallada',
               'Persona':u'Personas',
               }





def create(parent):
    return Frame3(parent)

[wxID_FRAME3, wxID_FRAME3FN, 
] = [wx.NewId() for _init_ctrls in range(2)]


matCtrl={}
matflag={}

def camposTree(mat, entidad, NB, init=False, tipoRep="normal"):
    global matflag
    # matflag contiene una correspondencia entre (entidad, campo) y control que controla su valor
    if init:
        matflag={}
    matflag[entidad]={} # ??? siempre ???
    matflag[entidad][tipoRep]={}
    
    if entidad not in status.printOpt.keys():
        status.printOpt[entidad]={}
    if tipoRep not in status.printOpt[entidad].keys():
            status.printOpt[entidad][tipoRep]={}
    #se genera un nuevo panel para presentar las opciones
    id = wx.NewId()
    panel = wx.Panel(id=id, 
              name=entidad,
              parent=NB,
              pos=wx.Point(0, 0), 
              size=wx.Size(540, 431), 
              style=wx.TAB_TRAVERSAL)
    txtEntidad = entidad
    if txtEntidad in entidad_alias.keys():
       txtEntidad =  entidad_alias[txtEntidad]
    #se agrega el panel al noteBook (NB)
    NB.AddPage(imageId=-1, page=panel, select=init, text=txtEntidad)
    # se agrega el boton de regresar al panel    
    id = wx.NewId()
    boton = wx.Button(id=id, label='Regresar',
              name='Regresar', parent=panel, pos=wx.Point(500, 20),
              size=wx.Size(75, 23), style=0)
    boton.Bind(wx.EVT_BUTTON, OnRegresarButton,
              id=id)
    contextHelpButton1 = wx.ContextHelpButton(parent=panel,
              pos=wx.Point(700, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)
    boton.SetHelpText(u'Haz clic aqu\xed una vez que hayas despalomeado los campos que no deseas que aparezcan en tu reporte. Regresar\xe1s a la pantalla de "Emisi\xf3n de reportes"')
    # ojo pendiente
              
    
    
    n = 0
    print mat[entidad]
    for i1 in mat[entidad]: 
        #para cada campo imprimible de la entidad se agrega un checkbox
        #print "i1 ", i1
        miCampo = i1.split('.')[0]
        id = wx.NewId()
        
        if tipoRep not in status.printOpt[entidad].keys():    
            status.printOpt[entidad][tipoRep]={}
        
        if miCampo not in status.printOpt[entidad][tipoRep].keys():
            status.printOpt[entidad][tipoRep][miCampo]=True
        
        
        label = campos[entidad][miCampo][0]
        if type(label) == tuple:
            label = ', '.join(label)
        nivel = nivelCampo(entidad, miCampo) #recupera datos para indentacion
        col = 93 + (nivel - 1) * 15
        
        #print "entidad ",entidad
        control= wx.CheckBox(id=id, label=label,  #genera un control checkbox para cada campo
              name=label, parent=panel, pos=wx.Point(col, 30 + n * 15),
                     size=wx.Size(300, 13), style=0)
        control.Bind(wx.EVT_CHECKBOX, OnCheckbox,
              id=id)
        
        myId = control.GetId()  
        matCtrl[myId] = (entidad, miCampo, tipoRep)  # asocia el id del control con (entidad, campo) (y tiporep?)
        control.SetValue(status.printOpt[entidad][tipoRep][miCampo])
        
        matflag[entidad][tipoRep][miCampo]=control
        
        
        n = n + 1
        if miCampo in mat.keys():
            camposTree(mat, miCampo, NB, tipoRep=tipoRep)
        
def OnCheckbox(event):
    control = event.GetEventObject()
    i= control.GetId()  
    print "evento", i
    print matCtrl[i]
    entidad, campo, tipoRep = matCtrl[i]
    status.printOpt[entidad][tipoRep][campo]=control.GetValue()
    

def seImprime(entidad, campo, tipoRep):
    print "checando ",campo," en ",entidad, tipoRep
    if entidad in status.printOpt.keys():
        if tipoRep in status.printOpt[entidad].keys():
             if campo in status.printOpt[entidad][tipoRep].keys():
                 
                print "regresando ",status.printOpt[entidad][tipoRep][campo], " para ",entidad, tipoRep, campo
                return status.printOpt[entidad][tipoRep][campo]
    return True
def OnRegresarButton(event):
    global frame
    frame.Close()

class Frame3(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME3, name='', parent=prnt,
              pos=wx.Point(87, 2), size=wx.Size(847, 723),
              style=wx.DEFAULT_FRAME_STYLE, title='Opciones de impresi\xf3n')
        self.SetClientSize(wx.Size(831, 687))

        self.FN = wx.lib.flatnotebook.FlatNotebook(id=wxID_FRAME3FN, name='FN',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(831, 687), style=0)
        self.FN.SetBackgroundColour(wx.Colour(221, 255, 221))

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.FN.SetWindowStyleFlag(wx.lib.flatnotebook.FNB_NO_X_BUTTON|wx.lib.flatnotebook.FNB_NODRAG)
        self.FN.Layout()
       
        #camposTree(por_imprimir, 'Caso', self.FN, init=True)
        #if 'Actos' in status.printOpt.keys():
        #    status.printOpt['actos']=matflag['Actos']
            
        self.FN.Layout()
        



def nivelCampo(entidad, campo):
    print campos[entidad][campo]
    if len(campos[entidad][campo]) <3:
        return 3
    return campos[entidad][campo][2]
        
def printConfig(prnt, entidad, tipoRep='normal'):
    global frame
    frame = Frame3(prnt)
    camposTree(por_imprimir, entidad, frame.FN, init=True, tipoRep=tipoRep)
    if 'Actos' in status.printOpt.keys():
            status.printOpt['actos']=matflag['Actos']
    LlenaAyuda(frame, 'printconfig')
    return frame
    

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
