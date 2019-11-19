
class Settings():
	"""
	将所有的参数都放在Settings类中进行统一的管理
	方便后期连带的改动
	"""
	def __init__(self):

		"""==================在联盟层面的参数=================="""
		# 联盟中企业的个数
		self.totolEnterprise = 4
		# 联盟中供应商的个数
		self.supplierNum = 2 
		# 联盟中制造商的个数
		self.manufactureNum = 2 
		# 联盟中企业在诚信的情况下遵守承诺的概率p(遵守|诚信型)
		self.obeyWhileHonest = 0.8
		# 联盟中企业在诚信的情况下偏离承诺的概率p(偏离|诚信型)
		self.cheatWhileHonest = 1 - self.obeyWhileHonest
		# 联盟中企业在投机的情况下遵守承诺的概率p(遵守|投机型)
		self.obeyWhileSpeculate = 0.6
		# 联盟中企业在投机的情况下偏离承诺的概率p(偏离|投机型)
		self.cheatWhileSpeculate = 1-self.obeyWhileSpeculate
		# 需要进行模拟的次数
		self.cycleNum = 20 

		"""==================在价格模型PM层面的参数=================="""
		# 此处是价格模型P = M - Q
		# pm指代M
		self.pm = 10
