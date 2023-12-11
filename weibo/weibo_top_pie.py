import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Pie
import matplotlib.pyplot as plt
 
def pie(weibo_file):
    plt.rcParams['font.family']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False
    data=pd.read_csv(weibo_file,engine='python', encoding='utf-8-sig')
    df1=data['热搜内容']
    df2=data['热搜热度']
 
    X=df1
    Y=[]
    s=sum(df2)
    for i in df2:
        a=i/s
        a=round(a,2)
        Y.append(a)
 
    plt.figure(figsize=(12, 12))
 
    plt.pie(x=Y,
           labels=X,
           wedgeprops={'width': 0.4},
           startangle=90,
            autopct='%.2f%%',
            pctdistance=0.9
          )
    plt.title('热搜对应的热度占比',fontsize=20)
    plt.savefig('.\图片\pie-{}.png'.format(weibo_file), dpi=1000, bbox_inches='tight')  # 保存至本地
    plt.show()
 
if __name__ == '__main__':
    pie('微博top_realtimehot.csv')


