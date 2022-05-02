from urllib import response
from  django.http import HttpResponse
from requests import request

def detail(request, questio_id):
  return HttpResponse("Você está olhando para a pergunta %s." % questio_id)

def results(request, question_id) :
  response = "Você está vendo os resultados da pergunta  %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("Você está votando na pergunta  %s." % question_id) 