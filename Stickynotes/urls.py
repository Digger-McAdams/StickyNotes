from django.conf.urls import patterns,url
from Stickynotes import views

urlpatterns=patterns('',
	url(r'^$',views.month,name='month'),
	url(r'^month/$',views.month,name='month'),
	url(r'^month/(\d+)/(\d+)/$', views.month,name='month'),
	url(r'^month/(\d+)/(\d+)/(prev|next)/$',views.month,name='month'),
	url(r'^add_entry/$',views.add_entry,name='add_entry'),
	url(r'^completed_entry/$',views.completed_entry,name='completed_entry'),
	url(r'^delete_entry/$',views.delete_entry,name="delete_entry"),
	url(r'^register/$',views.register,name="register"),
	url(r'^login/$',views.user_login,name="user_login"),
    	url(r'^logout/$',views.user_logout,name="user_logout"),
)
