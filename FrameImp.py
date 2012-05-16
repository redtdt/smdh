############ no se usa
#Boa:Frame:FrameImp

import wx
import module2
from moduleImp2 import validaCaso

def create(parent):
    return FrameImp(parent)

[wxID_FRAMEIMP, wxID_FRAMEIMPBUTTON1, wxID_FRAMEIMPSPINCTRL1, 
] = [wx.NewId() for _init_ctrls in range(3)]

class FrameImp(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEIMP, name='FrameImp', parent=prnt,
              pos=wx.Point(494, 53), size=wx.Size(400, 498),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame3')
        self.SetClientSize(wx.Size(392, 471))

        self.button1 = wx.Button(id=wxID_FRAMEIMPBUTTON1, label='button1',
              name='button1', parent=self, pos=wx.Point(112, 168),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAMEIMPBUTTON1)

        self.spinCtrl1 = wx.SpinCtrl(id=wxID_FRAMEIMPSPINCTRL1, initial=0,
              max=100, min=0, name='spinCtrl1', parent=self, pos=wx.Point(112,
              224), size=wx.Size(117, 21), style=wx.SP_ARROW_KEYS)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        import moduleImp1
        module2.status.importacion = True
        grupo = self.spinCtrl1.GetValue()
        cuenta=0
        importStatus = 1
        module2.status.idPersonas = set([])
        for P in moduleImp1.personas:
            p1 = moduleImp1.personaImport(P, grupo, importStatus)

        for P in moduleImp1.personas:
            p1 = moduleImp1.vinculosBiograficosImport(P, grupo, importStatus)


        for C in moduleImp1.casos:
            errores = validaCaso(C)
            if not errores:
                o1 = moduleImp1.casoImport(C, grupo, importStatus)
        ###o1 =     moduleImp1.casoImport(moduleImp1.caso7, grupo, importStatus)
        for C in moduleImp1.casos:
            o1 = moduleImp1.importarReferenciasDeCasos(C, grupo, importStatus)
            

        
        module2.session.flush()
        
        event.Skip()
