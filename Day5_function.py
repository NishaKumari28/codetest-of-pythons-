# Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
def div(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("The result of division is:", a / b)

div(60, 30)  


# Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number . 3. Using max() and min() functions display the maximum and minimum of 5 random numbers. 
def square(num):
    return num ** 2


result = square(3)
print("The square of 3 is:", result)
import random
numbers = [random.randint(1, 100) for _ in range(5)]
print("Random numbers:", numbers)
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))


# Accept a name from the user and display that in lower case using lower() function 


name = input("Enter your name: ")


print("Your name in lowercase is:", name.lower())
