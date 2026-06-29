
number = input('Please enter an integer number: ')

number = int(number)


if number % 3 == 0 and number % 5 == 0:
    print('افسانه ای')
elif number % 3 == 0:
    print('جادویی')
elif number % 5 == 0:
    print('نفرین شده')
else:
    print('معمولی')