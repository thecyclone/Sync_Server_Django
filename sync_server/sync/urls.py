from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'(?P<sec>\d+)$', views.index, name='index'),
]
