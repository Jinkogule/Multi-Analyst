from django.urls import path
from . import views
from .views import index
from openai_chat.views import chat_view

urlpatterns = [
    path('', index, name='index'),
    path('analise_basica/', views.analise_basica, name='analise_basica'),
    path('analise_especifica/', views.analise_especifica, name='analise_especifica'),
    path('chat/', chat_view, name='chat_view'),
]

