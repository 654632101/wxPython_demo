# coding=gbk
import wx
import time
from com.king.demo.demo_s import LoginKq
class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, (-1, -1), wx.Size(360, 200))
        panel = wx.Panel(self, -1)
        
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)  # 创建定时器
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)  # 绑定一个定时器事件
        self.timer.Start(1000)  # 设定时间间隔
        
        # 主box
        box = wx.BoxSizer(wx.VERTICAL)
        # 用户名密码box
        box_0 = wx.BoxSizer(wx.HORIZONTAL)  
        
        box_1 = wx.BoxSizer(wx.HORIZONTAL)
        box_2 = wx.BoxSizer(wx.HORIZONTAL)
        box_3 = wx.BoxSizer(wx.HORIZONTAL)
        
        box_0.Add(wx.StaticText(panel, -1, '用户名:', style=wx.TE_LEFT), flag=wx.LEFT | wx.TOP | wx.BOTTOM | wx.CENTER, border=5)
        self.user_name = wx.TextCtrl(panel, -1, '', style=wx.TE_LEFT)
        box_0.Add(self.user_name, flag=wx.LEFT | wx.TOP | wx.BOTTOM, border=5)
        box_0.Add(wx.StaticText(panel, -1, '密     码:', style=wx.TE_LEFT), flag=wx.LEFT | wx.TOP | wx.BOTTOM | wx.CENTER, border=5)
        self.pass_word = wx.TextCtrl(panel, -1, '', style=wx.TE_LEFT | wx.TE_PASSWORD)
        box_0.Add(self.pass_word, flag=wx.LEFT | wx.TOP | wx.BOTTOM, border=5)
        but_id = wx.NewId()
        
        # 創建grid對象，行，列，行間距，列間距
        gs = wx.GridSizer(3, 2, 2, 2)
        
        gs.Add(wx.StaticText(panel, -1, '姓名', size=(170, 20), style=wx.ALIGN_CENTER))
        gs.Add(wx.StaticText(panel, -1, '打卡时间', size=(170, 20), style=wx.ALIGN_CENTER))
        
        self.kq_01 = wx.StaticText(panel, -1, '', size=(170, 25), style=wx.ALIGN_CENTER)
        gs.Add(self.kq_01)
        self.kq_02 = wx.StaticText(panel, -1, '', size=(170, 20), style=wx.ALIGN_CENTER)
        gs.Add(self.kq_02)
        self.kq_03 = wx.StaticText(panel, -1, '', size=(170, 25), style=wx.ALIGN_CENTER)
        gs.Add(self.kq_03)
        self.kq_04 = wx.StaticText(panel, -1, '', size=(170, 20), style=wx.ALIGN_CENTER)
        gs.Add(self.kq_04)
        
        ti = wx.StaticText(panel, -1, '当前时间:', size=(150, -1), style=wx.ALIGN_CENTER)
        self.log = wx.StaticText(panel, -1, '', size=(200, -1), style=wx.ALIGN_CENTER)
        box_2.Add(ti)
        box_2.Add(self.log, flag=wx.CENTER)
        
        box_3.Add(gs, flag=wx.LEFT, border=5)
        login_in = wx.Button(panel, but_id, '登录')
        box_1.Add(login_in, 1, wx.LEFT, 5)
        box_1.Add(wx.Button(panel, -1, '打卡'), 1, wx.LEFT, 5)
        box_1.Add(wx.Button(panel, -1, '关闭'), 1, wx.LEFT, 5)
        self.Bind(wx.EVT_BUTTON, self.setVa, login_in)
        box.Add(box_0)
        # 添加分割线
        box.Add(wx.StaticLine(panel), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 2)
        box.Add(box_2, flag=wx.LEFT | wx.TOP | wx.BOTTOM, border=5)
        box.Add(wx.StaticLine(panel), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 1)
        box.Add(box_3)
        box.Add(box_1, flag=wx.CENTER)
        panel.SetSizer(box)
        self.Center()
    # 获取用户名进行登录
    def setVa(self, event):
        user_name = self.user_name.GetValue()
        pass_word = self.pass_word.GetValue()
        html = LoginKq(user_name, pass_word).login()
      #  print html
        print html[1]
        self.kq_01.SetLabel(html[1])
        self.kq_02.SetLabel(html[4])
    def Draw(self, dc):  # 绘制当前时间
        t = time.localtime(time.time())
        st = time.strftime("%Y-%m-%d      %I:%M:%S", t)
        self.log.SetLabel(st)
    def OnTimer(self, evt):  # 显示时间事件处理函数
        dc = wx.BufferedDC(wx.ClientDC(self))
        self.Draw(dc)

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        self.Draw(dc)
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, '打卡提醒系统')
        frame.Show(True)
        return True

app = MyApp(0)
app.MainLoop()
        
