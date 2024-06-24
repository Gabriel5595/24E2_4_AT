import json
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.read_db import read_bd

def search_car_plate(df, plate):
    car = df[df['plate'] == plate]
    if not car.empty:
        result = {
            'placa': str(car.iloc[0]['plate']),
            'marca': str(car.iloc[0]['brand']),
            'modelo': str(car.iloc[0]['model']),
            'ano': int(car.iloc[0]['year']),
            'cor': str(car.iloc[0]['color']),
            'classificacao': str(car.iloc[0]['classification'])
        }
        return json.dumps(result, indent=4)
    else:
        return json.dumps({'error': 'Car not found'}, indent=4)

def main():
    file_path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/AT/resources/cars_db.csv"
    df = read_bd(file_path)
    print(search_car_plate(df, "ABC1D23"))

main()