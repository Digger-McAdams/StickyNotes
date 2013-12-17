from django.conf.urls import patterns,url
from Stickynotes import views

urlpatterns=patterns('',
	url(r'^$',views.index,name='index'),
	url(r'^month/$',views.month,name='month'),
)
