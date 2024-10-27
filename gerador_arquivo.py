import json
import random

# Possíveis valores para os atributos
nomes = ["MeuPC", "SeuPC", "NossoPC"]
produtos = ["Laptop", "Desktop", "Servidor"]
versoes = [
    {"nome": "v1.0", "versao": "2022"},
    {"nome": "v2.0", "versao": "2023"}
]
atributos_possiveis = [
    ("memoria", ["8GB", "16GB", "32GB"]),
    ("cpu", ["Intel i5", "Intel i7", "AMD Ryzen"]),
    ("polegadas", ["13", "15.6", "17", "27"]),
    ("peso", ["1.5kg", "2kg", "3kg", "10kg"]),
    ("preco", ["500 USD", "1000 USD", "1500 USD", "2000 USD"])
]

# Função para gerar um computador aleatório
def gerar_computador():
    nome = random.choice(nomes)
    codigo = str(random.randint(10000, 99999))
    produto = random.choice(produtos)
    versao = random.choice(versoes)
    atributos = [{"chave": chave, "valor": random.choice(valores)} for chave, valores in atributos_possiveis]
    return {
        "nome": nome,
        "codigo": codigo,
        "produto": produto,
        "versao": versao,
        "atributos": atributos
    }

# Função para gerar e salvar os 80 mil registros
def gerar_arquivo_computadores(qtd_registros):
    computadores = [gerar_computador() for _ in range(qtd_registros)]

    # Salvar em um arquivo JSON
    with open(f'computadores_{qtd_registros}.json', 'w') as f:
        json.dump(computadores, f)

    print(f'Arquivo computadores_{qtd_registros}.json gerado com sucesso!')

def main():
    # gerar_arquivo_computadores(80000)
    #gerar_arquivo_computadores(360000)
    gerar_arquivo_computadores(10)

if __name__ == "__main__":
    main()
