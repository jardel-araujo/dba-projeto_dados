import os, pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv(override=True)

url= (f"postgresql+psycopg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")
engine= create_engine(url)

engine=create_engine(url)

df=pd.read_sql("select * from vw_vendas_detalhadas where status <> 'cancelado'",engine,)

print(df.shape)
resumo = (df.groupby("categoria")["subtotal"].sum().sort_values(ascending=False))
print(resumo)