from django import forms

from .models import Scoreboard

class ScoreForm(forms.ModelForm):

    class Meta:
        model = Scoreboard
        fields = ['score', 'enemyKilled','upgradeCount']