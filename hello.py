# name = input("What is your name: ")
# print('Hello')
# print(name.capitalize())
# first_name = 'JIE'
# last_name = 'SUN'
# output = 'Hello, ' + first_name + ' ' + last_name
# output = 'Hello, {} {}'.format(first_name, last_name)
# output = 'Hello, {1} {0}'.format(first_name, last_name)
# output = 'Hello, {0} {1}'.format(first_name, last_name)
# output = f'Hello, {first_name} {last_name}'
# print(output)
from datetime import datetime, timedelta

# today = datetime.now()
# today = datetime.today()
# print(datetime.now())
# print('Day: ' + str(today.day))
# print('Month: ' + str(today.month))
# print('Year: ' + str(today.year))

# one_day = timedelta(days=1)
# yesterday = today - one_day
# print('Yesterday was: ' + str(yesterday))

birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))

