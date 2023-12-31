import random
import time
import requests
from ..Objects.Video import video
from ..DataBase.DataCreate import dataBase
BVList = ['BV16b4y15765', 'BV1rH4y1C7kP', 'BV1VH4y117fN', 'BV1AN4y1U7ML', 'BV1YC4y1m7uS', 'BV1iw411N7sb', 'BV19Q4y1n7Qb', 'BV1Nw411s7NN', 'BV1mu4y1E7Z7', 'BV15w411X7zG', 'BV1qQ4y1W7Sp', 'BV1EC4y157LL', 'BV13w411r7By', 'BV1G34y1V7k2', 'BV1vr4y1f7sL', 'BV12h4y187dT', 'BV1A34y1N7Bu', 'BV17h4y1e7Rg', 'BV1MN411H7AJ', 'BV1Lj411k7DC', 'BV1ij41117RF', 'BV1594y147y4', 'BV1tP411Y7vG', 'BV1Zj411i72P']

class UP:
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Coockie':"_uuid=878EE489-E678-C886-CB107-F39AB65ED71F63288infoc; buvid3=EFD6599E-E3D6-2B77-C814-EE5180E2D60962144infoc; b_nut=1696230264; buvid4=6749DD6E-1212-5687-67F0-8BFA855CE73A62144-023100215-y4ShB8cTHmk4j9F0FNLCWQ%3D%3D; rpdid=|(J~J~JRkk)Y0J'uYmYkJ|J~m; SESSDATA=d31651b8%2C1711782421%2C17119%2Aa1CjALUSarmDjwuRBBD8jKNjjak0OY80GcX00oQj12rglLreZrQRWToDrkCMrGWbBPT5ISVnREaWF1VUdDaGJXa2V4ZkV0TjdWLVY4ZjFBb1NIX25tTk1UQS1UeHBQY1dQZGNjamJhVXdhMks0YnYwaXJKNnl4blJWQk5TTk4zcG50bm1kU3pJM2dBIIEC; bili_jct=7a5461c2c9b0c0e1fc9e4495151257f9; DedeUserID=396304390; DedeUserID__ckMd5=c7ab5e62eb1cc670; header_theme_version=CLOSE; buvid_fp_plain=undefined; CURRENT_QUALITY=80; enable_web_push=DISABLE; CURRENT_FNVAL=4048; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDM0MjI2MDksImlhdCI6MTcwMzE2MzM0OSwicGx0IjotMX0.jlBKdnB7AJJd_44hAHdzzzv4X_NY5R6K3HDo6aCLLW4; bili_ticket_expires=1703422549; home_feed_column=5; sid=7x59vocc; fingerprint=b10aeb1e2384b2cf001e1ee3d6bdeb15; buvid_fp=fa93fba8056bcc6711aac74e254b3a70; browser_resolution=2048-1042; PVID=1; b_lsid=4B610ED35_18C8D1B8166; bp_video_offset_396304390=877617734508085316",    'Origin':'https://space.bilibili.com',
    'Referer':'https://space.bilibili.com/544261015/video'
    }
    def __init__(self,mid = "544261015",db = None) -> None:
        self.mid = "544261015"
        self.mannager_id = ""
        self.location = "北京"
        self.sex   = "男"
        self.age   = ""
        self.level = "LV6"
        self.uper_name = "Chris的军事基地"
        #应当存储BV号和oid ,当然oid 可以通过爬取获得
        self.BVList = BVList
        self.oidList = [] 
        #up主应当持有video对象
        self.videos = []
        self.db = db
        self.initData()
        

    def writeDataBase(self,db):
        # 保存up自身的数据
        db.ResetDatabases()
        db.insert_uper_data(self.getData())
        
        # 保存video数据
        # for v in self.videos:
        #     v.writeDataBase(self.db)

    def getData(self)->dict:
        user_data = {
        'uper_id': f'{self.mid}',
        'mannager_id': f'{"001"}',
        'location': f'{self.location}',
        'sex': f'{self.sex}',
        'age': f'{26}',
        'uper_name': f'{self.uper_name}'
        }
        return user_data
    def initData(self):
        self.writeDataBase(self.db)
        #先初始化oids 
        self.__get_oids()
        #获取视频对象列表
        self.__get_videos() 
    
    def __get_videos(self):
        for i in range(len(self.BVList)):
            time.sleep(random.randint(0,3))
            self.videos.append(video(self.oidList[i] ,self.BVList[i],self.mid,self.db))

    def __get_oids(self):
        self.oidList = [self.__get_oid(BV) for BV in self.BVList]
    
    def __get_oid(self,BV):
        time.sleep(random.randint(0,3))
        url = f"https://api.bilibili.com/x/web-interface/view?bvid={BV}"
        response = requests.get(url,headers=UP.headers)
        data = response.json()
        oid = data['data']['aid']
        print("BV:",BV,"oid:",oid)
        return oid


if __name__ == "__main__":
    user = UP()
