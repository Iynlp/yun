#定义white_dreams的URL模式
from django.urls import path

from . import views

app_name = 'white_dreams'
urlpatterns = [
	#主页
	path('', views.index, name='index'),
	#所有主题的页面
	path('titles/', views.titles, name='titles'),
	#特定主题的页面
	path('titles/<int:title_id>/', views.title, name='title'),
	#添加主题的页面
	path('new_title/', views.new_title, name='new_title'),
	#添加内容的页面
	path('new_write/<int:title_id>/', views.new_write, name='new_write'),
]	
