import matplotlib.pyplot as plt
#绘制折线图
# plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
# plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置

#设置样式
plt.style.use("seaborn-ticks")

#输入值为input_value,输出值为squares
input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]
#fig表示整张图片，ax表示图片中的各图标
fig,ax = plt.subplots()
ax.plot(input_value,squares,linewidth=2)

#设置标题并给坐标轴加标签
ax.set_title("pingfang",fontsize=14)
ax.set_xlabel("zhi",fontsize=14)
ax.set_ylabel("zhidepingfang",fontsize=14)
ax.tick_params(axis='both',labelsize=10)

plt.show()
