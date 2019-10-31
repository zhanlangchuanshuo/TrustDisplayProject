from participant import Participant

class Manufacturer(Participant):
	def __init__(self, settings):
		super().__init__(settings)
		self.realOutput = 2
		self.promisedOutput = 1

		# 制造商的成本均值
		self.avgMs = 1
		# 当前制造商成本的实际值
		self.realMs = self.avgMs
		# 制造商的满意度下限satiesfaction floor（先在总的settings里面放着）
		self.msf = 0.8
		# 制造商的可接受下限acceptable floor
		self.maf = 0.6