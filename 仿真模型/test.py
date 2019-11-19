# b = 0.7
# a = 1 if b>=0.5 else 0
# print(a)
# import numpy as np 
# import matplotlib.pyplot as plt 
# x = []
# y = []
# for i in range(10000):
# 	x.append(i)
# 	y.append(np.random.uniform(1,2.5))
# plt.scatter(x,y)
# plt.show()

# 计算y = x^2 - 2x + 1 的最小值，区间为[-1,4]
# zuixiaozhi = (-1)*(-1)-2*(-1)
# index = -1+0/1000000
# for i in range(1000000):
# 	x = -1 + i * 5/1000000
# 	f = x*x-2*x 
# 	if f<zuixiaozhi:
# 		zuixiaozhi = f 
# 		index = x 
# print(index,zuixiaozhi)

# from matplotlib import pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
# figure = plt.figure()
# ax = Axes3D(figure)
# X = np.arange(0.1,4,0.1)
# Y = np.arange(0.1,4,0.1)
# X,Y = np.meshgrid(X,Y)
# R1 = (Y/(X+Y))*(2/3)*(10-(X*Y)/(X+Y)-0.5)*(X-0.5)
# # R2 = 6*Y-X*Y-Y*Y
# # Z = np.cos(R)
# ax.plot_surface(X,Y,R1,rstride=1,cstride=1,cmap='rainbow')
# # ax.plot_surface(X,Y,R2,rstride=1,cstride=1,cmap='rainbow')
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# # print(np.sqrt(2))

# x = np.arange(0,10,0.1)
# y = x/(x+1)
# plt.plot(x,y)
# plt.show()
import numpy as np
print(np.random.uniform())
def transform(a):
	for i in range(len(a)):
		for j in range(i,len(a)):
			t = a[i][j]
			a[i][j] = a[j][i]
			a[j][i] = t 
a = [[1,2,3],[4,5,6],[7,8,9]]
transform(a)
print(a)



