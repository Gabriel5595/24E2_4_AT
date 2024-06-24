import pandas as pd
from sqlalchemy import create_engine

def db_to_df(db_path):
    engine = create_engine(f'sqlite:///{db_path}')
    query = "SELECT * FROM cars"
    df = pd.read_sql(query, engine)
    return df