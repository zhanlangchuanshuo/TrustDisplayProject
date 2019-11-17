import numpy as np 

def makingPromise(settings, suppliers, manufacturers):
	"""
	期初，供应商和制造商制定承诺
	承诺的原则是按照供应链利益最大化/或者说是完全信息动态博弈的均衡
	"""
	# w = (M-cm+cs)/2
	price = (settings.pm - manufacturers[0].avgCost + suppliers[0].avgCost) / 2
	# q = (M-w-cm)/4
	quantity = (settings.pm - price - manufacturers[0].avgCost) / 4

	for i in range(settings.supplierNum):
		suppliers[i].promisedPrice = price 
	for i in range(settings.manufactureNum):
		manufacturers[i].promisedOutput = quantity

def observeCost(settings, suppliers, manufacturers):
	"""
	计算所有参与者当期的实际成本
	"""
	for i in range(settings.supplierNum):
		suppliers[i].getRealCost(suppliers[i].lCost, suppliers[i].hCost)
	for i in range(settings.manufactureNum):
		manufacturers[i].getRealCost(manufacturers[i].lCost, manufacturers[i].hCost)

def wholesalePriceDecision(settings, suppliers, manufacturers):
	"""
	供应商做出价格决策
	"""
	# Step1. 分散决策的两个变量w和q
	w_balance ,q_balance = equilibriumDecision(settings, suppliers, manufacturers)

	# Step2. 供应商会根据信誉度估算自身的可信收益
	# 估计制造商的总产量Q = qa+qb
	Q = 0 
	for i in range(settings.manufactureNum):
		Q += (manufacturers[i].promisedOutput * manufacturers[i].trustworthiness + q_balance * (1 - manufacturers[i].trustworthiness))
	for i in range(settings.supplierNum):
		# 估计另一供应商的批发价
		another_price = suppliers[1-i].promisedPrice * suppliers[1-i].trustworthiness + w_balance * (1 - suppliers[1-i].trustworthiness)
		# 该供应商预计能够获得的订单数量

def equilibriumDecision(settings, suppliers, manufacturers):
	"""
	分散决策
	获得均衡产量和均衡价格
	"""
	# w = (1/4)*[M-cm+sqrt((M-cm)(M-cm+8cs))]
	a = settings.pm - manufacturers[0].avgCost
	w = 0.25 * (a + np.sqrt(a * (a + 8 * suppliers[0].avgCost)))
	q = (a - w) / 3
	return w, q

