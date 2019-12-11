# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(876, 619), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_textCtrl1, 1, wx.ALL | wx.EXPAND, 5)

        self.open = wx.Button(self, wx.ID_ANY, u"open", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.open, 0, wx.ALL, 5)

        self.save = wx.Button(self, wx.ID_ANY, u"save", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.save, 0, wx.ALL, 5)

        bSizer1.Add(bSizer2, 0, wx.EXPAND, 5)

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer1.Add(self.m_textCtrl2, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.open.Bind(wx.EVT_BUTTON, self.open)
        self.save.Bind(wx.EVT_BUTTON, self.save)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def open(self, event):
        event.Skip()

    def save(self, event):
        event.Skip()
