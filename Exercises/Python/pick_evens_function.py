
def pick_evens(*args):
    evens = []
    for number in args:
        if number % 2 == 0:
            evens.append(number)

    print(f"you passed {len(evens)} even numbers out of {len(args)} numbers and the even numbers were", *evens)

input_numbers = []
wrong_input = True

while(wrong_input):
    try:
        input_numbers = input("Please enter list of numbers seperated by comma and I will return all the even numbers: ")
        input_numbers = list(map(int, (num.strip() for num in input_numbers.split(','))))
        wrong_input = False
    except ValueError:
        print("Inputs were not correct, please enter your numbers again.")

pick_evens(*input_numbers)