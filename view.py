import os, pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv(override=True)

url= (f"postgresql+psycopg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")
engine= create_engine(url)
sql = '''
CREATE OR REPLACE VIEW public.vw_vendas_detalhadas AS SELECT p.id AS pedido_id, p.data_pedido, p.status, c.nome AS client, c.cidade,
pr.nome AS produto, cat.nome AS categoria, i.quantidade, i.preco_unitario,
i.quantidade * i.preco_unitario AS subtotal
FROM analytics.itens_pedido i
JOIN analytics.pedidos p ON p.id = i.pedido_id
JOIN analytics.clientes c ON c.id = p.cliente_id
JOIN analytics.produtos pr ON pr.id = i.produto_id
JOIN analytics.categorias cat ON cat.id = pr.categoria_id;
'''

with engine.begin() as conn:
    conn.execute(text(sql))

print('view criada com sucesso')

