from django.urls import re_path
from groups import views

app_name = 'groups'

urlpatterns = [
    re_path(r'^$', views.ListGorupView.as_view(), name='all'),
    re_path(r'^new/$', views.CreateGroupView.as_view(), name='create'),
    re_path(r'^post/in/(?P<slug>[-\w]+)/$', views.SingleGroup.as_view(), name='single'),
]