# -*- coding: utf-8 -*-
'''
Created on 2018-03-01
@author: sun
Project: log/log.py
'''
import logging,os,re,time
import logging.handlers
from logging.handlers import TimedRotatingFileHandler
now=time.strftime("%Y-%m-%d",time.localtime(time.time()))  #获取当前时间
cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
report_path = os.path.join(cur_path, "Log"+"\\")


class Logger:
    log_fmt = '%(asctime)-12s\tline %(lineno)-8s \t%(levelname)-12s: %(message)-12s'
    formatter = logging.Formatter(log_fmt)
    log_file_handler = TimedRotatingFileHandler(filename=report_path+now+"_Test", when="D", interval=1, backupCount=7,encoding="UTF-8")
    log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
    log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)
    console = logging.StreamHandler()
    formatter1 = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter1)                # 屏幕输出日志
    logger = logging.getLogger()
    logger.addHandler(log_file_handler)             # 为logger添加handler
    logger.setLevel(logging.INFO)                   #打印日志级别INFO
    console.setLevel(logging.INFO)
    logging.getLogger('').addHandler(console)

    def loginfo(self, message):
        self.logger.info(message)

    def logdebug(self, message):
        self.logger.debug(message)

    def logwarning(self,message):
        self.logger.warning(message)

    def logerror(self,message):
        self.logger.warning(message)
