#-----------------------------------------------------------------------------
# Name:        FrameCompare.py
#
#
# RCS-ID:      $Id: FrameCompare.py $
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
#Boa:Frame:frameCompare

# -*- coding: utf-8 -*-

import wx
from module2 import session, Caso, Persona, MError
from xmlcompare import isEqualXML
import xmlcompare
from moduleExp1 import GeneraEnvio
import moduleExp1
import codecs
from getFileDialog import selectFile


def create(parent):
    return frameCompare(parent)

[wxID_FRAMECOMPARE, wxID_FRAMECOMPAREBTNCOMPARAR, wxID_FRAMECOMPAREBTNGUARDAR, 
 wxID_FRAMECOMPAREPANEL1, wxID_FRAMECOMPARERESULTADO, 
 wxID_FRAMECOMPARETXTACTIVIDAD, 
] = [wx.NewId() for _init_ctrls in range(6)]

class frameCompare(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMECOMPARE, name='frameCompare',
              parent=prnt, pos=wx.Point(399, 105), size=wx.Size(754, 617),
              style=wx.DEFAULT_FRAME_STYLE, title='Diferencias')
        self.SetClientSize(wx.Size(738, 581))

        self.panel1 = wx.Panel(id=wxID_FRAMECOMPAREPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(738, 581),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'MS Shell Dlg 2'))

        self.Resultado = wx.TextCtrl(id=wxID_FRAMECOMPARERESULTADO,
              name='Resultado', parent=self.panel1, pos=wx.Point(8, 32),
              size=wx.Size(712, 528), style=wx.TE_MULTILINE, value='')

        self.btnComparar = wx.Button(id=wxID_FRAMECOMPAREBTNCOMPARAR,
              label='Comparar', name='btnComparar', parent=self.panel1,
              pos=wx.Point(8, 0), size=wx.Size(75, 23), style=0)
        self.btnComparar.Bind(wx.EVT_BUTTON, self.OnBtnCompararButton,
              id=wxID_FRAMECOMPAREBTNCOMPARAR)

        self.txtActividad = wx.StaticText(id=wxID_FRAMECOMPARETXTACTIVIDAD,
              label='Comparando contenedores.....', name='txtActividad',
              parent=self.panel1, pos=wx.Point(568, 4), size=wx.Size(151, 13),
              style=0)
        self.txtActividad.SetForegroundColour(wx.Colour(200, 0, 0))

        self.btnGuardar = wx.Button(id=wxID_FRAMECOMPAREBTNGUARDAR,
              label='Guardar reporte', name='btnGuardar', parent=self.panel1,
              pos=wx.Point(88, 0), size=wx.Size(88, 23), style=0)
        self.btnGuardar.Enable(False)
        self.btnGuardar.Bind(wx.EVT_BUTTON, self.OnBtnGuardarButton,
              id=wxID_FRAMECOMPAREBTNGUARDAR)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.grupo = None
        self.txtActividad.SetLabel('')
    def OnBtnCompararButton(self, event):
        comparaColeccion(self, self.grupo)
        event.Skip()

    def OnBtnGuardarButton(self, event):
        nombre = selectFile(self, mask='*.txt', path="/smdh2/archivos", accion='Guardar', label='Guardar como', titulo='Guardar reporte de diferencias')
        f=codecs.open(nombre,'w','utf-8')
        f.write(self.Resultado.GetValue())
        
        f.close()
        MError(self, u'El reporte ha sido guardado como '+nombre)
        self.btnGuardar.Enable(False)
        event.Skip()

def frameCompara(prnt, grupo):
    f = frameCompare(prnt)
    f.grupo = grupo
    #f.MakeModal()
    f.Show()
    
def comparaColeccion(self, grupo):
    Traduccion = {
    'ColeccionCasos':u'Casos',
    'ColeccionPersonas':u'Personas'
    }
    salida = self.Resultado

    
    coleccionCasosT1 = session.query(Caso).filter(Caso.clavegrupo == grupo).filter(Caso.clavestatus == 1).order_by(Caso.id).all() #[:5]
    coleccionPersonasT1 = session.query(Persona).filter(Persona.clavegrupo == grupo).filter(Persona.clavestatus == 1).order_by(Persona.id).all() #[:5]
    
    coleccionCasosT2 = session.query(Caso).filter(Caso.clavegrupo == grupo).filter(Caso.clavestatus == 2).order_by(Caso.id).all() #[:5]
    coleccionPersonasT2 = session.query(Persona).filter(Persona.clavegrupo == grupo).filter(Persona.clavestatus == 2).order_by(Persona.id).all() #[:5]
    self.txtActividad.SetLabel('Comparando contenedores...')
    self.Update()
    moduleExp1.SWid=True
    moduleExp1.exportando=False
    envio1 = GeneraEnvio('','','',coleccionCasosT1, coleccionPersonasT1)
    r=envio1.toxml()
    fileObj = file( '1.xml', "w" )
    fileObj.write(r)
    fileObj.close()
    
    
    
    self.Update()
    
    envio2 = GeneraEnvio('','','',coleccionCasosT2, coleccionPersonasT2)
    r=envio2.toxml()
    fileObj = file( '2.xml', "w" )
    fileObj.write(r)
    fileObj.close()
    
    
    
    moduleExp1.SWid=False
    
    self.Update()
    xmlcompare.topLevel = 'ColeccionCasos'
    res1 = isEqualXML(envio1.childNodes[0].childNodes[1], envio2.childNodes[0].childNodes[1])
    xmlcompare.topLevel = 'ColeccionPersonas'
    res2 = isEqualXML(envio1.childNodes[0].childNodes[2], envio2.childNodes[0].childNodes[2])
    codificacion = 'utf-8'
    #codificacion = 'latin-1'
    lista=[]
    for res in [res1, res2]:
        if res:
            
           lista.append(Traduccion[res['objeto']]+'\n\n')
           #salida.WriteText(res['objeto']+'\n')
           
           for resultado in res['resultado']:
               
               accion = str(resultado['accion']).decode(codificacion, 'replace')
            

               campo  = resultado['campo']#.decode(codificacion, 'replace')


               contexto = resultado['contexto']#.decode(codificacion, 'replace')
               tmpcampo = campo if campo else '??'
               print type(tmpcampo)
               tmpcontexto = "(en "+contexto+")" if contexto else ' '
               expr = "%s: %s\n%s\n\n"%(accion, tmpcampo, tmpcontexto)
               print "ok"
               lista.append(expr)
               
               
           
    salida.SetValue(" ".join(lista))
    self.txtActividad.SetLabel('Reporte listo')
    self.btnGuardar.Enable()
