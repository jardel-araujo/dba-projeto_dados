import pandas as pd
from conexao import connect

# EXTRAIR
df= pd.read_sql('novos_produtos.csv', sep=';', decimal=',')
print(f'Linhas Lidas:{len(df)}')

#TRANSFORMAR 
invalidos= df[df['preco'].isna() | (df.[preco] <= 0)]
df = df.drop(invalidos.index)
df['nome'] = df['nome'].str.strip()
print(f'Linhas Descartadas: {len(invalidos)}')

