
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
		self.actualProfit = self.getactualProfit(self)
		# 参与者按照承诺获得的期望利润
		self.expectPromiseProfit = self.getEPP(self)
		# 参与者估计其它参与方的决策量后自己能获得的最大利润
		self.expectProfitByEstimate = self.getEPBE(self)
		# 参与者的历史总利润
		self.accumulatedProfit = 0 

	# 做出决策，产量或者价格
	def makingDecision(self):
		pass

	# 向中心汇报其它成员的遵守情况
	def report(self):
		pass

