# -*- coding: utf-8 -*-
"""
Created on 2018-03-01
@author: sun
Project:Etbc后台Demo
"""
import sys
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Constant.Constant_Path import *
from Utils.Excel_readline import ExcelUtil
from Utils.Getcsv_readline import csv_search
from Utils.ScreenShot import Screenshot
from Utils.log import Logger
from Utils.pull_down_list import is_pull_down_list
from Utils.test_db import MySQL

send_time=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))  #获取当前时间
logger_message=Logger()



class etbc_demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.option = webdriver.ChromeOptions()
        cls.option.add_argument('disable-infobars')
        cls.browser=webdriver.Chrome(chrome_options=cls.option)
        cls.browser.maximize_window()
        cls.browser.get(Constant_path().LOGIN_URL)

    def is_url_title(self):
        u"""判断是否取到登录地址"""
        try:
            result=EC.title_is(u'ESLink易联云客服')(self.browser)
            # print(u"%s\t方法名：%s\t判断title-----ESlink易联云客服：%s"%(send_time,sys._getframe().f_code.co_name,result))
            self.assertTrue(result)
            logger_message.loginfo(u"%s\t方法名：%s\t判断title-----ESlink易联云客服：%s" %(send_time,sys._getframe().f_code.co_name,result))

        except Exception as title_msg:
            Screenshot(self,u'登录地址异常')
            print(u"%s\t%s\t登录地址：%s" %(send_time,sys._getframe().f_code.co_name,title_msg))
            logger_message.logwarning(u"%s\t%s\t登录地址：%s" %(send_time,sys._getframe().f_code.co_name,title_msg))

    def login_user(self,LoginName,LoginPwd):

            u'''这里写了一个登录的方法,账号和密码参数化'''
            try:
                self.browser.implicitly_wait(30)
                self.browser.find_element_by_id('loginName').clear()
                self.browser.find_element_by_id('loginName').send_keys(LoginName)
                self.browser.find_element_by_id('loginPwd').clear()
                self.browser.find_element_by_id('loginPwd').send_keys(LoginPwd)
                self.browser.find_element_by_id('loginBt').click()
                self.browser.implicitly_wait(30)
                logger_message.loginfo(u'%s\t方法名：%s\t登录帐号：%s\t密码：%s'%(send_time,sys._getframe().f_code.co_name,LoginName,LoginPwd))
            except Exception as login_user_Error:
                Screenshot(self,u'登录帐号密码异常')
                # print(u"%s\t方法名：%s\t登录帐号密码异常：%s" %(send_time,sys._getframe().f_code.co_name,login_user_Error))
                logger_message.logwarning(u"%s\t方法名：%s\t登录帐号密码异常：%s" %(send_time,sys._getframe().f_code.co_name,login_user_Error))

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

    def is_channel_template(self):
        u"""渠道模板"""
        try:
            puth_title=u"渠道模板"
            locator_title=("id","menuitem-1156-itemEl")
            is_push_message = EC.text_to_be_present_in_element(locator_title,puth_title)(self.browser)
            self.assertTrue(is_push_message)
            logger_message.loginfo(u"%s\t方法名：%s\t渠道模板 %s" % (send_time,sys._getframe().f_code.co_name,is_push_message))
            self.browser.find_element_by_id("menuitem-1156-itemEl").click()
            self.browser.implicitly_wait(10)
        except Exception as is_channel_template_msg:
            Screenshot(self,u'渠道模板异常')
            print(u"%s\t方法名：%s\t渠道模板异常%s" % (send_time,sys._getframe().f_code.co_name,is_channel_template_msg))
            logger_message.logwarning(u"%s\t方法名：%s\t渠道模板异常%s" % (send_time,sys._getframe().f_code.co_name,is_channel_template_msg))
    def is_push_message(self):
            u"""消息推送"""
            try:
                puth_title=u"消息推送"
                locator_title=("id","menuitem-1154-itemEl")
                is_push_message = EC.text_to_be_present_in_element(locator_title,puth_title)(self.browser)
                self.assertTrue(is_push_message)
                logger_message.loginfo(u"消息推送 %s" % is_push_message)
                self.browser.find_element_by_id("menuitem-1154-itemEl").click()
                self.browser.implicitly_wait(10)

            except Exception as push_message_msg:
                Screenshot(self,u'消息推送异常')
                print(u"%s\t方法名：%s\t消息推送异常%s" % (send_time,sys._getframe().f_code.co_name,push_message_msg))
                logger_message.logwarning(u"%s\t方法名：%s\t消息推送异常%s" % (send_time,sys._getframe().f_code.co_name,push_message_msg))

    def is_iframe_page(self):
        u"""iframe页面"""
        time.sleep(1)
        self.browser.switch_to.frame(self.browser.find_element_by_tag_name("iframe"))
        self.browser.implicitly_wait(5)
        print('进入iframe1页面')

    def is_push_channel(self,mobel):
        u'''发送渠道的选择'''
        try:
            time.sleep(1)
            self.browser.implicitly_wait(5)
            push_channel=self.browser.find_element_by_xpath('//li[@data-channel-id="%s"]' % mobel)
            logger_message.loginfo(u"%s\t发送渠道选择：%s"%(send_time,push_channel.text))
            push_channel.click()
        except  Exception as push_channel_msg:
            Screenshot(self,u'发送渠道的选择异常')
            print(u"%s\t方法名：%s\t发送渠道选择-异常：%s"%(send_time,sys._getframe().f_code.co_name,push_channel_msg))
            logger_message.logwarning(u"%s\t方法名：%s\t发送渠道选择-异常：%s"%(send_time,sys._getframe().f_code.co_name,push_channel_msg))

    def is_wechat_group(self,group):
        u'''微信发送分组选择'''
        try:
            time.sleep(1)
            self.browser.implicitly_wait(5)
            self.browser.find_element_by_xpath('//label[@for="wechat-radio-group"]').click()
            time.sleep(1)
            self.browser.implicitly_wait(5)
            wechat_send_object=self.browser.find_element_by_xpath('//span[@title="你好"]').click()      #分组点击后出现下拉框
            try:
                message_No=0
                check_template=group
                while True:

                    message_No = message_No + 1

                    list_one=self.browser.find_elements_by_class_name("select2-results__option").pop(message_No).text

                    if check_template in list_one:

                        list_template=self.browser.find_elements_by_class_name("select2-results__option").pop(message_No)

                        print(list_template.text,'group_find')

                        logger_message.loginfo('group_find:%s'% list_template.text)

                        list_template.click()

                        break

            except Exception as is_check_message_template_error:

                Screenshot(self,u'短信渠道模版参数化-异常')

                print(u"短信渠道模版参数化-异常:%s" % is_check_message_template_error)

                logger_message.logwarning('%s\t方法名：%s\t短信渠道模版参数化-异常:%s'% (send_time,sys._getframe().f_code.co_name,is_check_message_template_error))

        except Exception as is_wechat_group:

            Screenshot(self,u'微信发送分组选择-异常')

            print(u"%s\t方法名：%s\t微信发送分组选择-异常：%s"%(send_time,sys._getframe().f_code.co_name,is_wechat_group))

            logger_message.logwarning(u"%s\t方法名：%s\t微信发送分组选择-异常：%s"%(send_time,sys._getframe().f_code.co_name,is_wechat_group))

    def is_wechat_send_type(self,type):
        u'''选择微信发送类型'''
        try:
            time.sleep(0.5)
            self.browser.implicitly_wait(5)
            type_choice=self.browser.find_element_by_xpath('//li[@data-id="%s"]' % type)
            logger_message.loginfo(u"%s\t微信发送类型：%s"%(send_time,type_choice.text))
            type_choice.click()
        except Exception as wechat_send_type_msg:
            Screenshot(self,u'微信发送类型-异常')
            print(u"%s\t方法名：%s\t微信发送类型-异常：%s"%(send_time,sys._getframe().f_code.co_name,wechat_send_type_msg))
            logger_message.logwarning(u"%s\t方法名：%s\t微信发送类型-异常：%s"%(send_time,sys._getframe().f_code.co_name,wechat_send_type_msg))

    def is_wechat_send_article(self,search_article):
        u'''微信搜索文章'''
        try:
            time.sleep(0.5)
            self.browser.implicitly_wait(5)
            add_article=self.browser.find_element_by_xpath('//div[@class="tab-content only-right"]/div[1]/button').click()                  #添加文章按钮
            self.browser.implicitly_wait(5)
            self.browser.switch_to.frame(self.browser.find_element_by_id("layui-layer-iframe4"))
            search_box=self.browser.find_element_by_xpath("html/body/div[1]/div[2]/div/div/div/div[2]/input").send_keys(search_article)
            time.sleep(0.5)
            self.browser.implicitly_wait(5)
            search_botton=self.browser.find_element_by_xpath("html/body/div[1]/div[2]/div/div/div/div[2]/a").click()
            self.browser.implicitly_wait(5)
            article_title=self.browser.find_element_by_xpath(".//*[@id='artical-table']/tbody/tr/td[3]").click()
            self.browser.implicitly_wait(5)
            self.browser.find_element_by_id("save").click()
            self.browser.implicitly_wait(5)
            self.browser._switch_to.default_content()
            self.browser.switch_to.frame(self.browser.find_element_by_tag_name("iframe"))#返回iframe页面
            for i in range(2):
                self.browser.find_element_by_class_name("ps-scrollbar-y").send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            self.browser.find_element_by_id("wechat-send").click()#发送按钮
            time.sleep(0.5)
            send_result=self.browser.find_element_by_class_name("layui-layer-content").text
            text="发送成功"
            assert_result=self.assertEqual(text,send_result, msg="失败的原因：%s != %s" %(text,send_result))
            print(assert_result)
            if  assert_result in "None":
                print("发送成功")
                logger_message.loginfo(u"%s\t发送成功")
            else:
                logger_message.loginfo(u"%s\t失败的原因：%s != %s" %(send_time,text,send_result))

        except Exception as wechat_article_msg:
            Screenshot(self,u'微信发送文章-异常')

            print(u'%s\t微信发送文章-异常:%s'%(send_time,wechat_article_msg))

            logger_message.logwarning(u'%s\t方法名：%s\t微信发送文章-异常:%s'%(send_time,sys._getframe().f_code.co_name,wechat_article_msg))

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

                logger_message.loginfo('短信模版：%s'%check_template)

                self.browser.find_element_by_xpath(".//*[@id='%s']" % csv_template[8]).send_keys(csv_template[9])

                self.browser.find_element_by_xpath(".//*[@id='%s']" % csv_template[10]).send_keys(csv_template[11])

                logger_message.loginfo(u'%s\t方法名：%s\t短信模版')

            elif template_name in str(check_template):

                logger_message.loginfo('短信模版：%s'%check_template)

                self.browser.find_element_by_xpath(".//*[@id='%s']" % csv_template[8]).send_keys(csv_template[9])

                self.browser.find_element_by_xpath(".//*[@id='%s']" % csv_template[10]).send_keys(csv_template[11])

                self.browser.find_element_by_xpath(".//*[@id='%s']" % csv_template[12]).send_keys(csv_template[13])

        except Exception as is_check_message_template_data_error:
            Screenshot(self,u'短信模版-异常')

            print(u"%s\t方法名：%s\t短信模版-异常:%s" % (send_time,sys._getframe().f_code.co_name,is_check_message_template_data_error))

            logger_message.logwarning(u"%s\t方法名：%s\t短信模版-异常:%s" % (send_time,sys._getframe().f_code.co_name,is_check_message_template_data_error))

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
            Screenshot(self,u'手机号参数化-异常')

            print(u'%s\t方法名：%s\t手机号参数化-异常:%s'%(send_time,sys._getframe().f_code.co_name,is_phone_number_error))

            logger_message.logwarning(u'%s\t方法名：%s\t手机号参数化-异常:%s'%(send_time,sys._getframe().f_code.co_name,is_phone_number_error))

    def is_check_send_message(self):
        u'''短信发送检验'''
        try:
            WebDriverWait(self.browser,10,1).until(lambda x: x.find_element_by_id("send-message").is_displayed())
            send_message=self.browser.find_element_by_id("send-message")
            AC(self.browser).click(send_message).perform()
            time.sleep(0.5)
            send_result=self.browser.find_element_by_class_name("layui-layer-content").text
            text="发送成功"
            self.assertEqual(text,send_result, msg="失败原因：%s != %s" % (text,send_result))
            print('%s\t方法名:%s\t短信发送：%s' % (send_time,sys._getframe().f_code.co_name,send_result))
            logger_message.loginfo('%s\t方法名:%s\t短信发送：%s' % (send_time,sys._getframe().f_code.co_name,send_result))
        except Exception as send_message_msg:
            Screenshot(self,u'短信推送异常')
            print(u"%s\t方法名:%s\t短信推送异常：%s" %  (send_time,sys._getframe().f_code.co_name,send_message_msg,))
            logger_message.logwarning(u"%s\t方法名:%s\t短信推送异常：%s" %  (send_time,sys._getframe().f_code.co_name,send_message_msg,))

    def is_check_template(self):
        u'''检查模版是否存在'''
        try:
            template_message=csv_search.csv_test(filename=Push_Template_path().push_template,indexs=2)
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
                logger_message.loginfo(u"%s\t方法名：模版信息：%s"%(send_time,result))
                sql="DELETE FROM push_channelmessagetemplate WHERE `code` = '%s';" % template_code
                database.query(sql)
            else:
                print('不存在模版:%s'%template_name)
                logger_message.loginfo(u"%s\t方法名：模版信息：%s"%(send_time,result))

        except Exception as is_check_template_Error:
            Screenshot(self,u'模版查询异常')
            logger_message.loginfo(u"%s\t方法名：模版查询异常：%s"%(send_time,is_check_template_Error))
            logger_message.loginfo(u"%s\t方法名：模版查询异常：%s"%(send_time,is_check_template_Error))

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
            print('%s\t方法名：%s\t模版名称：%s\t渠道类型：%s'%(send_time,sys._getframe().f_code.co_name,template_message[1],template_message[3]))
            logger_message.loginfo('%s\t方法名：%s\t模版名称：%s\t渠道类型：%s'%(send_time,sys._getframe().f_code.co_name,template_message[1],template_message[3]))
            time.sleep(1)
            self.browser.implicitly_wait(5)
            self.browser._switch_to.default_content()
            self.browser.switch_to.frame(self.browser.find_element_by_tag_name("iframe"))#返回iframe页面
            self.browser.implicitly_wait(5)
            self.browser.find_element_by_xpath('.//*[@id="layui-layer2"]/div[2]/a[1]').click()

        except Exception as is_Query_Channel_Template_error:
            Screenshot(self,u'渠道模版查询异常')
            print(u"%s\t方法名:%s\t渠道模版查询异常：%s" %  (send_time,sys._getframe().f_code.co_name,is_Query_Channel_Template_error))
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
            print(u"模板名称: %s | 模板状态: %s | 渠道类型: %s | 数据源:%s | 创建时间:%s | 最后修改时间:%s "
                % (name,statusName,channelName,datasourceName,createDate,lastUpdateDate))
            logger_message.loginfo( u"模板名称: %s | 模板状态: %s | 渠道类型: %s | 数据源:%s | 创建时间:%s | 最后修改时间:%s "
                % (name,statusName,channelName,datasourceName,createDate,lastUpdateDate))

        except Exception as push_send_recond:
            Screenshot(self,u'渠道模版查询记录异常')
            print(u"%s\t方法名：%s\t渠道模版查询记录异常原因：%s" % (send_time,sys._getframe().f_code.co_name,push_send_recond))
            logger_message.logwarning(u"%s\t方法名：%s\t渠道模版查询记录异常原因：%s" % (send_time,sys._getframe().f_code.co_name,push_send_recond))
            raise

    def test_demo(self):
        u'''短信发送'''
        self.is_url_title()

        self.login_user(u"zhangyang1",u"zj03030418")

        self.is_login_sucess()

        self.is_push_message()

        self.is_iframe_page()

        self.is_push_channel(u"9")

        self.is_check_message_template()

        self.is_phone_number()

        # self.is_check_send_message()
    #
    # def test_wechat(self):
    #     u'''微信发送'''
    #     self.is_url_title()
    #
    #     self.login_user(u"zhangyang1",u"zj03030418")
    #
    #     self.is_login_sucess()
    #
    #     self.is_push_message()
    #
    #     self.is_iframe_page()
    #
    #     self.is_push_channel(u"2")
    #
    #     self.is_wechat_group(u"张阳微信专测")
    #
    #     self.is_wechat_send_type(u"4")
    # #
    # #     self.is_wechat_send_article(u"测试文章0")
    #
    # def test_query(self):
    #     u'''微信发送'''
    #     self.is_url_title()
    #
    #     self.login_user(u"zhangyang1",u"zj03030418")
    #
    #     self.is_login_sucess()
    #
    #     self.is_channel_template()
    #
    #     self.is_iframe_page()
    #
    #     self.is_Query_Channel_Template()
    #
    #     self.is_query_template()

    @classmethod
    def tearDownClass(cls):

        time.sleep(2)

        cls.browser.quit()

if __name__ == '__main__':
    unittest.main()
