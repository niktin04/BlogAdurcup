from django.conf.urls import url
from . import views

app_name = 'mailers'

urlpatterns = [
    # /mailers/
    url(r'^$', views.mailers_form, name="update_mailers_form"),

    # /mailers/<mailer_id>
    url(r'^(?P<mailer_id>[0-9]+)$', views.mailer_check, name="mailer_check"),
]
