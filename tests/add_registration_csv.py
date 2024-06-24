import pandas as pd
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.read_db import read_bd

def add_registration_csv(file_path, df):
    new_registration = pd.read_csv(file_path)
    
    updated_df = pd.concat([df, new_registration], ignore_index=True)
    
    return updated_df

def main():
    
    file_path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/cars_db.csv"
    df = read_bd(file_path)
    
    new_file_path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/new_registration.csv"
    print(add_registration_csv(new_file_path, df))

main()
