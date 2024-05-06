import numpy as np
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

def remover_todos_zeros_da_lista(lista):
    return list(filter(lambda x: x != 0, lista))

def carregar_e_preprocessar_dados(arquivo_path):
    df = pd.read_csv(arquivo_path, header = None)
    df.replace(np.nan, 0, inplace=True)

    lista_todas_transacoes = []
    for index, row in df.iterrows():
        lista_de_transacoes = row.values.tolist()
        lista_de_transacoes = remover_todos_zeros_da_lista(lista_de_transacoes)
        lista_todas_transacoes.append(lista_de_transacoes)

    te = TransactionEncoder()
    te_ary = te.fit(lista_todas_transacoes).transform(lista_todas_transacoes)

    df = pd.DataFrame(te_ary, columns=te.columns_)
    return df

def gerar_conjuntos_itens_frequentes(df, suporte_minimo):
    conjuntos_itens_frequentes = apriori(df, min_support = suporte_minimo, use_colnames = True)
    return conjuntos_itens_frequentes

def gerar_regras(conjuntos_itens_frequentes, metrica = "confidence", limiar_minimo = 0.5):
    regras = association_rules(conjuntos_itens_frequentes, metric = metrica, min_threshold = limiar_minimo)
    regras.sort_values(by=['lift'], ascending = False, inplace = True)
    return regras