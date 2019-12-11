import wx

data = {0: "Zero", 1: "first", 2: "second", 3: "three", 4: "four", 5: "five", 6: "six", 7: "sevev", 8: "sevev", 9: "sevev", 10: "sevev", 11: "sevev", 12: "sevev", 13: "sevev"
        , 14: "sevev", 15: "sevev", 16: "sevev", 17: "sevev", 18: "sevev", 19: "sevev", 20: "sevev", 21: "sevev", 22: "sevev"}


class MyFrame(wx.Frame):
    def __init__(self, parent=None):
        super(MyFrame, self).__init__(parent, -1, "带位图的列表", size=(450, 250))
        il = wx.ImageList(100, 100, True)  # 创建图像列表

        for i in range(len(data)):
            img = wx.Image("IMG_20180729_110141.jpg", wx.BITMAP_TYPE_JPEG)
            # wx.ImageList()
            # img = wx.Image("IMG_20180729_110141.jpg", wx.BITMAP_TYPE_GIF)
            img.Rescale(100, 100)
            bmp = img.ConvertToBitmap()
            il.Add(bmp)

        self.list = wx.ListCtrl(self, -1, style=wx.LC_ICON | wx.LC_AUTOARRANGE)
        self.list.AssignImageList(il, wx.IMAGE_LIST_NORMAL)

        for x in range(len(data)):
            self.list.InsertImageStringItem(x, data[x], x)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()


