import wx
from wx.lib.wordwrap import wordwrap
import wx.lib.agw.ultimatelistctrl as ULC

class Frame(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)

        self.list = ULC.UltimateListCtrl(self, agwStyle=ULC.ULC_REPORT|ULC.ULC_HAS_VARIABLE_ROW_HEIGHT)
        self.items = ['list', 'list', 'I want to wrap words and content shold be placed in multiple lines for each item as the window is resized']
        colWidth = 200
        self.colWidthPad = 5
        self.list.InsertColumn(0, "test", width=colWidth)
        for item in self.items[::-1]:
            item = wordwrap(item, colWidth - self.colWidthPad, wx.ClientDC(self))
            self.list.InsertStringItem(0, item)

        self.list.Bind(wx.EVT_LIST_COL_DRAGGING, self.onDrag)

    def onDrag(self, evt):
        col = evt.GetItem().GetColumn()
        width = self.list.GetColumnWidth(col)
        itemCount = self.list.GetItemCount()

        for i in range(0, itemCount):
            text = wordwrap(self.items[i], width - self.colWidthPad, wx.ClientDC(self))
            self.list.SetStringItem(i, col, text)


app = wx.App(False)
frm = Frame(None, title="ULC wordwrap test")
frm.Show()
app.MainLoop()