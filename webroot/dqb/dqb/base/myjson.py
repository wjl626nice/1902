from django.shortcuts import HttpResponse
from rest_framework.renderers import JSONRenderer

from base.errcode import err_number


class JSONResponse(HttpResponse):
    """
    用于返回JSON数据.
    """

    def __init__(self,code,data='',total=1,count=-1,**kwargs):
        kwargs['content_type'] = 'application/json'
        try:
            content = JSONRenderer().render(data)
            if code:
                content = '{"code":' \
                          + str(code) \
                          + ',"msg":"' \
                          + err_number[str(code)] \
                          + '","data":[]}'
            else:
                if count < 0:
                    content = '{"code":'\
                              +str(code)\
                              +',"msg":"'\
                              +err_number[str(code)]\
                              +'","total":'\
                              +str(total)\
                              +',"data":'\
                              +str(content,encoding="utf-8")\
                              +'}'
                else:
                    content = '{"code":' \
                              + str(code) \
                              + ',"msg":"' \
                              + err_number[str(code)] \
                              + '","total":' \
                              + str(total) \
                              + ',"count":' \
                              + str(count) \
                              + ',"data":' \
                              + str(content, encoding="utf-8") \
                              + '}'
        except:
            content = '{"code":' \
                      + '-1' \
                      + ',"msg":"返回有误","data":[]}'
        super(JSONResponse, self).__init__(content, **kwargs)