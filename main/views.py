from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from analise_apriori.apriori import carregar_dados, preprocessar_dados, gerar_regras_minimo
from analise_apriori.forms import UploadFileForm
from analise_apriori.utils import detectar_encoding, detectar_header
from io import StringIO
from openai_chat.chatgpt_service import generate_response

def index(request):
    if request.method == 'POST':
        return analise_basica(request)
    form = UploadFileForm()
    return render(request, 'main/index.html', {'form': form})

def analise_basica(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        try:
            csv_file = request.FILES['csv_file']
            csv_data = detectar_encoding(csv_file)
            csv_data_string_io = StringIO(csv_data)
        except UnicodeDecodeError as e:
            return HttpResponse(f'Erro ao decodificar o CSV: {str(e)}')
        
        try:
            raw_df = carregar_dados(csv_data_string_io)
            preprocessed_df = preprocessar_dados(raw_df)
        except pd.errors.ParserError as e:
            return HttpResponse(f'Erro ao carregar ou preprocessar os dados: {str(e)}')
        
        try:
            regras = gerar_regras_minimo(preprocessed_df)
            regras_html = [(df.to_html(), descricao) for df, descricao in regras]
        except ValueError as e:
            return HttpResponse(f'Erro ao gerar regras: {str(e)}')
        
        try:
            prompt = (
                f"Os dados a seguir foram obtidos através de um processamento utilizando o algoritmo apriori sobre uma base de dados:\n{regras_html}\n\n Quais são os principais padrões identificados nos dados?"
            )
            insights = generate_response(prompt)
        except Exception as e:
            return HttpResponse(f'Erro ao gerar insights: {str(e)}')
        
        return render(request, 'main/analise_basica.html', {'regras': regras_html, 'insights': insights})
    
    return HttpResponse(f'Formulário inválido: {form.errors}')

def analise_especifica(request):
    return HttpResponse('Teste')
