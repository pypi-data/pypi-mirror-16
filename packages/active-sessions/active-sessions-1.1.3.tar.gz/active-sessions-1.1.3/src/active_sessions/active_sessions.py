from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.core.signals import request_finished
from django.dispatch import receiver
from django.utils import timezone
import active_sessions

def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    return User.objects.filter(id__in=user_id_list)


@receiver(request_finished)
def show_sessions(sender, **kwargs):
    queryset = get_current_users()
    print("Active sessions: ", queryset.count())
    for user in queryset:
        print("Usuário: (", user, ") Last login: ", user.last_login)

