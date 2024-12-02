# introdução a biblioteca Panda para manipulação de dados

import pandas as pd

data = {
    'Nome': ['João Vitor', 'Maria', 'Pedro'],
    'Idade': [ 28,26,35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba']
}

df = pd.DataFrame(data)

# Manipulando dados com panda
nomes = df['Nome']
print(nomes)

primeira_linha = df.iloc[0]

print(primeira_linha)
