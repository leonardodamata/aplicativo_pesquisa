from  django.http import HttpResponse

def index(request):
  return HttpResponse("Alô, mundo. Você está no índice das pesquisas.")

# Create your views here.
