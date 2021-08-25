#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 09:58:46 2021

@author: chris
"""

# -*- coding: utf-8 -*-
import jieba

# file = "2021"
# filename = file+"_清洗结果.txt"
# outfilename = file+"_50高频词.txt"
# outfile_jsonname = file+"_50高频词_带数值.txt"

file = "class_"
filename = file+"7.txt"
outfilename = filename+"_50高频词.txt"
outfile_jsonname = filename+"_50高频词_带数值.txt"

txt = open(filename, "r", encoding='utf-8', errors='ignore').read()
outputs = open(outfilename, "w", encoding='utf-8')

outputs_json = open(outfile_jsonname, "w", encoding='utf-8')

words = jieba.lcut(txt)     # 使用精确模式对文本进行分词
counts = {}     # 通过键值对的形式存储词语及其出现的次数

for word in words:
    if len(word) == 1:    # 单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序

# for i in range(50):
#     word, count = items[i]
#     print("{0:<10}{1:>10}".format(word, count))
#     outputs.write("'"+word+" "+str(count)+"'"+',')
#     outputs_json.write(word+' ')
#     outputs_json.write(str(count)+'\n')

for i in range(50):
    word, count = items[i]
    print("{0:<10}{1:>10}".format(word, count))
    outputs.write(word+" ")
    outputs_json.write(word+' ')
    outputs_json.write(str(count)+'\n')

outputs.close()
outputs_json.close()
