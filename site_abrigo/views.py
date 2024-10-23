from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.utils import timezone
from django.db.models import Q
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .forms import FormCadastroAnimal
from .models import GaleriaAnimal, CadastroAnimal


def home(request):
    # Buscar todos os animais cadastrados no banco de dados
    animais = CadastroAnimal.objects.all()
    
    # Renderizar o template com a lista de animais
    return render(request, 'home.html', context={'animais': animais})


def lista_animais(request):
    # Buscar todos os animais cadastrados no banco de dados disponivel para adoção
    animais = CadastroAnimal.objects.filter(disponivel_para_adocao = True)

    # animais = CadastroAnimal.objects.all()

    # Renderizar o template com a lista de animais
    return render(request, 'lista_animais.html', context={'animais': animais})


def pesquisar_animais(request):
    if 'pesquisa_query' in request.GET:
        pesquisa_query = request.GET['pesquisa_query']

        #fazendo pessquisa com multiplas palavra chaves e campos
        query_clean = Q(Q(nome___unaccent__icontains = pesquisa_query) | Q(raca___unaccent__icontains = pesquisa_query))

        animais = CadastroAnimal.objects.filter(query_clean)

        #fazendo pesquisa só de um campo
        # animais = CadastroAnimal.objects.filter(nome__icontains = pesquisa_query)
        
        return render(request, 'pesquisar_animais.html', {'pesquisa_query':pesquisa_query , 'animais': animais})
    
    else:
        return render(request, 'pesquisar_animais.html', {})



def detalhe_animal(request, animal_id):
    animal = get_object_or_404(CadastroAnimal, id=animal_id)

    # Supondo que você queira exibir todas as imagem na pasta do animal
    imagem = []
    if animal.imagem:
        # Aqui, a URL das imagem deve ser construída com base na pasta do animal
        imagem.append(animal.imagem.url)  # Adiciona a imagem principal
        # Caso tenha outras imagem em subpastas, você pode listar as imagem que deseja
        # Essa parte depende de como você estruturou as subpastas e como as imagem são nomeadas
        

    return render(request, 'detalhe_animal.html', {'animal': animal, 'imagem': imagem})

def cadastro_pessoa(request):
    return HttpResponse("<h1>ABRIGO DE ANIMAIS ! TESTE DE VIEW 'cadastro_pessoa'</h1>")


def gestao_doacao(request):
    return HttpResponse("<h1>ABRIGO DE ANIMAIS ! TESTE DE VIEW 'gestao_doacao'</h1>")



def cadastro_animal(request):
    if request.method == 'POST':
        form_animal = FormCadastroAnimal(request.POST, request.FILES)
        animal_imagem = request.FILES.getlist('animal_imagem')

        if form_animal.is_valid():
            animal = form_animal.save(commit=False)  # Não salva ainda

           # Deixar os campos de nome e raça em minúsculo
            animal.nome = animal.nome.lower()
            animal.save()  # Salve o animal primeiro para gerar o ID

            # Salvar a data de criação
            data_criacao = timezone.now()
            data_formatada = data_criacao.strftime('%Y%m%d')  # Formato: YYYYMMDD

            # Criar o caminho da nova pasta
            nome_pasta = f"{animal.nome}"
            caminho_pasta = os.path.join(settings.MEDIA_ROOT, 'galeria', nome_pasta)
            os.makedirs(caminho_pasta, exist_ok=True)  # Cria a pasta se não existir

             # Salva as imagens
            for i, imagem in enumerate(animal_imagem):
                # Novo nome do arquivo com o nome do animal e data de criação (e índice para evitar conflito)
                novo_nome_arquivo = f"{animal.nome}_{data_formatada}_{i+1}.jpg"

                # Cria uma instância de FileSystemStorage para salvar no caminho da nova pasta
                fs = FileSystemStorage(location=caminho_pasta)

                # Salva a imagem no novo diretório com o nome ajustado
                caminho_imagem_salva = fs.save(novo_nome_arquivo, imagem)

                # Salva a referência da imagem no banco de dados
                GaleriaAnimal.objects.create(
                    animal=animal, 
                    imagem=os.path.join('galeria', nome_pasta, novo_nome_arquivo)
                )

            # Define sucesso como True
            contexto = {
                'form_animal': FormCadastroAnimal(),  # Reseta o formulário após o envio
                'sucesso': True
            }
            return render(request, 'cadastro_pet.html', contexto)
        else:
            contexto = {
                'form_animal': form_animal,
                'error': 'Erro ao cadastrar animal. Verifique os dados informados.'
            }
            return render(request, 'cadastro_pet.html', contexto)
    
    else:
        form_animal = FormCadastroAnimal()
        return render(request, 'cadastro_pet.html', {'form_animal': form_animal})

                                                             



