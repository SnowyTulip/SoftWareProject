from flask import Flask, jsonify
from flask_cors import CORS
from Spider.DataBase.DataCreate import dataBase
import jieba
from nltk.corpus import stopwords
from collections import Counter
import string
app = Flask(__name__)
CORS(app)
@app.route('/data')
def return_data():
    db = dataBase()
    data = db.query_video_data_()
    db.close()
    return jsonify(data)
def data_clean(dict_data):
    return {key: value for key, value in dict_data.items() if not key.isspace() and key not in string.punctuation and dict_data[key] > 5}
stop_words = set(stopwords.words('chinese'))
def data_clean2(dict_data, stop_words):
    return {key: value for key, value in dict_data.items() if key not in stop_words and len(key) > 2}
@app.route('/commentData')
def return_comment_data():
    db = dataBase()
    data = db.get_all_comments()
    db.close()
    text = ''.join([item['content'] for item in data])
    words = list(jieba.cut(text))
    word_counts = Counter(words)
    word_counts = data_clean(word_counts)
    word_counts = data_clean2(word_counts,stop_words)
    print(word_counts)
    return jsonify(word_counts)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
