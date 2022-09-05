from django.shortcuts import render


# Create your views here.

''' def token(token_request):
    return HttpResponse('Togen has been gotten')

def token(token_request):
    return HttpResponse('Togen has been gotten')

def token(token_request):
    return HttpResponse('Togen has been gotten') '''

def login(request):
    return render(request, 'login.html')