from crime.services import CrimeService

class Crime_API(object):

    @staticmethod
    def main():
        crimeService = CrimeService()
        while 1:
            menu = input('0-Exit\n1-서울CCTV DF\n2-서울범죄 DF\n'
                         '3-경찰서위치 DF\n4-실업율 DF\n5-엑셀POP')
            if menu == '0':
                break
            elif menu == '1':
                crimeService.csv({'context':'./data/', 'fname':'cctv_in_seoul'})
            elif menu == '2':
                crimeService.csv({'context':'./data/', 'fname':'crime_in_seoul'})
            elif menu == '3':
                crimeService.csv({'context':'./data/', 'fname':'police_position'})
            elif menu == '4':
                crimeService.xls({'context':'./data/', 'fname':'pop_in_seoul'}, header=0, usecols=None)
            elif menu == '5':
                crimeService.csv({'context':'./data/', 'fname':'us_unemployment'})
            else:
                print('wrong number')
                continue

Crime_API.main()