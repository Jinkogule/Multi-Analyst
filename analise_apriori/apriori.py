import numpy as np
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
from analise_apriori.utils import detectar_header, remover_todos_zeros_da_lista, detectar_delimitador

def carregar_dados(arquivo_path):
    """Carrega dados de um arquivo CSV e detecta seu delimitador e header."""
    delimiter = detectar_delimitador(arquivo_path)
    arquivo_path.seek(0)
    has_header = detectar_header(arquivo_path, delimiter)
    header_option = 0 if has_header else None

    print(f"Delimiter detected: {delimiter}")
    print(f"Header detected: {has_header}")

    arquivo_path.seek(0)
    df = pd.read_csv(arquivo_path, header=header_option, sep=delimiter)
    df.replace(np.nan, 0, inplace=True)
    return df

def preprocessar_dados(df):
    lista_todas_transacoes = []
    for _, row in df.iterrows():
        lista_de_transacoes = remover_todos_zeros_da_lista(row.values.tolist())
        lista_todas_transacoes.append([str(item) for item in lista_de_transacoes])
    te = TransactionEncoder()
    te_ary = te.fit(lista_todas_transacoes).transform(lista_todas_transacoes)
    return pd.DataFrame(te_ary, columns=te.columns_)

def gerar_conjuntos_itens_frequentes(df, min_support):
    return apriori(df, min_support=min_support, use_colnames=True)

def gerar_regras(conjuntos_itens_frequentes, min_threshold):
    regras = association_rules(conjuntos_itens_frequentes, metric='lift', min_threshold=min_threshold)
    return regras.sort_values(by=['lift'], ascending=False)

def gerar_regras_minimo(df):
    combinacoes = [
        (0.5, 0.7, "Sobre min_support=0.5 e min_threshold=0.7"),
        (0.5, 0.3, "Sobre min_support=0.5 e min_threshold=0.3"),
        (0.1, 0.7, "Sobre min_support=0.1 e min_threshold=0.7"),
        (0.1, 0.3, "Sobre min_support=0.1 e min_threshold=0.3"),
        (0.05, 0.5, "Sobre min_support=0.05 e min_threshold=0.5"),
        (0.01, 0.5, "Sobre min_support=0.01 e min_threshold=0.5"),
        (0.01, 0.1, "Sobre min_support=0.01 e min_threshold=0.1")
    ]
    
    resultados = []
    for min_support, min_threshold, descricao in combinacoes:
        conjuntos_itens_frequentes = gerar_conjuntos_itens_frequentes(df, min_support)
        if not conjuntos_itens_frequentes.empty:
            regras = gerar_regras(conjuntos_itens_frequentes, min_threshold)
            if len(regras) >= 5:
                resultados.append((regras, descricao))
        if resultados:
            return resultados
    return resultados
