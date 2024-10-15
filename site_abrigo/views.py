from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse
from .forms import FormCadastroDeAnimal
from .models import CadastroAnimal

def home(request):
    # Buscar todos os animais cadastrados no banco de dados
    animais = CadastroAnimal.objects.all()
    
    # Renderizar o template com a lista de animais
    return render(request, 'home.html', context={'animais': animais})

def lista_animais(request):
    # Buscar todos os animais cadastrados no banco de dados
    animais = CadastroAnimal.objects.all()
    
    # Renderizar o template com a lista de animais
    return render(request, 'lista_animais.html', context={'animais': animais})

def detalhe_animal(request, animal_id):
    animal = get_object_or_404(CadastroAnimal, id=animal_id)

    # Supondo que você queira exibir todas as imagens na pasta do animal
    imagens = []
    if animal.imagens:
        # Aqui, a URL das imagens deve ser construída com base na pasta do animal
        imagens.append(animal.imagens.url)  # Adiciona a imagem principal
        # Caso tenha outras imagens em subpastas, você pode listar as imagens que deseja
        # Essa parte depende de como você estruturou as subpastas e como as imagens são nomeadas

    return render(request, 'detalhe_animal.html', {'animal': animal, 'imagens': imagens})

def cadastro_pessoa(request):
    return HttpResponse("<h1>ABRIGO DE ANIMAIS ! TESTE DE VIEW 'cadastro_pessoa'</h1>")

def cadastro_animal(request):
   form = FormCadastroDeAnimal()
   uploads = CadastroAnimal.objects.all()

   if request.method == "POST":
       form = FormCadastroDeAnimal(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect("home")
       else:
           # Feedback de erro (opcional)
           return render(request, "cadastro_animal.html", context={"form": form, "uploads": uploads, "error": "Formulário inválido"})

   return render(request, "cadastro_animal.html", context={"form": form, "uploads": uploads})

def gestao_doacao(request):
    return HttpResponse("<h1>ABRIGO DE ANIMAIS ! TESTE DE VIEW 'gestao_doacao'</h1>")
