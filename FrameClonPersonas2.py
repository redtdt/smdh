#-----------------------------------------------------------------------------
# Name:        FrameClonPersonas2.py
#
#
# RCS-ID:      $Id: FrameClonPersonas2.py $
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
#Boa:Frame:frameClonPersonas2

import wx
from module2 import status, Persona, session, MError, updateStatusC3
from FrameClonPersonas import ordenObjeto
from dlgRelacionar import aRelacionar
from persona_similar import persona_sim
from moduleClonPersona import clonaPersona

def create(parent):
    return frameClonPersonas2(parent)

[wxID_FRAMECLONPERSONAS2, wxID_FRAMECLONPERSONAS2CLONAR, 
 wxID_FRAMECLONPERSONAS2PANEL1, wxID_FRAMECLONPERSONAS2RELC3, 
] = [wx.NewId() for _init_ctrls in range(4)]

class frameClonPersonas2(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMECLONPERSONAS2,
              name='frameClonPersonas2', parent=prnt, pos=wx.Point(455, 225),
              size=wx.Size(405, 200), style=wx.DEFAULT_FRAME_STYLE,
              title='Copiar / Relacionar una persona al contenedor 3')
        self.SetClientSize(wx.Size(389, 164))
        self.Bind(wx.EVT_CLOSE, self.OnFrameClonPersonas2Close)

        self.panel1 = wx.Panel(id=wxID_FRAMECLONPERSONAS2PANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(389, 164),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'MS Shell Dlg 2'))

        self.relC3 = wx.Button(id=wxID_FRAMECLONPERSONAS2RELC3,
              label='Relacionar con persona en contenedor 3', name='relC3',
              parent=self.panel1, pos=wx.Point(96, 96), size=wx.Size(208, 23),
              style=0)
        self.relC3.Bind(wx.EVT_BUTTON, self.OnRelC3Button,
              id=wxID_FRAMECLONPERSONAS2RELC3)

        self.clonar = wx.Button(id=wxID_FRAMECLONPERSONAS2CLONAR,
              label='Copiar a contenedor 3', name='clonar', parent=self.panel1,
              pos=wx.Point(96, 32), size=wx.Size(208, 23), style=0)
        self.clonar.Bind(wx.EVT_BUTTON, self.OnClonarButton,
              id=wxID_FRAMECLONPERSONAS2CLONAR)

    def __init__(self, parent):
        self._init_ctrls(parent)
        print "iniciando clon personas"
        

    def OnBtnRelButton(self, event):
        
            
        event.Skip()

    def OnBtnClonButton(self, event):
        
        event.Skip()

    def OnFrameClonPersonas2Close(self, event):
        self.MakeModal(False) 
        event.Skip()

    def OnButton1Button(self, event):
        event.Skip()

    def OnRelC3Button(self, event):
        personas3 = session.query(Persona).filter(Persona.clavestatus == 3).all()
        personas3sim = [(p, persona_sim(p, self.personaActual)) for p in personas3]
        personas3sim.sort(lambda x,y:ordenObjeto(x,y)    )

        pers = aRelacionar(self, [(p, p.Descriptor()) for p,s in personas3sim])

        if pers:
            self.personaActual.personarelacionadac3 = pers.id
            session.add(self.personaActual)
            session.flush()
            MError(self, "La persona fue relacionada en el contenedor 3")
        event.Skip()

    def OnClonarButton(self, event):
        if self.personaActual:
            p=clonaPersona(self, self.personaActual)
            self.personaActual.personarelacionadac3 = p.id
            session.add(self.personaActual)
            session.flush()
            updateStatusC3(self.parent, status.personaActual)
            
            MError(self, "La persona fue copiada al contenedor 3")
        event.Skip()
        
def frameClonPersona(self, P):
    f=frameClonPersonas2(self)
    f.personaActual = P
    f.parent = self
    
    f.MakeModal()
    f.Show()
    print "abandonando clon personas"
