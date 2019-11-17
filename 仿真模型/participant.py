import numpy as np 

class Participant():
	"""
	所有参与者的父类，其中有所有参与者共同的行为以及属性
	"""

	def __init__(self, settings):
		"""
		
		"""
		self.settings = settings

		# 企业的类型:0表示诚信型、1表示投机型
		self.orientation = 0

		# 参与者的信誉度
		self.trustworthiness = 1 

		# 参与者最终的实际利润
		self.actualProfit = 0
		# 参与者按照承诺获得的期望利润，即最优期望收益
		self.expectPromiseProfit = 0 
		# 参与者估计其它参与方的决策量后自己能获得的最大利润，即可信收益
		self.trustProfit = 0 
		# 参与者的历史总利润
		self.accumulatedProfit = 0 

		# 参与者的决策临界点
		self.breakPoint = 0.6 if self.orientation==0 else 0.8

		# 控制量，成本下限
		self.lCost = 0 
		# 控制量，成本上限
		self.hCost = 1
		# 参与者的平均生产制造成本（就是下限和上限的均值）
		self.avgCost = 0.5 * (self.lCost + self.hCost)
		# 参与者的实际生产制造成本
		self.realCost = 0.5 

		# 参与者的报告矩阵
		self.reportMatrix = None 

	def setBreakPoint(self, value):
		"""
		修改参与者的决策临界点
		"""
		self.breakPoint = value 

	def resetReportMatrix(self):
		"""
		重置报告矩阵
		报告矩阵的样式是改参与者观察到与其有承诺的相关参与者的遵循承诺的情况，并且予以汇报的矩阵
		其中-1表示没有承诺，0表示观察到某参与者没有遵守承诺，1表示观察到某参与者遵守承诺
		"""
		self.reportMatrix = [-1 for i in range(self.settings.totolEnterprise)]

	def getRealCost(self, lCost, hCost):
		"""
		获得参与者当期的实际成本
		实际成本是用均匀分布进行随机产生的
		"""
		self.realCost = np.random.uniform(lCost, hCost)

	def setOrientation(self, value):
		if value == 0 or value == 1:
			self.orientation = value 
		else:
			# 应该引发一个异常处理需要再次输入
			pass


