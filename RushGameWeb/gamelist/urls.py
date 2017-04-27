from django.conf.urls import url
from . import views


app_name = 'gamelist'

urlpatterns = [
	#/gamelist
    url(r'^$',views.index, name='index'),
    url(r'^game1/$',views.game1, name='game1'),
    #url(r'^scoreboard/$',views.scoreboard, name='scoreboard'),
    url(r'^game1/score/$',views.new_score,name='score-add'),
    url(r'^game1/(?P<username>\w+)/(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='score'),
    url(r'^game1/profile/$',views.profile_view,name='profile'),
    url(r'^game1/leaderboard/$',views.leaderboard,name='leaderboard'),
   
   ]