import numpy as np 
class Center():
	"""
	联盟的中心
	接收各博弈方的报告，计算并且展示各成员信誉度
	"""
	def __init__(self, settings):
		self.settings = settings 
		
		# 初始化被评价的矩阵（和评价矩阵差一个转置）
		self.evaluateMatrix = None

	# 获取各参与方被评价矩阵
	def receiveReport(self, suppliers, manufacturers):
		rm = [0 for i in range(self.settings.totolEnterprise)]
		for i in range(self.settings.supplierNum):
			rm[i] = suppliers[i].reportMatrix
		for i in range(self.settings.manufactureNum):
			rm[i+2] = manufacturers[i].reportMatrix
		# 转置
		self.transform(rm)
		self.evaluateMatrix = rm 

	# 矩阵转置
	def transform(self, a):
		for i in range(len(a)):
			for j in range(i,len(a)):
				t = a[i][j]
				a[i][j] = a[j][i]
				a[j][i] = t 

	# 更新信誉度并且写入到各参与者中
	def updateTrustworthiness(self, suppliers, manufacturers):
		# 首先获取当前各参与方的信誉度
		tw = self.getTw(suppliers, manufacturers)
		em = self.evaluateMatrix

		p1 = self.settings.obeyWhileHonest		# p(遵守|诚信型)
		p2 = self.settings.cheatWhileHonest 	# p(偏离|诚信型)
		p3 = self.settings.obeyWhileSpeculate 	# p(遵守|投机型)
		p4 = self.settings.cheatWhileSpeculate 	# p(偏离|投机型)
		# 遍历参与方被评价矩阵，注意计算各自的信誉度列表
		tw_list = []
		for i in range(len(em)):
			h = 0 
			count = 0
			for j in range(len(em)):
				r = em[i][j]
				if r == -1:
					continue
				elif r == -2:
					h += tw[j]
					count += 1
				elif r == 1:
					h += (p1 * tw[j]) / (p1 * tw[j] + p3 * (1 - tw[j]))
					count += 1
				elif r == 0:
					h += (p2 * tw[j]) / (p2 * tw[j] + p4 * (1 - tw[j]))
					count += 1
			tw_list.append(h / count)
		# 将新产生的信誉度更新到各个参与方
		self.updateToParticipant(suppliers, manufacturers, tw_list)

	# 获取当前各参与方的信誉度
	def getTw(self, suppliers, manufacturers):
		tw = []
		for i in range(self.settings.supplierNum):
			tw.append(suppliers[i].trustworthiness)
		for i in range(self.settings.manufactureNum):
			tw.append(manufacturers[i].trustworthiness)
		return tw

	# 将新产生的信誉度更新到各个参与方
	def updateToParticipant(self, suppliers, manufacturers, tw):
		for i in range(self.settings.supplierNum):
			suppliers[i].trustworthiness = tw[i]
		for i in range(self.settings.manufactureNum):
			manufacturers[i].trustworthiness = tw[i+2]
