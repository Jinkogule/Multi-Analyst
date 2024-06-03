from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from analise_apriori.apriori import carregar_dados, preprocessar_dados, gerar_regras_minimo #obter_colunas
from io import StringIO
from analise_apriori.forms import UploadFileForm
import chardet

def index(request):
    if request.method == 'POST':
        return analise_basica(request)
    else:
        form = UploadFileForm()
        return render(request, 'main/index.html', {'form': form})
    
def analise_basica(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        try:
            try:
                csv_file = request.FILES['file'].read().decode('utf-8')
            except:
                rawdata = request.FILES['file'].read()
                result = chardet.detect(rawdata)
                encoding = result['encoding']
                if encoding is None:
                    encoding = 'iso-8859-1'
                csv_file = rawdata.decode(encoding)
            dados = StringIO(csv_file)
            """colunas = obter_colunas(csv_file)"""
        except UnicodeDecodeError as e:
            return HttpResponse(f'Erro ao decodificar o CSV: {str(e)}')
        try:
            dados_string = carregar_dados(dados)
            df = preprocessar_dados(dados_string)
        except pd.errors.ParserError as e:
            return HttpResponse(f'Erro ao carregar ou preprocessar os dados: {str(e)}')

        try:
            regras = gerar_regras_minimo(df)
            regras_html = []
            for regra in regras:
                df, descricao = regra
                regras_html.append(df.to_html())
        except ValueError as e:
            return HttpResponse(f'Erro ao gerar regras: {str(e)}')

        return render(request, 'main/analise_basica.html', {'regras': regras})
    else:
        return HttpResponse(f'Formulário inválido: {form.errors}')

def analise_especifica(request):
    return HttpResponse(f'teste')


