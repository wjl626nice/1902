# !/user/bin/env python
# !-*-coding:utf-8 -*-
# !@lime: 2018/12/7 15:00
# !@Author: fox
# !@File: tools.py
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def listing(list, page, count):
    paginator = Paginator(list, count)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return contacts