car_year = int(input())

if car_year <= 1969:
    print('Few safety features.\n')
elif car_year >= 1970:
    print('Probably has seat belts.\n')
    if car_year >= 1990:
        print('Probably has antilock brakes.\n')
    elif car_year >= 2000:
        print('Probably has airbags.\n')

