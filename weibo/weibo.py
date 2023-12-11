import os.path
import re
from jsonpath import jsonpath
import requests
import pandas as pd
import datetime
from fake_useragent import UserAgent
import weibo_pic
 
def trans_time(v_str):
    """转换GMT时间为标准格式"""
    GMT_FORMAT='%a %b %d %H:%M:%S +0800 %Y'
    timearray=datetime.datetime.strptime(v_str,GMT_FORMAT)
    ret_time=timearray.strftime("%Y-%m-%d %H:%M:%S")
    return ret_time
 
def get_weibo_list(v_keyword,v_max_page):
    """
    爬取微博内容列表
    :param v_keyword: 搜索关键字
    :param v_max_page: 爬取前几页
    :return: None
    """
    # 保存文件名
    v_weibo_file = '微博清单_{}_前{}页.csv'.format(v_keyword,v_max_page)
    # 如果csv存在，先删除
    if os.path.exists(v_weibo_file):
        os.remove(v_weibo_file)
        print('微博清单存在，已删除：{}'.format(v_weibo_file))
    for page in range(1,v_max_page+1):
        print('===开始爬取第{}页微博==='.format(page))
        # 请求头
        ua = UserAgent()
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encording": "gzip, deflate, br"
        }
        #请求地址
        url='https://m.weibo.cn/api/container/getIndex'
        #请求参数
        params={
            "containerid":"100103type=1&q={}".format(v_keyword),
            "page_type":"searchall",
            "page":page
        }
        #发送请求
        r=requests.get(url,headers=headers,params=params)
        print(r.status_code)
        #解析json数据
        cards=r.json()["data"]["cards"]
        #微博内容
        text_list=jsonpath(cards,'$..mblog.text')
        #微博内容-正则表达式数据清洗
        dr=re.compile(r'<[^>]+>',re.S)
        text2_list=[]
        print('text_list is:')
        print(text_list)
        if not text_list:#如果未获取到微博内容，则进入下一轮循环
            continue
        if type(text_list)==list and len (text_list)>0:
            for text in text_list:
                text2=dr.sub('',text)#正则表达式提取微博内容
                print(text2)
                text2_list.append(text2)
        #微博创建时间
        time_list = jsonpath(cards, '$..mblog.created_at')
        time_list=[trans_time(v_str=i) for i in time_list]
        #微博作者
        author_list = jsonpath(cards, '$..mblog.user.screen_name')
        #微博id
        id_list = jsonpath(cards, '$..mblog.user.id')
        # 微博bid
        bid_list = jsonpath(cards, '$..mblog.bid')
        # 转发数
        reposts_count_list = jsonpath(cards, '$..mblog.reposts_count')
        # 评论数
        comments_count_list = jsonpath(cards, '$..mblog.comments_count')
        # 点赞数
        attitudes_count_list = jsonpath(cards, '$..mblog.attitudes_count')
        df=pd.DataFrame(
            {
                '页码':[page]*len(id_list),
                '微博id':id_list,
                '微博bid': bid_list,
                '微博作者': author_list,
                '发布时间': time_list,
                '微博内容': text2_list,
                '转发数': reposts_count_list,
                '评论数': comments_count_list,
                '点赞数': attitudes_count_list
            }
        )
        #表头
        if os.path.exists(v_weibo_file):
            header=None
        else:
            header=['页码','微博id','微博bid','微博作者','发布时间','微博内容','转发数','评论数','点赞数']
        column=['页码','微博id','微博bid','微博作者','发布时间','微博内容','转发数','评论数','点赞数']
        #保存到csv文件
        df.to_csv(v_weibo_file,mode='a+',index=False,columns=column, header=header,encoding='utf-8-sig')
        print('csv保存成功：{}'.format(v_weibo_file))
    # 数据清洗、去重
    df = pd.read_csv(v_weibo_file, engine='python', encoding='utf-8-sig')
    os.remove(v_weibo_file)
    # 删除重复数据
    df.drop_duplicates(subset='微博bid', inplace=True, keep='first')
    # 再次保存csv文件
    header = ['页码','微博id','微博bid','微博作者','发布时间','微博内容','转发数','评论数','点赞数']
    column=header
    df.to_csv(v_weibo_file, mode='a+', index=False, columns=column, header=header,encoding='utf-8-sig')
    print('数据清洗完成')
    weibo_pic.main(v_weibo_file)
 
 
if __name__=='__main__':
    # 爬取关键字
    search_keyword = input("请输入搜索的关键词")
    #爬取页数
    max_search_page=int(input("请输入搜索的页数"))
    #调用爬取微博函数
    get_weibo_list(v_keyword=search_keyword,v_max_page=max_search_page)

