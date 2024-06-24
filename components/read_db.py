import pandas as pd
import sqlite3

def read_bd(file_path):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
        print(f"CSV file selected\nData:\n{df}\n")
    elif file_path.endswith('.xls') or file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
        print(f"Excel file selected\nData:\n{df}\n")
    else:
        raise ValueError("Formato de arquivo não suportado. Use .csv, .xls ou .xlsx.")
    
    db_path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/cars_db.db"
    conn = sqlite3.connect(db_path)
    df.to_sql('cars', conn, if_exists='replace', index=False)
    
    return conn