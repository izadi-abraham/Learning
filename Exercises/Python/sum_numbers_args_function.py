
def sum_numbers(*args):
    sum = 0
    for number in args:
        sum += number

    print(f"you passed {len(args)} numbers and sum of all the numbers is {sum}")

input_numbers = []
wrong_input = True

while(wrong_input):
    try:
        input_numbers = input("Please enter list of numbers seperated by comma and I will return sum of all the numbers: ")
        input_numbers = list(map(int, (num.strip() for num in input_numbers.split(','))))
        wrong_input = False
    except ValueError:
        print("Inputs were not correct, please enter your numbers again.")

sum_numbers(*input_numbers)