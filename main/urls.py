from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('analise_basica/', views.analise_basica, name='analise_basica'),
    path('analise_especifica/', views.analise_especifica, name='analise_especifica'),
]

