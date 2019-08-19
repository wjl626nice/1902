from django.urls import path
from app.controller.ActivityController import Activity_info,\
    Activity_create,\
    Activity_up,\
    Activity_delete,\
    Activity_org_list,\
    file,\
    Activity_filter,\
    Activity_org_sum

app_name = "activity"

urlpatterns = [
    path('info/',Activity_info,name='activity'),
    path('create/',Activity_create),
    path('up/',Activity_up),
    path('delete/',Activity_delete),
    path('org_list/',Activity_org_list),
    path('file/',file),
    path('filter/',Activity_filter),
    path('org_sum/',Activity_org_sum)
]
