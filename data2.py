import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig,ax = plt.subplots()

# xvalue = [1,2,3,4,5]
# yvalue = [1,4,9,16,25]

xvalue = range(1,1001)
# yval = []
# for x in xvalue:
#     yzhi=x**2
#     yval.append(yzhi)
# yvalue = [yval]
yvalue =[x**2 for x in xvalue]

ax.scatter(xvalue,yvalue,s=10,c='green')

#设置标题并给坐标轴加标签
ax.set_title("pingfang",fontsize=14)
ax.set_xlabel("zhi",fontsize=14)
ax.set_ylabel("zhidepingfang",fontsize=14)
ax.tick_params(axis='both',which='major',labelsize=14)
ax.axis([0,1100,0,1100000])

plt.show()
#保存图标
# plt.savefig('data2_test',bbox_inches='tight')