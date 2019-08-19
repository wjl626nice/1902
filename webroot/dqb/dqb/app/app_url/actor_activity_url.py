from django.urls import path
from app.controller.ActorActivityController import \
    Activity_my_list,\
    Activity_signup,\
    Activity_delete,\
    recommend_activity,\
    myParticipatingActivity,\
    my_historical_act,\
    Act_sum,\
    act_user_sum,\
    act_user,\
    together_ball

app_name = "actor_activity"

urlpatterns = [
    path('activity_my_list/',Activity_my_list,name='activity_my_list'),
    path('my_participating/',myParticipatingActivity,name='myParticipatingActivity'),
    path('signup/',Activity_signup,name='activity_signup'),
    path('delete/',Activity_delete,name='activity_delete'),
    path('recommend/',recommend_activity,name='recommend_activity'),
    path('historical/',my_historical_act,name='my_historical_act'),
    path('sum/',Act_sum),
    path('user_sum/',act_user_sum),
    path('user/',act_user),
    path('together_ball/',together_ball),

]
