import wx
import matplotlib.pyplot as plt
import os


# data = {0:"Zero",1:"first",2:"second",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven"}
class MyFrame(wx.Frame):
    def __init__(self, parent=None):
        super(MyFrame, self).__init__(parent, -1, "带位图的列表", size=(1000, 1000))  # super可以调用父类以及父类的方法
        self.imagelist = []
        il = wx.ImageList(150, 150, True)  # 创建图像列表
        self.list = wx.ListCtrl(self, -1, style=wx.LC_ICON | wx.LC_AUTOARRANGE | wx.LC_HRULES | wx.LC_VRULES)  # 创建ListCtrl
        for f in os.listdir(r'D:\\picture'):
            img = wx.Image("D:\\picture\\" + f, wx.BITMAP_TYPE_ANY)
            img.Rescale(150, 150)
            # img.Rescale(quality=wx.IMAGE_QUALITY_NORMAL)
            bmp = img.ConvertToBitmap()
            il.Add(bmp)
            img1 = plt.imread("D:\\picture\\" + f)
            self.imagelist.append(img1)
            # print(il.GetImageCount())
            # 调用InsertItem()方法出入列表项，并为图标设置说明字符串
            self.list.InsertItem(il.GetImageCount() - 1, f,
                                 il.GetImageCount() - 1)  # 把图像按索引存入ListCtrl :InsertItem(索引index,lable,AssignImageList存放的ImageList的index)
        self.list.AssignImageList(il, wx.IMAGE_LIST_NORMAL)
        self.list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.imagelistcontrol)  # 绑定左键点击事件:
        self.list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.imagelistcontrol2)  # 绑定左键双击事件:
        self.list.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.imagelistcontrol3)  # 绑定右键点击事件:
        self.list.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.imagelistcontrol4)  # 绑定左键取消事件:
        # self.Bind(wx.EVT_LIST_DELETE_ITEM, self.OnItemDelete, self.list)
        # self.Bind(wx.EVT_LIST_COL_CLICK, self.OnColClick, self.list)
        # self.Bind(wx.EVT_LIST_COL_RIGHT_CLICK, self.OnColRightClick, self.list)
        # self.Bind(wx.EVT_LIST_COL_BEGIN_DRAG, self.OnColBeginDrag, self.list)
        # self.Bind(wx.EVT_LIST_COL_DRAGGING, self.OnColDragging, self.list)
        # self.Bind(wx.EVT_LIST_COL_END_DRAG, self.OnColEndDrag, self.list)
        # self.Bind(wx.EVT_LIST_BEGIN_LABEL_EDIT, self.OnBeginEdit, self.list)

    def imagelistcontrol(self, event):
        print(self.list.GetItemText(self.list.GetFocusedItem()))  # 获取选中的item的 lable
        itemcount = self.list.GetItemCount()  # 获取list的count
        print(itemcount)
        for i in range(itemcount):
            if self.list.IsSelected(i):  # 如果是选中的
                wx.MessageBox("select:" + str(i), caption="Message", style=wx.OK)
                plt.imshow(self.imagelist[i])
                plt.show()

    def imagelistcontrol2(self, event):
        print("EVT_LIST_ITEM_ACTIVATED")

    def imagelistcontrol3(self, event):
        print("EVT_LIST_ITEM_RIGHT_CLICK")

    def imagelistcontrol4(self, event):
        print("EVT_LIST_ITEM_DESELECTED")


app = wx.App()

frame = MyFrame()
frame.Show()

app.MainLoop()

# AssignImageList和InsertImageStringItem去创建位图列表
