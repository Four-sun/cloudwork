
# from Utils.log import Logger
# logger_message=Logger()
# class log_server(unittest.TestCase):
#
#     def unnitest1(self):
#
#         log_message1="testcase1"
#         invokefuncName = sys._getframe().f_code.co_name
#         print(invokefuncName)
#         logger_message.loginfo('方法名：%s'%log_message1)
#     def unnitest2(self):
#
#         log_message2="testcase2"
#         print('test2')
#
#     def test1(self):
#
#         self.unnitest1()
#
# if  __name__=='__main__':
#     unittest.main()
# import inspect
# def get_current_function_name():
#     return inspect.stack()[1][3]
# class MyClass:
#     def function_one(self):
#         print( "%s.%s invoked"%(self.__class__.__name__, get_current_function_name()))
# if __name__ == "__main__":
#     myclass = MyClass()
#     myclass.function_one()