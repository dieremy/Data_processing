import pandas as pd

class DataCleaning:
    def __init__(self, data):
        self.data = data

    def drop_columns(self, sort):
        if sort == 'asc':
            sorted_cols = self.data.columns.sort_values()
        elif sort == 'desc':
            sorted_cols = self.data.columns.sort_values(ascending=False)
        else:
            sorted_cols = self.data.columns

        return sorted_cols
        
    def get_integers(self, column):
        return pd.to_numeric(column, errors='coerce')
    
