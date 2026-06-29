

def is_positive(input_n):
    return input_n >= 0




input_number = ''


while(True):
    try:
        input_number = int(input("Please enter an integer number: "))
        break
    except ValueError:
        print("Invalid integer.")



if is_positive(input_number):
    print("True")
else:
    print("False")

