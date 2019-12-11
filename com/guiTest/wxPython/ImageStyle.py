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
## Class MyPanel2
###########################################################################

class MyPanel2(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(485, 655),
                          style=wx.TAB_TRAVERSAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap1 = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"D:\\picture\\IMG_20180729_110141.jpg", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_bitmap1, 0, wx.ALL, 5)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.SetSizer(bSizer2)
        self.Layout()

    def __del__(self):
        pass

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,id=wx.ID_ANY)
        try:
            image_file = 'D:\\picture\\IMG_20180729_110141.jpg'
            to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))

            image_width = to_bmp_image.GetWidth()
            image_height = to_bmp_image.GetHeight()
            set_title = '%s %d x %d' % (image_file, to_bmp_image.GetWidth(), to_bmp_image.GetHeight())
            parent.SetTitle(set_title)
        except IOError:
            print('Image file %s not found' % image_file)
            raise SystemExit
        # 创建一个按钮
        self.button = wx.Button(self.bitmap, -1, label='启动', pos=(102, 125))


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "My Frame", size=(400, 300),
                          style=wx.DEFAULT_FRAME_STYLE)
        self.panel = wx.Panel(MyPanel2)
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)

    def OnEraseBack(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        # bmp = wx.Bitmap("background.jpg")
        # dc.DrawBitmap(bmp, 0, 0)


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, '登陆窗口', size=(300, 200))
    my_panel = MyPanel(frame)
    frame.Show()
    app.MainLoop()
