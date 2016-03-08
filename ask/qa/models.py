from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
	#slug = models.SlugField(unique=True)
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(blank=True, null=True)
	rating = models.IntegerField(null=True)
	author = models.CharField(max_length=255)
	likes = models.ManyToManyField(User)

	def __unicode__(self):
		return self.title

	def get_url(self):
		return reverse('show-question', kwargs={'slug': self.id})
		
	class Meta:
		db_table = 'question'

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(blank=True, null=True)
	question = models.ForeignKey(Question)
	author = models.CharField(max_length=255)
	
	class Meta:
		db_table = 'answer'
