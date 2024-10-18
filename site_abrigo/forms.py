from django import forms
from .models import CadastroAnimal, GaleriaImagem

class FormCadastroDeAnimal(forms.ModelForm):
    class Meta:
        model = CadastroAnimal
        fields = ['nome', 'idade', 'filhote', 'sexo', 'raca', 'especie', 'disponivel_para_adocao']
        labels = {
            'nome': 'Nome (apelido)',
            'idade': 'Idade (em anos)',
            'filhote': 'O bichinho é um filhote?',
            'sexo': 'Sexo',
            'raca': 'Raça',
            'especie': 'Espécie',
            'disponivel_para_adocao': 'Está disponível para adoção?',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', "required": True}),
            'idade': forms.TextInput(attrs={'class': 'form-control', "required": False}),
            'filhote': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
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

    def clean_nome_raca(self):
        """
        Limpa os dados para os campos 'nome' e 'raca', transformando-os em minúsculas
        e garantindo a consistência dos dados.
        """
        cleaned_data = super().clean()

        nome = cleaned_data.get('nome')
        raca = cleaned_data.get('raca')

        if nome:
            cleaned_data['nome'] = nome.lower()  # Converte o nome para minúsculas
        if raca:
            cleaned_data['raca'] = raca.lower()  # Converte a raça para minúsculas

        return cleaned_data
    
    
    def clean_idade(self):
        cleaned_data = super().clean()
        
        idade = self.cleaned_data.get('idade')

        if idade is None or idade == 0 :
            self.filhote = True

        return cleaned_data

    


class FormInserirImagem(forms.ModelForm):
    class Meta:
        model = GaleriaImagem
        fields = ['imagem']
        labels = {'imagem': 'Insira uma foto bem bonita do bichinho'}
        widgets = {
            'imagem': forms.ClearableFileInput
            (attrs={'class': 'form-control-file', 'onchange': 'previewImage(event)'})
        }
