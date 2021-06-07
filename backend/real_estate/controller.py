from real_estate.housing import Housing
from real_estate.dataset import Dataset

class Controller(object):

    @staticmethod
    def main():
        housing = Housing()
        dataset = Dataset()
        dataset.housing = housing.new_model('time_series_cost.xlsx')
        print(dataset.housing)

Controller.main()