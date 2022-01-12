from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in,)
def login_success(sender, request, user, **kwargs):
    print("-------------------------")
    print("-----Logged In Signal----")
    ip = request.META.get('REMOTE_ADDR')
    print("Client IP : ", ip)
    request.session['ip'] = ip