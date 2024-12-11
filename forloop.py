#. 1. Print the first 10 natural numbers using for loop
for num in range(1, 11):
    print(num)
#2. Python program to check if the given string is a palindrome
def is_palindrome(string):
    # Convert the string to lowercase to make the check case-insensitive
    string = string.lower()
    
    # Reverse the string and compare with the original string
    if string == string[::-1]:
        return True
    else:
        return False

# Input from user
input_string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
