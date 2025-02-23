from wcferry import Wcf
import logging

def sendMsg(wcf: Wcf, msg: str, receiver: str, aters: list | str = None) -> int:
    """ wcferry发送文本消息的优化

    Args:
        wcf: wcferry客户端
        msg: 消息字符串
        receiver: 接收人wxid或者群id
        at_list: 要@的wxid, @所有人则传入'all'即可, 有多个则传入列表(列表里不能出现all)

    Returns:
        int: 0 为成功，其他失败
    """

    # msg中不需要加@的人
    # 若传入aters, 则默认receiver是群id
    ats = ""
    at_str = ""

    if aters:
        if aters == 'all':
            ats = '@所有人'
            at_str = 'notify@all'
        else:
            for ater in aters:
                # 根据 wxid 查找群昵称, 空格不能删
                ats += f'@{wcf.get_alias_in_chatroom(ater, receiver)} '
                at_str += f'{ater},'

    at_str = at_str[:-1] if at_str.endswith(',') else ...

    if ats == "":
        logging.info(f'send text to {receiver}')
        return wcf.send_text(msg, receiver)
    else:
        logging.info(f'send text to {receiver}, at {aters}')
        return wcf.send_text(f"{ats} {msg}", receiver, at_str)