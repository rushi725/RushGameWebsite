from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.template import loader
from django.contrib.auth import authenticate
from django.views.generic import View
from django.views import generic
from django.db.models import F, Count
from django.db.models import Max, Avg
from .models import Scoreboard
from .forms import ScoreForm
#import sqlite3
form = ScoreForm()

def index(request):
	template = loader.get_template('gamelist/index.html')
	return render(request,'gamelist/index.html')

def game1(request):
    template = loader.get_template('gamelist/game1.html')
    return render(request,'gamelist/game1.html',{'form': form})

def profile_view(request):
    score = Scoreboard.objects.filter(user__username=request.user).annotate(tscore= F('score') + 100 * F('enemyKilled')).order_by('-tscore')

    count = Scoreboard.objects.filter(user__username=request.user).count()

    #maxi = Scoreboard.objects.filter(user__username=request.user).aggregate(Avg('tscore'))

    return render(request, "gamelist/profile.html", {'all_score' : score ,'count': count})

def leaderboard(request):
    return render(request,"gamelist/scoreboard.html")


class DetailView(generic.DetailView):
    model = Scoreboard
    template_name = 'gamelist/score.html'


def new_score(request):

    if request.method == "POST":
        forma = ScoreForm(request.POST)
        if forma.is_valid():
            post = forma.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('gamelist:score',username=post.user.username,pk=post.pk)
    else: 
        print("Hi")


    return render(request, 'gamelist/game1.html', {'form': forma})



