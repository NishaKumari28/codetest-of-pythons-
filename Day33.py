# LAB 3

# . Using input() function take one number from the user and using ternary operators check whether the number is even or odd

num = int(input("Enter a number: "))

result = "Even" if num % 2 == 0 else "Odd"

print(f"The number {num} is {result}.")



# Day3

# 1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd 

number =int(input("Enter a Number :"))
if number%2==0:
    print(number," IS even number")
else:
    print(number,"Is odd Number")

# 2. Using input function take two number and then swap the number 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

temp=num1
num1=num2
num2=temp

print(num1)
print(num2)

# 3. Write a Program to Convert Kilometers to Miles 

kmph=float(input("Enter a KiloMeter Number :"))

miph = (kmph * 0.6213712); 

print("Convert Kilometer into miles",miph)

#4 Find the Simple Interest on Rs. 200 for 5 years at 5% per year.

principal = float(input("Enter the Principal amount :"))
rate = float(input("Enter the Interest :"))
time = float(input("Enter the Time :"))

simple_interest =(principal*rate*time)/100
print("the simple interest is:",simple_interest)