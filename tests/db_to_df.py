import pandas as pd
from sqlalchemy import create_engine
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def db_to_df(db_path):
    engine = create_engine(f'sqlite:///{db_path}')
    query = "SELECT * FROM cars"
    df = pd.read_sql(query, engine)
    return df

def main():    
    db_path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/cars_db.db"
    df = db_to_df(db_path)
    print(df)

main()