from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from analise_apriori.apriori import carregar_dados, preprocessar_dados, gerar_regras_minimo
from analise_apriori.forms import UploadFileForm
from analise_apriori.utils import detectar_encoding
from io import StringIO

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
            dados = StringIO(csv_data)
        except UnicodeDecodeError as e:
            return HttpResponse(f'Erro ao decodificar o CSV: {str(e)}')
        try:
            dados_string = carregar_dados(dados)
            df = preprocessar_dados(dados_string)
        except pd.errors.ParserError as e:
            return HttpResponse(f'Erro ao carregar ou preprocessar os dados: {str(e)}')

        try:
            regras = gerar_regras_minimo(df)
            regras_html = [(df.to_html(), descricao) for df, descricao in regras]
        except ValueError as e:
            return HttpResponse(f'Erro ao gerar regras: {str(e)}')

        return render(request, 'main/analise_basica.html', {'regras': regras_html})
    
    return HttpResponse(f'Formulário inválido: {form.errors}')

def analise_especifica(request):
    return HttpResponse('Teste')
