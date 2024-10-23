from django.urls import path
from django.conf import settings

from .views import *

app_name = 'app_usuarios'

urlpatterns = [
    path("cadastro_pessoa/", cadastro_pessoa, name="cadastro_pessoa"),
 
]
