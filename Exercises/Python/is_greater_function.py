
def is_greater(a, b):
    return a > b

input_nums = []
a, b = (0, 0)

while(True):
    try:
        a, b = map(int, input('Please enter "a" and "b" numbers, separated by a space and I will tell you whether a is bigger than b or not: ').split(' '))
        break
    except ValueError:
        print('Input numbers were wrong, please enter valid numbers again.')

print(is_greater(a, b))

