# -*- coding: utf-8 -*-
"""
Created on 2018-03-15
@author: sun
Project:新增渠道模版
"""
from Eslink_Case.Test_etbc_qa_push.Push_Message_Send.etbc_qa_push_message import *
from Eslink_Case.Test_etbc_qa_push.Push_Record.etbc_qa_push_record import is_search_push_record
from Eslink_Case.Test_etbc_qa_push.Channel_Template.Add_Channel_Template import *
import unittest
from selenium import webdriver


class Push_Channel_template(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.option = webdriver.ChromeOptions()
        cls.option.add_argument('disable-infobars')
        cls.browser=webdriver.Chrome(chrome_options=cls.option)
        cls.browser.maximize_window()
        cls.browser.get("http://etbc-qa.eslink.net.cn/")

    def test_add_channel_template(self):

        u"""新增短信渠道模版"""

        is_url_title(self)

        login_user(self,u"zhangyang1",u"zj03030418")

        is_login_sucess(self)

        is_channel_template(self)

        is_iframe_page(self)

        is_add_channel_template(self)

    @classmethod
    def tearDownClass(cls):

        print('执行完成!')

        cls.browser.quit()

if __name__ == '__main__':
    unittest.main()
