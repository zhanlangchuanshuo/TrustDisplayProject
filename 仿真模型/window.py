import tkinter as tk 
from tkinter import ttk
import playingGame as pg 
import tkinter.messagebox

class Window():
	"""
	管理窗口的类
	"""
	def __init__(self, settings, center, suppliers, manufacturers):
		self.settings = settings
		self.center = center 
		self.suppliers = suppliers
		self.manufacturers = manufacturers
		self.root = tk.Tk()
		self.logo = tk.PhotoImage(file="image/logo1.png")
		# 两个调参子窗口
		self.confirm = None
		self.para = None 

		# 参数变量
		# 1.全局参数
		self.globalvar = self.getGlobal()
		# 2.企业参数
		self.firmvar = self.getParameters()
		# 为了让后面修改的参数可追踪，需要设置文本框的量
		self.Textbox = None
		self.initWindow()

	# 初始化最开始的窗口
	def initWindow(self):
		# 基本设置
		self.root.title("信任显示机制仿真研究平台")
		self.root.geometry("900x600")
		self.root.resizable(0, 0)

		# logo
		logo_label = tk.Label(self.root, image=self.logo)
		logo_label.place(x=10,y=10)
		# 实验背景部分
		bg_label = tk.Label(self.root, text="实验背景", font=("黑体",24))
		bg_label.place(x=350, y=115)
		bg_text = "为研究在产业联盟下各企业成员之间的信誉度，将使用本平台进行仿真研究"
		bg_text_label = tk.Label(self.root, text = bg_text, font=("仿宋",15), wraplength=800)
		bg_text_label.place(x =30,y=160)

		# 调整参数部分
		alterParamter = tk.Button(self.root, text="调整参数", font=("黑体",24), command=self.confirmWindow)
		alterParamter.place(x=340,y=240)
		ap_text = f"    在某个产业联盟中，共有{self.settings.totolEnterprise}个参与者，其中{self.settings.supplierNum}个供应商，{self.settings.manufactureNum}个制造商，该系统将会进行20次模拟决策过程，"+\
				f"并且将各企业的信誉度进行动态的展示，一些基本的参数为：在企业为诚信类型的前提下遵守承诺的概率为{self.settings.obeyWhileHonest}，在企业为"+\
			f"投机类型的前提下遵守承诺的概率为{self.settings.obeyWhileSpeculate}，更多的参数细节请点击调整参数"
		ap_text_label = tk.Label(self.root, text=ap_text, font=("仿宋",15), wraplength=800, justify="left", pady=10)
		ap_text_label.place(x=30,y=300)

		# 开始实验按钮
		startRun = tk.Button(self.root, text="开始实验", font=("黑体",24), command=self.startCycle)
		startRun.place(x=250,y=450)
		# 重置按钮
		reset = tk.Button(self.root, text="重置", font=("黑体",24), command=self.resetPlayer)
		reset.place(x=500,y=450)
		# 版权提示
		copyright = tk.Label(self.root, text="Copyright © 2019 战狼传说. All rights reserved.", font=("宋体",14))
		copyright.place(x=20,y=570)

	def startCycle(self):
		"""
		点击开始运行按钮之后的处理
		开始循环
		弹出提示完成窗口
		"""
		pg.startPlaying(self.settings,self.center,self.suppliers,self.manufacturers)
		tk.messagebox.showinfo(title="模拟完成",message=f"成功完成了所有参与者的{self.settings.cycleNum}次博弈！")

	def resetPlayer(self):
		"""
		点击重置按钮之后
		相当于重新生成了这些对象
		"""
		self.settings,self.center,self.suppliers,self.manufacturers = pg.initParticipant()
		tk.messagebox.showinfo(title="重置成功",message="已经重置成功")

	def confirmWindow(self):
		"""
		确认弹框
		"""
		self.confirm = tk.Toplevel()
		self.confirm.title("请确认")
		self.confirm.geometry("400x200")
		t1 = "本次实验无法修改参与者数量，固定由2个供应商和2个制造商组成产业联盟"
		l1 = tk.Label(self.confirm, text=t1, wraplength=360, font=("宋体",18))
		l1.place(x=10,y=20)
		l2 = tk.Label(self.confirm, text="进一步修改参数点击确定，关闭该窗口点击返回", font=("仿宋",12))
		l2.place(x=20,y=115)
		queding = tk.Button(self.confirm, text="继续", font=("黑体",18), command=self.parameterWindow)
		queding.place(x=100,y=140)
		fanhui = tk.Button(self.confirm,text="返回", font=("黑体", 18), command=self.confirmBack)
		fanhui.place(x=220,y=140)

	def confirmBack(self):
		"""
		点击确认窗口的返回按钮
		"""
		self.confirm.destroy()

	def parameterWindow(self):
		"""
		详细修改参数的弹框
		"""
		# 将前面的确认窗口关闭
		self.confirm.destroy()

		# 每次创建参数调整面板都需要重新初始化文本框列表
		self.Textbox = []
		# 创建参数调整面板并进行初始化
		self.para = tk.Toplevel()
		self.para.title("参数调整面板")
		self.para.geometry("660x440")
		font1=("黑体",20)
		font2=("中宋",16)
		
		# 全局参数frame
		f1 = tk.Frame(self.para, width=500, height=150)
		f1.place(x=10,y=10)
		self.globalvar = self.getGlobal()
		l1 = tk.Label(f1, text="全局参数", font=font1)			# 全局参数标签
		l1.place(x=10,y=10)
		l2 = tk.Label(f1, text="P(遵守|诚信型)：", font=font2)	# P(遵守|诚信型)标签
		l2.place(x=120,y=50)
		p1 = tk.Entry(f1, width=30, font=font2)					# P(遵守|诚信型)文本框p1
		p1.insert(tk.END, str(self.globalvar[0]))
		p1.place(x=300,y=50)
		l3 = tk.Label(f1, text="P(遵守|投机型)：", font=font2)	# P(遵守|投机型)标签
		l3.place(x=120,y=80)
		p2 = tk.Entry(f1, width=30, font=font2)					# P(遵守|投机型)文本框p2
		p2.insert(tk.END, str(self.globalvar[1]))
		p2.place(x=300,y=80)
		l4 = tk.Label(f1, text="博弈期数：", font=font2)
		l4.place(x=185,y=110)
		p3 = tk.Entry(f1, width=30, font=font2)
		p3.insert(tk.END, str(self.globalvar[2]))
		p3.place(x=300,y=110)
		self.Textbox.append([p1,p2,p3])

		# 企业参数frame
		f2 = tk.Frame(self.para, width=600, height=250)
		f2.place(x=10,y=150)
		l5 = tk.Label(f2, text="企业参数", font=font1)
		l5.place(x=10,y=20)
		l6 = tk.Label(f2, text="企业类型", font=font2)
		l6.place(x=130,y=60)
		l7 = tk.Label(f2, text="决策临界点", font=font2)
		l7.place(x=240,y=60)
		l8 = tk.Label(f2, text="成本下限", font=font2)
		l8.place(x=360,y=60)
		l9 = tk.Label(f2, text="成本上限", font=font2)
		l9.place(x=460,y=60)
		l10 = tk.Label(f2, text="供应商1", font=font2)
		l10.place(x=30,y=90)
		l11 = tk.Label(f2, text="供应商2", font=font2)
		l11.place(x=30,y=120)
		l12 = tk.Label(f2, text="制造商1", font=font2)
		l12.place(x=30,y=150)
		l13 = tk.Label(f2, text="制造商2", font=font2)
		l13.place(x=30,y=180)

		# 将这些做成一个一个列表，产生批量的文本框
		self.firmvar = self.getParameters()	# 获取所有企业参数的列表
		entryList = []
		for i in range(self.settings.totolEnterprise):
			e = []
			for j in range(self.settings.totolEnterprise):
				entry = tk.Entry(f2, width=8, font=font2)
				entry.insert(tk.END, self.firmvar[i][j])
				e.append(entry)
			entryList.append(e)
		self.Textbox.append(entryList)
		for i in range(4):
			for j in range(4):
				entryList[i][j].place(x=130+110*j,y=90+30*i)

		# 加一个确认按钮
		confirmUpdate = tk.Button(self.para, text="确认修改", font=("黑体",14), command=self.updatePara)
		confirmUpdate.place(x=300,y=375)
	
	def getGlobal(self):
		"""
		获取能够修改的全局变量参数
		"""
		g = []
		g.append(self.settings.obeyWhileHonest)
		g.append(self.settings.obeyWhileSpeculate)
		g.append(self.settings.cycleNum)
		return g
	def getParameters(self):
		"""
		获取各参与方的参数
		"""
		ps = []		# 所有参与者参数列表
		for i in range(self.settings.supplierNum):
			p = []		# 某个参与者的参数列表
			ort = "诚信型" if self.suppliers[i].orientation==0 else "投机型"
			p.append(ort)
			p.append(self.suppliers[i].breakPoint)
			p.append(self.suppliers[i].lCost)
			p.append(self.suppliers[i].hCost)
			ps.append(p)
		for i in range(self.settings.manufactureNum):
			p=[]
			ort = "诚信型" if self.manufacturers[i].orientation==0 else "投机型"
			p.append(ort)
			p.append(self.manufacturers[i].breakPoint)
			p.append(self.manufacturers[i].lCost)
			p.append(self.manufacturers[i].hCost)
			ps.append(p)
		return ps

	def updatePara(self):
		"""
		点击确认修改按钮后的处理
		1. 获取当前文本框的值
		2. 将现在的值更新到参与方以及全局参数变量中
		3. 关闭参数修改面板
		"""
		# 获取当前文本框的值并修改
		for i in range(len(self.Textbox)):
			if i==0:
				# 全局变量
				self.settings.obeyWhileHonest = float(self.Textbox[0][0].get())
				self.settings.obeyWhileSpeculate = float(self.Textbox[0][1].get())
				self.settings.cycleNum = int(self.Textbox[0][2].get())
			if i==1:
				# 参与者变量
				for j in range(4):
					if j<2:
						# 供应商
						ort = 0 if self.Textbox[1][j][0].get()=="诚信型" else 1
						self.suppliers[j].orientation = ort
						self.suppliers[j].breakPoint = float(self.Textbox[1][j][1].get())
						self.suppliers[j].lCost = float(self.Textbox[1][j][2].get())
						self.suppliers[j].hCost = float(self.Textbox[1][j][3].get())
					else:
						# 制造商
						ort = 0 if self.Textbox[1][j][0].get()=="诚信型" else 1
						self.manufacturers[j-2].orientation = ort
						self.manufacturers[j-2].breakPoint = float(self.Textbox[1][j][1].get())
						self.manufacturers[j-2].lCost = float(self.Textbox[1][j][2].get())
						self.manufacturers[j-2].hCost = float(self.Textbox[1][j][3].get())

		# 关闭参数修改面板
		self.para.destroy()

	def execute(self):
		"""
		执行窗口循环
		"""
		self.root.mainloop()
