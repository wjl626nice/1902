import base64
import os.path
import datetime
import time
import re


class MyFile(object):

    # 正常文件上传
    def mybase64(self, fils):
        bs_list = []
        path_list = []
        # 判断文件是否为空
        if fils:
            # 对多文件的防范处理
            for fil in fils:
                # 获取文件类型
                fil_type = fil.content_type
                # 获取文件后缀
                fil_suffix = os.path.splitext(fil.name)[1]
                # 文件目录存在跳过，不存在生成
                save_dir = ("static/"
                            + fil_type
                            + "/"
                            + re.sub('[-:. ]', '', str(datetime.datetime.now().date()))
                            )
                if os.path.exists(save_dir) is False:
                    os.makedirs(save_dir)
                # 生成base64编码
                bs = ["data:{0};base64,".format(fil_type), base64.b64encode(fil.read())]
                # 文件路径
                fil_path = (save_dir
                            + "/"
                            + str(int(time.time() * 10000000))
                            + fil_suffix)
                # 文件写到指定路径
                f = open(fil_path, "wb+")
                for chunk in fil.chunks():
                    f.write(chunk)
                f.close()
                path_list.append(fil_path)
                bs_list += bs
                if fils.index(fil) < (len(fils) - 1):
                    bs_list += '\n'
        return {'path_list': path_list}



    def Picture_download(self, file):
        lists = []
        if file:
            try:
                # 获取文件类型
                start = file.headers['content-type']
                # 获取文件名称
                img_name = eval(file.headers['content-disposition'].split('=')[1])
                # 获取时间戳
                timer = int(time.time() * 10000000)  # 文件名
                timed = str(datetime.datetime.now().date()).replace('-', '')  # 文件夹名
                # 获取上传文件后缀
                formater = os.path.splitext(img_name)[1]
                # 生成文件存放路径
                edit_file = 'static/qy{}/{}/'.format(formater, timed)
                # 如果路径不存在就生成该文件夹
                if not os.path.exists(edit_file):
                    os.makedirs(edit_file)
                filed = edit_file + '{}{}'.format(timer, formater)
                with open(filed, 'wb+') as f:
                    for chunk in file.iter_content(1024):
                        f.write(chunk)
                # 生成base64编码前缀
                st = 'data:{};base64,'.format(start)
                # 对上传文件进行base64编码
                encodestr = base64.b64encode(file.content)
                lists = [st, encodestr]
            except:
                filed = ''
            # 返回上传文件base64编码,文件路径
            return lists, filed
        else:
            filed = ''
            return lists, filed