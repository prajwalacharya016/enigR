from django.conf.urls import url
from mycomparison import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^comparison/(?P<comparison_id>[0-9]+)/$', views.comparison, name='comparison'),
]