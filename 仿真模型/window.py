import tkinter as tk 
# from PIL import Image,ImageTk
from settings import Settings

# 初始化最开始的窗口
def initWindow(root, settings, logo):
	# 基本设置
	root.title("信任显示机制仿真研究平台")
	root.geometry("900x600")
	root.resizable(0, 0)

	# logo
	logo_label = tk.Label(root, image=logo)
	logo_label.place(x=10,y=10)
	# 实验背景部分
	bg_label = tk.Label(root, text="实验背景", font=("黑体",24))
	bg_label.place(x=350, y=115)
	bg_text = "为研究在产业联盟下各企业成员之间的信誉度，将使用本平台进行仿真研究"
	bg_text_label = tk.Label(root, text = bg_text, font=("仿宋",15), wraplength=800)
	bg_text_label.place(x =30,y=160)

	# 调整参数部分
	alterParamter = tk.Button(root, text="调整参数", font=("黑体",24))
	alterParamter.place(x=340,y=240)
	a=4
	ap_text = f"    在某个产业联盟中，共有{settings.totolEnterprise}个参与者，其中{settings.supplierNum}个供应商，{settings.manufactureNum}个制造商，该系统将会进行20次模拟决策过程，"+\
			f"并且将各企业的信誉度进行动态的展示，一些基本的参数为：在企业为诚信类型的前提下遵守承诺的概率为{settings.obeyWhileHonest}，在企业为"+\
		f"投机类型的前提下遵守承诺的概率为{settings.obeyWhileSpeculate}，更多的参数细节请点击调整参数"
	ap_text_label = tk.Label(root, text=ap_text, font=("仿宋",15), wraplength=800, justify="left", pady=10)
	ap_text_label.place(x=30,y=300)

	# 开始实验按钮
	startRun = tk.Button(root, text="开始实验", font=("黑体",24))
	startRun.place(x=250,y=450)
	# 重置按钮
	reset = tk.Button(root, text="重置", font=("黑体",24))
	reset.place(x=500,y=450)
	# 版权提示
	copyright = tk.Label(root, text="Copyright © 2019 战狼传说. All rights reserved.", font=("宋体",14))
	copyright.place(x=20,y=570)


settings = Settings()
root = tk.Tk()
logo = tk.PhotoImage(file="image/logo1.png")
initWindow(root,settings,logo)
root.mainloop()