from io import StringIO
import numpy as np
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd
from collections import Counter
import csv

def remover_todos_zeros_da_lista(lista):
    return list(filter(lambda x: x != 0, lista))



def detectar_delimitador(csv_string_io):
    # Lê as primeiras num_linhas linhas do arquivo
    amostra = ''.join([csv_string_io.readline() for _ in range(5)])
    csv_string_io.seek(0)  # Retorna ao início do arquivo

    delimiters = [";", ",", "\t"]
    guess = max(delimiters, key=amostra.count)
    return guess


"""def detect_delimiter_string(csv_string):
    delimiters = [";", ",", "\t"]
    guess = max(delimiters, key=csv_string.count)
    return guess"""


"""def obter_colunas(csv_string):
    delimiter = detect_delimiter_string(csv_string)
    data = StringIO(csv_string)
    df = pd.read_csv(data,header = 0, sep=delimiter)
    return df.columns.tolist()"""

def carregar_dados(arquivo_path):
    delimiter = detectar_delimitador(arquivo_path)
    arquivo_path.seek(0)
    verifica_cabecalh = None
    arquivo_path.seek(0)
    df = pd.read_csv(arquivo_path, header=verifica_cabecalh, sep=delimiter)
    df.replace(np.nan, 0, inplace=True)
    return df

def preprocessar_dados(df):
    lista_todas_transacoes = []
    for _, row in df.iterrows():
        lista_de_transacoes = remover_todos_zeros_da_lista(row.values.tolist())
        lista_de_transacoes = [str(item) for item in lista_de_transacoes]
        lista_todas_transacoes.append(lista_de_transacoes)
    te = TransactionEncoder()
    te_ary = te.fit(lista_todas_transacoes).transform(lista_todas_transacoes)
    return pd.DataFrame(te_ary, columns=te.columns_)

def gerar_conjuntos_itens_frequentes(df, min_support):
    conjuntos_itens_frequentes = apriori(df, min_support=min_support, use_colnames=True)
    return conjuntos_itens_frequentes

def gerar_regras(conjuntos_itens_frequentes, min_threshold):
    regras = association_rules(conjuntos_itens_frequentes, metric='lift', min_threshold=min_threshold)
    regras.sort_values(by=['lift'], ascending=False, inplace=True)
    return regras

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




