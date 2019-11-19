from participant import Participant

class Manufacturer(Participant):
	def __init__(self, settings):
		super().__init__(settings)

		# 承诺产量和实际产量
		self.realOutput = 2
		self.promisedOutput = 1   

		# 成本的上下限具体取值
		self.lCost = 0 
		self.hCost = 1 
		self.avgCost = 0.5 * (self.lCost + self.hCost)
		self.realCost = self.getRealCost(self.lCost, self.hCost)