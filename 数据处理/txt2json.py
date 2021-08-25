#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:54:21 2021

@author: chris
"""

import re
import json

file = "20192020"
path = "20192020_100高频词_带数值.txt"
output = file+"_高频词.json"


def txtToJson():
    # 读取文件
    with open(path, 'r', encoding="utf-8") as file:
        # 定义一个用于切割字符串的正则
        seq = re.compile(":")
        result = []
        # 逐行读取
        for line in file:
            lst = seq.split(line.strip())
            item = {
                "name": lst[0]
            }
            result.append(item)
        print(type(result))
    # 关闭文件
    with open(output, 'w') as dump_f:
        json.dump(result, dump_f)


txtToJson()
