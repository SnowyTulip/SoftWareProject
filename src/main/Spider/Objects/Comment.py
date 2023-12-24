
from ..DataBase.DataCreate import dataBase
class comment:
    def __init__(self,oid,comment_index,thumbs,content,commenter_name,commenter_location,sex,db = None):
        self.video_id = oid
        self.comment_id = f"{int(oid) + int(comment_index)}" #这个是使用两个字段确定 oid(视频) + comment_index
        self.thumbs = thumbs
        self.content = content
        #没有存储评论者的信息,这里对评论者的信息进行一个存储
        self.commenter_name = commenter_name
        self.commenter_location = commenter_location
        self.sex = sex
        self.db = db

    def writeDataBase(self):
        # 保存评论
        self.db.insert_or_update_comment_data(self.getData())
        

    def getData(self):
        # comment
        comment_data = {
        'comment_id': f'{self.comment_id}',
        'video_id': f'{self.video_id}',
        'user_name': f'{self.commenter_name}',
        'thumbs': f'{self.thumbs}',
        'location': f'{self.commenter_location}',
        'emotion' : f'{"好"}',
        'content': f'{self.content}'
        }
        return comment_data

