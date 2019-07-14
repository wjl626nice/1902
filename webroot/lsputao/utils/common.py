def get_json_error(msg, code):
    """
    返回一个错误的字典
    :param msg:
    :param code:
    :return:
    """
    return {
        "code": code
        , "msg": msg
        , "data": {}
    }
