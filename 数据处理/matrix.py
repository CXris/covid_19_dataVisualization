#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:12:31 2021

@author: chris
"""
import xlwt

file = "2021"
filename = file + "_清洗结果.txt"
wordsfile = file + "_50高频词.txt"

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet(file)
wordslist = open(wordsfile, encoding='utf-8', errors='ignore').read()
wordslist = wordslist.strip().split(' ')
# print(wordslist)

f = open(filename, "r", encoding='utf-8', errors='ignore')
sentenceList = f.readlines()

# print(sentenceList)

num = len(sentenceList)

for p in range(len(wordslist)):
    worksheet.write(0, p, wordslist[p])
workbook.save(file+"_matrix.xls")

global k

for i in range(num):
    sentence = sentenceList[i]  # 返回单元格中的数据
    sentence = sentence.strip().split(' ')
    # print(sentence)

    k = 0

    for single_word in sentence:
        if k < 50:
            if single_word == wordslist[k]:
                worksheet.write(i+1, k, 1)
                k = k+1
            else:
                # worksheet.write(i+1,k,0)
                k = k+1
        else:
            break

workbook.save(file+"_matrix.xls")
