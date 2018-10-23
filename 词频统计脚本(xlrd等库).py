import xlrd
import xlwt
import jieba.analyse
from collections import Counter
Excelname = input("输入文件名 例如C://Users/Administrator/Desktop/波音.xlsx：“xxx.xlsx”")
#Excelname = 'C://Users/Administrator/Desktop/波音.xlsx'
ExcelFile=xlrd.open_workbook(Excelname)
sheet=ExcelFile.sheet_by_index(0)
print ('表名称',sheet.name,'\n','行数',sheet.nrows,'列数',sheet.ncols)
row2 = []
row1 = []
j = 3
for j in range(3,sheet.ncols):
    row0 = sheet.cell(0,j).value
    row2.append(row0)
f = open("词频统计输出.txt", "w")
print("关键词",row2,file = f)
#词频输出
for i in range(1,sheet.nrows):
    out_keyword = jieba.lcut(sheet.cell(i,1).value)
    #print(out_keyword)
    c = Counter()
    for x in out_keyword:
        if x in out_keyword:
            if len(x)>0 and x != '\r\n':
                c[x] +=1
    row1 = [c.get(row2[0]),
            c.get(row2[1]),
            c.get(row2[2]),
            c.get(row2[3]),
            c.get(row2[4]),
            c.get(row2[5])]

    #write的第一个,第二个参数时坐标, 第三个是要写入的数据
    print ("分析结果",row1)
    print ("分析结果",i,row1,file=f)
f.close()
