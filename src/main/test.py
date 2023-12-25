from snownlp import SnowNLP

def get_sentiment_description(text):
    s = SnowNLP(text)
    sentiment = s.sentiments

    if sentiment > 0.6:
        return "正向、积极"
    elif sentiment < 0.4:
        return "语言攻击、消极"
    else:
        return "中性"

# 测试
text1 = "你今天很好看!!!!!!!!!!!!"
text2 = "真垃圾，你什么都做不好"
text3 = "滚回家算了!"
text4 = "垃圾玩意"
text5 = "这是一句话"

print(get_sentiment_description(text1))  # 输出：正向、积极
print(get_sentiment_description(text2))  # 输出：语言攻击、消极
print(get_sentiment_description(text3))  # 输出：语言攻击、消极
print(get_sentiment_description(text4))  # 输出：语言攻击、消极
print(get_sentiment_description(text5))  # 输出：语言攻击、消极