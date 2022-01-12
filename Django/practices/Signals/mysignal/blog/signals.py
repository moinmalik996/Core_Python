from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("-----------------------------")
    print("-------Logged-in Signal------")
    print("Sender  :  ", sender)
    print("Request :  ", request)
    print("User    :  ", user)
    print(f"Kwargs :  {kwargs}")
    
    
# user_logged_in.connect(login_success, sender=User)


@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):
    print("-----------------------------")
    print("-------Logged-Out Signal------")
    print("Sender  :  ", sender)
    print("Request :  ", request)
    print("User    :  ", user)
    print(f"Kwargs :  {kwargs}")
    
    
# user_logged_out.connect(logout_success, sender=User)
    
    
#----------------------------------------------------------------------------//

@receiver(pre_save, sender=User)
def at_beggining_save(sender, instance, **kwargs):
    print("-----------------------------")
    print("-------Pre_Save Signal------")
    print("Sender  :  ", sender)
    print("Instance :  ", instance)
    print(f"Kwargs :  {kwargs}")    
    
    
@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    
    if created:
        print("-----------------------------")
        print("-------Post_Save Signal------")
        print("-------New Record Created------")
        print("Sender  :  ", sender)
        print("Created  :  ", created)
        print("Instance :  ", instance)
        print(f"Kwargs :  {kwargs}")
    else:
        print("-----------------------------")
        print("-------Post_Save Signal------")
        print("-------Update Record------")
        print("Sender  :  ", sender)
        print("Created  :  ", created)
        print("Instance :  ", instance)
        print(f"Kwargs :  {kwargs}")