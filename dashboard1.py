#-----------------------------------------------------------------------------
# Name:        dashboard1.py
#
#
# RCS-ID:      $Id: dashboard1.py $
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
#Boa:Frame:dashboard1

import wx
import cnf
import os

if __name__ == '__main__':
    import cnf
    cnf.user='admin'
    cnf.passwd='redtdt'
    
import module2
from module2 import session, Caso, Persona, Grupo, status, LlenaCtrl3, MyClientData, MError

import datetime
import getFileDialog
from dlggetpass import MyPass
from moduleImp2 import validaCaso

from FrameCompare import frameCompara
        
from moduleImp1 import get_a_document, personaImport, vinculosBiograficosImport, casoImport, importarReferenciasDeCasos
import Diagnostico

def create(parent):
    return dashboard1(parent)

[wxID_DASHBOARD1, wxID_DASHBOARD1AVANCE, wxID_DASHBOARD1BTNCERRAR, 
 wxID_DASHBOARD1BTNREPORTARDIFERENCIAS, wxID_DASHBOARD1CHOICEGRUPO, 
 wxID_DASHBOARD1IMPORTART1, wxID_DASHBOARD1IMPORTART2, wxID_DASHBOARD1PANEL1, 
 wxID_DASHBOARD1STATICBOX1, wxID_DASHBOARD1STATICLINE1, 
 wxID_DASHBOARD1STATICLINE2, wxID_DASHBOARD1STATICLINE3, 
 wxID_DASHBOARD1STATICLINE4, wxID_DASHBOARD1STATICLINE5, 
 wxID_DASHBOARD1STATICLINE6, wxID_DASHBOARD1STATICLINE7, 
 wxID_DASHBOARD1STATICTEXT1, wxID_DASHBOARD1STATICTEXT15, 
 wxID_DASHBOARD1STATICTEXT16, wxID_DASHBOARD1STATICTEXT2, 
 wxID_DASHBOARD1STATICTEXT3, wxID_DASHBOARD1STATICTEXT4, 
 wxID_DASHBOARD1TXTACTIVIDAD, wxID_DASHBOARD1TXTCASOSCOPIADOSC3, 
 wxID_DASHBOARD1TXTCASOSNOPRESENTESC3, wxID_DASHBOARD1TXTCASOSRELACIONADOSC3, 
 wxID_DASHBOARD1TXTNCASOS, wxID_DASHBOARD1TXTNCASOST2, 
 wxID_DASHBOARD1TXTNPERSONAS, wxID_DASHBOARD1TXTNPERSONAST2, 
 wxID_DASHBOARD1TXTPCOPIADASC3, wxID_DASHBOARD1TXTPNOPRESENTESC3, 
 wxID_DASHBOARD1TXTPRELACIONADASC3, wxID_DASHBOARD1TXTULTAMAIMP1, 
 wxID_DASHBOARD1TXTULTAMAIMP2, 
] = [wx.NewId() for _init_ctrls in range(35)]

class dashboard1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_DASHBOARD1, name='dashboard1',
              parent=prnt, pos=wx.Point(188, 116), size=wx.Size(1075, 472),
              style=wx.DEFAULT_FRAME_STYLE, title='Tablero de control')
        self.SetClientSize(wx.Size(1059, 436))
        self.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'MS Shell Dlg 2'))
        self.SetBackgroundColour(wx.Colour(194, 209, 173))

        self.panel1 = wx.Panel(id=wxID_DASHBOARD1PANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(1059, 436),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetForegroundColour(wx.Colour(0, 0, 0))

        self.staticLine1 = wx.StaticLine(id=wxID_DASHBOARD1STATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(9, 56),
              size=wx.Size(1031, 2), style=0)

        self.staticText2 = wx.StaticText(id=wxID_DASHBOARD1STATICTEXT2,
              label='Contenedor 3', name='staticText2', parent=self.panel1,
              pos=wx.Point(8, 280), size=wx.Size(67, 13), style=0)

        self.txtUltamaImp2 = wx.StaticText(id=wxID_DASHBOARD1TXTULTAMAIMP2,
              label='\xdaltima importaci\xf3n', name='txtUltamaImp2',
              parent=self.panel1, pos=wx.Point(8, 200), size=wx.Size(312, 13),
              style=0)

        self.txtPnopresentesC3 = wx.StaticText(id=wxID_DASHBOARD1TXTPNOPRESENTESC3,
              label='N\xfamero de personas no presentes aun en C3',
              name='txtPnopresentesC3', parent=self.panel1, pos=wx.Point(400,
              352), size=wx.Size(218, 13), style=0)

        self.ImportarT1 = wx.Button(id=wxID_DASHBOARD1IMPORTART1,
              label='Importar a contenedor 1', name='ImportarT1',
              parent=self.panel1, pos=wx.Point(8, 120), size=wx.Size(128, 23),
              style=0)
        self.ImportarT1.Bind(wx.EVT_BUTTON, self.OnImportarT1Button,
              id=wxID_DASHBOARD1IMPORTART1)

        self.btnReportarDiferencias = wx.Button(id=wxID_DASHBOARD1BTNREPORTARDIFERENCIAS,
              label='Reportar diferencias con contenedor 2',
              name='btnReportarDiferencias', parent=self.panel1,
              pos=wx.Point(144, 120), size=wx.Size(208, 23), style=0)
        self.btnReportarDiferencias.Bind(wx.EVT_BUTTON,
              self.OnBtnReportarDiferenciasButton,
              id=wxID_DASHBOARD1BTNREPORTARDIFERENCIAS)

        self.staticLine2 = wx.StaticLine(id=wxID_DASHBOARD1STATICLINE2,
              name='staticLine2', parent=self.panel1, pos=wx.Point(9, 173),
              size=wx.Size(1031, 2), style=0)

        self.txtNpersonas = wx.StaticText(id=wxID_DASHBOARD1TXTNPERSONAS,
              label='N\xfamero de personas', name='txtNpersonas',
              parent=self.panel1, pos=wx.Point(360, 96), size=wx.Size(99, 13),
              style=0)

        self.txtUltamaImp1 = wx.StaticText(id=wxID_DASHBOARD1TXTULTAMAIMP1,
              label='\xdaltima importaci\xf3n', name='txtUltamaImp1',
              parent=self.panel1, pos=wx.Point(8, 72), size=wx.Size(312, 13),
              style=0)

        self.txtNpersonasT2 = wx.StaticText(id=wxID_DASHBOARD1TXTNPERSONAST2,
              label='N\xfamero total de personas', name='txtNpersonasT2',
              parent=self.panel1, pos=wx.Point(400, 224), size=wx.Size(124, 13),
              style=0)

        self.txtPrelacionadasC3 = wx.StaticText(id=wxID_DASHBOARD1TXTPRELACIONADASC3,
              label='N\xfamero de personas relacionadas con otras en C3',
              name='txtPrelacionadasC3', parent=self.panel1, pos=wx.Point(400,
              328), size=wx.Size(242, 13), style=0)

        self.txtNcasos = wx.StaticText(id=wxID_DASHBOARD1TXTNCASOS,
              label='N\xfamero de casos', name='txtNcasos', parent=self.panel1,
              pos=wx.Point(8, 96), size=wx.Size(82, 13), style=0)

        self.txtPcopiadasC3 = wx.StaticText(id=wxID_DASHBOARD1TXTPCOPIADASC3,
              label='N\xfamero de personas copiadas a C3',
              name='txtPcopiadasC3', parent=self.panel1, pos=wx.Point(400, 304),
              size=wx.Size(170, 13), style=0)

        self.txtNcasosT2 = wx.StaticText(id=wxID_DASHBOARD1TXTNCASOST2,
              label='N\xfamero total de casos ', name='txtNcasosT2',
              parent=self.panel1, pos=wx.Point(8, 224), size=wx.Size(110, 13),
              style=0)

        self.txtCasosCopiadosC3 = wx.StaticText(id=wxID_DASHBOARD1TXTCASOSCOPIADOSC3,
              label='N\xfamero de casos copiados a C3',
              name='txtCasosCopiadosC3', parent=self.panel1, pos=wx.Point(8,
              304), size=wx.Size(153, 13), style=0)

        self.txtCasosRelacionadosC3 = wx.StaticText(id=wxID_DASHBOARD1TXTCASOSRELACIONADOSC3,
              label='N\xfamero de casos relacionados con otros en C3',
              name='txtCasosRelacionadosC3', parent=self.panel1, pos=wx.Point(8,
              328), size=wx.Size(225, 13), style=0)

        self.txtCasosNoPresentesC3 = wx.StaticText(id=wxID_DASHBOARD1TXTCASOSNOPRESENTESC3,
              label='N\xfamero de casos no presentes aun en C3',
              name='txtCasosNoPresentesC3', parent=self.panel1, pos=wx.Point(8,
              352), size=wx.Size(201, 13), style=0)

        self.staticText15 = wx.StaticText(id=wxID_DASHBOARD1STATICTEXT15,
              label='Contenedor 1', name='staticText15', parent=self.panel1,
              pos=wx.Point(8, 42), size=wx.Size(66, 13), style=0)

        self.staticText16 = wx.StaticText(id=wxID_DASHBOARD1STATICTEXT16,
              label='', name='staticText16', parent=self.panel1,
              pos=wx.Point(376, 16), size=wx.Size(0, 13), style=0)

        self.staticLine3 = wx.StaticLine(id=wxID_DASHBOARD1STATICLINE3,
              name='staticLine3', parent=self.panel1, pos=wx.Point(8, 40),
              size=wx.Size(1031, 2), style=0)

        self.staticLine4 = wx.StaticLine(id=wxID_DASHBOARD1STATICLINE4,
              name='staticLine4', parent=self.panel1, pos=wx.Point(9, 192),
              size=wx.Size(1031, 2), style=0)

        self.ImportarT2 = wx.Button(id=wxID_DASHBOARD1IMPORTART2,
              label='Importar a contenedor 2', name='ImportarT2',
              parent=self.panel1, pos=wx.Point(8, 240), size=wx.Size(128, 23),
              style=0)
        self.ImportarT2.Bind(wx.EVT_BUTTON, self.OnImportarT2Button,
              id=wxID_DASHBOARD1IMPORTART2)

        self.choiceGrupo = wx.Choice(choices=[], id=wxID_DASHBOARD1CHOICEGRUPO,
              name='choiceGrupo', parent=self.panel1, pos=wx.Point(56, 8),
              size=wx.Size(312, 21), style=0)
        self.choiceGrupo.Bind(wx.EVT_CHOICE, self.OnChoiceGrupoChoice,
              id=wxID_DASHBOARD1CHOICEGRUPO)

        self.staticText1 = wx.StaticText(id=wxID_DASHBOARD1STATICTEXT1,
              label='Grupo', name='staticText1', parent=self.panel1,
              pos=wx.Point(8, 16), size=wx.Size(29, 13), style=0)

        self.staticBox1 = wx.StaticBox(id=wxID_DASHBOARD1STATICBOX1,
              label='Actividad actual', name='staticBox1', parent=self.panel1,
              pos=wx.Point(408, 0), size=wx.Size(200, 40), style=0)

        self.txtActividad = wx.StaticText(id=wxID_DASHBOARD1TXTACTIVIDAD,
              label='Sin actividad                                            ',
              name='txtActividad', parent=self.panel1, pos=wx.Point(420, 16),
              size=wx.Size(193, 13), style=0)
        self.txtActividad.SetForegroundColour(wx.Colour(100, 0, 0))

        self.staticLine5 = wx.StaticLine(id=wxID_DASHBOARD1STATICLINE5,
              name='staticLine5', parent=self.panel1, pos=wx.Point(8, 277),
              size=wx.Size(1032, 2), style=0)

        self.staticText3 = wx.StaticText(id=wxID_DASHBOARD1STATICTEXT3,
              label='Contenedor 2', name='staticText3', parent=self.panel1,
              pos=wx.Point(8, 176), size=wx.Size(66, 13), style=0)

        self.staticLine6 = wx.StaticLine(id=wxID_DASHBOARD1STATICLINE6,
              name='staticLine6', parent=self.panel1, pos=wx.Point(8, 296),
              size=wx.Size(1032, 2), style=0)

        self.staticLine7 = wx.StaticLine(id=wxID_DASHBOARD1STATICLINE7,
              name='staticLine7', parent=self.panel1, pos=wx.Point(9, 376),
              size=wx.Size(1031, 2), style=0)

        self.btnCerrar = wx.Button(id=wxID_DASHBOARD1BTNCERRAR, label='Cerrar',
              name='btnCerrar', parent=self.panel1, pos=wx.Point(400, 392),
              size=wx.Size(75, 23), style=0)
        self.btnCerrar.Bind(wx.EVT_BUTTON, self.OnBtnCerrarButton,
              id=wxID_DASHBOARD1BTNCERRAR)

        self.avance = wx.Gauge(id=wxID_DASHBOARD1AVANCE, name='avance',
              parent=self.panel1, pos=wx.Point(617, 24), range=100,
              size=wx.Size(421, 12), style=wx.GA_HORIZONTAL)

        self.staticText4 = wx.StaticText(id=wxID_DASHBOARD1STATICTEXT4,
              label='Avance', name='staticText4', parent=self.panel1,
              pos=wx.Point(616, 4), size=wx.Size(36, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.grupo = None
        LlenaCtrl3(self.choiceGrupo, [(i,i.Descriptor()) for i in session.query(Grupo)])
        if cnf.OSlinux:
            module2.choiceFix(self, __name__)
    def OnTxtClaveGrupoTextEnter(self, event):
        v=txtClaveGrupo.GetValue()
        self.grupo = int(v)
        print "grupo ", self.grupo
        event.Skip()
    
        

    def OnImportarT1Button(self, event):
        
        if self.grupo:
            mascara = "archivos del grupo %04i sin encriptar|smdhdata%04i*.xml|archivos del grupo %04i encriptados|smdhdata%04i*.gpg"%(self.grupo, self.grupo, self.grupo, self.grupo) 
                      
            fileName=getFileDialog.selectFile(self, mask=mascara, path="c:\smdh2\import", titulo='Archivo a importar en contenedor 1', accion='Importar')
            if fileName:
                if fileName[-3:].upper() == 'GPG':
                    fileName = decripta(self, fileName)
                    print "file...", fileName
                if fileName:
            
                    self.txtActividad.SetLabel(u'Importando a contenedor 1...')
                    self.Update()
                    
                    importarDatos(self, self.grupo, 1, fileName)
            
                    
                    
                    T=datetime.datetime.now()
                    status.grupoActual.ultimolotet1fecha = T
                    status.grupoActual.ultimolotet1archivo = fileName
                    
                    session.add(status.grupoActual)
                    self.txtActividad.SetLabel(u'Sin actividad')
                    session.flush()
                    CasosYPersonasT1(self, self.grupo, 1)
                else:
                    MError(self, "No se realiza el proceso")    
            else:
                MError(self, "No se realiza el proceso")
        else:
            MError(self, u"A\xfan no hay un grupo seleccionado")    
        
        
        
        
        


    def OnBtnReportarDiferenciasButton(self, event):
        frameCompara(self, self.grupo)
        

    def OnImportarT2Button(self, event):
        if self.grupo:
            mascara = "smdhdata%04i*.xml"%self.grupo
            fileName=getFileDialog.selectFile(self, mask=mascara, path="c:\smdh2\import", titulo='Archivo a importar en contenedor 2', accion='Importar')
            if fileName:
            
                self.txtActividad.SetLabel(u'Importando a contenedor 2...')
                self.Update()
                importarDatos(self, self.grupo, 2, fileName)
        
                
                
                T=datetime.datetime.now()
                status.grupoActual.ultimolotet2fecha = T
                status.grupoActual.ultimolotet2archivo = fileName
                session.add(status.grupoActual)
                session.flush()
                self.txtActividad.SetLabel(u'Sin actividad')
                CasosYPersonasT2(self, self.grupo, 2)
                event.Skip() 
            else:
                MError(self, "No se realiza el proceso")
        else:
            MError(self, "A\xfan no hay un grupo seleccionado") 

    def OnCtrlGrupoTextEnter(self, event):
        self.grupo=self.ctrlGrupo.GetValue()
        print self.grupo
        event.Skip()

    def OnBtnLeerGrupoButton(self, event):
        self.grupo=int(self.ctrlGrupo.GetValue())
        
        status.grupoActual = session.query(Grupo).filter(Grupo.id == self.grupo).first()
        if status.grupoActual:
            self.staticText16.SetLabel( status.grupoActual.Descriptor())
            
        CasosYPersonasT1(self, self.grupo, 1)
        CasosYPersonasT2(self, self.grupo, 2)
        
        event.Skip()

    def OnChoiceGrupoChoice(self, event):
        status.grupoActual = MyClientData(self.choiceGrupo)
        self.grupo = int(status.grupoActual.id)
        
            
            
        #    self.staticText16.SetLabel( status.grupoActual.Descriptor())
        CasosYPersonasT1(self, self.grupo, 1)
        CasosYPersonasT2(self, self.grupo, 2)
        
        event.Skip()

    def OnBtnCerrarButton(self, event):
        self.MakeModal(False)
        self.Destroy()
        event.Skip()
        


def importarDatos(self, grupo, importStatus, fileName, desplegarErrores=True):
    
        mensajesDeError = []
        
        doc= get_a_document(name=fileName)
        module2.status.importacion = True
        envio = doc.childNodes[0]
        secciones={}
        for i in envio.childNodes:
            secciones[i.nodeName] = i.childNodes
        

        
        #datosGrupo = envio.childNodes[0].childNodes
        datosGrupo = secciones['Grupo']
        
        #casos = envio.childNodes[1].childNodes
        casos = secciones['ColeccionCasos']
        
        #personas = envio.childNodes[2].childNodes
        personas = secciones['ColeccionPersonas']
        rango = 2 * len(casos) + 2 * len(personas)
        totalprocesados = 0
        self.avance.SetRange(rango)
        
        for P in personas:
            totalprocesados += 1
            self.avance.SetValue(totalprocesados)
            p1 = personaImport(P, grupo, importStatus)

        for P in personas:
            totalprocesados += 1
            self.avance.SetValue(totalprocesados)
            p1 = vinculosBiograficosImport(P, grupo, importStatus)

        casosConError=[]
        
        
        session.bind.echo=True    
        for C in casos:
            totalprocesados += 1
            self.avance.SetValue(totalprocesados)
            errores = validaCaso(C)
            if errores:
                desc = C.getAttribute('descriptor')
                #desc = desc.encode("latin_1", 'replace')
                
                mensaje = u"En el caso %s se encontraron estos problemas:\n"%desc
                for e in errores:
                    mensaje += e
                #print mensaje
                mensajesDeError.append(mensaje)
                id = C.getAttribute('id')
                casosConError.append(id)
                
            else:
                o1 = casoImport(C, grupo, importStatus)
        ###o1 =     moduleImp1.casoImport(moduleImp1.caso7, grupo, importStatus)
        session.bind.echo=False
        for C in casos:
            totalprocesados += 1
            self.avance.SetValue(totalprocesados)
            id = C.getAttribute('id')
            if id not in casosConError:
                o1 = importarReferenciasDeCasos(C, grupo, importStatus)
            

        
        module2.session.flush()
        if mensajesDeError and desplegarErrores:
            Diagnostico.DespliegaDiagnostico(self, mensajesDeError, grupo=grupo)

def CasosYPersonasT1(self, grupo, Cstatus):
    Ncasos = session.query(Caso).filter(Caso.clavegrupo == grupo).filter(Caso.clavestatus == Cstatus).count()
    Npersonas = session.query(Persona).filter(Persona.clavegrupo == grupo).filter(Persona.clavestatus == Cstatus).count()
     
    
    self.txtNcasos.SetLabel( "Total de casos: %i"%Ncasos)
    self.txtNpersonas.SetLabel( "Total de personas: %i"%Npersonas)
    
    if status.grupoActual:
            
            if status.grupoActual.ultimolotet1archivo:
                self.txtUltamaImp1.SetLabel(u'\xdaltima importaci\xf3n: %s desde el archivo %s'%(status.grupoActual.ultimolotet1fecha, status.grupoActual.ultimolotet1archivo))
            else:
                self.txtUltamaImp1.SetLabel(u'\xdaltima importaci\xf3n: Ninguna')
            
    
    
    
def CasosYPersonasT2(self, grupo, Cstatus):
    casosC2 = session.query(Caso).filter(Caso.clavegrupo == grupo).filter(Caso.clavestatus == Cstatus).all()
    
    
    Ncasos = len(casosC2)
    IDs = [(c.id,c.casorelacionadoc3) for c in casosC2]
    IDcopiados = len([c.id for c in casosC2 if (str(c.id)[:-4] == str(c.casorelacionadoc3)[:-4]) and c.casorelacionadoc3 != None])
    IDrelaconados = len([c.id for c in casosC2 if (str(c.id)[:-4] != str(c.casorelacionadoc3)[:-4]) and c.casorelacionadoc3 != None])
    IDnoEnC3 = len([c.id for c in casosC2 if c.casorelacionadoc3 == None])
    
    self.txtCasosCopiadosC3.SetLabel(u'N\xfamero de casos copiados a C3: %i'%IDcopiados)
    self.txtCasosRelacionadosC3.SetLabel(u'N\xfamero de casos relacionados con otros en C3: %i'%IDrelaconados)
    self.txtCasosNoPresentesC3.SetLabel(u'N\xfamero de casos no presentes a\xfan en C3: %i'%IDnoEnC3)
    
    
    personasC2 = session.query(Persona).filter(Persona.clavegrupo == grupo).filter(Persona.clavestatus == Cstatus).all()
    Npersonas = len(personasC2)
    
    PDcopiados = len([c.id for c in personasC2 if (str(c.id)[:-4] == str(c.personarelacionadac3)[:-4]) and c.personarelacionadac3 != None])
    PDrelaconados = len([c.id for c in personasC2 if (str(c.id)[:-4] != str(c.personarelacionadac3)[:-4]) and c.personarelacionadac3 != None])
    PDnoEnC3 = len([c.id for c in personasC2 if c.personarelacionadac3 == None])
    
    
    self.txtPcopiadasC3.SetLabel(u'N\xfamero de personas copiadas a C3: %i'%PDcopiados)
    self.txtPrelacionadasC3.SetLabel(u'N\xfamero de personas relacionadas con otras en C3: %i'%PDrelaconados)
    self.txtPnopresentesC3.SetLabel(u'N\xfamero de personas no presentes a\xfan en C3: %i'%PDnoEnC3)

    self.txtNcasosT2.SetLabel(u"Total de casos: %i"%Ncasos)
    self.txtNpersonasT2.SetLabel(u"Total de personas: %i"%Npersonas)
    
    if status.grupoActual:
            

            if status.grupoActual.ultimolotet2archivo:
                self.txtUltamaImp2.SetLabel(u'\xdaltima importaci\xf3n: %s desde el archivo %s'%(status.grupoActual.ultimolotet2fecha, status.grupoActual.ultimolotet2archivo))
            else:
                self.txtUltamaImp2.SetLabel(u'\xdaltima importaci\xf3n: Ninguna')
    
    
def decripta(self, filename):
    miPass = MyPass(self)
    if miPass:
        outFilename = '%sxml'%(filename[:-3])
        comando="echo %s|c:\smdh2\utils\gpg.exe --homedir c:\smdh2\utils --batch --passphrase-fd 0 -o %s %s "%(miPass, outFilename, filename)
        #comando="echo %s|c:\smdh2\utils\gpg.exe --homedir c:\\tmp --batch --passphrase-fd 0 -o %s %s "%(miPass, outFilename, filename)
        print "comando ", comando
        error = os.system(comando)
        print "resultado ", error
        if error: 
            MError(self, u"No se pudo desencriptar el archivo")
            return ''
        return outFilename
    
    else:
       MError(self, u"No se provey\xf3 una contrase\xf1a. No se pudo desencriptar el archivo")
       return ''
        
    pass

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
