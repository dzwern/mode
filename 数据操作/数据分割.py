
import pandas as pd


list1=[
'华味亨开心果180g*2袋',
'德怡卡原味谷物圈200g*1盒',
'健达奇趣蛋女孩版20g*3*2盒',
'华味亨麻辣牛肉88g*2袋',
'青可儿纯净水500ml*15瓶（整箱）',
'一搏豆府醇厚抹茶30g*3盒',
'寻然集怡气合花养生茶11g*4盒',
'德怡卡蔓越莓星星谷物200g*1盒',
'饮光你燕麦奶250ml*12瓶',
'德怡卡原味谷物圈200g*1盒'
]

# 将列表转换为数据框

c={"商品名称" : list1}
data=pd.DataFrame(c)

# print(data)

# 对数据框中的字段进行分割

data['更改后的商品名称']=data['商品名称'].str.split('*')
data['商品名称2']=data['更改后的商品名称'].apply(lambda x:x[0])
data['规格']=data['更改后的商品名称'].apply(lambda x:x[-1].replace('（整箱）','').replace('整箱/',''))

data['数量']=data['规格'].apply(lambda x:x[0:len(x.encode('gbk'))-2])
data['规格2']=data['规格'].apply(lambda x:x[-1])
print(data[['商品名称','商品名称2','数量','规格2']])

