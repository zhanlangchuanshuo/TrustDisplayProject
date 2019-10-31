from participant import Participant

class Supplier(Participant):
	def __init__(self, settings):
		super().__init__()
		self.realPrice = 1
		self.promisedPrice = 2


		# 供应商的满意度下限satiesfaction floor（先在总的settings里面放着）
		self.ssf = 0.8
		# 供应商的可接受下限acceptable floor
		self.saf = 0.6

		# 供应商的成本均值
		self.avgCs = 1 
		# 当前供应商成本的实际值
		self.realCs = self.realCs

		

