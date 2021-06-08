from real_estate.housing import Housing
from real_estate.dataset import Dataset

class Controller(object):

    @staticmethod
    def main():
        while 1:
            menu= input('0.Exit 1.new_model\n'
                        '2.DF 생성')
            if menu == '1':
                housing = Housing()
                dataset = Dataset()
                dataset.housing = housing.new_model('time_series_cost.xlsx')
                # print(type(dataset.housing))
                Controller.print_this(dataset.housing)
            else :
                print('wrong number')

    @staticmethod
    def print_this(this):
        print('*' * 100)
        print(f'1. Housing 의 type\n{type(this)} 이다.')
        print(f'2. Housing 의 column\n{this.columns} 이다.')
        print(f'3. Housing 의 상위 1개 행\n{this.head(1)} 이다.')
        print(f'4. Housing 의 null 의 갯수\n {this.isnull().sum()}개')

Controller.main()