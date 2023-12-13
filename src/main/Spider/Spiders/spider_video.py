import requests
import time
import random
import requests
from bs4 import BeautifulSoup

# 构造请求头字典
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Cookie': "_uuid=878EE489-E678-C886-CB107-F39AB65ED71F63288infoc; buvid3=EFD6599E-E3D6-2B77-C814-EE5180E2D60962144infoc; b_nut=1696230264; buvid4=6749DD6E-1212-5687-67F0-8BFA855CE73A62144-023100215-y4ShB8cTHmk4j9F0FNLCWQ%3D%3D; CURRENT_FNVAL=4048; rpdid=|(J~J~JRkk)Y0J'uYmYkJ|J~m; SESSDATA=d31651b8%2C1711782421%2C17119%2Aa1CjALUSarmDjwuRBBD8jKNjjak0OY80GcX00oQj12rglLreZrQRWToDrkCMrGWbBPT5ISVnREaWF1VUdDaGJXa2V4ZkV0TjdWLVY4ZjFBb1NIX25tTk1UQS1UeHBQY1dQZGNjamJhVXdhMks0YnYwaXJKNnl4blJWQk5TTk4zcG50bm1kU3pJM2dBIIEC; bili_jct=7a5461c2c9b0c0e1fc9e4495151257f9; DedeUserID=396304390; DedeUserID__ckMd5=c7ab5e62eb1cc670; header_theme_version=CLOSE; buvid_fp_plain=undefined; CURRENT_QUALITY=80; enable_web_push=DISABLE; fingerprint=5521d8b38244af2d1c205f1a5637eeb0; buvid_fp=5521d8b38244af2d1c205f1a5637eeb0; bp_video_offset_396304390=873802192912384038; sid=7z8gpa7i; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDI1NTUwMTksImlhdCI6MTcwMjI5NTc1OSwicGx0IjotMX0.Q_xIreWF-iuJGTJKe4nYiu3PTHBvKsvkUkjX-j-4WvU; bili_ticket_expires=1702554959; PVID=1; home_feed_column=4; browser_resolution=718-777; b_lsid=93D31016D_18C5D23B1A4"
    }

def read_data(response):
    html_content = response.text
    # Create a Beautiful Soup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    view_count = soup.find('span', class_='view item').get_text(strip=True)
    dm_count   = soup.find("span", class_ ='dm item').get_text(strip=True)
    name       = soup.find("h1", class_ ='video-title').get_text(strip=True)
    like_count = soup.find("span", class_ ='video-like-info').get_text(strip=True)
    coin_count = soup.find("span", class_ ='video-coin-info').get_text(strip=True)
    video_fav  = soup.find("span",class_ = "video-fav-info").get_text(strip=True)

    print(f"播放量:{view_count}")
    print(f"弹幕量:{dm_count}")
    print(f"视频名称:{name}")
    print(f"点赞量:{like_count}")
    print(f"硬币:{coin_count}")
    print(f"收藏:{video_fav}")
    # f = open("./B_data.csv",mode = "a",encoding= 'utf-8',newline='')
    


def read_url(Url) :
    res = requests.get(url = Url,headers = headers,data= None)
    read_data(res)
    

if __name__ == "__main__":
    first_url = "https://www.bilibili.com/video/BV1EC4y157LL/"
    read_url(Url = first_url)
    # time.sleep(random.randint(0,3))


