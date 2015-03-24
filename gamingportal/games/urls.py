from django.conf.urls import patterns,url
from games import views

urlpatterns = patterns('',
	url(r'^register',views.register,name='register'),
	)

	
