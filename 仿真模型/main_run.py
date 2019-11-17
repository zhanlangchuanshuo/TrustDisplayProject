# from participant import Participant
from manufacturer import Manufacturer
from supplier import Supplier
from settings import Settings
from center import Center
import functions as f 

settings = Settings()

# 初始化所有的参与方
suppliers = []
manufacturers = []
for i in range(settings.supplierNum):
	suppliers.append(Supplier(settings))
for i in range(settings.manufactureNum):
	manufacturers.append(Manufacturer(settings))

# 开始主循环
for gen in range(settings.cycleNum):
	# 供应商和制造商承诺-->计算promisedPrice和promisedOutput
	f.makingPromise(settings, suppliers, manufacturers)
	# 获得所有参与者的当期成本
	f.observeCost(settings, suppliers, manufacturers)
	# 供应商做出价格决策
	f.wholesalePriceDecision(settings, suppliers, manufacturers)
	# 供应商和制造商向中心汇报

	# 中心进行计算并更新参与者的信誉度

	# 每个参与者各自核算自身的实际利润（核算当前利润和累计利润）

	pass

