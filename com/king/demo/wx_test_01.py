#!/usr/bin/env python  
# FileName: wxboxsizer.py  
import wx  
class MyFrame(wx.Frame):  
    def __init__(self,parent,ID,title):  
        print parent
        print ID
        print title
        wx.Frame.__init__(self,parent,ID,title,(-1,-1),wx.Size(250,50))  
        panel=wx.Panel(self,-1)  
        box=wx.BoxSizer(wx.HORIZONTAL)  
        box.Add( wx.Button( panel, -1, 'Button1' ), 1 )  
        box.Add( wx.Button( panel, -1, 'Button2' ), 1 )  
        box.Add( wx.Button( panel, -1, 'Button3' ), 1 )  
        panel.SetSizer(box)  
        
        self.Centre()  
      
class MyApp(wx.App):  
    def OnInit(self):  
        frame = MyFrame( None, -1, 'wxboxsize' )  
        frame.Show(True)  
        return True  
      
app = MyApp(0)  
app.MainLoop()  