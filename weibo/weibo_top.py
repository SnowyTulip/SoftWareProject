import os.path
import re
from jsonpath import jsonpath
import requests
import pandas as pd
from fake_useragent import UserAgent
import weibo_top_pic
import weibo_top_pie
import draw_cloud
 
def get_weibo_top():
    keyword=list(['realtimehot','gym','game','fun'])
    for search_keyword in keyword:
        # 保存文件名
        v_weibo_file = '微博top_{}.csv'.format(search_keyword)
        # 如果csv存在，先删除
        if os.path.exists(v_weibo_file):
            os.remove(v_weibo_file)
            print('微博榜单存在，已删除：{}'.format(v_weibo_file))
        print('===开始爬取{}微博榜单==='.format(search_keyword))
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
            "containerid":"106003type=25&t=3&disable_hot=1&filter_type={}".format(search_keyword),
            "title": "微博热搜",
            "show_cache_when_error": 1,
            "extparam": "seat=1&dgr=0&filter_type=realtimehot&region_relas_conf=0&pos=0_0&c_type=30&lcate=1001&mi_cid=100103&cate=10103&display_time=1684642048&pre_seqid=144917672",
            "luicode": 10000011,
            "lfid": 231583,
        }
        #发送请求
        r=requests.get(url,headers=headers,params=params)
        print(r.status_code)
        #解析json数据
        cards=r.json()["data"]["cards"][0]["card_group"]
        #热搜内容
        text_list=jsonpath(cards,'$..desc')
        print('text_list is:')
        print(text_list)
        #热搜连接地址
        href_list = jsonpath(cards, '$..scheme')
        # 热搜排名
        order_list = jsonpath(cards, '$..pic')
        # 热搜热度
        view_count_list = jsonpath(cards, '$..desc_extr')
        j=1
        for i in range(0, len(order_list)):
            if order_list[i] == 'https://simg.s.weibo.com/20210408_search_point_orange.png':
                order_list[i] = '无'
                view_count_list[i]=0
                continue
            if order_list[i] == "https://simg.s.weibo.com/20180205110043_img_search_stick%403x.png":
                view_count_list.insert(0, 0)
                order_list[i] = '无'
                continue
            view_count_list[i]=str(view_count_list[i])
            view_count_list[i]=int(re.sub("\D", "", view_count_list[i]))
            order_list[i] = j
            j = j + 1
        print(len(order_list),len(text_list),len(view_count_list),len(href_list))
        df=pd.DataFrame(
            {
                '热搜排名':order_list,
                '热搜内容': text_list,
                '热搜热度': view_count_list,
                '热搜连接地址': href_list,
            }
        )
        #表头
        if os.path.exists(v_weibo_file):
            header=None
        else:
            header=['热搜排名','热搜内容','热搜热度','热搜连接地址']
        column = ['热搜排名','热搜内容','热搜热度','热搜连接地址']
        #保存到csv文件
        df.to_csv(v_weibo_file,mode='a+',index=False,columns=column, header=header, encoding='utf-8-sig')
        print('csv保存成功：{}'.format(v_weibo_file))
        weibo_top_pic.main(v_weibo_file)
        weibo_top_pie.pie(v_weibo_file)
        #draw_cloud.draw_cloud(v_weibo_file)
 
 
if __name__=='__main__':
    #调用爬取微博函数
    get_weibo_top()


