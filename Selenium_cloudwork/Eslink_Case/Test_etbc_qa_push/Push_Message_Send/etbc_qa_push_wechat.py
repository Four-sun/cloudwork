#coding=utf-8
"""
Created on 2017-09-12
@author: sun
Project:微信推送
"""
import sys
import time

from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys

from Constant.Constant_Path import *
from Utils.Getcsv_readline import csv_search
from Utils.ScreenShot import Screenshot
from Utils.log import Logger
from Utils.pull_down_list import is_pull_down_list

send_time=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))  #获取当前时间
logger_message=Logger()


def is_sender_object(self):
    u'''发送对象信息'''
    try:
        self.browser.implicitly_wait(5)
        wechat_active=self.browser.find_element_by_xpath('//li[@data-channel-id="2"]')               #选择微信渠道推送
        time.sleep(0.5)
        self.browser.implicitly_wait(5)
        wechat_radio_group =self.browser.find_element_by_xpath('//label[@for="wechat-radio-group"]')            #选择发送对象：分组
        AC(self.browser).click(wechat_active).click(wechat_radio_group).perform()
        time.sleep(0.5)
        self.browser.implicitly_wait(5)
        wechat_send_object=self.browser.find_element_by_xpath('//span[@title="你好"]').click()         #选择分组
        self.browser.implicitly_wait(5)
        group=is_pull_down_list(self,u'张阳微信专测',".//*[@class='select2-results__option']")
        self. browser.implicitly_wait(10)
        Message_Description=self.browser.find_element_by_name("objectDescription").send_keys("推送测试")     #消息描述
        logger_message.loginfo(u'%s\t方法名：%s \t选择发送渠道：%s \t发送对象：%s'%(send_time,sys._getframe().f_code.co_name,wechat_active.text,wechat_radio_group.text))

    except Exception as login_user_Error:

        Screenshot(self,u'发送对象信息-异常')
        logger_message.logwarning(u"%s\t方法名：%s\t发送对象信息异常：%s" %(send_time,sys._getframe().f_code.co_name,login_user_Error))
        raise


def is_tab_wechat_mobel(self):

        u"""微信模版推送"""
        try:
            template_message=csv_search.csv_test(filename=Push_Template_path().push_template,indexs=3)
            type_choose=self.browser.find_element_by_xpath('//li[@data-id="5"]')                   #选择内容类型:模版
            AC(self.browser).click(type_choose).perform()
            self.browser.implicitly_wait(10)
            template_name=self.browser.find_element_by_xpath(".//*[@id='select2-wxSel-container']").text
            self.browser.find_element_by_xpath('//span[@title="%s"]'%template_name).click()
            self.browser.implicitly_wait(5)
            is_pull_down_list(self,template_message[1],'//ul[@class="select2-results__options"]/li')
            #send_keys 移动至底
            for i in range(5):
                self.browser.find_element_by_class_name("ps-scrollbar-y").send_keys(Keys.PAGE_DOWN)
            time.sleep(1)

            #微信模版
            self.browser.find_element_by_id(template_message[8]).send_keys(template_message[9])
            self.browser.find_element_by_id(template_message[10]).send_keys(template_message[11])
            self.browser.find_element_by_id(template_message[12]).send_keys(template_message[13])
            self.browser.find_element_by_id(template_message[14]).send_keys(template_message[15])
            time.sleep(2)
            # self.browser.find_element_by_id("wechat-send").click()
            # time.sleep(1)
            # send_result=self.browser.find_element_by_class_name("layui-layer-content").text
            # text="发送成功"
            # self.assertEqual(text,send_result, msg="失败的原因：%s != %s" %(text,send_result))

        except Exception as wechat_mobel_msg:

            print(wechat_mobel_msg)

            logger_message.logwarning(wechat_mobel_msg)

            raise


def is_tab_wechat_article(self):
        u'''微信文章推送'''
        try:
            type_choose=self.browser.find_element_by_xpath('//li[@data-id="4"]').click()                           #选择内容类型
            time.sleep(1)
            add_article=self.browser.find_element_by_xpath('//div[@class="tab-content only-right"]/div[1]/button').click()         #添加文章
            self.browser.switch_to.frame(self.browser.find_element_by_id("layui-layer-iframe4"))
            self.browser.find_element_by_xpath('//input[@data-index="2"]').click()                                     #新增文章--第三篇
            self.browser.find_element_by_id("save").click()                                                            #保存键
            self.browser.implicitly_wait(5)
            self.browser._switch_to.default_content()
            self.browser.switch_to.frame(self.browser.find_element_by_tag_name("iframe"))                           #返回iframe页面
            for i in range(2):
                self.browser.find_element_by_class_name("ps-scrollbar-y").send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            self.browser.find_element_by_id("wechat-send").click()                                                  #发送按钮
            time.sleep(0.5)
            send_result=self.browser.find_element_by_class_name("layui-layer-content").text
            text="发送成功"
            self.assertEqual(text,send_result, msg="失败的原因：%s != %s" %(text,send_result))
        except Exception as wechat_article_msg:

            print(wechat_article_msg)

            logger_message.logwarning(wechat_article_msg)

def is_tab_wechat_matter(self):
        u'''微信素材推送'''
        try:
            type_choose=self.browser.find_element_by_xpath('//li[@data-id="3"]').click()                     #选择内容类型
            add_materil=self.browser.find_element_by_xpath('//button[@class="btn btn-default add-material"]').click()     #添加素材
            time.sleep(1)
            self.browser.switch_to.frame(self.browser.find_element_by_id("layui-layer-iframe4"))
            self.browser.implicitly_wait(5)
            #循环8次选择文章
            for i in range(1,7,1):

                file_name = "//table[@class=\"tb-all-articles table table-hover table-striped\"]/tbody/tr[%s]/td[2]/img" % i

                self.browser.find_element_by_xpath('%s' % file_name).click()
            time.sleep(2)
            self.browser.find_element_by_id("save").click()
            self.browser._switch_to.default_content()
            self.browser.switch_to.frame(self.browser.find_element_by_tag_name("iframe"))
            time.sleep(1)

            for i in range(7):

                self.browser.find_element_by_class_name("ps-scrollbar-y").send_keys(Keys.PAGE_DOWN)

            time.sleep(2)
            self.browser.find_element_by_id("wechat-send").click()
            time.sleep(0.5)
            send_result=self.browser.find_element_by_class_name("layui-layer-content").text
            text="发送成功"
            self.assertEqual(text,send_result, msg="失败的原因：%s != %s" %(text,send_result))
        except Exception as wechat_matter_msg:

            print(wechat_matter_msg)

            logger_message.logwarning(wechat_matter_msg)