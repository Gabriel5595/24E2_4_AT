import pandas as pd
from sqlalchemy import create_engine

def df_to_sql(df, db_path):
    engine = create_engine(f'sqlite:///{db_path}')
    df.to_sql('cars', engine, if_exists='replace', index=False)
    print(f"Base de dados SQL criada com sucesso em: {db_path}")