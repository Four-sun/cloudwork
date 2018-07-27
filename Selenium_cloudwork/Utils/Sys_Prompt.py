# -*- coding: utf-8 -*-
"""
Created on 2018-03-29
@author: sun
Project:系统提示
"""
from Utils.log import Logger
from selenium.webdriver.support.wait import WebDriverWait
from Utils.ScreenShot import Screenshot
import time,sys

send_time=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))  #获取当前时间
logger_message=Logger()


def is_Sys_Prompt(self):
    u'''系统提示'''
    try:
        WebDriverWait(self.browser,10,0.2).until(lambda x: x.find_element_by_xpath('//div[@class=\"layui-layer-content\"]').is_displayed())
        send_result=self.browser.find_element_by_class_name("layui-layer-content").text
        text="转义模版不能为空"
        print(type(text),type(send_result))
        self.assertIn(text,send_result, msg="失败原因：%s != %s" % (text,send_result))
        print('%s\t方法名：%s\t系统提示：%s' % (send_time,sys._getframe().f_code.co_name,send_result))
        logger_message.loginfo(u'%s\t方法名：%s\t系统提示：%s' % (send_time,sys._getframe().f_code.co_name,send_result))
    except Exception as is_Sys_Prompt_error:
        # Screenshot(self,u'系统提示')
        logger_message.logwarning(u'%s\t方法名：%s\t系统提示-异常：%s' % (send_time,sys._getframe().f_code.co_name,is_Sys_Prompt_error))
