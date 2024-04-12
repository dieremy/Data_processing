import pandas

class DataCleaning:
    def __init__(self, data):
        self.data = data

    def helloworld():
        return "helloworld"

    def drop_columns(self, sort):
        if sort == 'asc':
            sorted_cols = self.data.columns.sort_values()
        elif sort == 'desc':
            sorted_cols = self.data.columns.sort_values(ascending=False)
        else:
            sorted_cols = self.data.columns

        return sorted_cols
        
    def get_integers(self):
        self.data
