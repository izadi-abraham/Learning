
def sum_of_squares(num1, num2):
    return pow(num1, 2) + pow(num2, 2)

wrong_input = True


while(wrong_input):
    input_num = input("please enter two integer number separated by a space: ")

    try:
        input_array = input_num.split(' ')
        
        if len(input_array) != 2:
            raise ValueError()
        num1 , num2 = map(int, input_array)
        print(sum_of_squares(num1, num2))
        wrong_input = False

    except ValueError:
        input_num = input("Numbers were not correct. Please enter two integer number seperated by a space: ")
        
