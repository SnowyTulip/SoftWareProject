import requests
from bs4 import BeautifulSoup

# 定义要爬取的微博用户的ID
user_id = '5710804425'

# 构造微博用户的主页URL
headers = {
    #不加cookie只能爬一页
    'cookie':'__bid_n=1883c7fc76e10d57174207; FPTOKEN=IBsER/uKazbtpMIEgvaOTfAuHsmYQM5g0VL9U1G3ybs72PsWHEBbiKv0w+R59BrOvSwxDKJevIDwL0SSwPV5yWd3lIFsx6KXQ/qYPpPTjTRW5kFr+j74rsScC6MKc1G9142e5tEEf7atvY/zTxl9B6jy/y7MEo0ETLT0VjL6nbpzkWe/SnIw97Tjb+9lqYoGHS6lPqZ5yAhDPKn0KK4htwxqr0qMglAG6ZcT7mn+BUZAygRSrqWZwZ6KSE0r27qsR0bDTAI8dsQFq1gPfYONp5UHfw9FFsBiscLULixqm31wTHYziK8gxi0/R6yIQ8Tq3OQkNmx+Kw7E/8YknGOiVmpjfRn5FNShZs3/t8SNBJEcZ9qaQnw/iF/jwPoFkMXz87Tp22aQUmFgeQu/u0wAYQ==|wC9ITrusKUtoBk6wTqvs+jaY6iwSJyX4pD0y+hSvnOA=|10|acf98643db3def55913fefef5034d5ee; WEIBOCN_FROM=1110106030; loginScene=102003; SUB=_2A25JbkPWDeRhGeNH7FIV-SjKzjyIHXVqkW2erDV6PUJbkdAGLRbkkW1NSoXhCHcUhbni8gGXfjdc5HNqec9qABj_; MLOGIN=1; _T_WM=98495433469; XSRF-TOKEN=a62fb7; mweibo_short_token=9f0e28d6c9; M_WEIBOCN_PARAMS=oid%3D4903111417922777%26luicode%3D20000061%26lfid%3D4903111417922777%26uicode%3D20000061%26fid%3D4903111417922777',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    'X-Xsrf-Token':'a62fb7'
}
url = 'https://weibo.cn/u/' + user_id

# 发起请求，获取页面内容
response = requests.get(url,headers = headers)

# 使用BeautifulSoup解析页面内容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到微博用户的微博列表
weibo_list = soup.find_all('div', class_='c')

# 遍历微博列表，找到每条微博的评论链接
for weibo in weibo_list:
    weibo_id = weibo.get('id')
    comment_url = 'https://weibo.cn/comment/' + weibo_id
    # 发起请求，获取评论页面内容
    comment_response = requests.get(comment_url)
    comment_soup = BeautifulSoup(comment_response.text, 'html.parser')
    # 找到评论内容
    comments = comment_soup.find_all('div', class_='c')
    for comment in comments:
        print(comment.text)
