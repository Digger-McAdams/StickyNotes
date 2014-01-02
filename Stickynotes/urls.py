from django.conf.urls import patterns,url
from Stickynotes import views

urlpatterns=patterns('',
	url(r'^$',views.month,name='month'),
	url(r'^month/$',views.month,name='month'),
	url(r'^month/(\d+)/(\d+)/$', views.month,name='month'),
	url(r'^month/(\d+)/(\d+)/(prev|next)/$',views.month,name='month'),
)
