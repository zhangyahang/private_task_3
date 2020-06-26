import pandas as pd
import numpy as np
import operator
from efficient_apriori import apriori
# Simple Progress Bar:
import sys  # for progress bar (sys.stdout)
#读取数据
data = pd.read_csv("apriori.csv",header=None, sep=',')
data=data[1:]
#得到频繁项集及关联规则

# itemsets, rules = apriori(data.values,min_support=0.5,  min_confidence=1)
# print(itemsets)
# print(rules)

# print(data.values)

a=data.values

count=0

for i in range(202099):
    count+=1
    # print(count)
    for j in range(38):
        if type(a[i][j]) is int or float:
            a[i][j]=str(a[i][j])
b=a.tolist()
print(type(b))
itemsets, rules = apriori(b,min_support=0.5,  min_confidence=1)
print(itemsets)
print(rules)
