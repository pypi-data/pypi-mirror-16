Shows the online users in the system using django.

You need just insert this app on INSTALLED_APPS. When you run the command:
python manage.py runserver, this app you print on shell the count of users and
your names.

You can get a queryset of online users using get_current_users()
