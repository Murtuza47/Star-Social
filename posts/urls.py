from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^$',  views.PostListView.as_view(), name='all'),
    re_path(r'new/$', views.CreatePostView.as_view(), name='create'),
    re_path(r'by/(?P<username>[-\w]+)', views.UserPosts.as_view(), name='for_user'),
    re_path(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.UserPosts.as_view(), name='single'),
    re_path(r'delete/(?P<pk>\d+)/$', views.DeletePostView.as_view(), name='delete')
]