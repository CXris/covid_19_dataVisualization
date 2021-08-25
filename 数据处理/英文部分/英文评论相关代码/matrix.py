# -*- coding: UTF-8 -*-

import xlrd
import xlwt

workbook = xlrd.open_workbook(r'Coursera_translate.xlsx')

print(workbook.sheet_names())
sheet2 = workbook.sheet_by_name('Sheet1')
nrows = sheet2.nrows
ncols = sheet2.ncols
print(nrows, ncols)

list = []
cell_A = sheet2.cell(0, 0).value

for i in range(nrows):
    cell_A = sheet2.cell(i, 0).value
    split = cell_A.split()

    #使用空格替换标点符号
    article = cell_A.replace(",","").replace(".","").replace(":","").replace(";","").replace("?","").replace("!","").replace("-","")

    #大写字母转换成小写字母
    exchange = article.lower();

    #生成单词列表
    list.append(exchange.split())

print('step1')

keywords2 = ("learning", "korean", "learn", "great", "language", "food", "good", "lot", "jira", "understand", "fashion",
             "easy", "brand", "learned", "life", "recommend", "professor", "information", "techniques", "interesting",
             "time", "excellent", "healthy", "knowledge", "dr", "health", "luxury", "things", "brain", "helpful",
             "nutrition", "concepts", "mason", "oakley", "theory", "negotiation", "agile", "barbara", "enjoyed",
             "basic", "videos", "examples", "amazing", "material", "business", "teacher", "nader", "people", "work",
             "game", "highly", "study", "informative", "eating", "private", "practice", "make", "equity", "management",
             "pe", "helped", "clear", "loved", "coursera", "content", "tavassoli", "peggy", "understanding", "eat",
             "experience", "simple", "courses", "industry", "interviews", "medical", "university", "love", "class",
             "students", "explained", "world", "improve", "made", "kang", "practical", "sejnowski", "taught", "start",
             "teaching", "tools", "wonderful", "maya", "school", "neurobiology", "tips", "yonsei", "studying",
             "branding", "found", "procrastination")

m = [[0] * 50 for i in range(nrows)]
for i in range(nrows):
    k = 0
    for j in range(50):
        temp = list[i].count(keywords2[j])
        m[i][k] = temp
        # if temp > 0:
        #     m[i][k] = 1
        k += 1

# 打开一个文件
#f = open("Matrix_Coursera_50.txt", "w", encoding='utf-8', errors='ignore')
#s = str(m)
#f.write(s)

# 关闭打开的文件，必须关闭不然电脑能炸裂
#f.close()

count = 0
workbook2 = xlwt.Workbook()
sheet3 = workbook2.add_sheet("Coursera_50_2")
for j in range(50):
    sheet3.write(0, j, keywords2[j])
for i in range(nrows):
    for j in range(50):
        sheet3.write(i + 1, j, m[i][j])
workbook2.save('Coursera_50_2.xls')