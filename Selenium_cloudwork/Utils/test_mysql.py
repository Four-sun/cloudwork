import unittest

from Utils.test_db import MySQL


class case(unittest.TestCase):

    def test_judge_data(self):

        database = MySQL()
        # sql = "SELECT id, article_time, article_id, article_url, title FROM article_name WHERE article_id=\'2031\'"
        sql = "SELECT receiveObject,messageContent,sendTime FROM push_message_sms WHERE ownership =\'0185\' AND objectDescription =\'18858271978\' GROUP BY sendTime DESC LIMIT 1"
        # print(sql)
        result = database.query(sql)
        # print(result)
        ReceiveObject =result[0][0]
        messageContent =result[0][1]
        sendTime =result[0][2]
        print ("ReceiveObject=%s,messageContent=%s,sendTime=%s " % \
            (ReceiveObject,messageContent,sendTime, ))
        print(messageContent)

    # def test_check_template(self):
    #     u'''检查模版是否存在'''
    #     try:
    #         Filename="D:\\pycharm-5.0.4\\Selenium_unittest\\Data\\push_template.csv"
    #         template_message=csv_search.csv_test(filename=Filename,indexs=2)
    #         database=MySQL()
    #         template = template_message[5]
    #         template_name=template_message[1]
    #         sql="Select * FROM push_channelmessagetemplate WHERE `code` = '%s' AND name = '%s';" % (template,template_name)
    #         print(sql)
    #
    #         result=database.query(sql)
    #         print(result)
    #         if  len(result) == 1:
    #             print('存在模版:%s'%template_name)
    #             sql="DELETE FROM push_channelmessagetemplate WHERE `code` = '%s';" % template
    #             result=database.query(sql)
    #         else:
    #             print('不存在模版:%s'%template_name)
    #
    #     except Exception as Error:
    #
    #         print(Error)

if __name__ == "__main__":
    unittest.main()
