from django.conf.urls import url
from . import views

app_name = 'delight'

urlpatterns = [
    # /delights/
    url(r'^$', views.delights, name="delights"),
]
