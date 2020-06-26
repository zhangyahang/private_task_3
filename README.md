# private_task_3
1、在listings.csv中计算各行政区房屋均价，和各行政区roomtype房屋均价（如朝阳区-private room ,朝阳区-entirehome/apart)
2、将对应分类价格高于行政区房屋均价的id记为1，否则0，计入“是否一类溢价”属性，同理计入各（行政区roomtype）房屋均价为“是否二类溢价‘
3、对listing.csv中name进行分词，取高频有效10词作为房屋特征标签，将这10个词汇增添为属性“特征标签-XX’（01变量）中，并额外增加‘特征标签数量’属性，计算每个id的属性值。
4、对reviews-detail.csv中的comments使用python卷积神经网络进行正负情感分析，只分正负，正记为1，负记为0，计正评论数/评论总数为该id的“评论评分”属性中；
5、以id为key，取listings.csv中id、‘是否一类溢价’、‘是否二类溢价’、‘特征标签-XX’，‘特征标签数量’，和reviews_detail.csv中‘评论评分’，合并总表并输出结果。
6、计算‘评论评分’、‘属性数量’、各类特征标签、reviews_per_month\avaliability_365同一类溢价与二类溢价的相关系数，并输出结果。
7、使用apriori算法挖掘各类特征标签之间的关联规则，并输出结果。
