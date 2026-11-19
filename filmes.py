import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from conexao import connect

with connect() as conn, conn.cursor () as cur:
    cur.execute("""
    SELECT titulo, acao, aventura, comedia, drama, ficcao FROM analytics.filmes ORDER BY titulo;
""")

    colunas = [desc[0] for desc in cur.description]
    df = pd.DataFrame(cur.fetchall(), columns=colunas)

coluna_generos = ['acao','aventura','comedia','drama','ficcao']
matriz_generos = df[coluna_generos]
matriz_similaridade = cosine_similarity(matriz_generos)
df_similaridade = pd.DataFrame(
    matriz_similaridade, 
    index=df['titulo'],
    columns= df['titulo']
)

def recomendar_filmes (filme_escolhido, qtd=3):
    if filme_escolhido not in df_similaridade.index:
        print(f"filmes '{filme_escolhido}' não encontrado no catálogo")
        return 
    scores = df_similaridade[filme_escolhido].sort_values(ascending=False)     
    recomendacoes = scores.drop(filme_escolhido).head(qtd)
    print(f"--- Quem assistiu '{filme_escolhido}' também pode gostar de: ---")
    for titulo, score in recomendacoes.items():
        print(f"{titulo} (similaridade {score*100:.1f}%)")
escolher_filme = input("Digite o nome do filme do catálogo ").strip()
recomendar_filmes(escolher_filme)