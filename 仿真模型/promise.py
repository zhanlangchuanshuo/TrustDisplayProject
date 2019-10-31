
class Promice():
	"""
	参与者进行承诺的类
	管理各参与者之间的各种承诺的量
	"""
	def __init__(self, settings, suppliers, manufacturers):
		self.suppliers = suppliers
		self.manufacturers = manufacturers
		self.settings = settings

	# 供应商的承诺价格计算,最终是改变供应商对象里面的承诺价格
	def makingPromisePrice(self):
		for i in range(settings.supplierNum):
			sup = self.suppliers[i]
			sup.promisedPrice = 
		pass

	# 制造商的承诺产量计算,最终是改变制造商对象里面的承诺价格
	def makingPromiseOutput(self):
		pass