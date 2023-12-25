# 将数据库中的所有评论数据进行情感分析
from snownlp import SnowNLP

def get_sentiment_description(text):
    s = SnowNLP(text)
    sentiment = s.sentiments
    return sentiment
    