# -*- coding: utf-8 -*-
"""
Created on 2017-09-12
@author: sun
Project:云推送-消息推送
"""
import sys
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from Constant.Constant_Path import *
from Utils.Excel_readline import ExcelUtil
from Utils.Getcsv_readline import csv_search
from Utils.ScreenShot import Screenshot
from Utils.log import Logger
from Utils.pull_down_list import is_pull_down_list

send_time=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))  #获取当前时间
logger_message=Logger()


def is_url_title(self):
        u"""判断是否取到登录地址"""
        try:
            self.browser.implicitly_wait(30)
            result=EC.title_is(u'ESLink易联云客服')(self.browser)
            # print(u"%s\t方法名：%s\t判断title-----ESlink易联云客服：%s"%(send_time,sys._getframe().f_code.co_name,result))
            self.assertTrue(result)
            logger_message.loginfo(u"%s\t方法名：%s\t判断title-----ESlink易联云客服：%s" %(send_time,sys._getframe().f_code.co_name,result))

        except Exception as title_msg:
            Screenshot(self,u'登录地址异常')
            print(u"%s\t%s\t登录地址：%s" %(send_time,sys._getframe().f_code.co_name,title_msg))
            logger_message.logwarning(u"%s\t%s\t登录地址：%s" %(send_time,sys._getframe().f_code.co_name,title_msg))
            raise


def login_user(self,LoginName,LoginPwd):

        u'''这里写了一个登录的方法,账号和密码参数化'''
        try:
            self.browser.find_element_by_id('loginName').clear()
            self.browser.find_element_by_id('loginName').send_keys(LoginName)
            self.browser.find_element_by_id('loginPwd').clear()
            self.browser.find_element_by_id('loginPwd').send_keys(LoginPwd)
            self.browser.find_element_by_id('loginBt').click()
            self.browser.implicitly_wait(50)

            logger_message.loginfo(u'%s\t方法名：%s\t登录帐号：%s\t密码：%s'%(send_time,sys._getframe().f_code.co_name,LoginName,LoginPwd))
        except Exception as login_user_Error:
            Screenshot(self,u'登录帐号密码异常')
            # print(u"%s\t方法名：%s\t登录帐号密码异常：%s" %(send_time,sys._getframe().f_code.co_name,login_user_Error))
            logger_message.logwarning(u"%s\t方法名：%s\t登录帐号密码异常：%s" %(send_time,sys._getframe().f_code.co_name,login_user_Error))
            raise

def is_login_sucess(self):
        u'''判断是否获取到登录账户名称'''
        try:
            text=u"欢迎：张阳1"
            locator=("id","label-1014")
            result=EC.text_to_be_present_in_element(locator,text)(self.browser)
            self.assertTrue(result)
            # print(u"%s\t方法名：%s判断是否获取到登录账户名称为---张阳1: %s"%(send_time,sys._getframe().f_code.co_name,result))
            logger_message.loginfo(u"%s\t方法名：%s判断是否获取到登录账户名称为---张阳1: %s"%(send_time,sys._getframe().f_code.co_name,result))
        except Exception as login_sucess_msg:
            Screenshot(self,u'登录账户名异常')
            # print(u"%s\t方法名：%s\t登录账户-异常:%s" % (send_time,sys._getframe().f_code.co_name,login_sucess_msg))
            logger_message.logwarning(u"%s\t方法名：%s\t登录账户-异常:%s" % (send_time,sys._getframe().f_code.co_name,login_sucess_msg))
            raise


def is_push_message(self):
        u"""消息推送菜单"""

        try:
            puth_title=u"消息推送"
            locator_title=("id","menuitem-1142")
            is_push_message = EC.text_to_be_present_in_element(locator_title,puth_title)(self.browser)
            self.assertTrue(is_push_message)
            logger_message.loginfo(u"%s\t方法名：%s消息推送菜单-%s"%(send_time,sys._getframe().f_code.co_name,is_push_message))
            self.browser.find_element_by_id("menuitem-1142").click()
            self.browser.implicitly_wait(10)

        except Exception as push_message_msg:
            Screenshot(self,u'消息推送异常')
            print(u"%s\t方法名：%s\t消息推送异常%s" % (send_time,sys._getframe().f_code.co_name,push_message_msg))
            logger_message.logwarning(u"%s\t方法名：%s\t消息推送异常%s" % (send_time,sys._getframe().f_code.co_name,push_message_msg))
            raise

def is_push_message_record(self):
        u"""推送记录菜单"""
        try:
            puth_title=u"推送记录"
            locator_title=("id","menuitem-1155-itemEl")
            result = EC.text_to_be_present_in_element(locator_title,puth_title)(self.browser)
            self.browser.implicitly_wait(10)
            self.browser.find_element_by_id("menuitem-1155-itemEl").click()
            logger_message.loginfo(u"%s\t方法名：%s\t推送记录-%s"%(send_time,sys._getframe().f_code.co_name,result))

        except Exception as push_message_msg:
            # print(u"%s\t推送记录菜单:%s" % (send_time,push_message_msg))
            logger_message.logwarning(u"%s\t方法名：%s\t推送记录菜单:%s" % (send_time,sys._getframe().f_code.co_name,push_message_msg))
            raise


def is_iframe_page(self):
        u"""iframe页面"""
        try:
            time.sleep(1)
            self.browser.implicitly_wait(5)
            self.browser.switch_to.frame(self.browser.find_element_by_tag_name("iframe"))
            logger_message.loginfo(u"%s\t方法名：%s\t切换iframe页面"%(send_time,sys._getframe().f_code.co_name))

        except Exception as iframe_page_error:

            logger_message.logwarning(u"%s\t方法名：%s\tiframe页面-异常：%s"%(send_time,sys._getframe().f_code.co_name,iframe_page_error))
            raise


def is_push_channel(self,mobel):
        u'''发送渠道的选择'''
        try:
            time.sleep(1)
            self.browser.implicitly_wait(5)
            push_channel=self.browser.find_element_by_xpath('//li[@data-channel-id="%s"]' % mobel)
            logger_message.loginfo(u"%s\t方法名：%s\t发送渠道选择：%s"%(send_time,sys._getframe().f_code.co_name,push_channel.text))
            push_channel.click()
        except  Exception as push_channel_msg:
            logger_message.logwarning(u"%s\t方法名：%s\t发送渠道选择-异常：%s"%(send_time,sys._getframe().f_code.co_name,push_channel_msg))
            raise

def is_check_message_template(self):

        u'''短信渠道模版参数化'''
        time.sleep(1)
        self.browser.find_element_by_xpath(".//*[@id='select2-dxSel-container']").click()
        self.browser.implicitly_wait(5)
        csv_template=csv_search.csv_test(filename=Push_Template_path().push_template,indexs=1)
        check_template=csv_template[1]
        Message_Template=is_pull_down_list(self,csv_template[1],".//*[@id='select2-dxSel-results']/li[%s]")

        try:

            template_name=self.browser.find_element_by_xpath(".//*[@id='select2-dxSel-container']").text

            if template_name in str(check_template):

                logger_message.loginfo('%s\t方法名：%s\t短信模版：%s'%(send_time,sys._getframe().f_code.co_name,check_template))

                self.browser.find_element_by_xpath(".//*[@id='%s']" % csv_template[8]).send_keys(csv_template[9])

                self.browser.find_element_by_xpath(".//*[@id='%s']" % csv_template[10]).send_keys(csv_template[11])

            elif template_name in str(check_template):

                logger_message.loginfo('短信模版：%s'%check_template)

                self.browser.find_element_by_xpath(".//*[@id='%s']" % csv_template[8]).send_keys(csv_template[9])

                self.browser.find_element_by_xpath(".//*[@id='%s']" % csv_template[10]).send_keys(csv_template[11])

                self.browser.find_element_by_xpath(".//*[@id='%s']" % csv_template[12]).send_keys(csv_template[13])

        except Exception as is_check_message_template_data_error:

            Screenshot(self,u'短信模版')

            # print(u"%s\t短信模版-异常:%s" % (send_time,is_check_message_template_data_error))

            logger_message.logwarning(u"%s\t方法名:%s\t短信模版-异常:%s" % (send_time,sys._getframe().f_code.co_name,is_check_message_template_data_error))
            raise

def is_phone_number(self):
        u'''手机号参数化'''
        try:

            fileName="D:\\pycharm-5.0.4\\Selenium_unittest\\Data\\mobiles.xlsx"

            sheetName = "Sheet1"

            data =ExcelUtil(fileName,sheetName)

            for number in data.dict_data():

                self.browser.find_element_by_xpath(".//*[@id='phone-numbers']").send_keys(number,',')

            self.browser.find_element_by_xpath(".//*[@id='phone-numbers']").send_keys(Keys.BACKSPACE)

        except Exception as is_phone_number_error:

            Screenshot(self,u'手机参数化异常')

            logger_message.logwarning(u'%s\t方法名：%s\t手机号参数化-异常:%s'%(send_time,sys._getframe().f_code.co_name,is_phone_number_error))
            raise

def is_check_send_message(self):
        u'''短信发送检验'''
        try:
            time.sleep(0.5)
            self.browser.implicitly_wait(5)
            self.browser.find_element_by_id("send-message").click()
            time.sleep(0.5)
            send_result=self.browser.find_element_by_class_name("layui-layer-content").text
            text="发送成功"
            self.assertEqual(text,send_result, msg="失败原因：%s != %s" % (text,send_result))
            print('%s\t短信发送：%s' % (send_time,send_result))
            logger_message.loginfo('%s\t短信发送：%s' % (send_time,send_result))
        except Exception as send_message_msg:
            Screenshot(self,u'短信推送异常')
            logger_message.logwarning(u"%s\t方法名:%s\t短信推送异常：%s" % (send_time,sys._getframe().f_code.co_name,send_message_msg))
            raise

def is_message_mobile(self):
        u"""选择短信模版"""
        try:
            #添加xlsx文件地址
            self.browser.find_element_by_id("mobiles").send_keys("D:\\pycharm-5.0.4\\Selenium_unittest\\Data\\mobiles.xlsx")
            self.browser.implicitly_wait(5)
            time.sleep(2)
            mobiles_selected=self.browser.find_element_by_id("file-name").text
            text="mobiles.xlsx"
            self.assertEqual(text,mobiles_selected, msg="失败的原因：%s != %s" %(text,mobiles_selected))

        except Exception as message_mobile_msg:

            Screenshot(self,u'短信模版推送异常')

            logger_message.logwarning(u"%s\t方法名：%s\t短信模版:%s" % (send_time,sys._getframe().f_code.co_name,message_mobile_msg))

            raise

def is_close_message_check(self):

        u"""关闭消息推送"""
        try:
            time.sleep(3)
            self.browser._switch_to.default_content()
            self.browser.find_element_by_xpath('.//span[@data-ref="closeEl"]').click()

        except Exception as is_close_message_check_error:

            Screenshot(self,u'关闭消息推送')

            logger_message.logwarning(u"%s\t方法名：%s\t短信模:%s" % (send_time,sys._getframe().f_code.co_name,is_close_message_check_error))

            raise



