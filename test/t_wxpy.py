# coding=utf-8
__author__ = 'wanglu'

from wxpy import get_wechat_logger

# 获得 Logger
logger = get_wechat_logger()

# 发送警告
logger.warning('这是一条 WARNING 等级的日志！')

# 捕获可能发生的异常，并发送
try:
    1 / 0
except:
    logger.exception('又出错啦！')

