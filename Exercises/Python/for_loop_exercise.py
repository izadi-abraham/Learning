number = int(input('Please enter number of iteration(s):'))


for _ in range(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = (number * 2) - 1


print(number)
