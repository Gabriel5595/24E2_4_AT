import pandas as pd
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.read_db import read_bd
from components.save_excel_file import save_excel_file

def search_car_classification(classification, df):
    """
    Busca todos os carros de uma dada classificação e salva em um arquivo XLS.

    Parâmetros:
    classificacao (str): Tipo de classificação dos carros (novo, semi-novo, usado).
    df (DataFrame): DataFrame do banco de dados.
    caminho_saida (str): Caminho do arquivo XLS para salvar os resultados.

    Retorna:
    None
    """
    # Filtra os carros pela classificação fornecida
    results = df[df['classification'] == classification]

    new_file_path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/results_excel.xlsx"
    
    save_excel_file(results,new_file_path)


def main():
    
    file_path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/cars_db.csv"
    df = read_bd(file_path)
    
    search_car_classification("Usado", df)

main()