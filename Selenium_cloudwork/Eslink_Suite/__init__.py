# import csv
#
# #获取某一行的某一列数据
# with open('D:\\pycharm-5.0.4\\Selenium_unittest\\Data\\push_template.csv', 'r') as FileName:
#     #返回一个生成器对象，reader是可迭代的
#     reader = csv.reader(FileName)
#     for index, rows in enumerate(reader):
#         if index == 0:
#             row = rows
#             indexs= index
#             print(row[1])


from Utils.Excel_readline import  ExcelUtil

try:
    filepath = "D:\\pycharm-5.0.4\\Selenium_unittest\\Data\\mobiles.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filepath, sheetName)
    print (int(data.dict_data()[0]))

except Exception as Error:

    print(Error)