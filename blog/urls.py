from django.urls import path, re_path

from . import views

app_name='blog'

urlpatterns = [
    path('', views.post_list_view, name='home'),
    path('create', views.post_create_view, name='create'),
    re_path(r'^post/(?P<slug>[\w-]+)/$', views.post_detail_view, name='post_detail'),
	re_path(r'^category/(?P<title>[\w-]+)/$', views.category_detail_view, name='category_detail'),

    

	

 ]