#-----------------------------------------------------------------------------
# Name:        FrameUtils.py
#
#
# RCS-ID:      $Id: FrameUtils.py $
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
#Boa:Frame:FrameUtils




import wx
import wx.lib.filebrowsebutton
import wx.lib.flatnotebook
import csv
import codecs
import os
import datetime
from module2 import LlenaCtrlCategoria, LlenaCtrl, LlenaCtrlTipificacion, LlenaCtrl2, Caso, Acto, status, TesNode, LlenaTree, EventoTipificacion, LlenaPerpetradores, Fuente, Localidad, Publicacion
from module2 import Involucramiento, Intervencion, Persona, LlenaCtrl3, getChoiceValueId, CtrlSelect, getChoiceValue, setDateCtrl, setDateField
from module2 import setCheckBoxValue, getCheckBoxValue, Derechoviolado, MError, Borrar, LlenaCtrlChildren, tesDesc, Loginfo, UpdateLogInfo, Caracrelevantes, FlushInfo
from module2 import PersonaTipificacion, LlenaCtrlPersonaTipificacion, MyClientData, LlenaPersonas, ParentsPattern,  QueryTesNode
import cnf
import sys
import traceback
import path_postgres

session = status.session

def create(parent):
    return FrameUtils(parent)

[wxID_FRAMEUTILS, wxID_FRAMEUTILSARCHIVOPARCHE, 
 wxID_FRAMEUTILSARCHIVORESPALDO, wxID_FRAMEUTILSAVANCE, 
 wxID_FRAMEUTILSBTNAPLICARPARCHE, wxID_FRAMEUTILSBTNCREARBASE, 
 wxID_FRAMEUTILSBTNIMPORTARTESAURO, wxID_FRAMEUTILSBTNRECUPERAR, 
 wxID_FRAMEUTILSBTNSALIR, wxID_FRAMEUTILSBTNSALIR2, 
 wxID_FRAMEUTILSBUTTONRESPALDO, wxID_FRAMEUTILSEXPTESAURO, 
 wxID_FRAMEUTILSFLATNOTEBOOK1, wxID_FRAMEUTILSPANEL1, wxID_FRAMEUTILSPANEL2, 
 wxID_FRAMEUTILSPANEL3, wxID_FRAMEUTILSPANEL4, wxID_FRAMEUTILSPANEL5, 
 wxID_FRAMEUTILSTXTIMPORTACION, 
] = [wx.NewId() for _init_ctrls in range(19)]

class FrameUtils(wx.Frame):
    def _init_coll_flatNotebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=False,
              text='Parches')
        parent.AddPage(imageId=-1, page=self.panel2, select=True,
              text='Tesauro')
        parent.AddPage(imageId=-1, page=self.panel3, select=False,
              text='Respaldos')
        parent.AddPage(imageId=-1, page=self.panel4, select=False,
              text='Recuperar respaldo')
        parent.AddPage(imageId=-1, page=self.panel5, select=False,
              text='Crear base de datos')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEUTILS, name='FrameUtils',
              parent=prnt, pos=wx.Point(574, 254), size=wx.Size(594, 312),
              style=wx.DEFAULT_FRAME_STYLE, title='Herramientas')
        self.SetClientSize(wx.Size(578, 276))
        self.Bind(wx.EVT_CLOSE, self.OnFrameUtilsClose)
        self.Bind(wx.EVT_IDLE, self.OnFrameUtilsIdle)

        self.flatNotebook1 = wx.lib.flatnotebook.FlatNotebook(id=wxID_FRAMEUTILSFLATNOTEBOOK1,
              name='flatNotebook1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(578, 276), style=0)
        self.flatNotebook1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'MS Shell Dlg 2'))

        self.panel1 = wx.Panel(id=wxID_FRAMEUTILSPANEL1, name='panel1',
              parent=self.flatNotebook1, pos=wx.Point(0, 0), size=wx.Size(0, 0),
              style=wx.TAB_TRAVERSAL)

        self.panel2 = wx.Panel(id=wxID_FRAMEUTILSPANEL2, name='panel2',
              parent=self.flatNotebook1, pos=wx.Point(0, 0), size=wx.Size(578,
              250), style=wx.TAB_TRAVERSAL)

        self.ArchivoParche = wx.lib.filebrowsebutton.FileBrowseButton(buttonText='Elegir parche',
              dialogTitle='Choose a file', fileMask='*.*',
              id=wxID_FRAMEUTILSARCHIVOPARCHE, initialValue='',
              labelText='Archivo:', parent=self.panel1, pos=wx.Point(8, 40),
              size=wx.Size(376, 96), startDirectory='parches',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type filename or click browse to choose file')
        self.ArchivoParche.SetName('ArchivoParche')
        self.ArchivoParche.SetToolTipString('Seleccionar el archivo de parche')
        self.ArchivoParche.SetHelpText('Usar esta funcion cuando existan instrucciones especificas para realizar adecuaciones a la base de datos')

        self.btnAplicarParche = wx.Button(id=wxID_FRAMEUTILSBTNAPLICARPARCHE,
              label='Aplicar parche', name='btnAplicarParche',
              parent=self.panel1, pos=wx.Point(136, 168), size=wx.Size(104, 23),
              style=0)
        self.btnAplicarParche.Bind(wx.EVT_BUTTON, self.OnBtnAplicarParche,
              id=wxID_FRAMEUTILSBTNAPLICARPARCHE)

        self.ExpTesauro = wx.Button(id=wxID_FRAMEUTILSEXPTESAURO,
              label='Exportar tesauro', name='ExpTesauro', parent=self.panel2,
              pos=wx.Point(136, 32), size=wx.Size(104, 23), style=0)
        self.ExpTesauro.Bind(wx.EVT_BUTTON, self.OnExpTesauro,
              id=wxID_FRAMEUTILSEXPTESAURO)

        self.btnImportarTesauro = wx.Button(id=wxID_FRAMEUTILSBTNIMPORTARTESAURO,
              label='Importar Tesauro', name='btnImportarTesauro',
              parent=self.panel2, pos=wx.Point(136, 96), size=wx.Size(104, 23),
              style=0)
        self.btnImportarTesauro.Bind(wx.EVT_BUTTON, self.OnBtnImportarTesauro,
              id=wxID_FRAMEUTILSBTNIMPORTARTESAURO)

        self.panel3 = wx.Panel(id=wxID_FRAMEUTILSPANEL3, name='panel3',
              parent=self.flatNotebook1, pos=wx.Point(0, 0), size=wx.Size(578,
              250), style=wx.TAB_TRAVERSAL)

        self.buttonRespaldo = wx.Button(id=wxID_FRAMEUTILSBUTTONRESPALDO,
              label='Efectuar un respaldo', name='buttonRespaldo',
              parent=self.panel3, pos=wx.Point(112, 88), size=wx.Size(216, 23),
              style=0)
        self.buttonRespaldo.Bind(wx.EVT_BUTTON, self.OnButtonRespaldoButton,
              id=wxID_FRAMEUTILSBUTTONRESPALDO)

        self.txtImportacion = wx.StaticText(id=wxID_FRAMEUTILSTXTIMPORTACION,
              label='Procesando importaci\xf3n...', name='txtImportacion',
              parent=self.panel2, pos=wx.Point(136, 192), size=wx.Size(126, 13),
              style=0)
        self.txtImportacion.Show(False)

        self.avance = wx.Gauge(id=wxID_FRAMEUTILSAVANCE, name='avance',
              parent=self.panel2, pos=wx.Point(32, 208), range=100,
              size=wx.Size(328, 16), style=wx.GA_HORIZONTAL)

        self.panel4 = wx.Panel(id=wxID_FRAMEUTILSPANEL4, name='panel4',
              parent=self.flatNotebook1, pos=wx.Point(0, 0), size=wx.Size(578,
              250), style=wx.TAB_TRAVERSAL)

        self.ArchivoRespaldo = wx.lib.filebrowsebutton.FileBrowseButton(buttonText='Seleccionar archivo de respaldo',
              dialogTitle='Choose a file', fileMask='*.sql',
              id=wxID_FRAMEUTILSARCHIVOPARCHE, initialValue='',
              labelText='Archivo:', parent=self.panel4, pos=wx.Point(8, 40),
              size=wx.Size(376, 96), startDirectory='archivos',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type filename or click browse to choose file')

        self.btnRecuperar = wx.Button(id=wxID_FRAMEUTILSBTNRECUPERAR,
              label='Recuperar respaldo', name='btnRecuperar',
              parent=self.panel4, pos=wx.Point(152, 144), size=wx.Size(128, 23),
              style=0)
        self.btnRecuperar.Bind(wx.EVT_BUTTON, self.OnBtnRecuperarButton,
              id=wxID_FRAMEUTILSBTNRECUPERAR)

        self.panel5 = wx.Panel(id=wxID_FRAMEUTILSPANEL5, name='panel5',
              parent=self.flatNotebook1, pos=wx.Point(0, 0), size=wx.Size(578,
              250), style=wx.TAB_TRAVERSAL)

        self.btnCrearBase = wx.Button(id=wxID_FRAMEUTILSBTNCREARBASE,
              label='Crear base', name='btnCrearBase', parent=self.panel5,
              pos=wx.Point(248, 80), size=wx.Size(75, 23), style=0)
        self.btnCrearBase.Bind(wx.EVT_BUTTON, self.OnBtnCrearBaseButton,
              id=wxID_FRAMEUTILSBTNCREARBASE)

        self.btnSalir = wx.Button(id=wxID_FRAMEUTILSBTNSALIR, label='Cerrar',
              name='btnSalir', parent=self.panel4, pos=wx.Point(184, 176),
              size=wx.Size(75, 23), style=0)
        self.btnSalir.Bind(wx.EVT_BUTTON, self.OnBtnSalirButton,
              id=wxID_FRAMEUTILSBTNSALIR)

        self.btnSalir2 = wx.Button(id=wxID_FRAMEUTILSBTNSALIR2, label='Cerrar',
              name='btnSalir2', parent=self.panel5, pos=wx.Point(248, 120),
              size=wx.Size(75, 23), style=0)
        self.btnSalir2.Bind(wx.EVT_BUTTON, self.OnBtnSalir2Button,
              id=wxID_FRAMEUTILSBTNSALIR2)

        self._init_coll_flatNotebook1_Pages(self.flatNotebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.flatNotebook1.Layout()
        self.ExpTesauro.Show(cnf.user == 'vocab')
        
        if status.sinTablas:
            self.flatNotebook1.DeletePage(0)
            self.flatNotebook1.DeletePage(0)
            self.flatNotebook1.DeletePage(0)
        else:
            self.flatNotebook1.DeletePage(3)
            self.flatNotebook1.DeletePage(3)

    def OnFrameUtilsClose(self, event):
        self.MakeModal(False)
        self.Destroy()
        event.Skip()

    def OnFrameUtilsIdle(self, event):
        event.Skip()

    def OnBtnAplicarParche(self, event):
        name = self.ArchivoParche.GetValue()
        print name
        exito, noexito = Parche(self, name) 
        mensaje = "Se aplicaron %i cambios. No se aplicaron %i cambios"%(exito, noexito)
        MError(self, mensaje)
        event.Skip()

    def OnExpTesauro(self, event):
        exportaTesauro(self)
        event.Skip()

    def OnBtnImportarTesauro(self, event):
        self.txtImportacion.Show()
        self.Update()
        importarTesauro(self)
        self.txtImportacion.Show(False)
        self.Update()
        event.Skip()

    def OnButtonRespaldoButton(self, event):
        pgpath = path_postgres.path_postgres()
        if pgpath:
            try:
                
                a=datetime.datetime.now()
        
                fecha = a.isoformat()[:16].replace(':','')
                name = 'respaldo'+fecha+'.sql'
                comando = status.drive+status.path+"\utils\dump_smdh.bat "+'  '+status.drive+status.path+"\\archivos\\"+name+'   '+cnf.db+' '+cnf.passwd+' '+'"'+pgpath+'"'
                print "comando:", comando
                os.system(comando)
                if validaRespaldo(self, status.drive+status.path+"\\archivos\\"+name):
                     MError(self, u"El archivo de respaldo fue generado en la carpeta\n '%s\\archivos' con el nombre de \n %s.\n Es conveniente trasladar ese archivo a algun medio externo, como un CD o disco r\xedgido externo"%(status.drive+status.path , name))
                else:
                    MError(self, u'El archivo de respaldo no pudo ser generado!!!')     
            except:
                MError(self, u'El procedimiento de respaldo no pudo ser efectuado!!!')
        else:
            MError(self, u"No fue posible localizar la instalacion de PostgreSQL")
            
        event.Skip()

    def OnBtnRecuperarButton(self, event):
        name = self.ArchivoRespaldo.GetValue()
        base = cnf.db
        
        restoreBackup(self, name, base)
        sys.exit()
        event.Skip()

    def OnBtnCrearBaseButton(self, event):
        try:
            pgpath = path_postgres.path_postgres()
            if pgpath:
                comando = '%s\\utils\\crearbase-aut2.bat %s %s "%s" '%(status.drive+status.path, cnf.passwd, cnf.db, pgpath)
                os.system(comando)
                MError(self, u"Operaci\xf3n realizada. El sistema ser\xe1 cerrado ahora.")
            else:
                MError(self, u"No fue posible localizar la instalacion de PostgreSQL")
        except:
            MError(self, u"La operaci\xf3n no pudo ser efectuada")
            tb=sys.exc_info()[2]
            #traceback.print_tb(tb)
            traceback.print_exc()
            
            sys.exit()
            
        sys.exit()
        
            
        event.Skip()

    def OnBtnSalirButton(self, event):
        self.Close()
        event.Skip()

    def OnBtnSalir2Button(self, event):
        self.Close()
        event.Skip()
        
def validaRespaldo(self, name):
    try:
        filein = codecs.open(name,'r','utf-8')
        lineas = filein.readlines()
        
    except:
        MError(self, "No fue posible abrir el archivo %s"%name)
        return False
    cadena = "ALTER DATABASE %s"%cnf.db
    long = len(cadena)
    exito = False
    for i in range(50):
        #print lineas[i]
        if lineas[i][:long] == cadena:
            
            exito = True
    if not exito:
        return False
    return True
        
    
def Parche(self, fileName):
    file_object = open(fileName)
    lines = file_object.read(  ).split(';')
    exito = 0
    noexito = 0
    for l in lines:
        try:
            session.execute(l)
            exito = exito + 1
        except:
            print l
            noexito = noexito + 1
            
    return exito, noexito
    
    
def exportaTesauro(self):
    q=QueryTesNode
    fileout = codecs.open('tesauro.csv','w','utf-8')
    writer = csv.writer(fileout)
    #fileout.write('### Tesauro \n')
    for i in q:
        if i.parent_id or i.name == u'rootnode':
        #writer.writerow([str(i.id), str(i.parent_id), i.name.encode('utf-8'), i.descripcion.encode('utf-8')])
            
            notas = i.notas.replace('\n',' ').replace('\r','') if i.notas else ''
            
            fileout.write('%(a)i|%(b)i|%(c)s|%(d)s|%(e)s|\n'%{'a':i.id, 'b':i.parent_id, 'c':i.name, 'd':i.descripcion,'e':notas})
        
        #writer.writerow([str(i.id), str(i.parent_id), i.name, i.descripcion])
    fileout.close()
    
def importarTesauro(self):
    try:
        l = 'ALTER TABLE "public"."tesauro"  DROP CONSTRAINT "tesauro_parent_id_fkey" RESTRICT;'
        session.execute(l)
    except:
        print l
    
    importar = set()
    yapresentes = set()
    try:
        filein = codecs.open('archivos\\tesauro.csv','r','utf-8')
        lineas = filein.readlines()
        filein = codecs.open('archivos\\tesauro.csv','r','utf-8')
    except:
        MError(self, "No fue posible abrir el archivo 'c:\\smdh2\\archivos\\tesauro.csv'")
        return
    
    q=QueryTesNode
    
    rango = len(lineas)
    self.avance.SetRange(rango)
    
    l = filein.readline()
    
    
    nuevas = 0
    actualizadas =0
    totalprocesados = 0
    while l:
        totalprocesados += 1
        self.avance.SetValue(totalprocesados)
        id,parent_id,name, descripcion,notas, ret = l.split('|')
        importar.add(int(id))
        if (id and parent_id) or (id == 1):
            print id
            id= int(id)
            parent_id= int(parent_id)
            upd = False
            try:
               t=q.filter(TesNode.id==id)[0]
               if t.name != name:
                    t.name=name
                    upd = True
               if t.parent_id != parent_id:
                    t.parent_id = parent_id
                    upd = True
                    
               if t.descripcion != descripcion:
                    t.descripcion=descripcion
                    upd = True
               if t.notas != notas:
                    t.notas=notas
                    upd = True
               if upd:     
                   session.add(t)
                   session.flush()
                   actualizadas = actualizadas + 1
            except:
                t=TesNode(name, descripcion, notas=notas)
                t.id = id
                t.parent_id = parent_id
                session.add(t)
                
                session.flush()
                nuevas = nuevas + 1
        l = filein.readline()
    terminos = QueryTesNode
    for i in terminos:
        yapresentes.add(int(i.id))
    sobrantes =  yapresentes - importar
    sobrantes = sobrantes - set([1])
    print [i for i in sobrantes]

    q= QueryTesNode
    for i in sobrantes:
        t=q.filter(TesNode.id == i).first()
        print i
        if t:
            
            try:
                
                session.delete(t)
                session.flush()
                print t.id, t.name,  " borrado"
            except:
                print t.id, t.name,  " no pudo ser borrado"
        
   

    MError(self, "Entradas nuevas:" + str(nuevas)+", entradas actualizadas:"+str(actualizadas))     

        
def muestraFrameUtils(self):
    
    f=FrameUtils(self)

    f.MakeModal()
    f.Show()
def restoreBackup(self, name, base):
    if not name:
        MError(self, u"A\xfan no hay un archivo de respaldo seleccionado")
        return False
        

    if validaRespaldo(self, name):
            pgpath = path_postgres.path_postgres()
            if pgpath:        
            
                comando = '%s\\utils\\restore.bat "%s" %s "%s" '%(status.drive+status.path, name, cnf.passwd, pgpath)
                os.system(comando)
                MError(self, u"Operaci\xf3n realizada")
                return True
            else:
                MError(self, u"No fue posible localizar la instalacion de PostgreSQL")
            
    else:
        MError(self, u"El archivo de respaldo no parece contener informaci\xf3n v\xe1lida para el SMDH")
        
        

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
