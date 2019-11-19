from manufacturer import Manufacturer
from supplier import Supplier
from settings import Settings
from center import Center
import functions as f 
import window as wf
import tkinker as tk 

settings = Settings()
center = Center(settings)

# 初始化所有的参与方
suppliers = []
manufacturers = []
for i in range(settings.supplierNum):
	suppliers.append(Supplier(settings))
for i in range(settings.manufactureNum):
	manufacturers.append(Manufacturer(settings))

# 创建窗口
root = tk.Tk()
logo = tk.PhotoImage(file="image/logo1.png")
wf.initWindow(root, settings, suppliers, manufacturers, logo)


# 开始主循环
for gen in range(settings.cycleNum):
	# 供应商和制造商承诺-->计算promisedPrice和promisedOutput
	f.makingPromise(settings, suppliers, manufacturers)
	# 获得所有参与者的当期成本
	f.observeCost(settings, suppliers, manufacturers)
	# 供应商做出价格决策
	f.wholesalePriceDecision(settings, suppliers, manufacturers)
	# 制造商做出产量决策
	f.OutputDecision(settings, suppliers, manufacturers)
	# 计算各参与者的实际收益
	f.nowProfit(settings, suppliers, manufacturers)
	# 计算各参与方的累计历史收益
	f.profitTillNow(settings, suppliers, manufacturers)
	# 参与方产生报告矩阵
	f.submitReport(settings, suppliers, manufacturers)
	# 中心收集各参与方的报告矩阵
	center.receiveReport(suppliers, manufacturers)
	# 中心计算各参与者的信誉度并更新显示
	center.updateTrustworthiness(suppliers, manufacturers)
	pass

tw = []
for i in range(2):
	tw.append(suppliers[i].accumulatedProfit)
for i in range(2):
	tw.append((manufacturers[i].accumulatedProfit))
print(tw)
