from django.conf.urls import include, url
from . import views

app_name = 'game'

urlpatterns = [
	#/game
    url(r'^$',views.index, name='index'),
    url(r'^register/$',views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.UserLoginView.as_view(), name='login'),
    url(r'^logout/$',views.logout_view, name="logout"),
    url(r'^gamelist/',include('gamelist.urls', namespace='gamelist')),
    ]
