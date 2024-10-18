from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.utils import timezone


from .forms import FormCadastroDeAnimal, FormInserirImagem
from .models import CadastroAnimal, GaleriaImagem

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

    # Supondo que você queira exibir todas as imagem na pasta do animal
    imagem = []
    if animal.imagem:
        # Aqui, a URL das imagem deve ser construída com base na pasta do animal
        imagem.append(animal.imagem.url)  # Adiciona a imagem principal
        # Caso tenha outras imagem em subpastas, você pode listar as imagem que deseja
        # Essa parte depende de como você estruturou as subpastas e como as imagem são nomeadas

    # import pdb; pdb.set_trace()
    return render(request, 'detalhe_animal.html', {'animal': animal, 'imagem': imagem})



def cadastro_pessoa(request):
    return HttpResponse("<h1>ABRIGO DE ANIMAIS ! TESTE DE VIEW 'cadastro_pessoa'</h1>")


def cadastro_animal(request):
# Sempre inicialize os formulários
    form_animal = FormCadastroDeAnimal()
    form_imagem = FormInserirImagem()

    if request.method == 'POST':
        form_animal = FormCadastroDeAnimal(request.POST)
        form_imagem = FormInserirImagem(request.FILES)

        if form_animal.is_valid() and form_imagem.is_valid():
            # Salvar a data de criação formatada
            animal.data_criacao = timezone.now()

            # Adicionar o nome e a raça ao nome do arquivo de imagem
            if animal.imagem:
                # Novo nome do arquivo com o nome e raça do animal
                novo_nome_arquivo = f"{animal.nome}_{animal.data_criacao}.jpg"
                    
                # Renomear o arquivo antes de salvar
                animal.imagem.name = novo_nome_arquivo

            # Salvar o animal
            animal = form_animal.save()

            # Salvar a imagem associada ao animal
            imagem = form_imagem.save(commit=False)
            imagem.animal = animal  # Atribuindo o animal ao modelo de imagem
            imagem.save()

            # Define a variável de sucesso para exibir a mensagem no template
            sucesso = True

            contexto = {
                'form': form_animal,  # Reseta o formulário após o envio
                'form_imagem': form_imagem,
                'sucesso': sucesso  # Indica que o cadastro foi bem-sucedido
            }

            return render(request, "cadastro_animal.html", contexto)
        
        else:
            # Se o formulário não for válido, retorna com os erros
            return render(request, "cadastro_animal.html", {
                'form': form_animal,
                'form_imagem': form_imagem,
                'error': "Formulário inválido"
            })

    # Renderiza a página inicialmente ou se não houver POST
    return render(request, "cadastro_animal.html", {'form': form_animal, 'form_imagem': form_imagem})

           
 

def gestao_doacao(request):
    return HttpResponse("<h1>ABRIGO DE ANIMAIS ! TESTE DE VIEW 'gestao_doacao'</h1>")
