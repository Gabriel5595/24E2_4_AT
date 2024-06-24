import json
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.read_db import read_bd
from components.search_car_plate import search_car_plate

def save_json_file(json_info, file_path):
    try:
        with open(file_path, 'w') as f:
            json.dump(json_info, f, indent=4)
        print(f"Arquivo '{file_path}' salvo com sucesso.")
        return True
    except FileNotFoundError:
        print(f"Erro: Caminho '{file_path}' não encontrado.")
        return False
    except Exception as e:
        print(f"Erro ao salvar arquivo '{file_path}': {str(e)}")
        return False

def main():
    file_path_bd = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/cars_db.csv"
    file_path_json = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/results_json.json"
    df = read_bd(file_path_bd)
    result = search_car_plate(df, "ABC1D23")
    save_json_file(result, file_path_json)

main()