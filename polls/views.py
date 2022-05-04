from genericpath import exists
from multiprocessing import context
from re import template
from unittest import loader
from urllib import response
from  django.http import HttpResponse
from requests import request
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Question

def detail(request, question_id):
  return HttpResponse("Você está olhando para a pergunta %s." % question_id)

def results(request, question_id) :
  response = "Você está vendo os resultados da pergunta  %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("Você está votando na pergunta  %s." % question_id) 

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
  question = Question.objects.get(pk=question_id)
  return render(request,'polls/detail.html', {'question': question})  
