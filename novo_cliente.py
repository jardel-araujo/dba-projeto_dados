from conexao import connect
import datetime as dt

novo_cliente = ('Bianca Freitas', 'bianca.freitas@gmail.com', 'Fortaleza', '85996660000')

def cadastrar_cliente(cliente):
    '''
    Retorna o id do cliente cadastrado no banco de dados loja_ceara
    '''
    try:
        with connect() as conn, conn.cursor() as cur:
                sql = '''
                    INSERT INTO analytics.clientes (nome, email, cidade, telefone)
                    VALUES ( %s, %s, %s, %s)
                    RETURNING id;
                '''
                cur.execute(sql, cliente)
        
                print('Cliente Cadastrado! ID: ', cur.fetchall()[0])    

    except Exception as e:
        data_hora_atual = dt.datetime.now().strftime('%d-%m-%Y %H:%M')
        print(f'[{data_hora_atual}] Erro ao connectarcom o Banco de Dados: {e}')
        return None 
    
cadastrar_cliente(novo_cliente)