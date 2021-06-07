from real_estate.dataset import Dataset
import pandas as pd

class Housing():

    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_excel(this.context + this.fname, sheet_name='평균전세', header=0, usecols= 'A:U')

