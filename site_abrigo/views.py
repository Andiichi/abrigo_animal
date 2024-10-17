from django.shortcuts import render, redirect,  get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.db.models import Q

from .forms import FormCadastroDeAnimal
from .models import CadastroAnimal


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
        query_clean = Q(Q(nome__icontains = pesquisa_query) | Q(raca__icontains = pesquisa_query))

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

def cadastro_animal(request):
    form = FormCadastroDeAnimal()
    uploads = CadastroAnimal.objects.all()

    if request.method == "POST":
        form = FormCadastroDeAnimal(request.POST, request.FILES)

        if form.is_valid():  # Valida se o formulário está correto
             
            animal = form.save(commit=False)  # Não salva ainda
           
            # Deixar os campos de nome e raça em minúsculo
            animal.nome = animal.nome.lower()
            animal.raca = animal.raca.lower()

            # Adicionar o nome e a raça ao nome do arquivo de imagem
            if animal.imagem:
                 # Novo nome do arquivo com o nome e raça do animal
                novo_nome_arquivo = f"{animal.nome}_{animal.raca}.jpg"
                
                # Renomear o arquivo antes de salvar
                animal.imagem.name = novo_nome_arquivo

                # Criar uma segunda imagem (opcional: pode ser uma versão editada)
                # Exemplo: redimensionar a imagem original para criar uma versão menor
                image = Image.open(animal.imagem)
                nova_imagem = image.resize((300, 300))  # Exemplo de redimensionamento

                # Salvar a nova imagem
                output = BytesIO()
                nova_imagem.save(output, format=image.format)
                output.seek(0)
                
                # Salvar a nova imagem no campo imagem do objeto
                animal.imagem.save(novo_nome_arquivo, ContentFile(output.read()), save=False)

            # Salvar a data de criação formatada
            animal.data_criacao = timezone.now().strftime('%d/%m/%Y')
            
            # Agora salva o objeto no banco
            animal.save()
            form.save()

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
