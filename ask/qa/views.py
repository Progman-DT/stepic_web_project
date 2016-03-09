from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import Http404
from django.http import HttpResponseRedirect
from qa.models import Question, Answer
from qa.forms import *

# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def list_qw(request):
	questions = Question.objects.all()
	questions = questions.order_by('-id')
	limit = request.GET.get('limit', 10);
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/?page='
	page = paginator.page(page)
	return render(request, 'qa/list_qw.html', {
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
	})

def list_popular(request):
	questions = Question.objects.all()
	questions = questions.order_by('-rating')
	limit = request.GET.get('limit', 10);
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/popular/?page='
	page = paginator.page(page)
	return render(request, 'qa/list_popular.html', {
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
	})

@require_GET
def show_question(request, slug):
	question = get_object_or_404(Question, id=slug)
	#answers = Answer.objects.filter(question=question)
	answers = question.answer_set.all()
	answers = answers.order_by('-added_at')
	if request.method == "GET":
		form = AnswerForm()
	return render(request, 'qa/show_question.html', {
		'question': question,
		'answers': answers,
		'form': form,
	})

def post_question(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		if form.is_valid():
			question = form.save()
			url = question.get_url()
			return HttpResponseRedirect(url)
	else:
		form = AskForm()
	return render(request, 'qa/post_question.html', {
		'form': form,
	})

@require_POST
def post_answer(request):
	#if request.method == "POST":
		form = AnswerForm(request.POST):
		if form.is_valid():
			answer = form.save()
			url = answer.question.get_url()
			return HttpResponseRedirect(url)




