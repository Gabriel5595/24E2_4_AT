import pandas as pd

def add_registration_excel(file_path, df):
    try:
        new_registration = pd.read_excel(file_path)
        updated_df = pd.concat([df, new_registration], ignore_index=True)
        return updated_df
    except Exception as e:
        print(f"Erro ao carregar arquivo Excel '{file_path}': {str(e)}")
        return False
    
    return updated_df