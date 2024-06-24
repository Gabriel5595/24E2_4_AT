import pandas as pd

def save_excel_file(df, new_file_path):
    df.to_excel(new_file_path, index=False)
    print(f"Arquivo salvo em: {new_file_path}")