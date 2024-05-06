from django.http import HttpResponse
from django.shortcuts import render
from analise_apriori.apriori import carregar_e_preprocessar_dados, gerar_conjuntos_itens_frequentes, gerar_regras
from io import StringIO
from analise_apriori.forms import UploadFileForm

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file'].read().decode('utf-8')
            data = StringIO(csv_file)
            df = carregar_e_preprocessar_dados(data)
            suporte_minimo = 0.01
            try:
                conjuntos_itens_frequentes = gerar_conjuntos_itens_frequentes(df, suporte_minimo)
                regras = gerar_regras(conjuntos_itens_frequentes)
                regras_html = regras.to_html()
            except ValueError as e:
                return HttpResponse(f'Não é possível analisar esta base de dados sobre as configurações atuais (itemsets vazios para suporte mínimo={suporte_minimo})')
            return render(request, 'main/index.html', {'regras': regras_html})
    else:
        form = UploadFileForm()
    return render(request, 'main/index.html', {'form': form})
