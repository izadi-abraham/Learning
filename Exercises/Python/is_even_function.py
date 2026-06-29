
def is_even(input_num):
    return input_num % 2 == 0

input_num = 0

while(True):
    try:
        input_num = int(input('Please enter a valid integer number and I will tell you whether it is an even number or not: '))
        break
    except ValueError:
        print('Input was wrong, please enter a valid integer number next time.')

print(is_even(input_num))

