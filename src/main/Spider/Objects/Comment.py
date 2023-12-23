

class comment:
    def __init__(self,oid,comment_index,thumbs,content,commenter_name,commenter_location,sex):
        self.video_id = oid
        self.comment_id = f"{int(oid) + int(comment_index)}" #这个是使用两个字段确定 oid(视频) + comment_index
        self.thumbs = thumbs
        self.content = content
        #没有存储评论者的信息,这里对评论者的信息进行一个存储
        self.commenter_name = commenter_name
        self.commenter_location = commenter_location
        self.sex = sex

