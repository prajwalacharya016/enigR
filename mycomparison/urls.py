from django.conf.urls import url, include
from mycomparison import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^comparison/(?P<comparison_id>[0-9]+)/$', views.comparison, name='comparison'),
    url(r'^comparison/login/$', views.login, name='locallogin'),

]
