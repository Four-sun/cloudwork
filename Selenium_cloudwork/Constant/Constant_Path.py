# -*- coding: utf-8 -*-
"""
@Time    : 2018-03-22
constant/Constant_Path.py
常量部分（固定不变使用频繁的参数维护在此处）
"""


class Constant_path(object):
    u'''url地址'''
    def __init__(self):
        self.LOGIN_URL = "http://etbc-qa.eslink.net.cn/"


class Error_Picture_path(object):
    u'''错误截图地址'''
    def __init__(self):
        self.Picture_path = "D:\\pycharm-5.0.4\\Selenium_unittest\\Error_picture\\"


class Push_Template_path(object):
    u'''推送模版地址'''
    def __init__(self):
        self.push_template = "D:\\pycharm-5.0.4\\Selenium_unittest\\Data\\push_template.csv"

