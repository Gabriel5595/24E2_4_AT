import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.read_db import read_bd
from components.search_car_plate import search_car_plate

def save_json_file(json_info, file_path):
    with open(file_path, 'w') as arquivo:
        arquivo.write(json_info)

def main():
    file_path_bd = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/cars_db.csv"
    file_path_json = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/results_json.json"
    df = read_bd(file_path_bd)
    result = search_car_plate(df, "ABC1D23")
    save_json_file(result, file_path_json)

main()