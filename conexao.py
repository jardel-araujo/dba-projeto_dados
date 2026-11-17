import os, psycopg as pg, datetime as dt
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())   # carrega as variáveis do arquivo .env

def connect():
    
    try:
        return pg.connect (
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            sslmode=os.getenv('DB_SSLMODE') 
        )
    except Exception as e:
        data_hora_atual = dt.datetime.now().strftime('%d-%m-%Y %H:%M')
        print(f'[{data_hora_atual}] Erro ao connectarcom o Banco de Dados: {e}')
        return None 