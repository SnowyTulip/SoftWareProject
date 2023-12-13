from Spider.Configs.CommentConfig import CommentConfig
from Spider.Spiders.SpiderComment import SpiderComment

if __name__ == "__main__":
    comment_config = CommentConfig(oid = "451979316")
    spider_comment = SpiderComment()
    spider_comment.add_config(comment_config)
    spider_comment.spider_data_all()
