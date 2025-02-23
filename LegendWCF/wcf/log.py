import logging.config
from ..data.yaml_ import read_yaml
import os

def SetLegendLogging():
    '''设置logger

    煮啵煮啵, 你的方法还是太吃操作了, 有没有什么简单又强势的写法吗?
    
    ——**有的兄弟,有的**, 这样的写法一共有9种
    '''

    logging_yaml = read_yaml("legendwcf\wcf\logging.yaml")
    handlers = logging_yaml['handlers']
    for key, value in handlers.items():
        if 'filename' in value:
            log_path = (os.path.split(value['filename'])[0])
            if not os.path.exists(log_path):
                os.makedirs(log_path)
    # 配置logging日志：主要从文件中读取handler的配置、formatter（格式化日志样式）、logger记录器的配置
    logging.config.dictConfig(config=logging_yaml)
    ###设置完毕###
    # 获取根记录器：配置信息从yaml文件中获取
    root = logging.getLogger()
    print("rootlogger:", root.handlers)