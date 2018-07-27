# -*- coding: utf-8 -*-
"""
Created on 2018-03-01
@author: sun
Project:云推送-新增渠道模版（短信）
"""
import sys
import time
from selenium.webdriver.support import expected_conditions as EC
from Constant.Constant_Path import *
from Eslink_Case.Test_etbc_qa_push.Push_Message_Send.etbc_qa_push_message import *
from Utils.Getcsv_readline import csv_search
from Utils.ScreenShot import Screenshot
from Utils.Sys_Prompt import is_Sys_Prompt
from Utils.pull_down_list import is_pull_down_list
from Utils.test_db import MySQL


def is_channel_template(self):
        u"""渠道模板菜单"""
        try:
            puth_title=u"渠道模板"
            locator_title=("id","menuitem-1158-itemEl")
            is_push_message = EC.text_to_be_present_in_element(locator_title,puth_title)(self.browser)
            self.assertTrue(is_push_message)
            logger_message.loginfo(u"%s\t方法名：%s\t渠道模板 %s" % (send_time,sys._getframe().f_code.co_name,is_push_message))
            self.browser.find_element_by_id("menuitem-1158-itemEl").click()
            self.browser.implicitly_wait(10)
        except Exception as is_channel_template_msg:
            Screenshot(self,u'渠道模板异常')
            print(u"%s\t方法名：%s\t渠道模板异常%s" % (send_time,sys._getframe().f_code.co_name,is_channel_template_msg))
            logger_message.logwarning(u"%s\t方法名：%s\t渠道模板异常%s" % (send_time,sys._getframe().f_code.co_name,is_channel_template_msg))


def is_add_channel_template(self):
        u'''添加csv文件新增渠道模版'''
        try:
            template_message=csv_search.csv_test(filename=Push_Template_path().push_template,indexs=3)
            time.sleep(0.5)
            self.browser.implicitly_wait(10)
            self.browser.find_element_by_xpath('.//*[@id="add"]').click()
            self.browser.implicitly_wait(5)
            self.browser._switch_to.default_content()
            self.browser.switch_to.frame(self.browser.find_element_by_tag_name("iframe"))
            time.sleep(0.5)
            self.browser.switch_to.frame(self.browser.find_element_by_id("layui-layer-iframe2"))
            self.browser.find_element_by_xpath('//*[@id="name"]').send_keys(template_message[1])     #模版名称：Name
            self.browser.implicitly_wait(5)
            self.browser.find_element_by_xpath('//*[@id="%s"]'%template_message[2]).click()          #模版状态：State,tmp-disable:禁用,tmp-enable:启用
            self.browser.implicitly_wait(5)
            self.browser.find_element_by_xpath('//*[@data-id="channelId"]').click()
            self.browser.implicitly_wait(5)
            is_pull_down_list(self,template_message[3],".//*[@id='query-form']/div[3]/div/div/div/div/ul/li")  #渠道名称：ChannelId
            self.browser.implicitly_wait(5)
            self.browser.find_element_by_xpath('.//*[@id="code"]').send_keys(template_message[5])     #模版编号:Code
            self.browser.implicitly_wait(5)
            self.browser.find_element_by_xpath('.//*[@id="content"]').send_keys(template_message[6])  #模版内容:Content
            self.browser.implicitly_wait(5)
            # self.browser.find_element_by_xpath('.//*[@id="escapeContent"]').send_keys(template_message[7])  #转义模版:EscapeContent
            # logger_message.loginfo('\n%s\n新增模版名称：%s\n模版状态：%s\n渠道名称：%s\n模版编号:%s\n模版内容：%s\n转义模版：%s'%
            #       (send_time,template_message[1],template_message[2],template_message[3],template_message[5],template_message[6],template_message[7]))

            self.browser.implicitly_wait(5)
            self.browser.find_element_by_xpath('.//*[@id="btn-add"]').click()
            is_Sys_Prompt(self)
        except Exception as is_add_channel_template_error:
            Screenshot(self,u'添加csv文件新增短信渠道模版-异常')
            print(u'%s\t方法名：%s\t添加csv文件新增短信渠道模版-异常：%s' % (send_time,sys._getframe().f_code.co_name,is_add_channel_template_error))
            logger_message.logwarning(u'%s\t方法名：%s\t添加csv文件新增短信渠道模版-异常：%s' % (send_time,sys._getframe().f_code.co_name,is_add_channel_template_error))
            raise

def is_check_messageTemplate(self):
    u'''确认是否存在短信模版'''
    try:
        template_message=csv_search.csv_test(filename=Push_Template_path().push_template,indexs=2)
        time.sleep(0.5)
        database=MySQL()
        template_code = template_message[5]
        template_name=template_message[1]
        sql="Select * FROM push_channelmessagetemplate WHERE `code` = '%s' AND name = '%s';" % (template_code,template_name)
        print(sql)
        logger_message.loginfo(u"%s\t方法名：%s\t模版名称：%s\t模版编号：%s"%(send_time,template_name,template_code))
        result=database.query(sql)
        print(result)
        if len(result) == 1:
            print('存在模版:%s'%template_name)
            logger_message.loginfo(u"%s\t方法名：%s模版信息：%s"%(send_time,sys._getframe().f_code.co_name,result))
            sql="DELETE FROM push_channelmessagetemplate WHERE `code` = '%s';" % template_code
            database.query(sql)
        else:
            print('不存在模版:%s'%template_name)
            logger_message.loginfo(u"%s\t方法名：%s模版信息：%s"%(send_time,sys._getframe().f_code.co_name,result))

    except Exception as is_check_template_Error:
        Screenshot(self,u'模版查询异常')
        logger_message.loginfo(u"%s\t方法名：%s\t模版查询异常：%s"%(send_time,sys._getframe().f_code.co_name,is_check_template_Error))
        logger_message.loginfo(u"%s\t方法名：%s\t模版查询异常：%s"%(send_time,sys._getframe().f_code.co_name,is_check_template_Error))
        raise


















