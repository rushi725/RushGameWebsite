from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.
class Scoreboard(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	score = models.IntegerField()
	enemyKilled = models.IntegerField()
	upgradeCount = models.IntegerField()

	def get_absolute_url(self):
		return reverse('gamelist:score',kwargs={'pk':self.pk})

	def __str__(self):
		return self.user.username 

	#def get_absolute_url(self):
		#return reverse('gamelist:scoreboard',kwargs={'pk':self.pk})

