"""dqb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from app.app_url import member_url,\
    activity_url,\
    actor_activity_url,\
    group_url,\
    message_url,\
    news_url,\
    replay_url,\
    put_forward_url,\
    recharge_url,\
    back_stage_url

from apscheduler.schedulers.blocking import BlockingScheduler
from app.controller.ActorActivityController import Activity_over

# schedule = BlockingScheduler()  # 实例化，固定格式
# schedule.add_job(func=Activity_over, trigger='interval', seconds=600)
# schedule.start()

urlpatterns = [
    path('activity/', include(activity_url, namespace='activity')),
    path('actor_activity/', include(actor_activity_url, namespace='actor_activity')),
    path('group/', include(group_url, namespace='group')),
    path('message/', include(message_url, namespace='message')),
    path('news/', include(news_url, namespace='news')),
    path('reply/', include(replay_url, namespace='reolay')),
    path('member/', include(member_url, namespace='member')),
    path('put_forward/', include(put_forward_url, namespace='put_forward')),
    path('recharge/', include(recharge_url, namespace='recharge')),
    path('admin/',include(back_stage_url,namespace='back_stage')),
]
