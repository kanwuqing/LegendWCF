import orjson

def read_json(file: str, encoding: str='utf-8') -> object:
    '''快速读取设置方法
    
    Args:
        file: 读取文件路径
        encoding: 读取时所用的编码格式
    
    Return:
        object类型, 表示读取到的内容, json格式
    '''
    f = open(file, 'rb')
    res = orjson.loads(f.read())
    f.close()
    return res

def write_json(file: str, data, encoding: str='utf-8') -> None:
    '''快速读取设置方法
    
    Args:
        file: 写入文件路径
        data: 写入内容
        encoding: 写入时所用的编码格式
    '''
    f = open(file, 'wb')
    f.write(orjson.dumps(data))
    f.close()
