#Boa:PopupWindow:PopupWindow1

import wx

def create(parent):
    return PopupWindow1(parent)

[wxID_POPUPWINDOW1] = [wx.NewId() for _init_ctrls in range(1)]

class PopupWindow1(wx.PopupWindow):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.PopupWindow.__init__(self, flags=wx.SIMPLE_BORDER, parent=prnt)
        self.SetSize(wx.Size(400, 497))
        self.Move(wx.Point(22, 25))

    def __init__(self, parent):
        self._init_ctrls(parent)
