import snownlp
import time
import xlrd
from snownlp import SnowNLP
f_name = 'C://Users/Administrator/Desktop/波音.xlsx'
Excel_data = xlrd.open_workbook(f_name)
sheet = Excel_data.sheet_by_index(0)
print('表名称',sheet.name,'行数',sheet.nrows,'列数',sheet.ncols)
start = time.clock()
for i in range(1,sheet.nrows):
    s = SnowNLP(sheet.cell(i,1).value)
    print('情感态度',i,s.sentiments)
end = time.clock()
s.words # [u'这个', u'东西', u'真心',u'很', u'赞']
s.tags # [(u'这个', u'r'), (u'东西', u'n'), (u'真心', u'd'), (u'很', u'd'),(u'赞', u'Vg')]
s.sentiments # 0.9769663402895832 positive的概率
print(s.sentiments)
print('行，运行时间是 %s 秒'%(end-start))
s.pinyin # [u'zhe', u'ge', u'dong', u'xi',u'zhen', u'xin', u'hen', u'zan']
s = SnowNLP(u'「繁體字」「繁體中文」的叫法在臺灣亦很常見。')

