# -*- coding: utf-8 -*-
"""
Created on 2018-03-21
@author: sun
Project:云推送-查询渠道模版（短信）
"""
import sys
import time

from Constant.Constant_Path import *
from Utils.Getcsv_readline import csv_search
from Utils.ScreenShot import Screenshot
from Utils.log import Logger
from Utils.pull_down_list import is_pull_down_list

send_time=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))  #获取当前时间
logger_message=Logger()


def is_Query_Channel_Template(self):
        u'''渠道模版查询'''
        try:
            template_message=csv_search.csv_test(filename=Push_Template_path().push_template,indexs=1)
            time.sleep(1)
            self.browser.implicitly_wait(10)
            self.browser.find_element_by_xpath('.//*[@id="query"]').click()
            self.browser.implicitly_wait(5)
            self.browser._switch_to.default_content()
            self.browser.switch_to.frame(self.browser.find_element_by_tag_name("iframe"))
            time.sleep(0.5)
            self.browser.switch_to.frame(self.browser.find_element_by_id("layui-layer-iframe2"))
            self.browser.find_element_by_xpath('.//*[@id="name"]').send_keys(template_message[1])
            self.browser.find_element_by_xpath('.//*[@data-id="channelId"]').click()
            Channel_type=is_pull_down_list(self,template_message[3],".//*[@class='dropdown-menu inner']/li")
            # print('%s\t方法名：%s\t模版名称：%s\t渠道类型：%s'%(send_time,sys._getframe().f_code.co_name,template_message[1],template_message[3]))
            logger_message.loginfo('%s\t方法名：%s\t模版名称：%s\t渠道类型：%s'%(send_time,sys._getframe().f_code.co_name,template_message[1],template_message[3]))
            time.sleep(1)
            self.browser.implicitly_wait(5)
            self.browser._switch_to.default_content()
            self.browser.switch_to.frame(self.browser.find_element_by_tag_name("iframe"))#返回iframe页面
            self.browser.implicitly_wait(5)
            self.browser.find_element_by_xpath('.//*[@id="layui-layer2"]/div[2]/a[1]').click()

        except Exception as is_Query_Channel_Template_error:
            Screenshot(self,u'渠道模版查询异常')
            # print(u"%s\t方法名:%s\t渠道模版查询异常：%s" %  (send_time,sys._getframe().f_code.co_name,is_Query_Channel_Template_error))
            logger_message.logwarning(u"%s\t方法名:%s\t渠道模版查询异常：%s" %  (send_time,sys._getframe().f_code.co_name,is_Query_Channel_Template_error))
            raise


def is_query_template(self):
        u'''渠道模版查询记录'''
        try:
            time.sleep(1)
            self.browser.implicitly_wait(5)
            name=self.browser.find_element_by_xpath(".//*[@id='messagetmp-table']/tbody/tr/td[1]").text
            statusName=self.browser.find_element_by_xpath(".//*[@id='messagetmp-table']/tbody/tr/td[2]").text
            channelName=self.browser.find_element_by_xpath(".//*[@id='messagetmp-table']/tbody/tr/td[3]").text
            datasourceName=self.browser.find_element_by_xpath(".//*[@id='messagetmp-table']/tbody/tr/td[4]").text
            createDate=self.browser.find_element_by_xpath(".//*[@id='messagetmp-table']/tbody/tr/td[5]").text
            lastUpdateDate=self.browser.find_element_by_xpath(".//*[@id='messagetmp-table']/tbody/tr/td[6]").text
            # print(u"模板名称: %s | 模板状态: %s | 渠道类型: %s | 数据源:%s | 创建时间:%s | 最后修改时间:%s "
            #     % (name,statusName,channelName,datasourceName,createDate,lastUpdateDate))
            logger_message.loginfo( u"模板名称: %s | 模板状态: %s | 渠道类型: %s | 数据源:%s | 创建时间:%s | 最后修改时间:%s "
                % (name,statusName,channelName,datasourceName,createDate,lastUpdateDate))

        except Exception as push_send_recond:
            Screenshot(self,u'渠道模版查询记录异常')
            # print(u"%s\t方法名：%s\t渠道模版查询记录异常原因：%s" % (send_time,sys._getframe().f_code.co_name,push_send_recond))
            logger_message.logwarning(u"%s\t方法名：%s\t渠道模版查询记录异常原因：%s" % (send_time,sys._getframe().f_code.co_name,push_send_recond))
            raise