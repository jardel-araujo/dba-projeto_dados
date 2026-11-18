import pandas as pd
from conexao import connect

# EXTRAIR
df = pd.read_csv('novos_produtos.csv', sep=';', decimal=',')
print(f'Linhas Lidas:{len(df)}')

#TRANSFORMAR 
invalidos= df[df['preco'].isna() | (df['preco'] <= 0)]
df = df.drop(invalidos.index)
df['nome'] = df['nome'].str.strip()
print(f'Linhas Descartadas: {len(invalidos)}')

#CARREGAR
sql_upsert = """
    INSERT INTO analytics.produtos (nome, preco, estoque, categoria_id)
    VALUES (%s, %s, %s, (SELECT id FROM analytics.categorias WHERE nome = %s))
    ON CONFLICT (nome)
    DO UPDATE SET preco = EXCLUDED.preco, estoque = EXCLUDED.estoque
"""

linhas = [
(r.nome, float(r.preco), int(r.estoque), r.categoria)
for r in df.itertuples(index=False)
]
with connect() as conn, conn.cursor() as cur:
    cur.executemany(sql_upsert, linhas)
    print(f"Linhas carregadas: {len(linhas)}")
# RELATÓRIO
    cur.execute("""
        SELECT c.nome, COUNT(p.id) AS qtd, SUM(p.estoque) AS estoque
        FROM analytics.categorias c
        JOIN analytics.produtos p ON p.categoria_id = c.id
        GROUP BY c.nome
        ORDER BY qtd DESC, c.nome
    """)
    
    relatorio = pd.DataFrame(cur.fetchall(), columns=["categoria", "produtos", "estoque"])
    
relatorio.to_csv("relatorio_estoque.csv", index=False, sep=";")
print(relatorio.to_string(index=False))