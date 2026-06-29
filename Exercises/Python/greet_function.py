
def greet(name):
    print(f"Hello, {name}")

def is_valid_name(name):
    return len(name.strip()) > 0


input_name = input('Please enter your name: ')

while (not is_valid_name(input_name)):
    input_name = input('Please enter a valid name: ')


greet(input_name)