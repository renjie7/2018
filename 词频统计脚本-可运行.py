import xlrd
import xlwt
from datetime import date,datetime
import jieba.analyse
from collections import Counter
#Excelname = input("输入文件名 例如C://Users/Administrator/Desktop/波音.xlsx：“xxx.xlsx”")
Excelname = 'C://Users/Administrator/Desktop/波音.xlsx'
ExcelFile=xlrd.open_workbook(Excelname)
#获取目标EXCEL文件sheet名
print (ExcelFile.sheet_names())
#若有多个sheet，则需要指定读取目标sheet例如读取sheet2
#sheet2_name=ExcelFile.sheet_names()[1]
#获取sheet内容【1.根据sheet索引2.根据sheet名称】
sheet=ExcelFile.sheet_by_index(0)
#sheet=ExcelFile.sheet_by_name('')
#打印sheet的名称，行数，列数
print ('表名称',sheet.name,'\n','行数',sheet.nrows,'列数',sheet.ncols)
#获取单元格内容
#获取单元格数据类型
print ('单元格数据类型',sheet.cell(1,1).ctype)
#三种写法print (sheet.cell_value(1,0).encode('utf-8')
#print (sheet.row(1)[0].encode('utf-8')
#print ('列:',sheet.cell(2,1).value)
print ('行:',sheet.cell(0,3).value)
print (sheet.cell(0,4).value)
print (sheet.cell(0,5).value)
print (sheet.cell(0,6).value)
print (sheet.cell(0,7).value)
print (sheet.cell(0,8).value)
#写入新表格
#创建新表格
new_f = xlwt.Workbook(encoding='utf-8')
#创建第一个sheet:
sheet1 = new_f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
row0 = [u'行数',
        sheet.cell(0,3).value,
        sheet.cell(0,4).value,
        sheet.cell(0,5).value,
        sheet.cell(0,6).value,
        sheet.cell(0,7).value,
        sheet.cell(0,8).value,]
column0 = [sheet.cell(1,1).value]

f = open("输出.txt", "w")
print("分析结果",row0,file=f)

#sheet1.write(0,0,"字体颜色代号{}".format(fsize),style_1)
for i in range(1,sheet.nrows):
    out_keyword = jieba.lcut(sheet.cell(i,1).value)
        #print(out_keyword)
        #遍历分词进行与关键词统计
    c = Counter()
    for x in out_keyword:
        if x in out_keyword:
            if len(x)>0 and x != '\r\n':
                c[x] +=1
        #print('统计分析结果***')#print ("Value : %s" %  c.get(sheet.cell(0,3).value))#print ("Value : %s" %  c.get(sheet.cell(0,4).value))#print ("Value : %s" %  c.get(sheet.cell(0,5).value))
    row1 = [c.get(sheet.cell(0,3).value),
            c.get(sheet.cell(0,4).value),
            c.get(sheet.cell(0,5).value),
            c.get(sheet.cell(0,6).value),
            c.get(sheet.cell(0,7).value),
            c.get(sheet.cell(0,8).value)]
    print("分析结果",row1)
    #write的第一个,第二个参数时坐标, 第三个是要写入的数据

    print ("分析结果",row1,file=f)
f.close()
