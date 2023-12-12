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
import matplotlib.pyplot as plt

start_id = 15
 
def trans_time(v_str):
    """转换GMT时间为标准格式"""
    GMT_FORMAT='%a %b %d %H:%M:%S +0800 %Y'
    timearray=datetime.datetime.strptime(v_str,GMT_FORMAT)
    ret_time=timearray.strftime("%Y-%m-%d %H:%M:%S")
    return ret_time
 
def get_bili_comment(weiboID_list,max_page):
    session = requests.Session()
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
            # 'cookie':'_T_WM=85512716398; MLOGIN=1; WEIBOCN_FROM=1110006030; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhCOXBy5U8P5383oK1HIpuJ5JpX5K-hUgL.FoeNS0-7Soq4eh52dJLoI05LxKML1h2LBo5LxKnL1h.LBozLxK.L1heL1h2LxK.L1hML1K2LxK.LBKqL1KLLdJBt; SCF=Atosv1bP171uPpe-v2gM7VqThsPml_n6r5qB4k3MpzdPeqKMqsrw4EltS3mxWfSA90xpJb0XfNQho4dQOd0aEkY.; SUB=_2A25IcrG6DeRhGeVJ7FcR9ijFyzyIHXVrDktyrDV6PUJbktANLUOikW1NT8L7n4MHs5dg7WuqJfnt8w0H7OS5aok6; SSOLoginState=1702281706; ALF=1704873706; XSRF-TOKEN=9f6e6c',
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
            print(url)
            time.sleep(random.random()*5)
            response = session.get(url, headers=headers)
            # 处理异常情况
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as errh:
                print("HTTP Error:", errh)
                break
            except requests.exceptions.ConnectionError as errc:
                print("Error Connecting:", errc)
                break
            except requests.exceptions.Timeout as errt:
                print("Timeout Error:", errt)
                break
            except requests.exceptions.RequestException as err:
                print("OOps: Something Else", err)
                break
            #ok = response.json()['ok']
            #print(ok)
            print("status_code:",response.status_code)
            try:
                data = response.json()
           # 处理 JSON 数据的现有代码
            except requests.exceptions.JSONDecodeError as e:
                print(f"JSON 解码错误: {e}")
                print(f"响应内容: {response.text}")
            # 根据需要处理非 JSON 响应

            max_id=response.json()['data']['max_id']
 
            #print(response.json()['data']['max_id'])
            print("max_id:",max_id)
 
            datas = []
            try:
                datas= response.json()['data']['data']
            except:
                print(f"page is {page}")
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
    weiboID_list=[str(x) for x in input("请输入微博ID(示例:4903111417922777),以逗号分隔：").split(',')]
    #weiboID_list=['4903111417922777']
    #最大爬取页
    max_page=int(input("请输入搜索的页数"))
    #调用爬取
    get_bili_comment(weiboID_list=weiboID_list,max_page=max_page)

