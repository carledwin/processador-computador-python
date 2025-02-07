# -*- coding: utf-8 -*-
"""processador-computadores.ipynb

Automatically generated by Colab.

Original file is located at

"""

import json
import pandas as pd
import os
from typing import List, Optional

class Atributo:
    def __init__(self, chave: str, valor: str):
        self.chave = chave
        self.valor = valor

    def __str__(self):
        return f'{self.chave}: {self.valor}'


class Computador:
    def __init__(self, nome: str, codigo: str, produto: str, versao: dict = None, atributos: Optional[List[Atributo]] = None):
        self.nome = nome
        self.codigo = codigo
        self.produto = produto
        self.versao = versao  # Aqui `versao` é um único objeto

        if isinstance(atributos, list):
          self.atributos = [Atributo(attr['chave'], attr['valor']) for attr in atributos]
        else:
          self.atributos = []  # Or a default value

    def __str__(self):
        atributos_str = ', '.join(str(attr) for attr in self.atributos)
        versao_str = f'{self.versao["nome"]}: {self.versao["versao"]}'
        return f'Computador(nome={self.nome}, codigo={self.codigo}, produto={self.produto}, versao=[{versao_str}], atributos=[{atributos_str}])'

def processar(arquivo_json: str):
    # Ler o arquivo JSON em um DataFrame Pandas
    df = pd.read_json(arquivo_json)

    # Imprimir o total de registros antes do filtro
    total_antes = len(df)
    print(f"Total de registros antes do filtro: {total_antes}")

    # Filtrar registros que atendem às condições especificadas
    df_filtrado = df[
        (df['versao'].isna()) |
        (df['versao'].apply(lambda x: x is None or ('nome' not in x if isinstance(x, dict) else True) or (
            x['nome'] is None if isinstance(x, dict) else True) or (
                                          x['nome'] != 'v2.0' if isinstance(x, dict) else True)))
    ]

    # Imprimir o total de registros após o filtro
    total_depois = len(df_filtrado)
    print(f"Total de registros após o filtro: {total_depois}")

    # Iterar pelos registros e criar objetos Computador
    computadores = []
    for _, row in df.iterrows():

        if 'versao' in row:  # Check if 'versao' key exists in row
            versao = row['versao']

            if isinstance(versao, dict) and versao:
                versao = {
                    'nome': versao['nome'] if 'nome' in versao and versao['nome'] else None,
                    'versao': versao['versao'] if 'versao' in versao and versao['versao'] else None
                }
            else:
                versao = {}

        else:
            versao = {}

        atributos = row['atributos'] if 'atributos' in row and row['atributos'] else None
        computador = Computador(row['nome'], row['codigo'], row['produto'], versao, atributos)
        computadores.append(computador)

    # Converter para DataFrame para salvar em CSV
    df_computadores = pd.DataFrame([{
        'nome': comp.nome,
        'codigo': comp.codigo,
        'produto': comp.produto,
        'versao_nome': comp.versao['nome'] if 'nome' in comp.versao and comp.versao['nome'] else None,
        'versao_versao': comp.versao['versao'] if 'versao' in comp.versao and comp.versao['versao'] else None,
        **{attr.chave: attr.valor for attr in comp.atributos}
    } for comp in computadores])

    # Gerar o nome do arquivo CSV com base no nome do arquivo JSON
    nome_csv = os.path.splitext(arquivo_json)[0] + '_processado.csv'

    # Salvar em arquivo CSV
    df_computadores.to_csv(nome_csv, index=False)
    print(f"Arquivo '{nome_csv}' salvo com sucesso!")

def main():
    #processar('./json/computadores_10_sem_atributos.json')
    #processar('./json/computadores_10_sem_campos_principais.json')
    processar('./json/computadores_10_sem_versao_ou_parte_da_versao.json')
    #processar('./json/computadores_360000_campos_inexistentes_vazios_none.json')

if __name__ == "__main__":
    main()