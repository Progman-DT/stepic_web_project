from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
	title = forms.CharField(max_length=255)
	text = forms.CharField(widget=forms.Textarea)
	
	def clean_title(self):
		title = self.cleaned_data['title']
		if len(title) > 255:
			raise forms.ValidationError(u'Слишком длинный заголовок', code='Long_title')
		return title

	def save(self):
		question = Question(**self.cleaned_data)
		question.save()
		return question

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField()

	def clean_question(self):
		question = self.cleaned_data['question']
		return question
	
	def save(self):
		answer = Answer(**self.cleaned_data)
		answer.save()
		return answer

