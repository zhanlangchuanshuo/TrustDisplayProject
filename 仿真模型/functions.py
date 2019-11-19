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

	# 做出承诺的同时，最佳的收益也就得出来了
	for i in range(settings.supplierNum):
		suppliers[i].promisedPrice = price 
		suppliers[i].expectPromiseProfit = quantity * (price - suppliers[i].avgCost)
	for i in range(settings.manufactureNum):
		manufacturers[i].promisedOutput = quantity
		manufacturers[i].expectPromiseProfit = (settings.pm - 2 * quantity - price - manufacturers[i].avgCost) * quantity

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
	for i in range(settings.supplierNum):
		# 估计另一供应商的批发价(对于两个供应商来说是这样，如果不是两个供应商应当做调整)
		another_price = suppliers[1-i].promisedPrice * suppliers[1-i].trustworthiness + w_balance * (1 - suppliers[1-i].trustworthiness)
		
		# 此时的情况稍微有些复杂，如果没有承诺，制造商会完全根据供应商的价格来确定产量，
		# 但是有了承诺之后，制造商对供应商价格的反应函数稍微有些变化
		# 但是这个供应商在决策的时候不需要去考虑这种变化，只是按照其决策思路进行
		# 因此其决策的思路为供应商和制造商承诺的东西是不会变的，但是，如果供应商的价格变化了，制造商相应的最佳反应也发生了变化
		# 所以供应商估计制造商的产量，应该是一个与供应商价格有关的函数
		# 此时再去分析供应商利润函数，并求其最大值
		trust_price, suppliers[i].trustProfit = calculate_trustPrice(settings, suppliers, manufacturers, another_price)

		# Step3. 看可信收益有没有到达自身的决策临界点
		# 自身的最佳收益
		best = suppliers[i].expectPromiseProfit
		if suppliers[i].trustProfit / best >= suppliers[i].breakPoint:
			# 超过了临界点，就使用承诺的批发价
			suppliers[i].realPrice = suppliers[i].promisedPrice
		else:
			# 没有超过临界点，就用可信价格（最佳反应）
			suppliers[i].realPrice = trust_price

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

def calculate_trustPrice(settings, suppliers, manufacturers, w2):
	"""
	计算在使用信誉度估计不同参与者的情况下供应商的最佳反应
	"""
	tw = [manufacturers[i].trustworthiness for i in range(settings.manufactureNum)]
	cs = suppliers[0].realCost
	cm = manufacturers[0].avgCost
	M = settings.pm 
	# 下面为一些为方便进行简记的参数
	m1 = manufacturers[0].promisedOutput * sum(tw)
	m2 = 2 - sum(tw)
	m3 = (w2 ** 2) - w2 * cs 
	m4 = 2 * (w2 ** 2) * m2 
	m5 = 3 * w2 - cs 

	# 一元二次方程的三个系数
	m6 = 3 * m1 * m5 + m2 * m5 * (M - cm - 2 * w2) - m4 
	m7 = 3 * m1 * m3 + 3 * m1 * m5 * w2 + m2 * m3 * (M + cm - 2 * w2) + m2 * m5 * w2 * (M - cm) + m4 * (cs - w2) 
	m8 = w2 * (3 * m1 * m3 + m2 * m3 * (M - cm) + m4 * cs)
	# print(m6)
	# print(m7)
	# print(m8)
	# 可信的批发价
	tp = solveF(m6, m7, m8)
	# 可信的收益 
	w = 2 * tp * w2 / (tp + w2)
	qs = (M - w - cm) / 3
	ra = (tp - cs) * w2 * (m1 + m2 * qs)

	return tp ,ra 

def solveF(a, b, c):
	"""
	求解一元二次方程的函数
	其中a，b，c为三个系数
	"""
	delta = b *b - 4 * a * c 
	if delta < 0:
		return None
	elif delta == 0:
		x = -1.0 * b / (2 * a)
		if x > 0:
			return x 
		else:
			return None
	else:
		x1 = (-1*b+np.sqrt(delta))/(2*a)
		x2 = (-1*b-np.sqrt(delta))/(2*a)
		# print(x1)
		# print(x2)
		if x1 > 0:
			return x1
		if x2 > 0:
			return x2 
		return x1

def OutputDecision(settings, suppliers, manufacturers):
	"""
	制造商做出产量决策
	""" 
	# Step1. 计算分散决策的产量、获取此时两供应商的批发价
	w_balance ,q_balance = equilibriumDecision(settings, suppliers, manufacturers)
	w1, w2 = suppliers[0].realPrice, suppliers[1].realPrice
	M = settings.pm 
	cm = manufacturers[0].realCost
	for i in range(settings.manufactureNum):
		# Step2. 此时已经获得了批发价，估计另一制造商的产量
		another_output = manufacturers[1-i].promisedOutput * manufacturers[1-i].trustworthiness + q_balance * (1 - manufacturers[1-i].trustworthiness)

		# Step3. 此时该制造商在估计的前提下最佳反应产量和可信收益
		trust_output = (M - another_output - 2 * w1 * w2 / (w1 + w2) - cm) / 2
		manufacturers[i].trustProfit = trust_output * (M - trust_output - another_output - cm - 2*w1*w2/(w1+w2))

		# Step4. 看可信收益有没有达到或者决策临界点
		best = manufacturers[i].expectPromiseProfit
		if manufacturers[i].trustProfit / best >= manufacturers[i].breakPoint:
			# 超过决策临界点，不偏离
			manufacturers[i].realOutput = manufacturers[i].promisedOutput
		else:
			# 没有超过临界点，偏离
			manufacturers[i].realOutput = trust_output
	
def nowProfit(settings, suppliers, manufacturers):
	"""
	计算各参与方的实际收益
	"""
	M = settings.pm 
	w1 = suppliers[0].realPrice
	w2 = suppliers[1].realPrice
	q1 = manufacturers[0].realOutput
	q2 = manufacturers[1].realOutput
	# 制造商的实际利润
	for i in range(settings.manufactureNum):
		cm = manufacturers[i].realCost
		q1 = manufacturers[i].realOutput
		q2 = manufacturers[1-i].realOutput
		manufacturers[i].actualProfit = (M - q1 - q2 - cm - 2*w1*w2/(w1+w2)) * q1
	# 供应商的实际利润
	for i in range(settings.supplierNum):
		cs = suppliers[i].realCost
		w1 = suppliers[i].realPrice
		w2 = suppliers[1-i].realPrice
		suppliers[i].actualProfit = (w1 - cs) * (w2/(w1+w2)) * (q1 + q2)

def profitTillNow(settings, suppliers, manufacturers):
	"""
	计算各参与方的累计历史收益
	"""
	for i in range(settings.supplierNum):
		suppliers[i].accumulatedProfit += suppliers[i].actualProfit
	for i in range(settings.manufactureNum):
		manufacturers[i].accumulatedProfit += manufacturers[i].actualProfit

def submitReport(settings, suppliers, manufacturers):
	"""
	产生参与方的观察报告矩阵
	"""
	# 有小概率会产生错误
	# 供应商
	for i in range(settings.supplierNum):
		# 首先重置/初始化报告矩阵
		suppliers[i].resetReportMatrix()

		for j in range(settings.supplierNum):
			if i == j:
				suppliers[i].reportMatrix[i] = -1
			else:
				promise = suppliers[j].promisedPrice
				actual = suppliers[j].realPrice
				suppliers[i].reportMatrix[j] = getReport(promise, actual)
		# 供应商不需要评价制造商，因此，将制造商的评价设置为-2
		for j in range(settings.supplierNum, settings.totolEnterprise):
			suppliers[i].reportMatrix[j] = -2

	# 制造商
	for i in range(settings.manufactureNum):
		# 首先重置/初始化报告矩阵
		manufacturers[i].resetReportMatrix()

		for j in range(settings.supplierNum):
			promise = suppliers[j].promisedPrice
			actual = suppliers[j].realPrice
			manufacturers[i].reportMatrix[j] = getReport(promise, actual)
		for j in range(settings.supplierNum, settings.totolEnterprise):
			if (i+2) == j:
				manufacturers[i].reportMatrix[j] = -1
			else:
				promise = manufacturers[j-2].promisedOutput
				actual = manufacturers[j-2].realOutput
				manufacturers[i].reportMatrix[j] = getReport(promise, actual)			

def getReport(a, b):
	"""
	判断是否遵守承诺
	并且有一定的概率会出错
	a 为承诺量，b 为实际量
	"""
	if (np.abs(a - b) / a) <= 0.05:
		# 实际的跟承诺的相差不超过±5%
		m = np.random.uniform()
		if m < 0.95:
			return 1
	else:
		m = np.random.uniform()
		if m >= 0.95:
			return 1
	return 0

