#-----------------------------------------------------------------------------
# Name:        FrameClonPersonas.py
#
#
# RCS-ID:      $Id: FrameClonPersonas.py $
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
#Boa:Frame:FramePersonasAC3

import wx
import module2
from module2 import MyClientData, Persona, Caso, session, status, MError, LlenaCtrlCasos, MyClientDataSelection
from moduleClonPersona import clonaPersona, clonaCaso
from persona_similar import persona_sim
from caso_similar import caso_sim
from dlgRelacionar import aRelacionar

listaPersonas=[]

def create(parent):
    return FramePersonasAC3(parent)

[wxID_FRAMEPERSONASAC3, wxID_FRAMEPERSONASAC3BTNCERRAR, 
 wxID_FRAMEPERSONASAC3BTNCOPIACASO, wxID_FRAMEPERSONASAC3BTNPASARAC3, 
 wxID_FRAMEPERSONASAC3BTNRELACIONACASO, wxID_FRAMEPERSONASAC3BTNRELACIONAR, 
 wxID_FRAMEPERSONASAC3LISTPERSONAS, wxID_FRAMEPERSONASAC3NOMBREDELCASO, 
 wxID_FRAMEPERSONASAC3OPERACIONES, wxID_FRAMEPERSONASAC3PANEL1, 
] = [wx.NewId() for _init_ctrls in range(10)]

class FramePersonasAC3(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEPERSONASAC3,
              name='FramePersonasAC3', parent=prnt, pos=wx.Point(173, 152),
              size=wx.Size(1055, 543), style=wx.DEFAULT_FRAME_STYLE,
              title='Pasar un caso a contenedor 3')
        self.SetClientSize(wx.Size(1039, 507))
        self.Bind(wx.EVT_CLOSE, self.OnFramePersonasAC3Close)

        self.panel1 = wx.Panel(id=wxID_FRAMEPERSONASAC3PANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(1039, 507),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'MS Shell Dlg 2'))

        self.listPersonas = wx.ListBox(choices=[],
              id=wxID_FRAMEPERSONASAC3LISTPERSONAS, name='listPersonas',
              parent=self.panel1, pos=wx.Point(32, 48), size=wx.Size(608, 288),
              style=wx.LB_EXTENDED | wx.HSCROLL)
        self.listPersonas.Bind(wx.EVT_LISTBOX_DCLICK,
              self.OnListPersonasListboxDclick,
              id=wxID_FRAMEPERSONASAC3LISTPERSONAS)
        self.listPersonas.Bind(wx.EVT_LISTBOX, self.OnListPersonasListbox,
              id=wxID_FRAMEPERSONASAC3LISTPERSONAS)

        self.btnRelacionar = wx.Button(id=wxID_FRAMEPERSONASAC3BTNRELACIONAR,
              label='Relacionar con persona existente en C3',
              name='btnRelacionar', parent=self.panel1, pos=wx.Point(656, 120),
              size=wx.Size(224, 23), style=0)
        self.btnRelacionar.Enable(False)
        self.btnRelacionar.Bind(wx.EVT_BUTTON, self.OnBtnRelacionarButton,
              id=wxID_FRAMEPERSONASAC3BTNRELACIONAR)

        self.btnPasaraC3 = wx.Button(id=wxID_FRAMEPERSONASAC3BTNPASARAC3,
              label='Pasar persona a Contenedor 3', name='btnPasaraC3',
              parent=self.panel1, pos=wx.Point(656, 152), size=wx.Size(224, 23),
              style=0)
        self.btnPasaraC3.Enable(False)
        self.btnPasaraC3.Bind(wx.EVT_BUTTON, self.OnBtnPasaraC3Button,
              id=wxID_FRAMEPERSONASAC3BTNPASARAC3)

        self.btnRelacionaCaso = wx.Button(id=wxID_FRAMEPERSONASAC3BTNRELACIONACASO,
              label='Relacionar un caso con otro existente en C3',
              name='btnRelacionaCaso', parent=self.panel1, pos=wx.Point(656,
              184), size=wx.Size(224, 23), style=0)
        self.btnRelacionaCaso.Bind(wx.EVT_BUTTON, self.OnBtnRelacionaCasoButton,
              id=wxID_FRAMEPERSONASAC3BTNRELACIONACASO)

        self.btnCopiaCaso = wx.Button(id=wxID_FRAMEPERSONASAC3BTNCOPIACASO,
              label='Pasar caso a C3', name='btnCopiaCaso', parent=self.panel1,
              pos=wx.Point(656, 216), size=wx.Size(224, 23), style=0)
        self.btnCopiaCaso.Bind(wx.EVT_BUTTON, self.OnBtnCopiaCasoButton,
              id=wxID_FRAMEPERSONASAC3BTNCOPIACASO)

        self.Operaciones = wx.StaticText(id=wxID_FRAMEPERSONASAC3OPERACIONES,
              label='Operaciones', name='Operaciones', parent=self.panel1,
              pos=wx.Point(720, 48), size=wx.Size(87, 19), style=0)
        self.Operaciones.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.NombreDelCaso = wx.StaticText(id=wxID_FRAMEPERSONASAC3NOMBREDELCASO,
              label='            ', name='NombreDelCaso', parent=self.panel1,
              pos=wx.Point(32, 16), size=wx.Size(36, 13), style=0)

        self.btnCerrar = wx.Button(id=wxID_FRAMEPERSONASAC3BTNCERRAR,
              label='Cerrar', name='btnCerrar', parent=self.panel1,
              pos=wx.Point(496, 376), size=wx.Size(75, 23), style=0)
        self.btnCerrar.Bind(wx.EVT_BUTTON, self.OnBtnCerrarButton,
              id=wxID_FRAMEPERSONASAC3BTNCERRAR)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.personaActual=None
        self.casoActual = status.casoActual
        self.parent = parent

    def OnFramePersonasAC3Close(self, event):
        LlenaCtrlCasos(self.parent.listaCasos)
        self.MakeModal(False) 
        self.Destroy()
        event.Skip()

    def OnListPersonasListboxDclick(self, event):
        #self.personaActual=MyClientData(event)
        #if self.personaActual:
        #    self.btnRelacionar.Enable()
        #    self.btnPasaraC3.Enable()
            
        
        
        event.Skip()

    def OnBtnPasaraC3Button(self, event):
        global listaPersonas
        if listaPersonas:
            for pi in listaPersonas:
            #if self.personaActual:
                p=clonaPersona(self, pi)
                #self.personaActual.personarelacionadac3 = p.id
                #session.add(self.personaActual)
                #session.flush()
            MError(self, u"Se complet\xf3 el copiado de la(s) persona(s) al contenedor 3")
            llenaCtrlPersonas(self, self.casoActual)
            self.btnRelacionar.Enable(False)
            self.btnPasaraC3.Enable(False)
            listaPersonas=[]
            
        
        event.Skip()

    def OnBtnRelacionarButton(self, event):
        global listaPersonas
        if listaPersonas:
            self.personaActual = listaPersonas[0]
            personas3 = session.query(Persona).filter(Persona.clavestatus == 3).all()
            personas3sim = [(p, persona_sim(p, self.personaActual)) for p in personas3]
            personas3sim.sort(lambda x,y:ordenObjeto(x,y)    )
            for i in personas3sim:
                print i[0], i[1]
            pers = aRelacionar(self, [(p, p.Descriptor()) for p,s in personas3sim])
            
            if pers:
                self.personaActual.personarelacionadac3 = pers.id
                session.add(self.personaActual)
                session.flush()
                MError(self, u"Se estableci\xf3 la relaci\xf3n de la persona con otra persona presente en C3")
                llenaCtrlPersonas(self, self.casoActual)
                self.btnRelacionar.Enable(False)
                self.btnPasaraC3.Enable(False)
                
            
            
        event.Skip()

    def OnBtnRelacionaCasoButton(self, event):
        casos3 = session.query(Caso).filter(Caso.clavestatus == 3).all()
        casos3sim = [(c, caso_sim(c, self.casoActual)) for c in casos3]
        casos3sim.sort(lambda x,y:ordenObjeto(x,y)    )
        for i in casos3sim:
            print i[0], i[1]
        casosarel = aRelacionar(self, [(c, c.Descriptor()) for c,s in casos3sim])
        if casosarel:
            self.casoActual.casorelacionadoc3 = casosarel.id
            self.casoActual.clavestatusc3 = 3
            session.add(self.casoActual)
            session.flush()
            module2.updateStatusC3(self.parent, status.casoActual)
            MError(self, u"Se estableci\xf3 la relaci\xf3n del caso con otro caso presente en C3")
            # llenar que?
            
            
        event.Skip()

    def OnBtnCopiaCasoButton(self, event):
        if self.casoActual:
            c=clonaCaso(self, self.casoActual)
            self.casoActual.casorelacionadoc3 = c.id
            self.casoActual.clavestatusc3 = 2
            session.add(self.casoActual)
            session.flush()
            c.refrescar()
            module2.updateStatusC3(self.parent, status.casoActual)
            MError(self, u"Se complet\xf3 el copiado del caso al contenedor 3")
            
        event.Skip()

    def OnBtnCerrarButton(self, event):
        LlenaCtrlCasos(self.parent.listaCasos)
        self.MakeModal(False)
        self.Destroy()
        event.Skip()

    def OnListPersonasListbox(self, event):
        global listaPersonas 
        listaPersonas = MyClientDataSelection(event)
        if listaPersonas:

            self.btnRelacionar.Enable()
            self.btnPasaraC3.Enable()

        event.Skip()
        
def ordenObjeto(x,y):
    if x[1] or y[1]:
        return cmp(y[1],x[1])
    else:
        return cmp(x[0].Descriptor(), y[0].Descriptor())
    
def frameClonCaso(self, miCaso, nombreDelCaso=''):
    f=FramePersonasAC3(self)
    f.parent = self
    f.casoActual = miCaso
    llenaCtrlPersonas(f, miCaso)
    f.NombreDelCaso.SetLabel(nombreDelCaso)
    f.MakeModal()
    f.Show()
    
def llenaCtrlPersonas(f, miCaso):
    casoListo = True
    personas = miCaso.Personas_relacionadas()
    personas_pendientes = []
    for p in personas:
        if not p.personarelacionadac3:
            localstatusC3 = ''
            casoListo = False
        elif str(p.personarelacionadac3)[:-4] == str(p.id)[:-4]:
            localstatusC3 = ' / presente en C3'
        else:
            localstatusC3 = ' / relacionada con otra persona en C3'
            
        personas_pendientes.append((p,p.Descriptor()+localstatusC3))
    #personas_pendientes = [(p,p.Descriptor()) for p in personas if not p.personarelacionadac3]
    
    module2.LlenaCtrl3(f.listPersonas, personas_pendientes)
    
    f.btnCopiaCaso.Show(casoListo)
    f.btnRelacionar.Show()
    f.btnPasaraC3.Show()
    

    
