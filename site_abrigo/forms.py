from django import forms
from .models import CadastroAnimal

class FormCadastroDeAnimal(forms.ModelForm):
   class Meta:
       model = CadastroAnimal
       fields = "__all__"