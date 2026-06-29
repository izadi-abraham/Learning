
def divide(a, b):
    result = a / b
    return result

while(True):
    try:
        num1 = int(input("Enter first number: "))
        break
    except ValueError as e:
        print("You did not enter a number. Please try again!")

while(True):
    try:
        num2 = int(input("Enter second number: "))
        if num2 == 0:
            raise ZeroDivisionError
        else:
            break
    except ValueError as e:
        print("You did not enter a number. Please try again!")
    except ZeroDivisionError as e:
        print("Second number can not be zero, it causes a Zero division error. Please try again!")


try:
    result = divide(num1, num2)
    print(f"Result: {result}")
except Exception as e:
    print("Sorry there was an error!")
finally:
    print("The program ran successfully!")



