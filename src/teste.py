import pandas as pd

df = pd.read_csv('date2.tsv', delimiter ='\t')

# Obtendo os valores únicos das colunas
col1 = set(df[0].unique())
col2 = set(df[1].unique())

# Criando o dicionário de mapeamento
mapping = {}
for index, row in df.iterrows():
    key = (row[0], str(row[1]))
    value = row[2]
    if key in mapping:
        mapping[key].add(value)
    else:
        mapping[key] = {value}

# Obtendo os valores únicos das colunas restantes
col3 = set(df[2].unique())
col4 = set(df[3].unique())
col5 = set(df[4].unique())

# Imprimindo o resultado
result = (col1, col2, mapping, col3, col4)
print(result)