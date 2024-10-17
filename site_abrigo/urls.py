from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("lista_animais/", views.lista_animais, name="lista_animais"),
    path('animal/<int:animal_id>/', views.detalhe_animal, name='detalhe_animal'),
    path("cadastro_pessoa/", views.cadastro_pessoa, name="cadastro_pessoa"),
    path("cadastro_animal/", views.cadastro_animal, name="cadastro_animal"),
    path("gestao_doacao/", views.gestao_doacao, name="gestao_doacao"),
    path("pesquisar_animais/", views.pesquisar_animais, name="pesquisar_animais"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)