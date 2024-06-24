import pandas as pd
import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def read_bd(file_path):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
        print(f"CSV file selected\nData:\n{df}")
    elif file_path.endswith('.xls') or file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
        print(f"Excel file selected\nData:\n{df}")
    else:
        raise ValueError("Formato de arquivo não suportado. Use .csv, .xls ou .xlsx.")
    
    db_path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/cars_db.db"
    conn = sqlite3.connect(db_path)
    df.to_sql('cars', conn, if_exists='replace', index=False)
    
    return conn

def main():
    file_path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/cars_db.csv"
    print(read_bd(file_path))
    
    db_path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/cars_db.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "SELECT * FROM cars LIMIT 5"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    conn.close()

main()