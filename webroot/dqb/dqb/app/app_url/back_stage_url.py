from django.urls import path
from app.controller.BackStageController import createAdmin,\
    setAdminPassword,\
    log_in,\
    log_out,\
    createFeedback,\
    getFeedbackAll,\
    upFeedbackState,\
    adminAll,\
    delete_admin,\
    resetPassword

app_name = 'back_stage'

urlpatterns = [
    # 创建用户
    path('create/',createAdmin),

    # 修改密码
    path('setPassword/',setAdminPassword),

    # 重置密码
    path('reset/',resetPassword),

    # 登录
    path('logIn/',log_in),

    # 退出
    path('logOut/',log_out),

    # 查询所有后台用户
    path('all/',adminAll),

    # 删除指定admin用户
    path('delete/',delete_admin),

    # 前端用户 创建意见反馈
    path('Feedback/',createFeedback),

    # 后台 查询意见反馈
    path('FeedbackAll/',getFeedbackAll),

    # 修改 意见反馈数据状态
    path('upFeedback/',upFeedbackState)
]
