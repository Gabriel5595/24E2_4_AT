import pandas as pd
import json

def add_registration_json(json_data, df):
    new_registration = json.loads(json_data)
    
    new_df = pd.DataFrame([new_registration])
    
    updated_df = pd.concat([df, new_df], ignore_index=True)
    
    return updated_df