from datetime import date

todays_date = date.today()

name = input("What is your name? ")
age = int(input("How old are you? "))
year = todays_date.year - age

print('Hello ', name, '!' + ' You were born in ', (year), '.')
