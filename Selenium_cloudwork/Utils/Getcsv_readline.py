# -*- coding: utf-8 -*-
"""
Created on 2018-03-07
@author: sun
Project:csv文件读取
"""
import csv


class csv_search():

    def csv_test(filename,indexs):
        u'''csv文件查询'''
         #获取某一行的某一列数据
        with open(filename, 'r') as FileName:
            #返回一个生成器对象，reader是可迭代的
            reader = csv.reader(FileName)
            for index, rows in enumerate(reader):
                index1 = indexs
                if index == index1:
                    row = rows
                    return row