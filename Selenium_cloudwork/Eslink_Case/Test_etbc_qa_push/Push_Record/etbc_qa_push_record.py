# -*- coding: utf-8 -*-
"""
Created on 2018-03-01
@author: sun
Project:云推送-推送记录
"""
import time
from Utils.log import Logger
from Constant.Constant_Path import *

send_time=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))  #获取当前时间
logger_message=Logger()
Picture_path=Error_Picture_path().Picture_path


def is_search_push_record(self):
    u'''推送记录'''
    try:
        time.sleep(1)
        self.browser.implicitly_wait(5)
        operationTypeDes=self.browser.find_element_by_xpath('//table[@id="push-table"]/tbody/tr[1]/td[1]').text
        sendTypeDes=self.browser.find_element_by_xpath('//table[@id="push-table"]/tbody/tr[1]/td[2]').text
        objectDescription=self.browser.find_element_by_xpath('//table[@id="push-table"]/tbody/tr[1]/td[3]').text
        messageStatusDes=self.browser.find_element_by_xpath('//table[@id="push-table"]/tbody/tr[1]/td[4]').text
        sendTime=self.browser.find_element_by_xpath('//table[@id="push-table"]/tbody/tr[1]/td[5]').text
        planNumber=self.browser.find_element_by_xpath('//table[@id="push-table"]/tbody/tr[1]/td[6]').text
        successNumber=self.browser.find_element_by_xpath('//table[@id="push-table"]/tbody/tr[1]/td[7]').text
        failureNumber=self.browser.find_element_by_xpath('.//*[@id="push-table"]/tbody/tr[1]/td[8]').text
        print(
            u"操作类型: %s | 发送类型: %s | 消息描述: %s | 消息状态%s: | 创建时间:%s | 计划数:%s | 成功数：%s | 失败数：%s "
            % (operationTypeDes,sendTypeDes,objectDescription,messageStatusDes,sendTime,planNumber,successNumber,failureNumber)
        )
        logger_message.loginfo( u"操作类型: %s | 发送类型: %s | 消息描述: %s | 消息状态%s: | 创建时间:%s | 计划数:%s | 成功数：%s | 失败数：%s "
            % (operationTypeDes,sendTypeDes,objectDescription,messageStatusDes,sendTime,planNumber,successNumber,failureNumber)
        )

    except Exception as push_send_recond:

            filename= Picture_path + send_time + u"推送记录查询异常" +".png"
            login_safecheck_list=self.browser.get_screenshot_as_file(filename)
            print(u"%s\t推送记录查询异常：%s" % (push_send_recond,send_time))
            logger_message.logwarning(u"%s\t异常原因：%s\t错误截图:%s" % (send_time,push_send_recond,login_safecheck_list))