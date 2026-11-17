from conexao import connect

con = connect()

if con:
    # Valida se a conexão foi estabelecida com sucesso e imprime uma mensagem de confirmação
    print(f'Conectado ao Banco de Dados: {con.info.dbname}')
    con.close()
