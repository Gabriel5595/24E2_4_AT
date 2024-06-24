import json

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