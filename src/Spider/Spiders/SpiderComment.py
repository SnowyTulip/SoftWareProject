import hashlib
from urllib.parse import quote_plus
import ISpider

from Configs import CommentConfig

class SpiderComment(ISpider):
    headers_ = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Cookie': "_uuid=878EE489-E678-C886-CB107-F39AB65ED71F63288infoc; buvid3=EFD6599E-E3D6-2B77-C814-EE5180E2D60962144infoc; b_nut=1696230264; buvid4=6749DD6E-1212-5687-67F0-8BFA855CE73A62144-023100215-y4ShB8cTHmk4j9F0FNLCWQ%3D%3D; CURRENT_FNVAL=4048; rpdid=|(J~J~JRkk)Y0J'uYmYkJ|J~m; SESSDATA=d31651b8%2C1711782421%2C17119%2Aa1CjALUSarmDjwuRBBD8jKNjjak0OY80GcX00oQj12rglLreZrQRWToDrkCMrGWbBPT5ISVnREaWF1VUdDaGJXa2V4ZkV0TjdWLVY4ZjFBb1NIX25tTk1UQS1UeHBQY1dQZGNjamJhVXdhMks0YnYwaXJKNnl4blJWQk5TTk4zcG50bm1kU3pJM2dBIIEC; bili_jct=7a5461c2c9b0c0e1fc9e4495151257f9; DedeUserID=396304390; DedeUserID__ckMd5=c7ab5e62eb1cc670; header_theme_version=CLOSE; buvid_fp_plain=undefined; CURRENT_QUALITY=80; enable_web_push=DISABLE; fingerprint=5521d8b38244af2d1c205f1a5637eeb0; buvid_fp=5521d8b38244af2d1c205f1a5637eeb0; bp_video_offset_396304390=873802192912384038; sid=7z8gpa7i; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDI1NTUwMTksImlhdCI6MTcwMjI5NTc1OSwicGx0IjotMX0.Q_xIreWF-iuJGTJKe4nYiu3PTHBvKsvkUkjX-j-4WvU; bili_ticket_expires=1702554959; PVID=1; home_feed_column=4; browser_resolution=718-777; b_lsid=93D31016D_18C5D23B1A4"
    }

    def __init__(self,headers = {},data_name = ""):
        self.__headers = SpiderComment.headers_
        self.__configs = []
        self.__data_name = ""
        self.__csv_writer = None

        if len(headers) != 0:
            self.__headers = headers
        if len(data_name) != 0:
            self.__data_name = data_name
        try:
    
    def add_config(self,CommentConfig):
        self.configs.append(CommentConfig)

    @staticmethod
    def read_data(config:CommentConfig):

        pass

    def read_data(self,response):
        pass
    
    @staticmethod
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
