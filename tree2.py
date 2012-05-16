# example of wx.TreeCtrl()

import wx

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="tree example", size=(300,130))
        self.cb1 = wx.CheckBox(self, -1, "test1", pos=(280,10))
        self.cb1.Hide()
        self.tree = wx.TreeCtrl(self, size=(280,100))
        root = self.tree.AddRoot("Example")
        
        items = ["test1",
               "test2",
               "test3",]
      
        self.AddTreeNodes(root, items)
      
        self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded, self.tree)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.OnItemCollapsed, self.tree)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.tree)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivated, self.tree)
     
        self.tree.Expand(root)
      
    def AddTreeNodes(self, parentItem, items):
        for item in items:
            if type(item) == str:
                self.tree.AppendItem(parentItem, item)
            else:
                newItem = self.tree.AppendItem(parentItem, item[0])
                self.AddTreeNodes(newItem, item[0])
                
    def GetItemText(self, item):
        if item:
            return self.tree.GetItemText(item)
        else:
            return ""
        
    def OnItemExpanded(self, evt):
        print "OnItemExpanded: ", self.GetItemText(evt.GetItem())
        
    def OnItemCollapsed(self, evt):
        print "OnItemCollapsed:", self.GetItemText(evt.GetItem())

    def OnSelChanged(self, evt):
        print "OnSelChanged:   ", self.GetItemText(evt.GetItem())
        if self.GetItemText(evt.GetItem()) == "test1":
            self.cb1.SetValue(True)
            self.cb1.Show()
        else:
            self.cb1.Hide()
            
    def OnActivated(self, evt):
        print "OnActivated:    ", self.GetItemText(evt.GetItem())


app = wx.PySimpleApp(None)
frame = TestFrame()
frame.Show()
app.MainLoop()
