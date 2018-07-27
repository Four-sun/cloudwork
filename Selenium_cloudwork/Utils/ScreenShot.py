# -*- coding: utf-8 -*-
"""
Created on 2018-03-22
@author: sun
Project:截图
"""
from Utils.log import Logger
from Constant.Constant_Path import *
import time,sys
send_time=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))  #获取当前时间
logger_message=Logger()
Picture_path=Error_Picture_path().Picture_path


def Screenshot(self,title):
    u'''截图'''
    try:
        filename= Picture_path + send_time + title +".png"
        self.browser.get_screenshot_as_file(filename)
        logger_message.logwarning(u"%s\t方法名：%s\t截图" % (send_time,sys._getframe().f_code.co_name))

    except Exception as Screenshot_Error:

        print(u"%s\t方法名：%s\t截图-异常:%s" % (send_time,sys._getframe().f_code.co_name,Screenshot_Error))
        logger_message.logwarning(u"%s\t方法名：%s\t截图-异常:%s" % (send_time,sys._getframe().f_code.co_name,Screenshot_Error))
