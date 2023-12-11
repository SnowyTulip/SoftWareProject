import requests# 发送请求
import pandas as pd#保存csv文件
import os # 判断文件是否存在
import datetime
import time
from time import sleep# 设置等待，防止反爬
import json
import random# 生成随机数
import os.path
import requests
import csv
import re
import weibo_comment_pic
 
def trans_time(v_str):
    """转换GMT时间为标准格式"""
    GMT_FORMAT='%a %b %d %H:%M:%S +0800 %Y'
    timearray=datetime.datetime.strptime(v_str,GMT_FORMAT)
    ret_time=timearray.strftime("%Y-%m-%d %H:%M:%S")
    return ret_time
 
def get_bili_comment(weiboID_list,max_page):
    for weibo_id in weiboID_list:
 
        #保存文件名
        wbComment_file='weiboComment_{}pages_{}.csv'.format(max_page,weibo_id)
        #如果csv存在，先删除
        if os.path.exists(wbComment_file):
            os.remove(wbComment_file)
            print('存在，已删除：{}'.format(wbComment_file))
        #请求头
        headers = {
            #不加cookie只能爬一页
            'cookie':'__bid_n=1883c7fc76e10d57174207; FPTOKEN=IBsER/uKazbtpMIEgvaOTfAuHsmYQM5g0VL9U1G3ybs72PsWHEBbiKv0w+R59BrOvSwxDKJevIDwL0SSwPV5yWd3lIFsx6KXQ/qYPpPTjTRW5kFr+j74rsScC6MKc1G9142e5tEEf7atvY/zTxl9B6jy/y7MEo0ETLT0VjL6nbpzkWe/SnIw97Tjb+9lqYoGHS6lPqZ5yAhDPKn0KK4htwxqr0qMglAG6ZcT7mn+BUZAygRSrqWZwZ6KSE0r27qsR0bDTAI8dsQFq1gPfYONp5UHfw9FFsBiscLULixqm31wTHYziK8gxi0/R6yIQ8Tq3OQkNmx+Kw7E/8YknGOiVmpjfRn5FNShZs3/t8SNBJEcZ9qaQnw/iF/jwPoFkMXz87Tp22aQUmFgeQu/u0wAYQ==|wC9ITrusKUtoBk6wTqvs+jaY6iwSJyX4pD0y+hSvnOA=|10|acf98643db3def55913fefef5034d5ee; WEIBOCN_FROM=1110106030; loginScene=102003; SUB=_2A25JbkPWDeRhGeNH7FIV-SjKzjyIHXVqkW2erDV6PUJbkdAGLRbkkW1NSoXhCHcUhbni8gGXfjdc5HNqec9qABj_; MLOGIN=1; _T_WM=98495433469; XSRF-TOKEN=a62fb7; mweibo_short_token=9f0e28d6c9; M_WEIBOCN_PARAMS=oid%3D4903111417922777%26luicode%3D20000061%26lfid%3D4903111417922777%26uicode%3D20000061%26fid%3D4903111417922777',
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            'X-Xsrf-Token':'a62fb7'
        }
        max_id = ''
        for page in range(1,max_page + 1):
 
            if page==1:#第一页没有max_id参数
                 url='https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id_type=0'.format(weibo_id,weibo_id)
 
 
            else:
 
                if max_id == '0':#max_id=0，说明没有下一页了，结束循环
                    print('max_id==0,break now')
                    break
                url='https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id={}&max_id_type=0'.format(weibo_id,weibo_id,max_id)
 
            response = requests.get(url, headers=headers)
            #ok = response.json()['ok']
            #print(ok)
            print(response.status_code)
            max_id=response.json()['data']['max_id']
 
            #print(response.json()['data']['max_id'])
            print(max_id)
 
 
 
            datas= response.json()['data']['data']
            page_list = []
            id_list = []
            text_list=[]
            time_list=[]
            like_count_list=[]
            source_list=[]
            username_list=[]
            user_id_list=[]
            user_gender_list=[]
            follow_count_list=[]
            followers_count_list=[]
 
            for data in datas:
                page_list.append(page)
                id_list.append(data['id'])
                dr=re.compile(r'<[^>]+>',re.S)#用正则表达式清洗评论数据
 
                text2 = dr.sub('', data['text'])
                text_list.append(text2)#评论内容
                time_list.append(trans_time(data['created_at']))#评论时间
                like_count_list.append(data['like_count'])#点赞
                source_list.append(data['source'])#属地
                username_list.append(data['user']['screen_name'])#评论者姓名
                user_id_list.append(data['user']['id'])
                user_gender_list.append(data['user']['gender'])# 评论者性别
                follow_count_list.append(data['user']['follow_count'])#评论者关注数
                followers_count=str(data['user']['followers_count'])
                if(followers_count[-1]=='万'):
                    followers_count=int(float(followers_count.strip('万')))*10000
                followers_count_list.append(followers_count)#评论者粉丝数
 
                #把列表拼接为dataFrame数据
                df=pd.DataFrame({
                    '评论页码':page_list,
                    '微博id':[weibo_id]*len(time_list),
                    '评论id':id_list,
                    '评论内容':text_list,
                    '评论时间':time_list ,
                    '评论点赞数':like_count_list,
                    '评论属地':source_list,
                    '评论者姓名':username_list ,
                    '评论者id':user_id_list ,
                    '评论者性别':user_gender_list,
                    '评论者关注数':follow_count_list,
                    '评论者粉丝数':followers_count_list,
                })
                # 表头
                if os.path.exists(wbComment_file):
                    header = None
                else:
                    header = ['评论页码','微博id', '评论id','评论内容','评论时间','评论点赞数','评论属地', '评论者姓名','评论者id','评论者性别', '评论者关注数','评论者粉丝数']
                column=['评论页码','微博id', '评论id','评论内容','评论时间','评论点赞数','评论属地', '评论者姓名','评论者id','评论者性别', '评论者关注数','评论者粉丝数']
 
                # 保存到csv文件
                df.to_csv(wbComment_file, mode='a+', index=False, columns=column, header=header, encoding='utf-8-sig')
                #print('csv保存成功：{}'.format(bili_file))
            #print(df)
            print('第{}页爬取完成'.format(page))
 
 
        # 数据清洗、去重
        df = pd.read_csv(wbComment_file, engine='python', encoding='utf-8-sig')
        os.remove(wbComment_file)
        # 删除重复数据
        df.drop_duplicates(subset='评论内容', inplace=True, keep='first')
        # 再次保存csv文件
        column=header = ['评论页码', '微博id', '评论id', '评论内容', '评论时间', '评论点赞数', '评论属地', '评论者姓名',
                  '评论者id', '评论者性别', '评论者关注数', '评论者粉丝数']
        df.to_csv(wbComment_file, mode='a+', index=False, columns=column,header=header, encoding='utf-8-sig')
        print('数据清洗完成')
        weibo_comment_pic.main(wbComment_file)
 
 
if __name__=='__main__':
    #目标微博https: // m.weibo.cn / detail / 4903111417922777
    #目标微博ID，可循环爬取多个（这里只爬一个）
    weiboID_list=[str(x) for x in input("请输入微博ID(示例：4903111417922777),以逗号分隔：").split(',')]
    #weiboID_list=['4903111417922777']
    #最大爬取页
    max_page=int(input("请输入搜索的页数"))
    #调用爬取
    get_bili_comment(weiboID_list=weiboID_list,max_page=max_page)

