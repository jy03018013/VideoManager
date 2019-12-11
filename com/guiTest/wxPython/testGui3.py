import wx

# 限定图片大小
def scale_bitmap(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result


class Panel(wx.Panel):
    def __init__(self, parent, path):
        super(Panel, self).__init__(parent, -1)
        bitmap = wx.Bitmap(path)
        bitmap = scale_bitmap(bitmap, 300, 200)
        control = wx.StaticBitmap(self, -1, bitmap)
        control.SetPosition((10, 10))


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = wx.Frame(None, -1, 'Scaled Image')
    panel = Panel(frame, 'D:\\picture\\IMG_20180729_110141.jpg')
    frame.Show()
    app.MainLoop()