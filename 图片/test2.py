import easyocr
reader = easyocr.Reader(['ch_sim', 'en'])
result = reader.readtext('./20220427115259.png', detail=0)
article = ''  # 定义一个空的字符串
for i in range(len(result)):
    article += result[i]  # 将列表中的字符串依次拼接在一起
print(article)

