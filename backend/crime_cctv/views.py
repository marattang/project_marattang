from services import CrimeService

if __name__ == '__main__':

    service = CrimeService()

    while 1:
        menu = input('0.Exit 1.cctv_in_seoul_MakeDF\n'
                     '2.crime_in_seoul_MakeDF\n'
                     '3.police_position_MakeDF\n'
                     '4.pop_in_seoul_MakeDF\n'
                     '5.us_unemployment_MakeDF')
        if menu == '0':
            break
        elif menu == '1':
            df = service.new_model_csv('cctv_in_seoul')
            service.print_dframe(df)
        elif menu == '2':
            df = service.new_model_csv('crime_in_seoul')
            service.print_dframe(df)
        elif menu == '3':
            df = service.new_model_csv('police_position')
            service.print_dframe(df)
        elif menu == '4':
            df = service.new_model_xls('pop_in_seoul')
            service.print_dframe(df)
        elif menu == '5':
            df = service.new_model_csv('us_unemployment')
            service.print_dframe(df)
        else:
            print('wrong number')
            continue