import requests
import re
import csv
import hashlib
import time
from urllib.parse import quote_plus
import random

# 构造请求头字典
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Cookie': "_uuid=878EE489-E678-C886-CB107-F39AB65ED71F63288infoc; buvid3=EFD6599E-E3D6-2B77-C814-EE5180E2D60962144infoc; b_nut=1696230264; buvid4=6749DD6E-1212-5687-67F0-8BFA855CE73A62144-023100215-y4ShB8cTHmk4j9F0FNLCWQ%3D%3D; CURRENT_FNVAL=4048; rpdid=|(J~J~JRkk)Y0J'uYmYkJ|J~m; SESSDATA=d31651b8%2C1711782421%2C17119%2Aa1CjALUSarmDjwuRBBD8jKNjjak0OY80GcX00oQj12rglLreZrQRWToDrkCMrGWbBPT5ISVnREaWF1VUdDaGJXa2V4ZkV0TjdWLVY4ZjFBb1NIX25tTk1UQS1UeHBQY1dQZGNjamJhVXdhMks0YnYwaXJKNnl4blJWQk5TTk4zcG50bm1kU3pJM2dBIIEC; bili_jct=7a5461c2c9b0c0e1fc9e4495151257f9; DedeUserID=396304390; DedeUserID__ckMd5=c7ab5e62eb1cc670; header_theme_version=CLOSE; buvid_fp_plain=undefined; CURRENT_QUALITY=80; enable_web_push=DISABLE; fingerprint=5521d8b38244af2d1c205f1a5637eeb0; buvid_fp=5521d8b38244af2d1c205f1a5637eeb0; bp_video_offset_396304390=873802192912384038; sid=7z8gpa7i; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDI1NTUwMTksImlhdCI6MTcwMjI5NTc1OSwicGx0IjotMX0.Q_xIreWF-iuJGTJKe4nYiu3PTHBvKsvkUkjX-j-4WvU; bili_ticket_expires=1702554959; PVID=1; home_feed_column=4; browser_resolution=718-777; b_lsid=93D31016D_18C5D23B1A4"
    }
g_base_url = "https://api.bilibili.com/x/v2/reply/wbi/main?oid=747023094&type=1&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=4f857129be750e0c5ecc8b9299484c7b&wts=1702346878"

def get_wid(pagination_str,timeStamp):
    ct = "ea1db124af3c7062474693fa704f4ff8"
    ut = {
    "oid":"747023094",
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

def read_data(response):
    f = open("./B_data.csv",mode = "a",encoding= 'utf-8',newline='')
    csv_writer = csv.DictWriter(f,fieldnames=["昵称","性别","地区","评论","点赞"])
    json_data = response.json()
    try:
        next_pagination_str = json_data["data"]["cursor"]["pagination_reply"]["next_offset"]
        session_id = json_data["data"]["cursor"]["session_id"]
        replies = json_data["data"]["replies"]
    except:
        print(response.text)
    csv_writer.writeheader()
    for item in replies:
        message = item['content']['message']
        like = item['like']
        member = item["member"]
        uname = member["uname"]
        sex = member["sex"]
        location  = item["reply_control"]["location"].replace("IP属地：","")
        data_dic = {"昵称":uname,"性别":sex,"地区":location,"评论":message,"点赞":like}
        csv_writer.writerow(data_dic)
        # print(f"昵称:{uname}  性别:{sex} 地区:{location}")
        # print(f"评论:{message}")
        # print(f"点赞{item['like']}")
        # print()
    f.close()
    next_pagination_str = '''{"offset":"{\\\"type\\\":1,\\\"direction\\\":1,\\\"session_id\\\":\\\"%s\\\",\\\"data\\\":{}}"}''' % session_id
    print(next_pagination_str)
    return next_pagination_str


def read_url(pagination_str,is_first = False,FirstUrl = "") :
    '''返回下一个page_id'''
    #参数部分
    timeStamp = int(time.time() * 1000)
    w_rid = get_wid(pagination_str,timeStamp)
    url = "https://api.bilibili.com/x/v2/reply/wbi/main"
    data = {
    "oid":"747023094",
    "type":"1",
    "mode":"3",
    "pagination_str":pagination_str,
    "plat":"1",
    "web_location":"1315875",
    'w_rid':f"{w_rid}",
    "wts":str(timeStamp)
    }
    res = ''
    if is_first:
        res = requests.get(url= FirstUrl,headers= headers)
    else:
        res = requests.get(url= url,headers= headers,params = data)
    next_pagination_str  = read_data(res)
    return next_pagination_str
    

if __name__ == "__main__":
    pagination_str = {"offset":""} #首次的pagination_str是空的
    first_url = "https://api.bilibili.com/x/v2/reply/wbi/main?oid=747023094&type=1&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=2ac902dd0fe6b7d6a0aff23db29f4b01&wts=1702372856"
    next_pagination_str = read_url("",is_first= True,FirstUrl = first_url)
    # print(get_wid(next_pagination_str,1702364752))
    time.sleep(random.randint(0,3))
    page_count = 18
    for index in range(page_count):
        next_pagination_str = read_url(next_pagination_str)
        time.sleep(random.randint(0,3))
        print(f"page:{index+1}")
    # print(next_pagination_str)
    # next_pagination_str = '''{"offset":"{\\\"type\\\":1,\\\"direction\\\":1,\\\"session_id\\\":\\\"1743229803535075\\\",\\\"data\\\":{}}"}'''
    # print(next_pagination_str)
    # print(get_wid(next_pagination_str,1702373092))



