#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 09:58:46 2021

@author: chris
"""

# -*- coding: utf-8 -*-
import jieba

# 创建停用词列表


def stopwordslist():
    stopwords = [line.strip() for line in open(
        'stop_words.txt', encoding='UTF-8').readlines()]
    return stopwords

# 对句子进行中文分词


def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    # print("正在分词")
    sentence_depart = jieba.cut(sentence.strip())
    # 创建一个停用词列表
    stopwords = stopwordslist()
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        word = word.encode('utf-8').decode("utf-8", "ignore")
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


# 给出文档路径
file = "2021"
filename = file+".csv"
outfilename = file+"_清洗结果.txt"

inputs = open(filename, 'r', encoding='utf-8')
outputs = open(outfilename, 'w', encoding='utf-8')

# 将输出结果写入out.txt中
global i
i = 0

for line in inputs:
    line_seg = seg_depart(line)
    outputs.write(line_seg + '\n')

    i = i+1
    # print("-------------------正在分词和去停用词-----------")

outputs.close()
inputs.close()

print("删除停用词和分词成功！！！")
