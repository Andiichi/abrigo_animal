from django import forms

from .models import CadastroAnimal, GaleriaImagem

class FormCadastroDeAnimal(forms.ModelForm):
    class Meta:
        model = CadastroAnimal
        fields = ['nome', 'idade','sexo','raca', 'especie', 'disponivel_para_adocao']
        labels = {
            'nome': 'Nome (apelido)',  # Alterando a label do campo 'nome'
            'idade': 'Idade (em anos)',  # Alterando a label do campo 'idade'
            'sexo': 'Sexo',
            'raca': 'Raça',
            'especie': 'Espécie',
            'disponivel_para_adocao': 'Está disponível para adoção?',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', "required": True}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control', 'required': True}, 
                choices=[
                ('macho', 'Macho'),
                ('femea', 'Fêmea'),
            ]),
            'especie': forms.Select(attrs={'class': 'form-control', 'required': True}, 
                choices=[
                ('gato', 'Gato'),
                ('cachorro', 'Cachorro'),
                ('outros', 'Outros'),
            ]),
            'raca': forms.TextInput(attrs={'class': 'form-control'}),
            'disponivel_para_adocao': forms.CheckboxInput(attrs={'class': 'form-check-input', "required": True}),

        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        return nome.lower()  # Convertendo o nome para minúsculas

    def clean_raca(self):
        raca = self.cleaned_data.get('raca')
        return raca.lower()  # Convertendo a raça para minúsculas


class FormInserirImagem(forms.ModelForm):
    class Meta:
        model = GaleriaImagem
        fields = ['imagem']  # Define quais campos incluir no formulário
        label = {'imagem': 'Insira uma foto bem bonita do bichinho'}
        widgets = {'imagem': forms.ClearableFileInput(
            attrs={'class': 'form-control-file', 'onchange': 'previewImage(event)'})}