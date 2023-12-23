import csv
import hashlib
import random
import time
from urllib.parse import quote_plus

import requests
from. import ISpider
print(__package__) 
from ..Configs.CommentConfig import CommentConfig
from ..Objects.Comment import comment

class SpiderComment:
    headers_ = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Cookie': "_uuid=878EE489-E678-C886-CB107-F39AB65ED71F63288infoc; buvid3=EFD6599E-E3D6-2B77-C814-EE5180E2D60962144infoc; b_nut=1696230264; buvid4=6749DD6E-1212-5687-67F0-8BFA855CE73A62144-023100215-y4ShB8cTHmk4j9F0FNLCWQ%3D%3D; CURRENT_FNVAL=4048; rpdid=|(J~J~JRkk)Y0J'uYmYkJ|J~m; SESSDATA=d31651b8%2C1711782421%2C17119%2Aa1CjALUSarmDjwuRBBD8jKNjjak0OY80GcX00oQj12rglLreZrQRWToDrkCMrGWbBPT5ISVnREaWF1VUdDaGJXa2V4ZkV0TjdWLVY4ZjFBb1NIX25tTk1UQS1UeHBQY1dQZGNjamJhVXdhMks0YnYwaXJKNnl4blJWQk5TTk4zcG50bm1kU3pJM2dBIIEC; bili_jct=7a5461c2c9b0c0e1fc9e4495151257f9; DedeUserID=396304390; DedeUserID__ckMd5=c7ab5e62eb1cc670; header_theme_version=CLOSE; buvid_fp_plain=undefined; CURRENT_QUALITY=80; enable_web_push=DISABLE; fingerprint=5521d8b38244af2d1c205f1a5637eeb0; buvid_fp=5521d8b38244af2d1c205f1a5637eeb0; bp_video_offset_396304390=873802192912384038; sid=7z8gpa7i; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDI1NTUwMTksImlhdCI6MTcwMjI5NTc1OSwicGx0IjotMX0.Q_xIreWF-iuJGTJKe4nYiu3PTHBvKsvkUkjX-j-4WvU; bili_ticket_expires=1702554959; PVID=1; home_feed_column=4; browser_resolution=718-777; b_lsid=93D31016D_18C5D23B1A4"
    }


    def __init__(self,headers = {},data_name = "",commentConfig = None):
        self.__headers = SpiderComment.headers_
        self.__configs = []
        self.__data_name = "test"
        self.__csv_writer = None
        self.__f = None
        self.__csv_writer = None
        self.__comment_data = [] #存放返回Comment对象

        if len(headers) != 0:
            self.__headers = headers
        if len(data_name) != 0:
            self.__data_name = data_name
        if commentConfig != None:
            self.commentConfig = commentConfig
        try:
            self.__f = open(f"./Data/{self.__data_name}.csv",mode = "a",encoding= 'utf-8',newline='')
            self.__csv_writer = csv.DictWriter(self.__f,fieldnames=["昵称","性别","地区","评论","点赞"])
            self.__csv_writer.writeheader()
        except:
            print(f"{data_name}.csv make error")
        

    
    def add_config(self,CommentConfig):
        self.__configs.append(CommentConfig)

    def set_config(self,commentConfig):
        '''使用这个配置爬取视频的配置
        需要先设置commentConfig中的oid
        '''
        self.commentConfig = commentConfig

    def spider_data(self):
        '''使用这个进行设置爬取对象
        返回一个List[comment]
        '''
        self.__comment_data.clear()
        self.__sipder_data(self.commentConfig)
        return self.__comment_data


    def __sipder_data(self,config:CommentConfig):
        pagination_str = config.get_pagination_str()
        oid = config.get_oid()
        url = config.get_base_url()
        while pagination_str !="":
            pagination_str = self.__read_url(pagination_str,oid,url)
            time.sleep(random.random() * 3)
        pass 

    def spider_data_all(self):
        for config in self.__configs:
            self.__sipder_data(config)
            
        pass


    def __read_url(self,pagination_str,oid,url):
        time_stamp = int(time.time() * 1000)
        w_rid = SpiderComment.__get_wid(pagination_str,time_stamp,oid)
        data = {
            "oid":f"{oid}",
            "type":"1",
            "mode":"3",
            "pagination_str":f"{pagination_str}",
            "plat":"1",
            "web_location":"1315875",
            'w_rid':f"{w_rid}",
            "wts":str(time_stamp)
        }
        next_pagination_str = ""
        try :
            res = requests.get(url= url,headers= self.__headers,params = data)
            next_pagination_str  = self.__write_data(res)
        except:
            print("read url error")
            next_pagination_str = ""    
        return next_pagination_str
    
    def __write_data(self,response):
        csv_writer = self.__csv_writer
        json_data = response.json()
        try:
            next_pagination_str = json_data["data"]["cursor"]["pagination_reply"]["next_offset"]
            session_id = json_data["data"]["cursor"]["session_id"]
            replies = json_data["data"]["replies"]
        except:
            print(response.text)
            print("read data error")
            next_pagination_str = ""
        # csv_writer.writeheader()
        try :
            for item in replies:
                message = item['content']['message']
                like = item['like']
                member = item["member"]
                uname = member["uname"]
                sex = member["sex"]
                location  = item["reply_control"]["location"].replace("IP属地：","")
                data_dic = {"昵称":uname,"性别":sex,"地区":location,"评论":message,"点赞":like}
                csv_writer.writerow(data_dic)
                #这里还需要添加返回评论的能力
                fcomment = comment(self.commentConfig.get_oid(),\
                                len(self.__comment_data),\
                                like,message,uname,location,sex)
                self.__comment_data.append(fcomment)
                # print(f"昵称:{uname}  性别:{sex} 地区:{location}")
                print(f"评论:{message}")
                # print(f"点赞{item['like']}")
                # print()
            next_pagination_str = '''{"offset":"{\\\"type\\\":1,\\\"direction\\\":1,\\\"session_id\\\":\\\"%s\\\",\\\"data\\\":{}}"}''' % session_id
        except:
            next_pagination_str = ""
        return next_pagination_str
    
    
    def __get_wid(pagination_str,timeStamp,oid):
        ct = "ea1db124af3c7062474693fa704f4ff8"
        ut = {
        "oid":f"{oid}",
        "type":"1",
        "mode":"3",
        "pagination_str":pagination_str,
        "plat":"1",
        "web_location":"1315875",
        "wts":str(timeStamp)
        }

        Nt = ['mode','oid','pagination_str','plat','seek_rpid','type','web_location','wts']
        Zt = []
        for kt in Nt:
            yt = ut.get(kt,None)
            if yt != None and yt == yt.replace('[!\'()*]', ''):
                Zt.append(quote_plus(kt) + '=' + quote_plus(yt))
        Ut = '&'.join(Zt)
        # print(Ut)
        s = Ut + ct
        MD5 = hashlib.md5()
        MD5.update(s.encode('utf-8'))
        w_rid = MD5.hexdigest()
        return w_rid
