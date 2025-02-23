def get_key(d: dict, value, idx = 0):
    '''获取字典中第idx个值为value的键'''
    res = []
    for k, v in d.items():
        if v == value:
            res.append(k)
    if len(res) == 0:
        return None
    try:
        return res[idx]
    except IndexError:
        return res[0]

def get_keys(d: dict, value):
    '''获取字典中所有值为value的键'''
    res = []
    for k, v in d.items():
        if v == value:
            res.append(k)
    if len(res) == 0:
        return None
    return res

def count_key(d: dict, value):
    '''获取字典中值为value的键的个数'''
    res = []
    for k, v in d.items():
        if v == value:
            res.append(k)
    return len(res)