import matplotlib.pyplot as plt
from randomwalk import Ramdomwalk

#设置可控多次调试
# while True:
#     rw = Ramdomwalk(num_pionts=3000)
#     rw.fillwalk()
#
#     plt.style.use('classic')
#     fig, ax = plt.subplots()
#     ax.scatter(rw.x_value, rw.y_value, s=7, c='green')
#
#     plt.show()
#
#     keepruning = input("keep runing?(y/n): ")
#     if keepruning == 'n':
#         break

rw = Ramdomwalk(num_pionts=5000)
rw.fillwalk()

plt.style.use('classic')
#调整尺寸适应
fig,ax = plt.subplots(figsize=(16,9))
# fig, ax = plt.subplots()
#分别表示横纵坐标，s点的大小，c颜色，edgecolor消除点的轮廓，cmap为渐变
ax.scatter(rw.x_value, rw.y_value, s=3, c='green',cmap=plt.cm.Blues,edgecolor="none")
#突出起点和终点
ax.scatter(0,0,c='yellow',s=25)
ax.scatter(rw.x_value[-1],rw.y_value[-1],c='red',s=25)
#隐藏坐标轴
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)

plt.show()
