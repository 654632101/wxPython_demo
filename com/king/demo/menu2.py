#!/usr/bin/python  
# FileName: menu2.py  
import wx  
  
class MyMenu(wx.Frame):  
    def __init__(self, parent, ID, title):  
        wx.Frame.__init__(self, parent, -1, title,  
        wx.DefaultPosition, wx.Size(380, 250))  
        menubar = wx.MenuBar()  
        file = wx.Menu()  
        edit = wx.Menu()  
        help = wx.Menu()  
        file.Append(101, '&Open', 'Open a new document')  
        file.Append(102, '&Save', 'Save the document')  
        file.AppendSeparator()  
        quit = wx.MenuItem(file, 105, '&Quit\tCtrl+Q', 'Quit the Application')  
        quit.SetBitmap(wx.Image ('0.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap())  
        file.AppendItem(quit)  
        edit.Append(201, 'check item1', '', wx.ITEM_CHECK)  
        edit.Append(202, 'check item2', kind= wx.ITEM_CHECK)  
        submenu = wx.Menu()  
        submenu.Append(301, 'radio item1', kind=wx.ITEM_RADIO)  
        submenu.Append(302, 'radio item2', kind=wx.ITEM_RADIO)  
        submenu.Append(303, 'radio item3', kind= wx.ITEM_RADIO)  
        edit.AppendMenu(203, 'submenu', submenu)  
        menubar.Append(file, '&File')  
        menubar.Append(edit, '&Edit')  
        menubar.Append(help, '&Help')  
        self.SetMenuBar(menubar)  
        self.Centre()  
  
        wx.EVT_MENU(self, 105, self.OnQuit)  
    def OnQuit(self, event):  
        self.Close()  
class MyApp(wx.App):  
    def OnInit(self):  
        frame = MyMenu(None, -1, 'menu2.py')  
        frame.Show(True)  
        return True  
app = MyApp(0)  
app.MainLoop()  