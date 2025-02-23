import yaml

def read_yaml(file: str) -> object:
    '''快速读取设置方法
    
    Args:
        file: 读取文件路径
        encoding: 读取时所用的编码格式
    
    Return:
        object类型, 表示读取到的内容, json格式
    '''
    with open(file, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data

def write_yaml(file: str, data) -> None:
    '''快速读取设置方法
    
    Args:
        file: 写入文件路径
        data: 写入内容
        encoding: 写入时所用的编码格式
    '''
    with open(file, 'w', encoding='utf-8') as file:
        yaml.dump(data, file)