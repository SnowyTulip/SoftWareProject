# 允许副本存在，忽略报错
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
 
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
 
 
def view(info,weibo_file):
    my_font = font_manager.FontProperties(fname='./STHeiti-TC-Medium.ttf')  # 设置中文字体（图标中能显示中文）
    likes = info['评论点赞数']  # 点赞数
    reply = info['评论者粉丝数']  # 粉丝数
    forward = info['评论者关注数']  # 关注数
    author = info['评论者姓名']  # 作者，因为内容太长了
    # print(comment)
 
    # 为了坐标轴上能显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
 
    # **********************************************************************综合评分和播放量对比
    # *******点赞数条形图
    fig, ax1 = plt.subplots()
    length = len(author)
    plt.bar(x=np.arange(length), tick_label=author, height=likes, color='blue')  # 设置柱状图
    plt.title('评论点赞数、粉丝数和关注数的数据分析', fontproperties=my_font)  # 表标题
    ax1.tick_params(labelsize=6)
    plt.xlabel('微博内容')  # 横轴名
    plt.ylabel('评论点赞数')  # 纵轴名
    plt.xticks(rotation=90, color='green')  # 设置横坐标变量名旋转度数和颜色
 
    # *******评论者粉丝数折线图
    ax2 = ax1.twinx()  # 组合图必须加这个
    ax2.plot(reply, color='red')  # 设置线粗细，节点样式
    # *******评论者关注数折线图
    ax2.plot(forward, color='yellow')  # 设置线粗细，节点样式
    plt.ylabel('粉丝/关注数')  # y轴
 
    plt.plot(1, label='评论者点赞数', color="blue", linewidth=5.0)  # 图例
    #plt.plot(1, label='评论者粉丝数', color="red", linewidth=1.0, linestyle="-")  # 图例
    #plt.plot(1, label='评论者关注数', color="yellow", linewidth=1.0, linestyle="-")  # 图例
    plt.legend()
 
    plt.savefig('.\图片\pic-{}.png'.format(weibo_file), dpi=1000, bbox_inches='tight')  # 保存至本地
 
    plt.show()
 
 
def main(weibo_file):
    info = pd.read_csv(weibo_file,engine='python', encoding='utf-8-sig')
    info = info.nlargest(100, '评论点赞数')
    info = info.reset_index(drop=True)
    view(info,weibo_file)
 
 
if __name__ == '__main__':
    main('weiboComment_15pages_4903111417922777.csv')


