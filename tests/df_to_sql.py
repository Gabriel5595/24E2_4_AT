import pandas as pd
from sqlalchemy import create_engine
import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def df_to_sql(df, db_path):
    engine = create_engine(f'sqlite:///{db_path}')
    df.to_sql('cars', engine, if_exists='replace', index=False)
    print(f"Base de dados SQL criada com sucesso em: {db_path}")

def main():
    df = pd.DataFrame({
    'placa': ['ABC1D23', 'DEF2G34'],
    'marca': ['Ford', 'Renault'],
    'modelo': ['Ka', 'Clio'],
    'ano': [2018, 2019],
    'cor': ['Preto', 'Verde'],
    'classificacao': ['Usado', 'Usado']})
        
    db_path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/cars_db.db"
    df = df_to_sql(df,db_path)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "SELECT * FROM cars"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    conn.close()

main()