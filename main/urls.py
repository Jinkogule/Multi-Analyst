from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('analise_basica/', views.analise_basica, name='analise_basica'),
    path('gerar_insights/', views.gerar_insights, name='gerar_insights'),
]

