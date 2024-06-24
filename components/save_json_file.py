from components.read_db import read_bd
from components.search_car_plate import search_car_plate

def save_json_file(json_info, file_path):
    with open(file_path, 'w') as arquivo:
        arquivo.write(json_info)