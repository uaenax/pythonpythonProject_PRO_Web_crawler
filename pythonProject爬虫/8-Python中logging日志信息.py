# 导入模块
import logging

# 设置日志等级和输出日志格式
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s"- %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# 输出日志信息到终端
logging.debug('这是一个debug级别的日志')
logging.info('这是一个info级别的日志')
logging.warning('这是一个warning级别的日志')
logging.error('这是一个error级别的日志')
logging.critical('这是一个critical级别的日志')