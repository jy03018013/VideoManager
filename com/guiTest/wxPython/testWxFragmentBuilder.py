import wx

from com.guiTest import noname


class CalcFrame(noname.MyFrame1):
    def __init__(self, parent):
        noname.MyFrame1.__init__(self, parent)

    # 按键事件触发函数
    def btn_submit(self, event):
        num = int(self.m_textCtrl1.GetValue())
        self.m_textCtrl2.SetValue(str(num * num))


def main():
    app = wx.App(False)
    frame = CalcFrame(None)
    frame.Show(True)
    # start the applications
    app.MainLoop()


if __name__ == '__main__':
    main()
