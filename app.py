# -*- coding:utf-8 -*-
from email import message
from imp import init_frozen
from unicodedata import name
import wx
import ipinfor
import ipchange

class Frame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title='自用IP快速配置', size=(
		    400, 300), name='frame', style=541072960)
		self.qdck = wx.Panel(self)
		self.Centre()
		self.zhk1 = wx.ComboBox(self.qdck, value='下拉选择', pos=(
		    9, 9), name='comboBox', choices=[], style=16)
		self.zhk1.SetSize((115, 31))
		self.zhk1.Bind(wx.EVT_COMBOBOX, self.zhk1_xzlbx)
		self.zhk1.Bind(wx.EVT_COMBOBOX_DROPDOWN, self.zhk1_dclbx)
		self.bjk1 = wx.TextCtrl(self.qdck,size=(173, 23),pos=(175, 13),value='IP地址',name='text',style=0)
		self.bjk1.Bind(wx.EVT_TEXT,self.bjk1_nrbgb)
		self.bjk2 = wx.TextCtrl(self.qdck,size=(173, 23),pos=(175, 40),value='子网掩码',name='text',style=0)
		self.bjk3 = wx.TextCtrl(self.qdck,size=(173, 23),pos=(175, 70),value='自行输入网关否则不生效',name='text',style=0)
		self.an1 = wx.Button(self.qdck,size=(126, 47),pos=(175, 200),label='确认更改',name='button')
		self.an1.Bind(wx.EVT_BUTTON,self.an1_anbdj)
		# tpk1_图片 = wx.Image(r'C:\Users\XIA\Desktop\py\network\—Pngtree—question mark_1862963.png').ConvertToBitmap()
		# self.tpk1 = wx.StaticBitmap(self.qdck, bitmap=tpk1_图片,size=(349, 206),pos=(-59, 162),name='staticBitmap',style=0)

	def zhk1_xzlbx(self, event):
		# 获取网卡名称self.zhk1.GetStringSelection()
		macname=self.zhk1.GetStringSelection()
		print(self.zhk1.GetStringSelection())
		ip=ipinfor.get_ip(macname)
		# 将ip写入文本框
		mask=ipinfor.get_yanma(macname)
		self.bjk1.SetValue(ip)    
		self.bjk2.SetValue(mask)
	
	# 文本框内容改变,self.bjk1.GetValue() 获得改变后的值
	def bjk1_nrbgb(self,event):
		# print('bjk1,内容被改变')
		print(self.bjk1.GetValue())


# 弹出列表时将infor插入到选项中s
	def zhk1_dclbx(self,event):
		infor=ipinfor.get_mac()
		self.zhk1.SetItems(infor)
		print('zhk1,弹出列表项')
# 点击确认，获取网卡名，ip，子网，网关，  更改（待完善）
	def an1_anbdj(self,event):
		macname=self.zhk1.GetStringSelection()
		newip=self.bjk1.GetValue()
		newmac=self.bjk2.GetValue()
		newgetway=self.bjk3.GetValue()
		log=ipchange.ip_change(macname,newip,newmac,newgetway)
		if log == 1:
			message=wx.MessageDialog(None,"更改失败","失败提示",wx.OK)
			answer=message.ShowModal()
			message.Destroy
			print('更改%sip%s子网掩码%s失败'%(macname,newip,newmac))
		else:
			message=wx.MessageDialog(None,"更改成功","成功提示",wx.OK)
			answer=message.ShowModal()
			message.Destroy

		print(log)

class myApp(wx.App):
	def  OnInit(self):
		self.frame = Frame()
		self.frame.Show(True)
		return True

if __name__ == '__main__':
	app = myApp()
	app.MainLoop()