from conexao import connect
import datetime as dt

categorias = [('Cosméticos',), ('Games',), ('Papelaria',), ('Pet Shop',)]

def cadastrar_categorias(categorias):
    '''
    Retorna o id da categoria cadastrado no banco de dados loja_ceara
    '''
    try:
        sql = '''
            INSERT INTO analytics.categorias (nome)
            VALUES ( %s) ON CONFLICT (nome) DO NOTHING
        '''
        with connect() as conn, conn.cursor() as cur:
                cur.executemany(sql, categorias)
                cur.execute('SELECT COUNT(*) FROM analytics.categorias;')   
                print('Total de Catregorias ', cur.fetchone()[0])
    
    except Exception as e:
        data_hora_atual = dt.datetime.now().strftime('%d-%m-%Y %H:%M')
        print(f'[{data_hora_atual}] Erro ao connectarcom o Banco de Dados: {e}')
        return None 
        
cadastrar_categorias(categorias)