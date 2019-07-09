from django.conf import settings

def auto_config(request):
    config ={
        'user': request.session.get('user'),
        'menu': settings.MENU
    }
    return config