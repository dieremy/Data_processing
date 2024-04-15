import os
import pandas as pd


ARTWORK_DATA = os.path.abspath('../data/artwork_data.csv')
ARTIST_DATA = os.path.abspath('../data/artist_data.csv')

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
    