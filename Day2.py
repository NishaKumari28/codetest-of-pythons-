# LAB 2
# Calculate the multiplication and sum of two numbers
a=float(input("Enter the fist Number"))
b=float(input("Enter the Second Number"))

c=a*b

print(c,"Multiplication of two number")


# Declare two variables and print that which variable is largest using ternary operators
a = 15
b = 10


largest = a if a > b else b


print(f"The largest number is: {largest}")

# 3. Python program to convert the temperature in degree centigrade to Fahrenheit



temp_celsius = float(input("Enter temperature in Celsius: "))


temp_fahrenheit = (temp_celsius * 9/5) + 32


print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F")

# 4 Python program to find the area of a triangle whose sides are given

import math

# Get user input for the sides of the triangle
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))


s = (side1 + side2 + side3) / 2


area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))


print(f"The area of the triangle with sides {side1}, {side2}, and {side3} is: {area:.2f}")


# Day2
a =30
b =20

print("Arithmetic Operations:")
print(f"Addition: {a} + {b} = {a + b}")        
print(f"Subtraction: {a} - {b} = {a - b}")     
print(f"Multiplication: {a} * {b} = {a * b}")  
print(f"Division: {a} / {b} = {a / b}")        
print(f"Modulus: {a} % {b} = {a % b}")          
print(f"Exponentiation: {a} ** {b} = {a ** b}")  
print(f"Floor Division: {a} // {b} = {a // b}")   




number = 10

print(f"Initial value: {number}")


number = 15
print(f"After simple assignment: {number}")


number += 5  
print(f"After addition assignment (number += 5): {number}")


number -= 3  
print(f"After subtraction assignment (number -= 3): {number}")


number *= 2  
print(f"After multiplication assignment (number *= 2): {number}")


number /= 4  
print(f"After division assignment (number /= 4): {number}")


number %= 3  
print(f"After modulus assignment (number %= 3): {number}")


number **= 2  
print(f"After exponentiation assignment (number **= 2): {number}")


number //= 2  
print(f"After floor division assignment (number //= 2): {number}")



a = 13
b = 15

c = a + b 
print(c)


a = 13
b = 15
a+=b
print(a)



a = 13
b = 15
a-=c
print(a)


a = 13
b = 15
a *= b
print(a)


a = 13
b = 15
a/=b
print(a)


a = 13
b = 15
a%=b
print(b)



a = 13
b = 15
a//=b
print(a)


a = 13
b = 15
a**=b
print(a)


# 
a=int(input("Enter the Number a :"))
b=int(input("Enter the Number b :"))
c=int(input("Enter the Number c :"))

if a>=b and a>=c:
    print(a,"a is greatest")
elif b>=a and b>=c:
    print(b,"b is greastest")
else:
    print(c,"c is greatest")

# circle
r =float(input("Enter the circumfrance :"))
r=3.14*r*r
print("The area of the circle is",r)

# triangle
base=float(input("Enter the Base :"))
height=float(input("Enter the height :"))

area = 0.5*base*height
print("triangle",area)

# rectangle

base=float(input("Enter the base of rectangle :"))
height=float(input("Enter the height of rectangle :"))
area = base*height
print("rectangle",area)

# sqaur
side=float(input("Enter the side of square :"))
area = side*side
print("square",area)


