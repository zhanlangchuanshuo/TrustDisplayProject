from participant import Participant

class Supplier(Participant):
	def __init__(self, settings):
		super().__init__(settings)

		# 承诺价格和实际价格
		self.realPrice = 1
		self.promisedPrice = 2

		# 成本的上下限具体取值
		self.lCost = 0 
		self.hCost = 1 
		self.avgCost = 0.5 * (self.lCost + self.hCost)
		self.realCost = self.getRealCost(self.lCost, self.hCost)
