import pandas as pd

def add_registration_csv(file_path, df):
    new_registration = pd.read_csv(file_path)
    
    updated_df = pd.concat([df, new_registration], ignore_index=True)
    
    return updated_df
