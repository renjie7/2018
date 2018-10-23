import jieba.analyse
word_lst = []
key_lst = []
#encoding='gbk',errors='ignore'
import jieba
for line in open('C://Users/Administrator/Desktop/test.txt',encoding='gbk',errors='ignore'):
    item = line.strip('\n\r').split('\t')
    tags = jieba.analyse.extract_tags(item[0])
    for t in tags:
        word_lst.append(t)
print(word_lst)
word_dict = {}
with open("C://Users/Administrator/Desktop/test1.txt",'w') as wf2:
    for item in word_lst:
        if item not in word_dict:
            word_dict[item] = 1
        else:
            word_dict[item] += 1
print(word_dict)
