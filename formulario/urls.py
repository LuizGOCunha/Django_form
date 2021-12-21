from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('revisao_de_dados/', views.revisao, name='revisao'),
]