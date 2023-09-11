import pandas as pd

# Importando arquivo csv.
df = pd.read_csv('dados.csv')

# Criando uma variável com um DataFrame com as colunas especificadas.
novo_df = df[['col1', 'col2', 'col3']]

print(novo_df)

# Criando uma nova seleção, filtrando pela coluna 'data'
novo_df = novo_df.loc[novo_df['data'] <= pd.to_datetime('2020-01-01')]

print(novo_df) # Aqui apresenta erro pois a coluna data não foi adicionada na primeira atribuição


# --------------------------------------------------------------------


# Arquivo corrigido:

# Importando arquivo csv.
df = pd.read_csv('dados.csv')

# Criando uma variável com um DataFrame com as colunas especificadas.
novo_df = df[['col1', 'col2', 'col3', 'data']]

# Converte a coluna 'data' para Timestamps
novo_df['data'] = pd.to_datetime(novo_df['data'])

# Criando uma nova seleção, filtrando pela coluna 'data'
novo_df = novo_df.loc[novo_df['data'] <= pd.to_datetime('2020-01-01')]

print(novo_df)
