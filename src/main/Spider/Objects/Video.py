import random
from ..Spiders.spider_video import SpiderVideo
from ..Configs.VideoConfig import VideoConfig
from ..Configs.CommentConfig import CommentConfig
from ..Spiders.SpiderComment import SpiderComment
from ..DataBase.DataCreate import dataBase
import time
class video:
    def __init__(self,video_oid,BV,uper_id,db = None):
        self.oid = video_oid
        self.BV = BV
        self.uper_id = uper_id
        self.video_name = ""
        self.thumb = ""
        self.coin = ""
        self.share = "" 
        self.bullets   = "" #弹幕数量
        self.views = "" 
        self.fav  = "" 
        self.comments = []
        self.db = db
        # 爬虫及初始化
        self.spider_config = VideoConfig(BV)
        self.spider_video  = SpiderVideo(videoConfig = self.spider_config)
        self.init_by_spider()

    def init_by_spider(self):
        # 爬取视频信息需要BV号
        try:
            time.sleep(random.randint(0,2))
            data = self.spider_video.spider_data()
            self.video_name = data ["视频名称"]
            self.thumb      = data ["点赞量"]
            self.coin       = data ["硬币"]
            self.share      = data ["转发"]
            self.bullets    = data ["弹幕量"]
            self.views      = data ["播放量"]
            self.fav        = data ["收藏"]
            self.writeDataBase(self.db)
            # 爬取评论需要oid
            self.__init_comments()
        except:
            print(f"爬取视频信息失败:{self.oid}")
        pass

    def __init_comments(self):
        comment_cfg = CommentConfig(oid = self.oid)
        spider_comment = SpiderComment(db = self.db)
        spider_comment.set_config(comment_cfg)
        self.comments = spider_comment.spider_data()
        print(f"爬取评论:{len(self.comments)}条")
        ...
    def writeDataBase(self,db):
        # 保存视频数据
        db.insert_or_update_video_data(self.getData())
        # 保存评论数据
        # for comment in self.comments:
        #     comment.writeDataBase(db)

    def getData(self):
        # video
        video_data = {
            'video_id': f'{self.oid}',
            'uper_id': f'{self.uper_id}',
            'video_name': f'{self.video_name}',
            'thumbs': f'{self.thumb}',
            'coin': f'{self.coin}',
            'share': f'{self.share}',
            'bullet_num': f'{self.bullets}',
            'view_count': f'{self.views}',
            'fav_count': f'{self.fav}',
            'content': f'{""}'
        }
        return video_data