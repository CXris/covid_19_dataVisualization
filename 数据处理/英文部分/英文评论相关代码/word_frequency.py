# -*- coding: UTF-8 -*-

import xlrd

workbook = xlrd.open_workbook(r'Coursera_translate.xlsx')

print(workbook.sheet_names())
sheet2 = workbook.sheet_by_name('Sheet1')
nrows = sheet2.nrows
ncols = sheet2.ncols
print(nrows, ncols)

list = []
cell_A = sheet2.cell(0, 0).value

for i in range(nrows):
    print(i)
    cell_A = sheet2.cell(i, 0).value
    split = cell_A.split()

    #使用空格替换标点符号
    article = cell_A.replace(",","").replace(".","").replace(":","").replace(";","").replace("?","").replace("!","").replace("-","")

    #大写字母转换成小写字母
    exchange = article.lower();

    #生成单词列表
    list.append(exchange.split())

print('step1')

dic = {}
m = len(list) // 100
for n in range(m):
    print(n, 'step2')
    for i in range(100):
        for j in range(len(list[100 * n + i])):
            word = list[100 * n + i][j]
            count = 0
            for k in range(100):
                count += list[100 * n + k].count(word)
            if dic.get(word, 0) == 0:
                dic[word] = count
            else:
                dic[word] = dic[word] + count

for i in range(len(list) - 100 * m):
    for j in range(len(list[100 * m + i])):
        word = list[100 * m + i][j]
        count = 0
        for k in range(len(list) - 100 * m):
            count += list[100 * m + k].count(word)
        if dic.get(word, 0) == 0:
            dic[word] = count
        else:
            dic[word] = dic[word] + count
print(dic)

#排除特定单词
stopwords = {"a","a's","able","about","above","according","accordingly","across","actually","after","afterwards","again",
        "against","ain't","all","allow","allows","almost","alone","along","already","also","although","always","am",
        "among","amongst","an","and","another","any","anybody","anyhow","anyone","anything","anyway","anyways",
        "anywhere","apart","appear","appreciate","appropriate","are","aren't","around","as","aside","ask","asking",
        "associated","at","available","away","awfully","b","be","became","because","become","becomes","becoming",
        "been","before","beforehand","behind","being","believe","below","beside","besides","best","better","between",
        "beyond","both","brief","but","by","c","c'mon","c's","came","can","can't","cannot","cant","cause","causes",
        "certain","certainly","changes","clearly","co","com","come","comes","concerning","consequently","consider",
        "considering","contain","containing","contains","corresponding","could","couldn't","course","currently","d",
        "definitely","described","despite","did","didn't","different","do","does","doesn't","doing","don't","done",
        "down","downwards","during","e","each","edu","eg","eight","either","else","elsewhere","enough","entirely",
        "especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","exactly",
        "example","except","f","far","few","fifth","first","five","followed","following","follows","for","former",
        "formerly","forth","four","from","further","furthermore","g","get","gets","getting","given","gives","go",
        "goes","going","gone","got","gotten","greetings","h","had","hadn't","happens","hardly","has","hasn't","have",
        "haven't","having","he","he's","hello","help","hence","her","here","here's","hereafter","hereby","herein",
        "hereupon","hers","herself","hi","him","himself","his","hither","hopefully","how","howbeit","however","i",
        "i'd","i'll","i'm","i've","ie","if","ignored","immediate","in","inasmuch","inc","indeed","indicate","indicated",
        "indicates","inner","insofar","instead","into","inward","is","isn't","it","it'd","it'll","it's","its","itself",
        "j","just","k","keep","keeps","kept","know","known","knows","l","last","lately","later","latter","latterly",
        "least","less","lest","let","let's","like","liked","likely","little","look","looking","looks","ltd","m",
        "mainly","many","may","maybe","me","mean","meanwhile","merely","might","more","moreover","most","mostly","much",
        "must","my","myself","n","name","namely","nd","near","nearly","necessary","need","needs","neither","never",
        "nevertheless","new","next","nine","no","nobody","non","none","noone","nor","normally","not","nothing","novel",
        "now","nowhere","o","obviously","of","off","often","oh","ok","okay","old","on","once","one","ones","only",
        "onto","or","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall",
        "own","p","particular","particularly","per","perhaps","placed","please","plus","possible","presumably",
        "probably","provides","q","que","quite","qv","r","rather","rd","re","really","reasonably","regarding",
        "regardless","regards","relatively","respectively","right","s","said","same","saw","say","saying","says",
        "second","secondly","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sensible","sent",
        "serious","seriously","seven","several","shall","she","should","shouldn't","since","six","so","some",
        "somebody","somehow","someone","something","sometime","sometimes","somewhat","somewhere","soon","sorry",
        "specified","specify","specifying","still","sub","such","sup","sure","t","t's","take","taken","tell","tends",
        "th","than","thank","thanks","thanx","that","that's","thats","the","their","theirs","them","themselves","then",
        "thence","there","there's","thereafter","thereby","therefore","therein","theres","thereupon","these","they",
        "they'd","they'll","they're","they've","think","third","this","thorough","thoroughly","those","though","three",
        "through","throughout","thru","thus","to","together","too","took","toward","towards","tried","tries","truly",
        "try","trying","twice","two","u","un","under","unfortunately","unless","unlikely","until","unto","up","upon",
        "us","use","used","useful","uses","using","usually","uucp","v","value","various","very","via","viz","vs","w",
        "want","wants","was","wasn't","way","we","we'd","we'll","we're","we've","welcome","well","went","were",
        "weren't","what","what's","whatever","when","whence","whenever","where","where's","whereafter","whereas",
        "whereby","wherein","whereupon","wherever","whether","which","while","whither","who","who's","whoever","whole",
        "whom","whose","why","will","willing","wish","with","within","without","won't","wonder","would","wouldn't","x",
        "y","yes","yet","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves","z","zero"}
for i in stopwords:
    if dic.get(i, 0) != 0:
        del (dic[i])
print(dic)

#排序
dic1= sorted(dic.items(),key=lambda d:d[1],reverse= True)
print(dic1)
print("-----------------------------------------------------------------------------------")

#输出词频最大的前十位单词
for i in range(100):
    print(dic1[i])
print("-----------------------------------------------------------------------------------")
for i in range(50):
    print(dic1[i])
# print("-----------------------------------------------------------------------------------")
# print(dic1)

# 打开一个文件
#f = open("Words_Coursera_100.txt", "w", encoding='utf-8', errors='ignore')
#s = str(dic1)
#f.write(s)

# 关闭打开的文件，必须关闭不然电脑能炸裂
#f.close()