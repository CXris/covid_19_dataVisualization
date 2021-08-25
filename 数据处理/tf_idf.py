#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:54:21 2021

@author: chris
"""

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import jieba
import matplotlib.pyplot as plt


def segment_jieba(text): return " ".join(jieba.cut(text))


# 加载语料
file = "2021"
filename = file+"_清洗结果.txt"

corpus = []

with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        # 去掉标点符号
        corpus.append(segment_jieba(line.strip()))
# print(corpus)

# 2、计算tf-idf设为权重

vectorizer = CountVectorizer(
    max_df=0.8, min_df=2, token_pattern=u'(?u)\\b[^\\d\\W]\\w+\\b')
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

# 3、获取词袋模型中的所有词语特征 如果特征数量非常多的情况下可以按照权重降维

word = vectorizer.get_feature_names()
# print(word)
print("word feature length: {}".format(len(word)))
# 4、导出权重，到这边就实现了将文字向量化的过程，矩阵中的每一行就是一个文档的向量表示

tfidf_weight = tfidf.toarray()

# 5、对向量进行聚类

# 指定分成7个类
kmeans = KMeans(n_clusters=7)
kmeans.fit(tfidf_weight)

class_1 = open("class_1.txt", "w", encoding="utf-8")
class_2 = open("class_2.txt", "w", encoding="utf-8")
class_3 = open("class_3.txt", "w", encoding="utf-8")
class_4 = open("class_4.txt", "w", encoding="utf-8")
class_5 = open("class_5.txt", "w", encoding="utf-8")
class_6 = open("class_6.txt", "w", encoding="utf-8")
class_7 = open("class_7.txt", "w", encoding="utf-8")

num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
num_6 = 0
num_7 = 0

classlist = [class_1, class_2, class_3, class_4, class_5, class_6, class_7]
sentencenum = [num_1, num_2, num_3, num_4, num_5, num_6, num_7]
# 打印出各个族的中心点
# print(kmeans.cluster_centers_)

for index, label in enumerate(kmeans.labels_, 1):
    # print("index: {}, label: {}".format(index, label))
    sentence = corpus[index-1]
    classlist[label].write(sentence+'\n')
    sentencenum[label] = sentencenum[label]+1

class_1.close()
class_2.close()
class_3.close()
class_4.close()
class_5.close()
class_6.close()
class_7.close()

# 样本距其最近的聚类中心的平方距离之和，用来评判分类的准确度，值越小越好
# k-means的超参数n_clusters可以通过该值来评估
print("inertia: {}".format(kmeans.inertia_))
# 6、可视化

# 使用T-SNE算法，对权重进行降维，准确度比PCA算法高，但是耗时长
tsne = TSNE(n_components=2)
decomposition_data = tsne.fit_transform(tfidf_weight)

x = []
y = []

coordinate = open(str(sentencenum)+".txt", "w", encoding="utf-8")

for i in decomposition_data:
    x.append(i[0])
    y.append(i[1])
    coordinate.write(str(i[0])+' '+str(i[1])+'\n')

coordinate.close()

fig = plt.figure(figsize=(10, 10))
ax = plt.axes()
plt.scatter(x, y, c=kmeans.labels_, marker="x")
plt.xticks(())
plt.yticks(())
# plt.show()
plt.savefig('./'+file+'聚类.png', aspect=1)
print(sentencenum)
