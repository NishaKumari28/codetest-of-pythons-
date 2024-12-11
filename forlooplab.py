# 1. Print the first 10 natural numbers using for loop
for i in range(1, 11):
    print(i)

# 2. Python program to check if the given string is a palindrome
def is_palindrome(s):
    s = s.lower()  # Convert to lowercase
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

s = input("Enter a string: ")
if is_palindrome(s):
    print(s, "is a palindrome.")
else:
    print(s, "is not a palindrome.")

#3. Python program to check if a given number is an Armstrong number
def is_armstrong(n):
    # Convert the number to a string to find its length
    num_str = str(n)
    num_len = len(num_str)

    # Initialize a variable to store the sum of the digits
    sum_of_digits = 0

    # Iterate over each digit in the number
    for digit in num_str:
        # Add the cube of the current digit to the sum
        sum_of_digits += int(digit) ** num_len

    # Check if the sum of the digits is equal to the original number
    return sum_of_digits == n

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
#4. Python program to get the Fibonacci series between 0 to 50
def fibonacci_series(n):
    fib_series = [0, 1]
    for i in range(2, n+1):
        next_num = fib_series[i-1] + fib_series[i-2]
        if next_num > n:
            break
        fib_series.append(next_num)
    return fib_series

n = 50
fib_series = fibonacci_series(n)
print("Fibonacci series between 0 to", n, "is:")
for num in fib_series:
    print(num)

# 5. Python program to check the validity of password input by users
import re

def validate_password(password):
    # Define the password validation rules
    rules = [
        lambda p: len(p) >= 8,  # Password should be at least 8 characters long
        lambda p: len(p) <= 32,  # Password should be at most 32 characters long
        lambda p: any(c.isupper() for c in p),  # Password should have at least one uppercase letter
        lambda p: any(c.islower() for c in p),  # Password should have at least one lowercase letter
        lambda p: any(c.isdigit() for c in p),  # Password should have at least one digit
        lambda p: any(c in "!@#$%^&*()_+-=" for c in p),  # Password should have at least one special character
        lambda p: not re.search(r"\s", p)  # Password should not have any whitespace characters
    ]

    # Check if the password passes all the validation rules
    for rule in rules:
        if not rule(password):
            return False

    return True

password = input("Enter a password: ")
if validate_password(password):
    print("Password is valid.")
else:
    print("Password is not valid. Please ensure it meets the following criteria:")
    print("  * At least 8 characters long")
    print("  * At most 32 characters long")
    print("  * Has at least one uppercase letter")
    print("  * Has at least one lowercase letter")
    print("  * Has at least one digit")
    print("  * Has at least one special character")
    print("  * Does not have any whitespace characters")
























