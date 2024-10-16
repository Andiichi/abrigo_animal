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
        if form.is_valid():  # Valida se o formulário está correto
            form.save()  # Salva o novo animal no banco de dados
            # Define a variável de sucesso para exibir a mensagem no template
            sucesso = True
            contexto = {
                'form': FormCadastroDeAnimal(),  # Reseta o formulário após o envio
                'uploads': uploads,
                'sucesso': sucesso  # Indica que o cadastro foi bem-sucedido
            }
            return render(request, "cadastro_animal.html", contexto)
        else:
            # Se o formulário não for válido, retorna com os erros
            return render(request, "cadastro_animal.html", {
                'form': form,
                'uploads': uploads,
                'error': "Formulário inválido"
            })

    # Renderiza a página inicialmente ou se não houver POST
    return render(request, "cadastro_animal.html", {'form': form, 'uploads': uploads})

def gestao_doacao(request):
    return HttpResponse("<h1>ABRIGO DE ANIMAIS ! TESTE DE VIEW 'gestao_doacao'</h1>")
