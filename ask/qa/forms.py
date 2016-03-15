from django import forms
from qa.models import *

class AskForm(forms.Form):
	title = forms.CharField(max_length=255)
	text = forms.CharField(widget=forms.Textarea)
	
	def __init__(self, user, **kwargs):
		self._user = user
		super(AskForm, self).__init__(**kwargs)

	def clean_title(self):
		title = self.cleaned_data['title']
		if len(title) > 255:
			raise forms.ValidationError('Title field is too long', code='Long_title')
		return title

	def save(self):
		self.cleaned_data['author'] = self._user
		return Question.objects.create(**self.cleaned_data) 

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField()

	def __init__(self, user, **kwargs):
		self._user = user
		super(AnswerForm, self).__init__(**kwargs)

	def clean_question(self):
		question = self.cleaned_data['question']
		if False:
			raise forms.ValidationError('Hello', code='1234')
		return question
	
	def save(self):
		self.cleaned_data['author'] = self._user
		return Answer.objects.create(**self.cleaned_data) 

class LoginForm(forms.Form):
	username = forms.CharField(max_length=64)
	password = forms.CharField(max_length=32, widget=forms.PasswordInput) 

	def clean_username(self):
		if len(username) > 64:
			raise forms.ValidationError('Username is too long', code='Long_name')
		return username

class SignupForm(forms.Form):
	username = forms.CharField(max_length=64)
	email = forms.EmailField()
	password = forms.CharField(max_length=32, widget=forms.PasswordInput) 
	
	def clean_username(self):
		if len(username) > 64:
			raise forms.ValidationError('Username is too long', code='Long_name')
		return username

	def save(self):
		return User.objects.create_user(**self.cleaned_data)

