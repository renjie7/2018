import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.matplotlib_fname()
print(matplotlib.matplotlib_fname())
##输入中文   修改matplotlib配置文件，去掉#，font.family ：Microsoft YaHei
#import matplotlib
#matplotlib.rcParams['font.sans-serif']=['SimHei']
#from pylab import mpl
#mpl.rcParams['font.sans-serif'] = ['SimHei']    #显示中文
#mpl.rcParams['aces.unicode_minus'] = False  #正常显示负号(不可行)
#matplotlib.rcParams['aces.unicode_minus']=False  #正常显示负号（不可行）
#画曲线
# 取均值点(在-1到1中，取50个点)
x = np.linspace(-3,3,50)
print(x)
y = x*x*2+2
y1 = x*(-x)*2+2

#设置轴的名称lable
plt.xlabel("我是xxxxxxx轴",color='blue')
plt.ylabel("I am y",color='purple')
#设置坐标轴名字title
plt.title('picture name',fontsize='large',fontweight='bold') #设置字体大小与格式
plt.title('图的名字 name',color='red') #设置字体颜色
#设置坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-5, 5))
#设置坐标轴刻度
my_x_ticks = np.arange(-3, 3, 1)
my_y_ticks = np.arange(-5, 5, 1)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
#修改图的显色，线条
plt.plot(x,y,
        color='blue',
         linewidth=1.0,
         linestyle='--',#线的样子
         label='line---111',
        )
plt.plot(x,y1,
         color='green',
         linewidth=5.0,
         )
plt.show()
