"""
WSGI config for py1902 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
# 接收apache发送的http请求，并且启动django,把请求信息给django
import os
import sys
from django.core.wsgi import get_wsgi_application
# os.path.dirname(/user/local/111.py)  ： /user/local/
# __file__当前文件的物理路径  os.path.dirname(__file__)

# 把当前项目的物理路径加入到python   模块路径列表（sys.path）中
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'py1902.settings')



application = get_wsgi_application()
