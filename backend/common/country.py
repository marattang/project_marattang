class Country(object):
    name = 'Country Name'
    population = 'Population'
    capital = 'Capital'

    def show(self):
        print('Country Class Method')

class Korea(Country):

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f'Country Name is {self.name}')

def main():
    k = Korea()
    k.name = '한국'
    k.show_name()

main()