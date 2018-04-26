# -*- coding: utf-8 -*-
import xlrd,xlwt,os,sys

# ##读取
# #打开xls文件
# book = xlrd.open_workbook("2007.xlsx")
# print ("表单数量：",book.nsheets)
# print ("表单名称：",book.sheet_names())
# #获取第1个表单
# sh = book.sheet_by_index(0)
# print ("表单%s共%d行%d列"%(sh.name,sh.nrows,sh.ncols))
# print ("第二行第三列：",sh.cell_value(1,2))
# #遍历所有表单
# for s in book.sheets():
#     for r in range(s.nrows):
#         #输出指定行
#         print (s.row(r))
#
# ##写入
# wb = xlwt.Workbook()
# sh = wb.add_sheet('test')
# sh.write(0,0,1234.56)
# sh.write(2,0,5665)
# sh.write(1,2,'gfgr')
# sh.write(2,1,'dfww')
#
# wb.save('2008.xlsx')
#
#
# ##修改
# from xlrd import open_workbook
# from xlutils.copy import copy
#
# rb=open_workbook('2008.xlsx')
# wb=copy(rb)
#
# s=wb.get_sheet(0)
#
# s.write(0,1,'new data')
#
# wb.save('2008.xlsx')






# #2007以后的xlsx
# import openpyxl
#
# def write_Excel(path):
#        wb = openpyxl.Workbook()
#        sheet = wb.active
#        sheet.title = '2007测试表'
#        value = [["名称", "价格", "出版社", "语言"],
#                 ["如何高效读懂一本书", "22.3", "机械工业出版社", "中文"],
#                 ["暗时间", "32.4", "人民邮电出版社", "中文"],
#                 ["拆掉思维里的墙", "26.7", "机械工业出版社", "中文"]]
#        for i in range(0,4):
#            for j in range(0,len(value[i])):
#                sheet.cell(row=i+1,column=j+1,value=str(value[i][j]))
#
#            wb.save(path)
#            print("写入数据成功！")
#
# def read_Excel(path):
#     wb = openpyxl.load_workbook( path )
#     sheet = wb.get_sheet_by_name( '2007测试表' )
#
#     for row in sheet.rows:
#         for cell in row:
#             print(cell.value,"\t",end="")
#         print()
# file_2007 = '2007.xlsx'
# write_Excel(file_2007)
# read_Excel(file_2007)


#比较异同
l_p = [] #定义两个全局list，分别存储原始和目的需要对比的数据
l_t = []
def read_excel():
    wb_pri = xlrd.open_workbook('baidu.xlsx') # 打开原始文件
    wb_tar = xlrd.open_workbook('baidu.xlsx') # 打开目标文件
    wb_result = xlwt.Workbook() # 新建一个文件，用来保存结果
    sheet_result = wb_result.add_sheet('result', cell_overwrite_ok=True)
    result_i = 0
    result_j = 0
    for sheet_i in range(2, 6):
        sheet_pri = wb_pri.sheet_by_index(sheet_i)
        sheet_tar = wb_tar.sheet_by_index(sheet_i)
        sheet_backup = wb_backup.get_sheet(sheet_i)
        print(sheet_pri.name, sheet_tar.name)
# 为什么是取这一列，因为这就是需要对比的数据阿
        l_p = sheet_pri.col_values(2)
        l_t = sheet_tar.col_values(2)
# tmp =[var for val in a if val in b] #这个是求交集,老大没要求是用不上的
# 求参数在pri（原始数据）中存在，而在tar（目标）中不存在的
        tmp_pd = list(set(l_p).difference(set(l_t)))
# 求参数在tar中存在，而在pri中不存在的
        tmp_td = list(set(l_t).difference(set(l_p)))
        if result_i < result_j:
            result_i = result_j
        else:
            result_j = result_i
        for pd_i in tmp_pd:
            result_i = result_i + 1
            sheet_result.write(result_i, 0, sheet_pri.name)
            sheet_result.write(result_i, 2, pd_i)
        for td_i in tmp_td:
            result_j = result_j + 1
            sheet_result.write(result_j, 1, sheet_tar.name)
            sheet_result.write(result_j, 3, td_i)
# 好了，可以去名为result的excel中查看结果了
    wb_result.save('result.xls')

if __name__ == '__main__':
    read_excel()
