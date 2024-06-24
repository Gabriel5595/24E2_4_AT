import pandas as pd
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def save_excel_file(df, new_file_path):
    df.to_excel(new_file_path, index=False)
    print(f"Arquivo salvo em: {new_file_path}")