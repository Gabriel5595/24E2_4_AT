import pandas as pd

def read_bd(file_path):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xls') or file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Formato de arquivo não suportado. Use .csv, .xls ou .xlsx.")
    
    return df