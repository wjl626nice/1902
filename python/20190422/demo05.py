#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys

# 把用户输入的命令执行
print(' '.join(sys.argv[1:]))

os.system(' '.join(sys.argv[1:]))