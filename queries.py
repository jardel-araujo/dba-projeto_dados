from conexao import connect

def consultar_categorias():
    """
    Retorna as categorias cadastradas no banco de dados loja_ceara
    """

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT id, nome FROM analytics.categorias order by nome')
            return cur.fetchall() #lista de tuplas


for id, nome in consultar_categorias():
    print(f'{id} - {nome}')

def consultar_clientes():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT id, nome, email, cidade, estado FROM analytics.clientes ORDER BY cidade')
            return cur.fetchall()

for id, nome, email, cidade, estado in consultar_clientes():
    print(f'{id} - {nome} - {email} - {cidade} - {estado}')
    



    