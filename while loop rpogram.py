# 1.Write a python program to reverse a number using a while loop.

def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Add the digit to the reversed number
        num = num // 10  # Remove the last digit from num
    return reversed_num

number = int(input("Enter a number: "))

# Call the function and display the reversed number
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)

# 2. Write a python program to check whether a number is palindrome or not?
def is_palindrome(num):
    original_num = num  # Store the original number
    reversed_num = 0
    
    # Reverse the number
    while num > 0:
        digit = num % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Add the digit to the reversed number
        num = num // 10  # Remove the last digit
    
    # Check if the original number is equal to the reversed number
    if original_num == reversed_num:
        return True
    else:
        return False

number = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

#3. Write a python program finding the factorial of a given number using a while loop.


def factorial(num):
    result = 1
    while num > 0:
        result *= num  # Multiply the result by the current number
        num -= 1  # Decrease the number by 1
    return result
number = int(input("Enter a number: "))

# Check if the number is non-negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate and display the factorial
    fact = factorial(number)
    print(f"The factorial of {number} is {fact}.")
#4. Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.

# Initialize a variable to store the sum of numbers
total_sum = 0
while True:
    number = int(input("Enter a number (enter 0 to stop): "))
    if number == 0:
        break
    total_sum += number
print(f"The sum of all entered numbers is: {total_sum}")


    
    
