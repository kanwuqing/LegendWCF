import jieba
import jieba.posseg
import logging
import re

class LegendJieba:
    def __init__(self, userdict: str = None) -> None:
        '''Legend微信机器人的自然语言处理模块

        用户字典格式参照jieba模块的要求

        Args
            userdict: 用户字典(txt文件为宜)路径
        '''

        if userdict:
            jieba.load_userdict(userdict)
            logging.info('用户词典加载成功')
        
        logging.info('jieba分词初始化完成')

    def strtime(self, text):
        '''自然语言时间转成标准格式时间

        Args:
            text: 仅保证'(年)月日时(分)的处理结果

        Returns:
            两个str, 分别是转换后的年月日与时间(不包含日期则第一个返回值为None)
        '''
        text = text.replace("年", "-").replace("月", "-").replace("日", " ").replace("号", "").replace("/", "-").replace("点", ":").replace('时', ':').replace('分', '').strip()
        text = re.sub(r"\s+", " ", text)
        t = ""
        regex = r"(\d{1,2}:\d{1,2})"
        t =  re.search(regex, text)
        t = t.group(1) if t else None

        regex_list = [
            r"(\d{4}-\d{1,2}-\d{1,2})",
            r"(\d{1,2}-\d{1,2})"
        ]
        for regex in regex_list:
            d =  re.search(regex, text)
            if d:
                d = d.group(1)
                return d, t
        else:
            return None, t
    