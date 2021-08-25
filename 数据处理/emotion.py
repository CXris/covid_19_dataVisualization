#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 10:38:22 2021

@author: chris
"""

from snownlp import SnowNLP

file = "2019"
filepath = file+".csv"

inputs = open(filepath, 'r', encoding='utf-8')

sentenceList = []
with open(filepath, "r", encoding="utf-8") as f:
    for line in f:
        # 去掉空格
        sentenceList.append(line.strip())

# print(sentenceList)

# s1 = sentenceList[2]
# print(s1)

# ss = SnowNLP(s1)
# print(ss.sentiments)

global score
score = 0

for sentence in sentenceList:
    text = sentence
    try:
        textScore = SnowNLP(text)
        tempScore = textScore.sentiments
    except:
        tempScore = 0

    if tempScore > 0.8:
        temp = 1
    else:
        temp = 0
    score = score + temp

score = score/len(sentenceList)

print(score)
