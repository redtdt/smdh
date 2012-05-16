#-----------------------------------------------------------------------------
# Name:        getFileDialog.py
#
#
# RCS-ID:      $Id: getFileDialog.py $
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
#Boa:Dialog:fileDialog

import wx
import wx.lib.filebrowsebutton

def create(parent):
    return fileDialog(parent)

[wxID_FILEDIALOG, wxID_FILEDIALOGAPLICAR, wxID_FILEDIALOGBTNCANCELAR, 
 wxID_FILEDIALOGFILEBROWSEBUTTON1, 
] = [wx.NewId() for _init_ctrls in range(4)]

class fileDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_FILEDIALOG, name='fileDialog',
              parent=prnt, pos=wx.Point(87, 100), size=wx.Size(679, 259),
              style=wx.DEFAULT_DIALOG_STYLE, title='Seleccione un archivo')
        self.SetClientSize(wx.Size(663, 223))
        self.SetBackgroundColour(wx.Colour(230, 239, 173))
        self.Bind(wx.EVT_INIT_DIALOG, self.OnFileDialogInitDialog)

        self.fileBrowseButton1 = wx.lib.filebrowsebutton.FileBrowseButton(buttonText='Seleccionar',
              dialogTitle='Elija un archivo', fileMask='*.*',
              id=wxID_FILEDIALOGFILEBROWSEBUTTON1, initialValue='',
              labelText='Archivo           ', parent=self, pos=wx.Point(80, 48),
              size=wx.Size(528, 48), startDirectory='c:\smdh2\import',
              style=wx.TAB_TRAVERSAL, toolTip='Elija un archivo')
        self.fileBrowseButton1.SetLabel('Archivo               ')
        self.fileBrowseButton1.SetValue('')
        self.fileBrowseButton1.Bind(wx.EVT_LEFT_DCLICK,
              self.OnFileBrowseButton1LeftDclick)

        self.Aplicar = wx.Button(id=wxID_FILEDIALOGAPLICAR, label='Aplicar',
              name='Aplicar', parent=self, pos=wx.Point(208, 120),
              size=wx.Size(75, 23), style=0)
        self.Aplicar.Bind(wx.EVT_BUTTON, self.OnAplicarButton,
              id=wxID_FILEDIALOGAPLICAR)

        self.btnCancelar = wx.Button(id=wxID_FILEDIALOGBTNCANCELAR,
              label='Cancelar', name='btnCancelar', parent=self,
              pos=wx.Point(296, 120), size=wx.Size(75, 23), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_FILEDIALOGBTNCANCELAR)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.resultado=None
        #self.fileBrowseButton1.buttonText='Guardar como'
    def getData(self):
        return self.resultado

    def OnFileBrowseButton1LeftDclick(self, event):
        event.Skip()

    def OnAplicarButton(self, event):
        self.resultado=self.fileBrowseButton1.GetValue()
        self.Close()
        
        event.Skip()

    def OnFileDialogInitDialog(self, event):
        event.Skip()

    def OnBtnCancelarButton(self, event):
        self.resultado=None
        self.Close()
        event.Skip()
    
def selectFile(self, mask='*.*', path=".", default='', accion='Aplicar', titulo='', label='Archivo'):
    dlg=fileDialog(self)
    dlg.fileBrowseButton1.startDirectory=path
    dlg.fileBrowseButton1.fileMask=mask
    dlg.fileBrowseButton1.SetValue(default)
    dlg.fileBrowseButton1.SetLabel(label)
    dlg.Aplicar.SetLabel(accion)
    dlg.SetTitle(titulo)
    
    dlg.ShowModal()
    res=dlg.resultado
    dlg.Destroy()
    return res
    
    
    
    
    


if __name__ == '__main__':
    app = wx.PySimpleApp()
    res=selectFile(None)
    print "res ",res
    #dlg = create(None)
    #try:
    #    dlg.ShowModal()
    #finally:
    
    #app.MainLoop()
