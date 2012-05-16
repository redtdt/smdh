#-----------------------------------------------------------------------------
# Name:        frameRep5.py
#
#
# RCS-ID:      $Id: frameRep5.py $
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
import wx.lib.filebrowsebutton
from module2 import *
import module2
from moduleRep4 import generaCruce2
from moduleRep3 import ReporteAnalitico
import webbrowser
from sqlalchemy.sql import func, expression
from midataset import GeneraQueryCaso, GeneraQueryPersona
import os
from moduleRep1 import printObj
import printconfig
import pickle
from dlggetdescrip import MyDescrip
import re
import cnf
from listacampos import camposEntidad
import pprint

session = status.session


#FileNamePattern = re.compile('[a-z][a-z0-9\\\\.]*', re.IGNORECASE)
FileNamePattern = re.compile('[a-z][a-z0-9_]*', re.IGNORECASE)

def FileNameValido(str):
    r = FileNamePattern.match(str)
    if r:
        grupo = r.group()
        if r.group() == str:
            return True
    return False

# XXX construir una funcion que regrese una lista ce Casos.id en funcion al filtro activo
# luego se puede filtar el query del cruce acorde con una expresion del tipo 
#   session.query(Caso.id).filter(Caso.id.in_([50,40,12])).all()
# o sea filtro - filter(Caso.id.in_([50,40,12]))

def create(parent):
    return Frame3(parent)

[wxID_FRAME3, wxID_FRAME3BITMAPBUTTON1, wxID_FRAME3BITMAPBUTTON2, 
 wxID_FRAME3BITMAPBUTTON4, wxID_FRAME3BITMAPBUTTON5, wxID_FRAME3BITMAPBUTTON6, 
 wxID_FRAME3BTNCASOSSELECCIONADOS, wxID_FRAME3BTNLIMPIAROPCIONES, 
 wxID_FRAME3BTNPERSONAS, wxID_FRAME3BTNPRIN5, wxID_FRAME3BTNREPCASOS, 
 wxID_FRAME3BTNREPINTERVENCIONES, wxID_FRAME3BTNREPORTEACTOS, 
 wxID_FRAME3BTNSAVECFG, wxID_FRAME3BTNSAVECFGAS, 
 wxID_FRAME3BTNTIPOACTOXCARREL, wxID_FRAME3BUTTON2, 
 wxID_FRAME3CASOOPCIONESACTIVO, wxID_FRAME3CASOOPCIONESVISIBLES, 
 wxID_FRAME3CHKAPLICARSELECCION, wxID_FRAME3CHOICEPRINTCFG, 
 wxID_FRAME3COMBOBOXABRIRCON, wxID_FRAME3CONTEXTHELPBUTTON1, 
 wxID_FRAME3DELMODELO, wxID_FRAME3FILEBROWSE, wxID_FRAME3LBLAPLICARSELECCION, 
 wxID_FRAME3OPENREP, wxID_FRAME3PANEL1, wxID_FRAME3PERSONAOPCIONES, 
 wxID_FRAME3STATICTEXT1, wxID_FRAME3STATICTEXT10, wxID_FRAME3STATICTEXT11, 
 wxID_FRAME3STATICTEXT12, wxID_FRAME3STATICTEXT13, wxID_FRAME3STATICTEXT14, 
 wxID_FRAME3STATICTEXT15, wxID_FRAME3STATICTEXT2, wxID_FRAME3STATICTEXT3, 
 wxID_FRAME3STATICTEXT4, wxID_FRAME3STATICTEXT5, wxID_FRAME3STATICTEXT6, 
 wxID_FRAME3STATICTEXT7, wxID_FRAME3STATICTEXT8, wxID_FRAME3STATICTEXT9, 
 wxID_FRAME3STRCASOSSELECCIONADOS, wxID_FRAME3TEXTCTRLFILENAME, 
] = [wx.NewId() for _init_ctrls in range(46)]

def OpenBrowser(filename):
    webbrowser.open(filename)

def OpenWord(filename):
    if cnf.OSwin:
        os.system('start winword '+ filename)
    else:
        MError(None, "No disponible para Linux. Usar OpenOffice")
    
    
    
def OpenOpenWriter(filename):
    if cnf.OSwin:
        os.system('start swriter '+ filename)
    if cnf.OSlinux:
        os.system('/usr/lib/openoffice/program/swriter '+filename)
    
def OpenOpenCalc(filename):
    if cnf.OSwin:
        os.system('start scalc '+ filename)
    if cnf.OSlinux:
        os.system('/usr/lib/openoffice/program/scalc '+filename)


def OpenExcel(filename):
    if cnf.OSwin:
        os.system('start excel '+ filename)
    else:
        MError(None, "No disponible para Linux. Usar OpenOffice")
    
class Frame3(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME3, name='', parent=prnt,
              pos=wx.Point(362, 2), size=wx.Size(628, 726),
              style=wx.DEFAULT_FRAME_STYLE, title='Reportes')
        self.SetClientSize(wx.Size(612, 690))
        self.SetBackgroundColour(wx.Colour(252, 224, 129))
        self.Bind(wx.EVT_CLOSE, self.OnFrame3Close)

        self.panel1 = wx.Panel(id=wxID_FRAME3PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(612, 690),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetToolTipString('')

        self.staticText1 = wx.StaticText(id=wxID_FRAME3STATICTEXT1,
              label='Emisi\xf3n de reportes', name='staticText1',
              parent=self.panel1, pos=wx.Point(192, 32), size=wx.Size(162, 19),
              style=0)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.staticText2 = wx.StaticText(id=wxID_FRAME3STATICTEXT2,
              label='Derechos Afectados y Estado', name='staticText2',
              parent=self.panel1, pos=wx.Point(56, 272), size=wx.Size(200, 13),
              style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME3STATICTEXT3,
              label='Personas y entidades responsables de violaciones de DH',
              name='staticText3', parent=self.panel1, pos=wx.Point(56, 393),
              size=wx.Size(208, 24), style=0)
        self.staticText3.Show(True)

        self.staticText4 = wx.StaticText(id=wxID_FRAME3STATICTEXT4,
              label='Responsables involucrados en violaciones a los derechos humanos',
              name='staticText4', parent=self.panel1, pos=wx.Point(56, 328),
              size=wx.Size(208, 24), style=0)
        self.staticText4.Show(True)

        self.staticText5 = wx.StaticText(id=wxID_FRAME3STATICTEXT5,
              label='Tipo de acto vs Caracter\xedsticas relevantes',
              name='staticText5', parent=self.panel1, pos=wx.Point(56, 368),
              size=wx.Size(224, 13), style=0)
        self.staticText5.Show(True)

        self.textCtrlFilename = wx.TextCtrl(id=wxID_FRAME3TEXTCTRLFILENAME,
              name='textCtrlFilename', parent=self.panel1, pos=wx.Point(272,
              450), size=wx.Size(128, 21), style=0, value='salida')
        self.textCtrlFilename.Bind(wx.EVT_TEXT_ENTER,
              self.OnTextCtrlFilenameTextEnter, id=wxID_FRAME3TEXTCTRLFILENAME)
        self.textCtrlFilename.Bind(wx.EVT_TEXT, self.OnTextCtrlFilenameText,
              id=wxID_FRAME3TEXTCTRLFILENAME)
        self.textCtrlFilename.Bind(wx.EVT_KILL_FOCUS,
              self.OnTextCtrlFilenameKillFocus)

        self.staticText6 = wx.StaticText(id=wxID_FRAME3STATICTEXT6,
              label='Archivo a generar', name='staticText6', parent=self.panel1,
              pos=wx.Point(136, 454), size=wx.Size(120, 13), style=0)

        self.comboBoxAbrircon = wx.ComboBox(choices=[],
              id=wxID_FRAME3COMBOBOXABRIRCON, name='comboBoxAbrircon',
              parent=self.panel1, pos=wx.Point(272, 472), size=wx.Size(130, 21),
              style=0, value='')
        self.comboBoxAbrircon.SetLabel('')
        self.comboBoxAbrircon.SetSelection(1)
        self.comboBoxAbrircon.Bind(wx.EVT_COMBOBOX,
              self.OnComboBoxAbrirconCombobox, id=wxID_FRAME3COMBOBOXABRIRCON)

        self.staticText7 = wx.StaticText(id=wxID_FRAME3STATICTEXT7,
              label='Abrir con', name='staticText7', parent=self.panel1,
              pos=wx.Point(136, 476), size=wx.Size(80, 13), style=0)

        self.btnPrin5 = wx.BitmapButton(bitmap=wx.Bitmap('bin/doc.gif',
              wx.BITMAP_TYPE_GIF), id=wxID_FRAME3BTNPRIN5, name='btnPrin5',
              parent=self.panel1, pos=wx.Point(280, 328), size=wx.Size(24, 24),
              style=wx.BU_AUTODRAW)
        self.btnPrin5.SetBackgroundColour(wx.Colour(165, 167, 248))
        self.btnPrin5.Show(True)
        self.btnPrin5.Bind(wx.EVT_BUTTON, self.OnBtnPrin5Button,
              id=wxID_FRAME3BTNPRIN5)

        self.bitmapButton1 = wx.BitmapButton(bitmap=wx.Bitmap('bin/doc.gif',
              wx.BITMAP_TYPE_GIF), id=wxID_FRAME3BITMAPBUTTON1,
              name='bitmapButton1', parent=self.panel1, pos=wx.Point(280, 264),
              size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.bitmapButton1.SetBackgroundColour(wx.Colour(165, 167, 248))
        self.bitmapButton1.Bind(wx.EVT_BUTTON, self.OnBitmapButton1Button,
              id=wxID_FRAME3BITMAPBUTTON1)

        self.bitmapButton2 = wx.BitmapButton(bitmap=wx.Bitmap('bin/doc.gif',
              wx.BITMAP_TYPE_GIF), id=wxID_FRAME3BITMAPBUTTON2,
              name='bitmapButton2', parent=self.panel1, pos=wx.Point(280, 392),
              size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.bitmapButton2.SetBackgroundColour(wx.Colour(165, 167, 248))
        self.bitmapButton2.Show(True)
        self.bitmapButton2.Bind(wx.EVT_BUTTON, self.OnBitmapButton2Button,
              id=wxID_FRAME3BITMAPBUTTON2)

        self.btnTipoActoXCarRel = wx.BitmapButton(bitmap=wx.Bitmap('bin/doc.gif',
              wx.BITMAP_TYPE_GIF), id=wxID_FRAME3BTNTIPOACTOXCARREL,
              name='btnTipoActoXCarRel', parent=self.panel1, pos=wx.Point(280,
              360), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.btnTipoActoXCarRel.SetBackgroundColour(wx.Colour(165, 167, 248))
        self.btnTipoActoXCarRel.Show(True)
        self.btnTipoActoXCarRel.Bind(wx.EVT_BUTTON, self.OnTipoActoXCarRel,
              id=wxID_FRAME3BTNTIPOACTOXCARREL)

        self.lblAplicarseleccion = wx.StaticText(id=wxID_FRAME3LBLAPLICARSELECCION,
              label=u'Aplicar selecci\xf3n de casos o personas',
              name='lblAplicarseleccion', parent=self.panel1, pos=wx.Point(136,
              491), size=wx.Size(120, 29), style=0)

        self.chkAplicarseleccion = wx.CheckBox(id=wxID_FRAME3CHKAPLICARSELECCION,
              label='', name='chkAplicarseleccion', parent=self.panel1,
              pos=wx.Point(272, 496), size=wx.Size(70, 13), style=0)
        self.chkAplicarseleccion.SetValue(True)

        self.strCasosSeleccionados = wx.StaticText(id=wxID_FRAME3STRCASOSSELECCIONADOS,
              label='Reporte narrativo de casos visibles',
              name='strCasosSeleccionados', parent=self.panel1, pos=wx.Point(56,
              91), size=wx.Size(208, 13), style=0)

        self.bitmapButton4 = wx.BitmapButton(bitmap=wx.Bitmap('bin/doc.gif',
              wx.BITMAP_TYPE_GIF), id=wxID_FRAME3BITMAPBUTTON4,
              name='bitmapButton4', parent=self.panel1, pos=wx.Point(280, 112),
              size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.bitmapButton4.SetBackgroundColour(wx.Colour(165, 167, 248))
        self.bitmapButton4.Bind(wx.EVT_BUTTON, self.repCasoActivo,
              id=wxID_FRAME3BITMAPBUTTON4)

        self.staticText9 = wx.StaticText(id=wxID_FRAME3STATICTEXT9,
              label='Reporte narrativo de persona activa', name='staticText9',
              parent=self.panel1, pos=wx.Point(56, 243), size=wx.Size(208, 13),
              style=0)

        self.bitmapButton5 = wx.BitmapButton(bitmap=wx.Bitmap('bin/doc.gif',
              wx.BITMAP_TYPE_GIF), id=wxID_FRAME3BITMAPBUTTON5,
              name='bitmapButton5', parent=self.panel1, pos=wx.Point(280, 232),
              size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.bitmapButton5.SetBackgroundColour(wx.Colour(165, 167, 248))
        self.bitmapButton5.Bind(wx.EVT_BUTTON, self.OnBitmapButton5Button,
              id=wxID_FRAME3BITMAPBUTTON5)

        self.fileBrowse = wx.lib.filebrowsebutton.FileBrowseButton(buttonText='Buscar',
              dialogTitle='Elija un archivo', fileMask='*.htm',
              id=wxID_FRAME3FILEBROWSE, initialValue='', labelText='Reporte:',
              parent=self.panel1, pos=wx.Point(136, 520), size=wx.Size(296, 80),
              startDirectory='../archivos', style=wx.TAB_TRAVERSAL,
              toolTip='Escriba un nombre o escoja un archivo')
        self.fileBrowse.Bind(wx.EVT_LEFT_DOWN, self.OnFileBrowseLeftDown)

        self.openRep = wx.Button(id=wxID_FRAME3OPENREP, label='Abrir reporte',
              name='openRep', parent=self.fileBrowse, pos=wx.Point(48, 56),
              size=wx.Size(168, 23), style=0)
        self.openRep.Bind(wx.EVT_BUTTON, self.OnOpenRepButton,
              id=wxID_FRAME3OPENREP)

        self.casoOpcionesVisibles = wx.Button(id=wxID_FRAME3CASOOPCIONESVISIBLES,
              label='Opciones', name='casoOpcionesVisibles', parent=self.panel1,
              pos=wx.Point(312, 80), size=wx.Size(72, 23), style=0)
        self.casoOpcionesVisibles.Bind(wx.EVT_BUTTON,
              self.OnCasoOpcionesVisiblesButton,
              id=wxID_FRAME3CASOOPCIONESVISIBLES)

        self.personaOpciones = wx.Button(id=wxID_FRAME3PERSONAOPCIONES,
              label='Opciones', name='personaOpciones', parent=self.panel1,
              pos=wx.Point(312, 232), size=wx.Size(72, 23), style=0)
        self.personaOpciones.Bind(wx.EVT_BUTTON, self.OnPersonaOpcionesButton,
              id=wxID_FRAME3PERSONAOPCIONES)

        self.choicePrintCfg = wx.Choice(choices=[],
              id=wxID_FRAME3CHOICEPRINTCFG, name='choicePrintCfg',
              parent=self.panel1, pos=wx.Point(136, 608), size=wx.Size(344, 21),
              style=0)
        self.choicePrintCfg.Bind(wx.EVT_CHOICE, self.OnChoicePrintCfgChoice,
              id=wxID_FRAME3CHOICEPRINTCFG)

        self.btnSaveCfg = wx.Button(id=wxID_FRAME3BTNSAVECFG,
              label='Guardar modelo', name='btnSaveCfg', parent=self.panel1,
              pos=wx.Point(480, 608), size=wx.Size(128, 23), style=0)
        self.btnSaveCfg.Bind(wx.EVT_BUTTON, self.OnBtnSaveCfgButton,
              id=wxID_FRAME3BTNSAVECFG)

        self.btnSaveCfgAs = wx.Button(id=wxID_FRAME3BTNSAVECFGAS,
              label='Guardar modelo como', name='btnSaveCfgAs',
              parent=self.panel1, pos=wx.Point(480, 632), size=wx.Size(128, 23),
              style=0)
        self.btnSaveCfgAs.Bind(wx.EVT_BUTTON, self.OnBtnSaveCfgAsButton,
              id=wxID_FRAME3BTNSAVECFGAS)

        self.staticText10 = wx.StaticText(id=wxID_FRAME3STATICTEXT10,
              label='Reporte narrativo de caso activo', name='staticText10',
              parent=self.panel1, pos=wx.Point(56, 123), size=wx.Size(208, 13),
              style=0)

        self.btnCasosSeleccionados = wx.BitmapButton(bitmap=wx.Bitmap('bin/doc.gif',
              wx.BITMAP_TYPE_GIF), id=wxID_FRAME3BTNCASOSSELECCIONADOS,
              name='btnCasosSeleccionados', parent=self.panel1,
              pos=wx.Point(280, 80), size=wx.Size(24, 24),
              style=wx.BU_AUTODRAW)
        self.btnCasosSeleccionados.SetBackgroundColour(wx.Colour(165, 167, 248))
        self.btnCasosSeleccionados.Bind(wx.EVT_BUTTON,
              self.OnBtnCasosSeleccionadosButton,
              id=wxID_FRAME3BTNCASOSSELECCIONADOS)

        self.CasoOpcionesActivo = wx.Button(id=wxID_FRAME3CASOOPCIONESACTIVO,
              label='Opciones', name='CasoOpcionesActivo', parent=self.panel1,
              pos=wx.Point(312, 112), size=wx.Size(72, 23), style=0)
        self.CasoOpcionesActivo.Bind(wx.EVT_BUTTON,
              self.OnCasoOpcionesActivoButton,
              id=wxID_FRAME3CASOOPCIONESACTIVO)

        self.staticText8 = wx.StaticText(id=wxID_FRAME3STATICTEXT8,
              label='Modelo de impresi\xf3n', name='staticText8',
              parent=self.panel1, pos=wx.Point(24, 613), size=wx.Size(97, 13),
              style=0)

        self.staticText11 = wx.StaticText(id=wxID_FRAME3STATICTEXT11,
              label='Reporte de intervenciones', name='staticText11',
              parent=self.panel1, pos=wx.Point(56, 304), size=wx.Size(127, 13),
              style=0)

        self.btnRepIntervenciones = wx.BitmapButton(bitmap=wx.Bitmap('bin/doc.gif',
              wx.BITMAP_TYPE_GIF), id=wxID_FRAME3BTNREPINTERVENCIONES,
              name='btnRepIntervenciones', parent=self.panel1, pos=wx.Point(280,
              296), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.btnRepIntervenciones.SetBackgroundColour(wx.Colour(165, 167, 248))
        self.btnRepIntervenciones.Bind(wx.EVT_BUTTON,
              self.OnBtnRepIntervencionesButton,
              id=wxID_FRAME3BTNREPINTERVENCIONES)

        self.staticText12 = wx.StaticText(id=wxID_FRAME3STATICTEXT12,
              label='Listado de casos', name='staticText12', parent=self.panel1,
              pos=wx.Point(56, 185), size=wx.Size(160, 13), style=0)

        self.btnRepCasos = wx.BitmapButton(bitmap=wx.Bitmap('bin/doc.gif',
              wx.BITMAP_TYPE_GIF), id=wxID_FRAME3BTNREPCASOS,
              name='btnRepCasos', parent=self.panel1, pos=wx.Point(280, 176),
              size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.btnRepCasos.SetBackgroundColour(wx.Colour(165, 167, 248))
        self.btnRepCasos.Bind(wx.EVT_BUTTON, self.OnBtnRepCasosButton,
              id=wxID_FRAME3BTNREPCASOS)

        self.button2 = wx.Button(id=wxID_FRAME3BUTTON2, label='button2\xd3',
              name='button2', parent=self.panel1, pos=wx.Point(536, 344),
              size=wx.Size(75, 23), style=0)
        self.button2.Show(False)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME3BUTTON2)

        self.bitmapButton6 = wx.BitmapButton(bitmap=wx.Bitmap('bin/doc.gif',
              wx.BITMAP_TYPE_GIF), id=wxID_FRAME3BITMAPBUTTON6,
              name='bitmapButton6', parent=self.panel1, pos=wx.Point(280, 144),
              size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.bitmapButton6.SetBackgroundColour(wx.Colour(165, 167, 248))
        self.bitmapButton6.Bind(wx.EVT_BUTTON, self.OnBitmapButton6Button,
              id=wxID_FRAME3BITMAPBUTTON6)

        self.staticText13 = wx.StaticText(id=wxID_FRAME3STATICTEXT13,
              label='Reporte resumido de caso activo', name='staticText13',
              parent=self.panel1, pos=wx.Point(56, 152), size=wx.Size(208, 13),
              style=0)

        self.btnLimpiarOpciones = wx.Button(id=wxID_FRAME3BTNLIMPIAROPCIONES,
              label='Limpiar opciones', name='btnLimpiarOpciones',
              parent=self.panel1, pos=wx.Point(136, 640), size=wx.Size(112, 23),
              style=0)
        self.btnLimpiarOpciones.Bind(wx.EVT_BUTTON,
              self.OnBtnLimpiarOpcionesButton,
              id=wxID_FRAME3BTNLIMPIAROPCIONES)

        self.delModelo = wx.Button(id=wxID_FRAME3DELMODELO,
              label='Borrar modelo', name='delModelo', parent=self.panel1,
              pos=wx.Point(480, 656), size=wx.Size(128, 23), style=0)
        self.delModelo.Bind(wx.EVT_BUTTON, self.OnDelModeloButton,
              id=wxID_FRAME3DELMODELO)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self.panel1,
              pos=wx.Point(584, 8), size=wx.Size(20, 24), style=wx.BU_AUTODRAW)

        self.staticText14 = wx.StaticText(id=wxID_FRAME3STATICTEXT14,
              label='Violaciones a los derechos humanos', name='staticText14',
              parent=self.panel1, pos=wx.Point(56, 426), size=wx.Size(186, 13),
              style=0)

        self.btnReporteActos = wx.BitmapButton(bitmap=wx.Bitmap('bin/doc.gif',
              wx.BITMAP_TYPE_GIF), id=wxID_FRAME3BTNREPORTEACTOS,
              name='btnReporteActos', parent=self.panel1, pos=wx.Point(280,
              421), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.btnReporteActos.SetBackgroundColour(wx.Colour(165, 167, 248))
        self.btnReporteActos.Show(True)
        self.btnReporteActos.Bind(wx.EVT_BUTTON, self.OnBtnReporteActosButton,
              id=wxID_FRAME3BTNREPORTEACTOS)

        self.btnPersonas = wx.BitmapButton(bitmap=wx.Bitmap('bin/doc.gif',
              wx.BITMAP_TYPE_GIF), id=wxID_FRAME3BTNPERSONAS,
              name='btnPersonas', parent=self.panel1, pos=wx.Point(280, 205),
              size=wx.Size(24, 23), style=wx.BU_AUTODRAW)
        self.btnPersonas.Bind(wx.EVT_BUTTON, self.OnBtnPersonasButton,
              id=wxID_FRAME3BTNPERSONAS)

        self.staticText15 = wx.StaticText(id=wxID_FRAME3STATICTEXT15,
              label='Listado de personas', name='staticText15',
              parent=self.panel1, pos=wx.Point(56, 213), size=wx.Size(97, 13),
              style=0)

    def __init__(self, parent):
#-------------------------------------------------------------------------------
        self._init_ctrls(parent)
        viewers = [(OpenBrowser,'Navegador'),(OpenWord,'Word'),(OpenExcel,'Excel'), (OpenOpenWriter,'OpenOffice writer'), (OpenOpenCalc,'OpenOffice calc') ]
        LlenaCtrl3(self.comboBoxAbrircon, viewers, selected=OpenBrowser)
        self.comboBoxAbrircon.SetSelection(1)
        self.view = OpenBrowser
        self.filename='salida'
        self.textCtrlFilename.SetValue(self.filename)
        
        nombre = 'bin%sdoc.gif'%status.slash
        
        self.printconfigCaso=None
        self.printconfigCasoVisible=None
        self.printconfigPersona=None
        
        
        
        if (status.filtroCaso and status.filtroCaso.FiltroActivo() ) or \
            (status.filtroPersona and status.filtroPersona.FiltroActivo('Persona')):
            self.chkAplicarseleccion.SetValue(True)
            self.chkAplicarseleccion.Show()
            self.lblAplicarseleccion.Show()
        else:
            self.chkAplicarseleccion.SetValue(False)
            self.chkAplicarseleccion.Show(False)
            self.lblAplicarseleccion.Show(False)
        self.LoadDataPrintCfg()
        CtrlSelect(self.choicePrintCfg,status.Reporte_con_todos_los_campos)
        LlenaAyuda(self, u'frameRep5')
        CamposSololectura(self, camposEntidad['reportes'], CanEdit(status.casoActual))
        
        # se cancelan las opciones de impresion
        LimpiarOpciones(self)
        #
        
        
        if cnf.OSlinux:
            module2.choiceFix(self, __name__)
    def OnBitmapButton2Button(self, event):
        # tipo de acto vs perpetrador
        dependencias = []
        filtrar = status.filtroCaso and self.chkAplicarseleccion.GetValue()  and status.filtroCaso.FiltroActivo()
        if filtrar:
            
            dependencias = status.filtroCaso.busquedaActualDependencias
        
        
            
        
        MiDataset = GeneraQueryCaso(['AB', 'AAA']+ dependencias, id=False, counter=True, Entidad=Acto)
        MiDataset = filtraPorContenedores(MiDataset, Caso)
        
        MiDataset = MiDataset.filter(TesTipodeacto.id > 0 )
        MiDataset = MiDataset.filter(PerPerpetrador.id > 0)
        
        
        
        MiDataset = MiDataset.add_column(PerPerpetrador.id).group_by(PerPerpetrador.id)
        MiDataset = MiDataset.add_column(TesTipodeacto.id).group_by(TesTipodeacto.id)
        
        
        if filtrar:
            #filtro = Caso.id.in_(status.casoIdseleccionados)
            filtro = status.filtroCaso.Filtro()
            MiDataset = MiDataset.filter(filtro)
        print >>status.log, "tipo de acto vs perpetrador"    
        print >>status.log, "MiDataset 2 ",MiDataset

        MiDataset = MiDataset.all()
        DJRaiz = session.query(TesNode).filter(TesNode.name == u'T04').first()
    
        file = generaCruce2(MiDataset,  Persona, TesNode,
                            filename=FileNameCompleto(self.filename), 
                            titulo=u'Personas y entidades responsables de violaciones de DH',
                            DJRaiz=DJRaiz, 
                            descriptorJprt=Descriptor,
                            descriptorJsrt=nameTesauro, 
                            strTituloCol1='Tipo de Acto/VDH',
                            strTotal ='Perpetradores x Acto/VDH', #columna 2
                            TotalJIzq=True,
                            PieDePagina=u'El reporte muestra el n\xfamero de perpetradores involucrados en cada acto, ya sea bajo una responsabilidad individual, institucional o ambas. Este n\xfamero puede ser diferente al n\xfamero de actos registrados, ya que puede haber actos con m\xe1s de un perpetrador, y actos sin perpetradores'
                            
                            )
        self.view(file)
        event.Skip()


    def OnBtnPrin5Button(self, event):
        #tipo de acto vs tipo de perp
        
        dependencias = []
        filtrar = status.filtroCaso and self.chkAplicarseleccion.GetValue()  and status.filtroCaso.FiltroActivo()
        if filtrar:
            dependencias = status.filtroCaso.busquedaActualDependencias
            
        
        MiDataset = GeneraQueryCaso(['AB', 'AAB']+ dependencias, id=False, counter=True, Entidad=Involucramiento)
        MiDataset = filtraPorContenedores(MiDataset, Caso)
        
        # DI, tipo de perpetrador (columnas)
        MiDataset = MiDataset.add_column(TesTipoPerpetrador.id).group_by(TesTipoPerpetrador.id)
        # DJ, tipo de acto (renglones)
        MiDataset = MiDataset.add_column(TesTipodeacto.id).group_by(TesTipodeacto.id)
        

        MiDataset = MiDataset.filter(TesTipodeacto.id > 0 )
        MiDataset = MiDataset.filter(TesTipoPerpetrador.id > 0)
        
        
        
        if filtrar:
            filtro = status.filtroCaso.Filtro()
            #filtro = Caso.id.in_(status.casoIdseleccionados)
            MiDataset = MiDataset.filter(filtro)
            
        
            
        print >>status.log, u'Involucramientos por Tipo de acto vs. Tipo de perpetrador'
        print >>status.log, MiDataset
        MiDataset = MiDataset.all()
        DJRaiz = session.query(TesNode).filter(TesNode.name == u'T04').first()
        file = generaCruce2(MiDataset, TesNode, TesNode, 
                            filename=FileNameCompleto(self.filename), 
                            titulo=u'Responsables involucrados en violaciones a los derechos humanos *', 
                            DJRaiz=DJRaiz, 
                            descriptorJprt=Descriptor,
                            descriptorJsrt=nameTesauro, 
                            descriptorIprt=nameLongTesauro,
                            descriptorIsrt=nameLongTesauro,
                            TotalJIzq=True, 
                            PieDePagina = u"El reporte muestra el n\xfamero de perpetradores involucrados en cada acto. Este n\xfamero puede ser diferente al n\xfamero de actos registrados, ya que puede haber actos con m\xe1s de un perpetrador, y actos sin perpetradores",
                            strTotal=u'Tipo de perpetrador x Acto/VDH',
                            strTituloCol1='Acto/VDH')
        self.view(file)
        event.Skip()        
        
    def OnBitmapButton1Button(self, event):
        # reporte de casos, estado, personas afectadas....
        dependencias = []
        if status.filtroCaso and self.chkAplicarseleccion.GetValue()  and status.filtroCaso.FiltroActivo():
            dependencias = status.filtroCaso.busquedaActualDependencias
        
        
            
        
        MiDataset = GeneraQueryCaso(['EA', 'GB'] + dependencias, Entidad=Caso)
        MiDataset = filtraPorContenedores(MiDataset, Caso)
        if status.filtroCaso and self.chkAplicarseleccion.GetValue()  and status.filtroCaso.FiltroActivo():
            
            filtro = status.filtroCaso.Filtro()
            MiDataset = MiDataset.filter(filtro)
        MiDataset = MiDataset.order_by(TesDerechoAfectado.name)
        MiDataset = MiDataset.order_by(TesEstado.descripcion)
        MiDataset = MiDataset.order_by(Caso.fecha_inicio)
        print >>status.log, "mi data set:", MiDataset
        file=ReporteAnalitico(MiDataset,
                                 [('EventoTipificacionDerechosAfectados','tipificacion/DescriptorCompleto'),
                                 # EventoTipificacionDerechosAfectados = aliased(EventoTipificacion)
                                  ('TesEstado','descripcion'),
                                  ('Caso','Pfecha_inicio'),
                                  ('Caso','PrtDescriptor'),
                                  ('Caso','no_persona_afectadas')
                                  ],
                                  #[['D',1],['D',4]],
                                  [['D',5]],
                                  filename=FileNameCompleto(self.filename), 
                                  titulo=u'Reporte de derechos afectados y estado',
                                  cols = ['Derechos afectados', 'Estado' ,'Fecha inicial del caso',u'Caso','No. de personas afectadas' ]
                                 )
        self.view(file)

    def OnFrame3Close(self, event):
        
        
        
        self.MakeModal(False)     
        
        event.Skip()

    def OnComboBoxAbrirconCombobox(self, event):
        c = event.GetEventObject()
        i= c.Selection
        
        self.view = c.GetClientData(i)
        event.Skip()

    def OnTextCtrlFilenameTextEnter(self, event):

        event.Skip()

    def OnTextCtrlFilenameText(self, event):
        self.filename = self.textCtrlFilename.GetValue()
        
        event.Skip()

    def OnTipoActoXCarRel(self, event):
        " reporte tipo de acto x caracteristicas relevantes"
        dependencias = []
        filtrar = status.filtroCaso and self.chkAplicarseleccion.GetValue()  and status.filtroCaso.FiltroActivo()
        if filtrar:
            dependencias  = status.filtroCaso.Dependencias()
        
            
        
        MiDataset = GeneraQueryCaso(['AB', 'AEA']+ dependencias, id=False, counter=True, Entidad=Acto)
        MiDataset = filtraPorContenedores(MiDataset, Caso)
        
        MiDataset = MiDataset.add_column(TesCaracRelevante.id).group_by(TesCaracRelevante.id)
        MiDataset = MiDataset.add_column(TesTipodeacto.id).group_by(TesTipodeacto.id)
        
        MiDataset = MiDataset.filter(TesCaracRelevante.id > 0)   
        MiDataset = MiDataset.filter(TesTipodeacto.id > 0 )     
        
        if filtrar:
            filtro = status.filtroCaso.Filtro()
            MiDataset = MiDataset.filter(filtro)
        

        MiDataset = MiDataset.all()
        
        DJRaiz = session.query(TesNode).filter(TesNode.name == u'T04').first()
        
        
        
        file = generaCruce2(MiDataset, # la matriz con la lista de datos, ya cuantificados
                                       # donde la columna 0 es el No de ocurrencias
                                       # la columna 1 corresponde a la i
                                       # la columna 2 corresponde a la j
                            TesNode,   # la clase para obtener los titulos de la columna i
                            TesNode,   # la clase para obtener los titulos de la columna j
                            filename=FileNameCompleto(self.filename), 
                            titulo=u"Tipo de acto X Caracter\xedsticas relevantes de la v\xedctima",
                            DJRaiz=DJRaiz, # en caso de tener que generar titulos de taxonomias
                                           # de nivel jerarquico superior
                            descriptorJprt=Descriptor,
                            descriptorJsrt=nameTesauro, 
                            TotalJIzq=True,
                            strTotal = u'Caracter\xedsticas relevantes x Acto/VDH', #titulo de columna 2 (de totales)
                            strTituloCol1=u'Tipo de Acto/VDH',   # titulo columna 1

                            PieDePagina=u'El reporte muestra las caracter\xedsticas relevantes de las v\xedctimas por cada acto registrado. No refleja el n\xfamero de v\xedctimas o actos registrados, ya que la caracter\xedstica relevante de la v\xedctima puede ser distinta para cada acto, y puede haber v\xedctimas sin caracter\xedstica relevante. ')
        self.view(file)
        event.Skip()



        event.Skip()

    def repCasoActivo(self, event):
        if status.casoActual:
            file=printObj([status.casoActual], 'HTML', "Caso", filename=FileNameCompleto(self.filename), titulo='Reporte narrativo de caso')
            self.view(file)
        event.Skip()

    def OnBitmapButton5Button(self, event):
        if status.personaActual:
            file=printObj([status.personaActual], 'HTML', "Persona", filename=FileNameCompleto(self.filename), titulo='Reporte narrativo de persona',  tipoRep="visible")
            self.view(file)
        
        event.Skip()



    def OnFileBrowseLeftDown(self, event):
        
        
        event.Skip()

    def OnOpenRepButton(self, event):
        try:
            
            file = self.fileBrowse.GetValue()
            
            self.view(file)
        except:
            MError(self, "Problema al abrir el archivo")
        event.Skip()

    def OnCasoOpcionesActivoButton(self, event):
        if not self.printconfigCaso:
            #self.printconfigCaso = printconfig.Frame3(self)
            self.printconfigCaso = printconfig.printConfig(self, "Caso", tipoRep="normal")
        self.printconfigCaso.Show()
        event.Skip()

    def OnPersonaOpcionesButton(self, event):
        if not self.printconfigPersona:

            self.printconfigPersona = printconfig.printConfig(self, "Persona", tipoRep="normalP")
        self.printconfigPersona.Show()
        event.Skip()

    def OnBtnSaveCfgButton(self, event):
        if status.printConfigActual and status.printOpt:
            status.printConfigActual.contenido = pickle.dumps(status.printOpt)
            session.add(status.printConfigActual)
            FlushInfo(id=201)
            self.LoadDataPrintCfg()
        else:
            #MError(self, u"No hay una configuaci\xf3n de impresi\xf3n para guardar")
            MError(self, u"Primero selecciona el Modelo de impresi\xf3n que deseas modificar. El bot\xf3n 'Guardar modelo' sirve para guardar los cambios hechos a un modelo de reporte ya existente, para crear un nuevo Modelo de reporte, utiliza el bot\xf3n 'Guardar modelo como'. ")


    def OnBtnSaveCfgAsButton(self, event):
        descrip = MyDescrip(self)
        if descrip:
            PrtCfg = ConfigTdt(u'PrintConfig')
            PrtCfg.descripcion = descrip
            PrtCfg.contenido = pickle.dumps(status.printOpt)
            session.add(PrtCfg)
            FlushInfo(id=200)
            self.LoadDataPrintCfg()
            CtrlSelect(self.choicePrintCfg,descrip)
            
        event.Skip()
        
    def LoadDataPrintCfg(self):
        l=session.query(ConfigTdt).filter(ConfigTdt.tipo == u'PrintConfig').all()
        self.choicePrintCfg.Clear()
        self.choicePrintCfg.Append(status.Reporte_con_todos_los_campos,None)
        LlenaCtrl3(self.choicePrintCfg, [(i,i.Descriptor()) for i in l],append=True)

    def OnChoicePrintCfgChoice(self, event):
        status.printConfigActual = MyClientData(event)
        if status.printConfigActual:
            status.printOpt = pickle.loads(str(status.printConfigActual.contenido))
        else:
            status.printOpt = {}
            

        event.Skip()

    def OnBtnCasosSeleccionadosButton(self, event):
        pprint.pprint(status.printOpt)
        if status.casosSeleccionados:
            file=printObj(status.casosSeleccionados, 'HTML', "Caso", filename=FileNameCompleto(self.filename), tipoRep="visible")
            self.view(file)
        else:
            MError(self, "A\xfan no hay casos seleccionados")
        event.Skip()

    def OnBtnRepIntervencionesButton(self, event):
        # reporte de intervenciones
        print >>status.log, "reporte de intervenciones"
        dependencias = []
        if status.filtroCaso and self.chkAplicarseleccion.GetValue()  and status.filtroCaso.FiltroActivo():
            dependencias = status.filtroCaso.busquedaActualDependencias

        MiDataset = GeneraQueryCaso(['ID','IC','IB','IE'] + dependencias, Entidad=Intervencion)
        MiDataset = filtraPorContenedores(MiDataset, Caso)
        if status.filtroCaso and self.chkAplicarseleccion.GetValue()  and status.filtroCaso.FiltroActivo():
            #filtro = Caso.id.in_(status.casoIdseleccionados)
            filtro = status.filtroCaso.Filtro()
            MiDataset = MiDataset.filter(filtro)
            
        MiDataset = MiDataset.order_by(TesIntervTipo.name)
        MiDataset = MiDataset.order_by(Intervencion.fecha)
        
        
        
        file=ReporteAnalitico(MiDataset,
                                 # lista de duplas entidad - campoImprimible, donde campoImprimible esta en 
                                 # el diccionario 'campos en moduleRep6
                                 [
                                  ('Intervencion','tipo/DescriptorCompleto'),
                                  
                                  ('Intervencion','Pfecha'),
                                  ('PerInterviniente','PrtDescriptor'),
                                  ('PerContraparte','PrtDescriptor'),
                                  ('Intervencion','respuesta'),
                                  
                                  ('Caso','PrtDescriptor')
                                  ],
                                  # lista de grupo de columnas
                                  [['D',6]],
                                  filename=FileNameCompleto(self.filename), 
                                  titulo=u'Reporte de intervenciones por tipo de intervenci\xf3n',
                                  cols = [u'Tipo de intervenci\xf3n',
                                          'Fecha',
                                           u'Qui\xe9n inicia o realiza esta intervenci\xf3n',
                                           u'A qui\xe9n se le dirigi\xf3 esta intervenci\xf3n',
                                           u'Respuesta a la intervenci\xf3n',
                                           
                                           'Caso' ]
                                 )
        self.view(file)

    def OnBtnRepCasosButton(self, event):
        dependencias = []
        if status.filtroCaso and self.chkAplicarseleccion.GetValue()  and status.filtroCaso.FiltroActivo():
            dependencias = status.filtroCaso.busquedaActualDependencias

        MiDataset = GeneraQueryCaso([] + dependencias)
        MiDataset=filtraPorContenedores(MiDataset, Caso)
        if status.filtroCaso and self.chkAplicarseleccion.GetValue():
            #filtro = Caso.id.in_(status.casoIdseleccionados)
            filtro = status.filtroCaso.Filtro()
            MiDataset = MiDataset.filter(filtro)
        
        
        MiDataset = MiDataset.order_by(Caso.fecha_inicio)
        
        file=ReporteAnalitico(MiDataset,
                                 # lista de duplas entidad - campoImprimible, donde campoImprimible esta en 
                                 # el diccionario campos en moduleRep6
                                 [

                                  
                                  ('Caso','PrtDescriptor'),
                                  ('Caso','Pfecha_inicio'),
                                  ('Caso','resumen_descripcion')
                                  ],

                                  [['D',3]],
                                  filename=FileNameCompleto(self.filename), 
                                  titulo=u'Listado de casos',
                                  cols = [u'Num',u'Nombre del caso', 'Fecha inicial',u'Resumen de los hechos' ],
                                  numerar=True
                                 )
        self.view(file)
        event.Skip()

    def OnButton2Button(self, event):
        import ModuleRep7
        status.printOpt = ModuleRep7.CasoResumenOpts
        status.printOpt = pickle.loads(str(ModuleRep7.CasoResumen))
        file=printObj([status.casoActual], 'HTML', "Caso", filename=FileNameCompleto(self.filename), titulo='Reporte resumido de caso')
        self.view(file)
        event.Skip()

    def OnBitmapButton6Button(self, event):
        import ModuleRep7
        printOptSave = status.printOpt
        status.printOpt = ModuleRep7.CasoResumenOpts
        #status.printOpt = pickle.loads(ModuleRep7.CasoResumen)
        file=printObj([status.casoActual], 'HTML', "Caso", filename=FileNameCompleto(self.filename), titulo='Reporte resumido de caso')
        #status.printOpt = {}
        status.printOpt = printOptSave
        self.view(file)
        event.Skip()

    def OnBtnLimpiarOpcionesButton(self, event):
        LimpiarOpciones(self)
        event.Skip()

    def OnDelModeloButton(self, event):
        status.printConfigActual = MyClientData(self.choicePrintCfg)
        if status.printConfigActual:
            if Borrar(self, u"Borrar este modelo de impresi\xf3n?"):
                    session.delete(status.printConfigActual)
                    FlushInfo()
                    self.LoadDataPrintCfg()
                        
        event.Skip()

    def OnTextCtrlFilenameKillFocus(self, event):
        if not FileNameValido(self.textCtrlFilename.GetValue()):
            MError(self, u"El nombre del archivo a generar no es v\xe1lido")
        
        event.Skip()

    def OnBtnReporteActosButton(self, event):
        
    # reporte de actos sumarizado por tipo de acto
        #dependencias = []
        #MiDataset = GeneraQueryCaso(['AB'] + dependencias, Entidad=Acto)
        if status.filtroCaso and self.chkAplicarseleccion.GetValue()  and status.filtroCaso.FiltroActivo():
            dependencias  = status.filtroCaso.Dependencias()
        else:
            dependencias = []
        
        MiDataset = GeneraQueryCaso(['AB']+ dependencias, id=False, counter=True, Entidad=Acto)
        MiDataset = filtraPorContenedores(MiDataset, Caso)
        
        MiDataset = MiDataset.add_column(TesTipodeacto.id).group_by(TesTipodeacto.id)
        MiDataset = MiDataset.add_column(TesTipodeacto.id).group_by(TesTipodeacto.id)
        #MiDataset = MiDataset.add_column(TesCaracRelevante.id).group_by(TesCaracRelevante.id)
        
        MiDataset = MiDataset.filter(TesTipodeacto.id > 0 )
         
        
        
        if status.filtroCaso and self.chkAplicarseleccion.GetValue()  and status.filtroCaso.FiltroActivo():
            filtro = status.filtroCaso.Filtro()
            MiDataset = MiDataset.filter(filtro)
        

        MiDataset = MiDataset.all()
        DJRaiz = session.query(TesNode).filter(TesNode.name == u'T04').first()
        file = generaCruce2(MiDataset, TesNode, TesNode, 
                            filename=FileNameCompleto(self.filename), 
                            titulo=u"Violaciones a los derechos humanos", 
                            OmitirColumnas=True, 
                            DJRaiz=DJRaiz, 
                            descriptorJsrt=nameTesauro,
                            strGranTotal='Total de violaciones reportadas',
                            strTotal='')
        self.view(file)        
        
        
        
        event.Skip()

    def OnCasoOpcionesVisiblesButton(self, event):
        if not self.printconfigCasoVisible:
            
            self.printconfigCasoVisible = printconfig.printConfig(self, "Caso", tipoRep="visible")
        self.printconfigCasoVisible.Show()
        event.Skip()

    def OnBtnPersonasButton(self, event):
        dependencias = []
        
        
        
        
        
        if status.filtroPersona and self.chkAplicarseleccion.GetValue()  and status.filtroPersona.FiltroActivo('Persona'):
            dependencias = status.filtroPersona.busquedaActualDependencias
            
            
        
        MiDataset = GeneraQueryPersona([] + dependencias)
        
        
        
        if status.filtroPersona and self.chkAplicarseleccion.GetValue():
        
            filtro = status.filtroPersona.Filtro()
            MiDataset = MiDataset.filter(filtro)
        else:
            if status.tipoPersona:
                filtro = None
                if status.tipoPersona == 'Individual':
                    filtro = Persona.esindividual == 1
                if status.tipoPersona == 'Colectiva':
                    filtro = Persona.esindividual == 0
                if status.tipoPersona == 'Relacionadas con el caso':
                    if status.casoActual:
                       session.refresh(status.casoActual)
                       filtro = status.casoActual.Personas_relacionadas_filtro()
                if filtro:
                    MiDataset = MiDataset.filter(filtro)
        
        #ordenar la lista
        MiDataset = MiDataset.order_by(expression.desc(Persona.esindividual), Persona.apellido)
        
        file=ReporteAnalitico(MiDataset,
                                 # lista de duplas entidad - campoImprimible, donde campoImprimible esta en 
                                 # el diccionario campos en moduleRep6
                                 [

                                  
                                  ('Persona','PrtDescriptor'),
                                  ('Persona','Ptipo'),
                                  ('Persona','Pocupacion'),
                                  ('Persona','descripcion_del_grupo'),
                                  ('Persona','strRoles'),
                                  ],

                                  [['D',5]],
                                  filename=FileNameCompleto(self.filename), 
                                  titulo=u'Listado de personas',
                                  cols = [u'N\xfam',u'Nombre', 'Tipo de grupo',u'Ocupaci\xf3n',u'Descripci\xf3n del grupo', 'Roles' ],
                                  numerar=True
                                 )
        self.view(file)
        
        
        
        
        event.Skip()

def FileNameCompleto(name):
    return 'archivos\\'+name+'.htm'

def LimpiarOpciones(self):
    status.printOpt = {}
    self.choicePrintCfg.SetSelection(0)



if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
