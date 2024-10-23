from django.shortcuts import render


# Create your views here.

def cadastro_pessoa(request):
    
    return render (request, 'cadastro_pessoa.html')