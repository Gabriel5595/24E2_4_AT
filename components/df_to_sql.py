import pandas as pd
from sqlalchemy import create_engine

def df_to_sql(df, db_path):
    try:
        engine = create_engine(f'sqlite:///{db_path}')
        df.to_sql('cars', engine, if_exists='replace', index=False)
        return engine.connect()
    except Exception as e:
        print(f"Erro ao criar base de dados SQL a partir do arquivo Excel: {str(e)}")
        return False