import pandas as pd
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.read_db import read_bd

def add_registration_excel(file_path, df):
    """
    Adiciona um registro ao DataFrame a partir de um arquivo XLS.

    Parâmetros:
    caminho_xls (str): Caminho do arquivo XLS com os dados do carro.
    df (DataFrame): DataFrame do banco de dados.

    Retorna:
    DataFrame: DataFrame atualizado com o novo registro.
    """
    # Lê o novo registro do arquivo XLS
    new_registration = pd.read_excel(file_path)
    
    # Concatena o novo registro com o DataFrame existente
    updated_df = pd.concat([df, new_registration], ignore_index=True)
    
    return updated_df

def main():
    
    file_path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/cars_db.csv"
    df = read_bd(file_path)
    
    new_file_path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/new_registration.xlsx"
    print(add_registration_excel(new_file_path, df))

main()