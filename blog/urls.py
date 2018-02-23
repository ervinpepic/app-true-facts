from django.urls import path, re_path

from . import views

app_name='blog'

urlpatterns = [
	
    path('', views.post_list_view, name='home'),
    path('<title>', views.category_detail_view, name='category_detail'),
    path('create', views.post_create_view, name='create'),
    path('<slug>', views.post_detail_view, name='detail'),

	

 ]