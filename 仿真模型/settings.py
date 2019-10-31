
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

		# 这一部分放到供应商和制造商各自的类中，方便后面的修改
		# """==================在供应商层面的参数=================="""
		# # 供应商的成本均值
		# self.cs = 1 
		# # 供应商的满意度下限satiesfaction floor（先在总的settings里面放着）
		# self.ssf = 0.8
		# # 供应商的可接受下限acceptable floor
		# self.saf = 0.6

		# """==================在制造商层面的参数=================="""
		# # 制造商的成本均值
		# self.ms = 1
		# # 制造商的满意度下限satiesfaction floor（先在总的settings里面放着）
		# self.msf = 0.8
		# # 制造商的可接受下限acceptable floor
		# self.maf = 0.6

		"""==================在价格模型PM层面的参数=================="""
		# 此处是价格模型P = M - k * Q，有两个参数
		# pm中第一个参数是指的M，第二个参数指的k
		self.pm = [10,1]
