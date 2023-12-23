import pymysql

# 插入数据接口
def insert_uper_data(conn:pymysql.Connection,user_data:dict):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Upers WHERE uper_id=%s", (user_data['uper_id'],))
        existing_user = cursor.fetchone()
        if existing_user:
            # 如果用户已经存在，执行更新操作
            sql = "UPDATE Upers SET mannager_id=%s, location=%s, sex=%s, age=%s, uper_name=%s WHERE uper_id=%s"
            cursor.execute(sql, (user_data['mannager_id'], user_data['location'], user_data['sex'], user_data['age'], user_data['uper_name'], user_data['uper_id']))
        else:
            # 如果用户不存在，执行插入操作
            sql = "INSERT INTO Upers (uper_id, mannager_id, location, sex, age, uper_name) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (user_data['uper_id'], user_data['mannager_id'], user_data['location'], user_data['sex'], user_data['age'], user_data['uper_name']))

    conn.commit()
    print("User Data Inserted Successfully")

# 查询接口
def query_uper_data(conn,uper_id):
    with conn.cursor() as cursor:
        # 根据uper_id查询数据
        sql = "SELECT * FROM Upers WHERE uper_id=%s"
        cursor.execute(sql, (uper_id,))
        result = cursor.fetchone()

    # 将查询结果转换为字典
    if result:
        user_data = {
            'uper_id': result[0],
            'mannager_id': result[1],
            'location': result[2],
            'sex': result[3],
            'age': result[4],
            'uper_name': result[5]
        }
    else:
        user_data = None

    return user_data

def insert_or_update_video_data(video_data):
    with conn.cursor() as cursor:
        # 检查是否已经存在该视频
        cursor.execute("SELECT * FROM videos WHERE video_id=%s", (video_data['video_id'],))
        existing_video = cursor.fetchone()

        if existing_video:
            # 如果视频已经存在，执行更新操作
            sql = "UPDATE videos SET uper_id=%s, video_name=%s, thumbs=%s, coin=%s, share=%s, bullet_num=%s, view_count=%s, fav_count=%s, content=%s WHERE video_id=%s"
            cursor.execute(sql, (video_data['uper_id'], video_data['video_name'], video_data['thumbs'], video_data['coin'], video_data['share'], video_data['bullet_num'], video_data['view_count'], video_data['fav_count'], video_data['content'], video_data['video_id']))
        else:
            # 如果视频不存在，执行插入操作
            sql = "INSERT INTO videos (video_id, uper_id, video_name, thumbs, coin, share, bullet_num, view_count, fav_count, content) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (video_data['video_id'], video_data['uper_id'], video_data['video_name'], video_data['thumbs'], video_data['coin'], video_data['share'], video_data['bullet_num'], video_data['view_count'], video_data['fav_count'], video_data['content']))
    conn.commit()

# 查询视频数据
def query_video_data(video_id):
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT * FROM videos WHERE video_id=%s", (video_id,))
        video_data = cursor.fetchone()
        return video_data
    
# 插入或更新评论数据
def insert_or_update_comment_data(conn, comment_data):
    with conn.cursor() as cursor:
        # 检查是否已经存在该评论
        cursor.execute("SELECT * FROM comments WHERE comment_id=%s", (comment_data['comment_id'],))
        existing_comment = cursor.fetchone()

        if existing_comment:
            # 如果评论已经存在，执行更新操作
            sql = "UPDATE comments SET video_id=%s, user_name=%s, thumbs=%s, location=%s,emotion=%s, content=%s WHERE comment_id=%s"
            cursor.execute(sql, (comment_data['video_id'], comment_data['user_name'], comment_data['thumbs'], comment_data['location'], comment_data['emotion'],comment_data['content'], comment_data['comment_id']))
        else:
            # 如果评论不存在，执行插入操作
            sql = "INSERT INTO comments (comment_id, video_id, user_name, thumbs, location,emotion,content) VALUES (%s, %s, %s, %s, %s,%s, %s)"
            cursor.execute(sql, (comment_data['comment_id'], comment_data['video_id'], comment_data['user_name'], comment_data['thumbs'], comment_data['location'],comment_data['emotion'], comment_data['content']))
    conn.commit()

# 查询评论数据
def query_comment_data(conn, comment_id):
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT * FROM comments WHERE comment_id=%s", (comment_id,))
        comment_data = cursor.fetchone()
        return comment_data
    
# 插入或更新uper_result数据
def insert_or_update_uper_result_data(conn, uper_data):
    with conn.cursor() as cursor:
        # 检查是否已经存在该uper_result
        cursor.execute("SELECT * FROM uper_result WHERE uper_id=%s", (uper_data['uper_id'],))
        existing_uper_result = cursor.fetchone()

        if existing_uper_result:
            # 如果uper_result已经存在，执行更新操作
            sql = "UPDATE uper_result SET emotion=%s, feature=%s, hobby=%s WHERE uper_id=%s"
            cursor.execute(sql, (uper_data['emotion'], uper_data['feature'], uper_data['hobby'], uper_data['uper_id']))
        else:
            # 如果uper_result不存在，执行插入操作
            sql = "INSERT INTO uper_result (uper_id, emotion, feature, hobby) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (uper_data['uper_id'], uper_data['emotion'], uper_data['feature'], uper_data['hobby']))
    conn.commit()

# 查询uper_result数据
def query_uper_result_data(conn, uper_id):
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT * FROM uper_result WHERE uper_id=%s", (uper_id,))
        uper_data = cursor.fetchone()
        return uper_data

# 插入或更新uper_annalysis数据
def insert_or_update_uper_annalysis_data(conn, uper_data):
    with conn.cursor() as cursor:
        # 检查是否已经存在该uper_annalysis
        cursor.execute("SELECT * FROM uper_annalysis WHERE uper_id=%s", (uper_data['uper_id'],))
        existing_uper_annalysis = cursor.fetchone()

        if existing_uper_annalysis:
            # 如果uper_annalysis已经存在，执行更新操作
            sql = "UPDATE uper_annalysis SET rank_value=%s, time_seq=%s, view_seq=%s, thumb_seq=%s WHERE uper_id=%s"
            cursor.execute(sql, (uper_data['rank_value'], uper_data['time_seq'], uper_data['view_seq'], uper_data['thumb_seq'], uper_data['uper_id']))
        else:
            # 如果uper_annalysis不存在，执行插入操作
            sql = "INSERT INTO uper_annalysis (uper_id, rank_value, time_seq, view_seq, thumb_seq) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (uper_data['uper_id'], uper_data['rank_value'], uper_data['time_seq'], uper_data['view_seq'], uper_data['thumb_seq']))
    conn.commit()

# 查询uper_annalysis数据
def query_uper_annalysis_data(conn, uper_id):
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT * FROM uper_annalysis WHERE uper_id=%s", (uper_id,))
        uper_data = cursor.fetchone()
        return uper_data

# 插入或更新video_analysis数据
def insert_or_update_video_analysis_data(conn, video_data):
    with conn.cursor() as cursor:
        # 检查是否已经存在该video_analysis
        cursor.execute("SELECT * FROM video_analysis WHERE video_id=%s", (video_data['video_id'],))
        existing_video_analysis = cursor.fetchone()

        if existing_video_analysis:
            # 如果video_analysis已经存在，执行更新操作
            sql = "UPDATE video_analysis SET title_str=%s, time_seq=%s, view_seq=%s, thumb_seq=%s WHERE video_id=%s"
            cursor.execute(sql, (video_data['title_str'], video_data['time_seq'], video_data['view_seq'], video_data['thumb_seq'], video_data['video_id']))
        else:
            # 如果video_analysis不存在，执行插入操作
            sql = "INSERT INTO video_analysis (video_id, title_str, time_seq, view_seq, thumb_seq) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (video_data['video_id'], video_data['title_str'], video_data['time_seq'], video_data['view_seq'], video_data['thumb_seq']))
    conn.commit()
# 查询video_analysis数据
def query_video_analysis_data(conn, video_id):
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT * FROM video_analysis WHERE video_id=%s", (video_id,))
        video_data = cursor.fetchone()
        return video_data
    
if __name__ == "__main__":
    conn = pymysql.connect(host='localhost', user='pi', password='admin')
    conn.select_db('BLDataBase')
    user_data = {
    'uper_id': '001',
    'mannager_id': '002',
    'location': 'Beijing',
    'sex': 'Male',
    'age': '30',
    'uper_name': '张三'
    }
    insert_uper_data(conn,user_data)
    print(query_uper_data(conn,"001"))
    # video
    video_data = {
        'video_id': '001',
        'uper_id': '001',
        'video_name': 'test',
        'thumbs': 'test',
        'coin': 'test',
        'share': 'test',
        'bullet_num': 'test',
        'view_count': 'test',
        'fav_count': 'test',
        'content': 'test'
    }
    insert_or_update_video_data(video_data)
    print(query_video_data(video_data['video_id']))
    # comment
    comment_data = {
        'comment_id': '12312',
        'video_id': '12312312',
        'user_name': 'gaobopi',
        'thumbs': '10',
        'location': '123123',
        'emotion' : 'test',
        'content': '123899999'
    }
    insert_or_update_comment_data(conn,comment_data)
    print(query_comment_data(conn,comment_data['comment_id']))

    # 插入或更新数据
    uper_data = {'uper_id': '1', 'emotion': 'happy', 'feature': 'creative', 'hobby': 'painting'}
    insert_or_update_uper_result_data(conn, uper_data)
    # 查询数据
    print(query_uper_result_data(conn, '1'))

    # 插入或更新数据
    uper_data = {
        'uper_id': '1',
        'rank_value': 'A',
        'time_seq': '["2023-12-20", "2023-12-21", "2023-12-22"]',
        'view_seq': '["100", "150", "200"]',
        'thumb_seq': '["50", "75", "100"]'
    }
    insert_or_update_uper_annalysis_data(conn, uper_data)
    # 查询数据
    result = query_uper_annalysis_data(conn, '1')
    print(result)

    # 插入或更新数据
    video_data = {
        'video_id': '001',
        'title_str': 'Video Title',
        'time_seq': '["2023-12-20", "2023-12-21", "2023-12-22"]',
        'view_seq': '["100", "150", "200"]',
        'thumb_seq': '["50", "75", "100"]'
    }
    insert_or_update_video_analysis_data(conn, video_data)
    # 查询数据
    result = query_video_analysis_data(conn, '001')
    print(result)

    conn.close()