import json

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