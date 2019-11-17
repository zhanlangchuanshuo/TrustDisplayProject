import numpy as np 
from settings import Settings
class Center():
	"""
	联盟的中心
	接收各博弈方的报告，计算并且展示各成员信誉度
	"""
	def __init__(self, settings):
		self.settings = settings 
		# 初始化信誉度矩阵
		self.allTrustworthiness = self.initTW()
		# 初始化评价的矩阵
		self.evaluateMatrix = self.initEM()

	#初始化信誉度
	def initTW(self):
		"""初始化信誉度的值"""
		tw = []
		for i in range(self.settings.totolEnterprise):
			tw.append(1)
		return np.array(tw)

	# 重新设定成员信誉度的值
	def resetTW(self, tw=[1,1,1,1]):   
		"""
		重新设定成员信誉度的初始值
		默认为最开始的全是1，也能够传入所有成员信誉度的数组
		如果传入的数组长度小于企业的数量，将会在后面增补1补齐
		"""
		# 设定tw为numpy数组形式
		if not isinstance(tw,np.ndarray):
			tw = np.array(tw)
		# 如果数组元素小于原本长度，那么后面将用1补全
		if len(tw) != self.settings.totolEnterprise:
			while(len(tw)!=self.settings.totolEnterprise):
				tw = np.append(tw,1)		# 往后面增加1
		self.allTrustworthiness = tw

	# 初始化评价矩阵
	def initEM(self):
		em = [[0 for i in range(self.settings.totolEnterprise)] \
		for j in range(self.settings.totolEnterprise)]
		return np.array(em)

	# 获取各参与方评价矩阵

	# 收集各参与方的信誉度


# settings = Settings() 
# center = Center(settings)
# print(center.allTrustworthiness)
# center.resetTW([1,2,3])
# print(center.allTrustworthiness)
# center.resetTW()
# print(center.allTrustworthiness)
# a = np.array([1,2,3,4,5,6])
