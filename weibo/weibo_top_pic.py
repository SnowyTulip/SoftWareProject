# 允许副本存在，忽略报错
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
 
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
 
 
def view(info,weibo_file):
    my_font = font_manager.FontProperties(fname='./STHeiti-TC-Medium.ttf')  # 设置中文字体（图标中能显示中文）
    heat = info['热搜热度']
    content = info['热搜内容']
 
    # 为了坐标轴上能显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
 
    # **********************************************************************综合评分和播放量对比
    # *******点赞数条形图
    fig, ax1 = plt.subplots()
    length=len(content)
    plt.bar(x = np.arange(length),tick_label=content, height=heat, color='blue')  # 设置柱状图
    plt.title('热搜内容和热搜热度的数据分析', fontproperties=my_font)  # 表标题
    ax1.tick_params(labelsize=6)
    plt.xlabel('热搜内容')  # 横轴名
    plt.ylabel('热搜热度')  # 纵轴名
    plt.xticks(rotation=90, color='green')  # 设置横坐标变量名旋转度数和颜色
 
    plt.plot(1, label='热搜热度', color="blue", linewidth=5.0)  # 图例
    plt.legend()
 
    plt.savefig('.\图片\pic-{}.png'.format(weibo_file), dpi=1000, bbox_inches='tight')  # 保存至本地
 
    plt.show()


