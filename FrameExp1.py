#-----------------------------------------------------------------------------
# Name:        FrameExp1.py
#
#
# RCS-ID:      $Id: FrameExp1.py $
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
#Boa:Frame:FrameExp

import wx
from  moduleExp1 import PreparaEnvio
import moduleExp1
import module2

import datetime
import getFileDialog

import codecs

def create(parent):
    return FrameExp(parent)

[wxID_FRAMEEXP, wxID_FRAMEEXPBTNGUARDARREPORTE, 
 wxID_FRAMEEXPINICIAREXPORTACION, wxID_FRAMEEXPRESULTADO, wxID_FRAMEEXPSALIR, 
 wxID_FRAMEEXPSTATUS, 
] = [wx.NewId() for _init_ctrls in range(6)]

class FrameExp(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEEXP, name='FrameExp', parent=prnt,
              pos=wx.Point(410, 85), size=wx.Size(562, 507),
              style=wx.DEFAULT_FRAME_STYLE, title='Exportar datos')
        self.SetClientSize(wx.Size(546, 471))
        self.Show(False)
        self.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'MS Shell Dlg 2'))

        self.IniciarExportacion = wx.Button(id=wxID_FRAMEEXPINICIAREXPORTACION,
              label='Iniciar exportaci\xf3n', name='IniciarExportacion',
              parent=self, pos=wx.Point(8, 8), size=wx.Size(104, 23), style=0)
        self.IniciarExportacion.Bind(wx.EVT_BUTTON,
              self.OnIniciarExportacionButton,
              id=wxID_FRAMEEXPINICIAREXPORTACION)

        self.salir = wx.Button(id=wxID_FRAMEEXPSALIR, label='Salir',
              name='salir', parent=self, pos=wx.Point(8, 440), size=wx.Size(75,
              23), style=0)
        self.salir.Bind(wx.EVT_BUTTON, self.OnSalirButton,
              id=wxID_FRAMEEXPSALIR)

        self.status = wx.StaticText(id=wxID_FRAMEEXPSTATUS,
              label='Exportaci\xf3n en proceso', name='status', parent=self,
              pos=wx.Point(128, 16), size=wx.Size(113, 13), style=0)
        self.status.Show(False)

        self.resultado = wx.TextCtrl(id=wxID_FRAMEEXPRESULTADO,
              name='resultado', parent=self, pos=wx.Point(8, 40),
              size=wx.Size(528, 384), style=wx.TE_MULTILINE, value='')
        self.resultado.SetEditable(False)

        self.btnGuardarReporte = wx.Button(id=wxID_FRAMEEXPBTNGUARDARREPORTE,
              label='Guardar reporte', name='btnGuardarReporte', parent=self,
              pos=wx.Point(416, 8), size=wx.Size(115, 23), style=0)
        self.btnGuardarReporte.Show(False)
        self.btnGuardarReporte.Bind(wx.EVT_BUTTON,
              self.OnBtnGuardarReporteButton,
              id=wxID_FRAMEEXPBTNGUARDARREPORTE)

    def __init__(self, parent):

        self._init_ctrls(parent)
        

    def OnIniciarExportacionButton(self, event):
        
        
        self.btnGuardarReporte.Show(False)
        self.Update()
        NoGrupo = module2.status.OrgClave
        hashCode = module2.status.OrgHash

        nombreGrupo = module2.status.OrgNombre
        self.resultado.Clear()
        self.Update()
        if hashCode != module2.myHash(str(NoGrupo)):
            module2.MError(self, u"Para exportar debes registrar en Datos Generales la clave de la organizaci\xf3n y el c\xf3digo de verificaci\xf3n")
        else:
            self.status.Show()
            self.Update()
            moduleExp1.exportando=True
            res, archivo = PreparaEnvio(nombreGrupo,NoGrupo,hashCode)

            texto = "\n\n".join(res)
            
            self.resultado.SetValue(texto)
            self.status.Show(False)
            #self.Update()
            if res:
                module2.MError(self, u"Se generaron mensajes de diagn\xf3stico")
                self.btnGuardarReporte.Show()
            module2.MError(self, u"Se gener\xf3 el archivo "+archivo+'.gpg')
            

    def OnSalirButton(self, event):
        self.Close()
        event.Skip()

    def OnBtnGuardarReporteButton(self, event):
        fecha=datetime.datetime.now()
        fecha=fecha.isoformat()[:16].replace(':','')
        default='c:/smdh2/archivos/diag-exportacion-'+fecha+'.txt'
        nombre = getFileDialog.selectFile(self, mask='*.txt', path="/smdh2/archivos", default=default, accion='Guardar', titulo='Guardar reporte')
        f=codecs.open(nombre,'w','utf-8')
        f.write(self.resultado.GetValue())
        
        f.close()
        module2.MError(self, u'El reporte ha sido guardado como '+nombre)



if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
