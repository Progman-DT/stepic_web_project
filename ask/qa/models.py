from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
	slug = models.SlugField(unique=True)
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	rating = models.IntegerField()
	author = models.CharField(max_length=255)
	likes = models.ManyToManyField(User)

	def __unicode__(self):
		return self.title

	def get_url(self):
		return reverse('qa:show-question', kwargs={'slug': self.slug})
		
	class Meta:
		db_table = 'question'

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	question = models.ForeignKey(Question)
	author = models.CharField(max_length=255)
	
	class Meta:
		db_table = 'answer'
