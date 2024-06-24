import pandas as pd
import json
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.read_db import read_bd

def add_registration_json(json_data, df):
    new_registration = json.loads(json_data)
    
    new_df = pd.DataFrame([new_registration])
    
    updated_df = pd.concat([df, new_df], ignore_index=True)
    
    return updated_df

def main():
    json_data = json.dumps({
        'plate': 'DEF2G34',
        'brand': 'Renault',
        'model': 'Clio',
        'year': 2019,
        'color': 'Verde',
        'classification': 'Usado'
    })
    
    file_path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/cars_db.csv"
    df = read_bd(file_path)
    
    print(add_registration_json(json_data, df))

main()