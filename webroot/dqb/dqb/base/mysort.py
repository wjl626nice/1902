import datetime

def my_sort(type):
    if type == '1':
        return 'activity_time'
    elif type == '-1':
        return '-activity_time'
    elif type == '2':
        return 'formater'
    elif type == '-2':
        return '-formater'
    else:
        return 'id'


def time_stamp(e):
    '''
    获取指定日期时间的 时间戳
    :param e: 指定日期格式的字符串,如:'2018-12-27'或'2018-12-27 18:30:00'
    :return: 时间戳
    '''
    t_list = e.split(' ')

    t_y = t_list[0].split('-')

    t1 = datetime.datetime(int(t_y[0]),int(t_y[1]),int(t_y[2]),0,0,0)
    t2 = datetime.datetime(int(t_y[0]),int(t_y[1]),int(t_y[2]),23,59,59)
    t0 = datetime.datetime(1970,1,1,8,0,0)

    t_star = (t1 - t0).total_seconds()
    t_end = (t2 - t0).total_seconds()
    print(t_star,'--',t_end)

    return {'star':str(int(t_star)),'end':str(int(t_end))}

if __name__ == '__main__':
    print(time_stamp('2018-12-27'))