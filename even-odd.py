def check_even_odd(number):
    if number % 2 == 0:
        result = "even"
    else:
        result = "odd"
    
    return result

# Take input from the user
user_input = input("Enter a number: ")
try:
    num = int(user_input)
    result = check_even_odd(num)
    print(f"The number {num} is {result}.")
except ValueError:
    print("Please enter a valid integer.")