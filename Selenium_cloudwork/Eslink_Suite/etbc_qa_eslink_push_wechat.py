#coding=utf-8
"""
Created on 2018-03-027
@author: sun
Project:微信推送
"""
import unittest
from selenium import webdriver
from Eslink_Case.Test_etbc_qa_push.Push_Message_Send.etbc_qa_push_message import *
from Eslink_Case.Test_etbc_qa_push.Push_Message_Send.etbc_qa_push_wechat import *


class push_wechat_case(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.option = webdriver.ChromeOptions()
        cls.option.add_argument('disable-infobars')
        cls.browser=webdriver.Chrome(chrome_options=cls.option)
        cls.browser.maximize_window()
        cls.browser.get(Constant_path().LOGIN_URL)

    def test_push_message(self):
        u"""短信推送"""

        is_url_title(self)

        login_user(self,u"zhangyang1",u"zj03030418")

        is_login_sucess(self)

        is_push_message(self)

        is_iframe_page(self)

        is_sender_object(self)

        is_tab_wechat_mobel(self)

        is_close_message_check(self)


    @classmethod
    def tearDownClass(cls):

        print('执行完成!')

        cls.browser.quit()

if __name__ == '__main__':
    unittest.main()