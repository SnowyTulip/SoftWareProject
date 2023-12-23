from ..Spiders.spider_video import SpiderVideo
from ..Configs.VideoConfig import VideoConfig
from ..Configs.CommentConfig import CommentConfig
from ..Spiders.SpiderComment import SpiderComment
class video:
    def __init__(self,video_oid,BV,uper_id):
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
        # 爬虫及初始化
        self.spider_config = VideoConfig(BV)
        self.spider_video  = SpiderVideo(videoConfig = self.spider_config)
        self.init_by_spider()

    def init_by_spider(self):
        # 爬取视频信息需要BV号
        data = self.spider_video.spider_data()
        self.video_name = data ["视频名称"]
        self.thumb      = data ["点赞量"]
        self.coin       = data ["硬币"]
        self.share      = data ["转发"]
        self.bullets    = data ["弹幕量"]
        self.views      = data ["播放量"]
        self.fav        = data ["收藏"]
        # 爬取评论需要oid
        self.__init_comments()
        pass

    def __init_comments(self):
        comment_cfg = CommentConfig(oid = self.oid)
        spider_comment = SpiderComment()
        spider_comment.set_config(comment_cfg)
        self.comments = spider_comment.spider_data()
        ...