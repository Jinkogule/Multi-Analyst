import asyncio
import json
import pandas as pd
from io import StringIO
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from analise_apriori.apriori import carregar_dados, preprocessar_dados, gerar_regras_minimo
from analise_apriori.utils import detectar_encoding
from openai_chat.chatgpt_service import generate_response
from channels.layers import get_channel_layer

def index(request):
    return render(request, 'main/index.html')

def analise_basica(request):
    if request.method == 'POST':
        try:
            csv_file = request.FILES.get('csv_file')
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
            regras_json = json.dumps(regras_html)
        except ValueError as e:
            return HttpResponse(f'Erro ao gerar regras: {str(e)}')

        context_description = request.POST.get('context_description', '')

        return render(request, 'main/analise_basica.html', {
            'regras': regras_html,
            'regras_json': regras_json,
            'context_description': context_description,
        })
    return render(request, 'main/index.html')

@csrf_exempt
def gerar_insights(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body.decode('utf-8'))
            regras = body.get('regras')
            context_description = body.get('context_description')

            if not regras or not context_description:
                return JsonResponse({'status': 'error', 'message': 'Regras ou contexto não fornecidos.'})

            prompt = (
                f"Os dados a seguir foram obtidos através de um processamento utilizando o algoritmo apriori sobre uma base de dados:\n{regras}\n\n"
                f"Tais dados possuem o seguinte contexto:\n'{context_description}'\n\n"
                f"Considere que a ideia é identificar padrões e insights úteis para usuários leigos em análise de dados, além disso, formate a resposta de maneira que o subtítulo de cada item seja igual ao conteúdo contido entre parênteses em cada item:\n"
                "1. Identifique padrões, tendências ou associações notáveis nos dados. (Padrões, tendências ou associações notáveis:)\n"
                "2. Extraia insights gerais dessas associações, listando-os de maneira clara e simples para um público geral. (Insights identificados:)\n"
                "3. Explique como esses insights podem ser aplicados em um contexto prático. (Como estes insights podem ser úteis?)\n"
            )

            channel_layer = get_channel_layer()
            room_group_name = 'insights_group'
            asyncio.run(generate_response(prompt, channel_layer, room_group_name))

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
