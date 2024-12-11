# Day4


# Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
Age=int(input("Enter the Age "))
if Age<18:
    print("Your are not eligiable for vote")
else:
    print("Your are eligiable for vote")

# Write a Python program that determines if a given year is a leap year or not

Year=int(input("Enter the Year :"))
if Year%4==0:
    print("Yes it's Leap Year")
else:
    print("No a Leap Year")


# Create a Python program that checks if a user-given number is positive, negative, or zero.

Number=int(input("Enter the Number :"))
if Number<0:
    print(Number,"It's a negative number")
elif Number>0:
    print(Number,"It's a positive number")
else:
    print(Number,"It's Zero")

# Write a Python program that determines the largest of three numbers entered by the user.
a=int(input("Enter the Number :"))
b=int(input("Enter the Number :"))
c=int(input("Enter the Number :"))

if a>b and a>c:
    print(a,"a is largest ")
elif b>a and b>c:   
    print(b,"b is largest")
else:
    print(c,"c is largest")    



# A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively. Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

    Product = int(input("Enter the product number (1 for Battery Code , 2 for Key code , 3 for Charging Code :)"))
    order_amount = int(input("Enter the amount :"))
 
    discount= 0
 
    if Product == 1:
      if order_amount > 1000:
       discount =0.10*order_amount

    elif Product == 2:
       if order_amount > 100:
            discount = 0.05 * order_amount
    elif Product == 3:
        if order_amount > 500:
            discount = 0.10 * order_amount
    else:       
      print("Invalid code")

    net_amount = order_amount - discount
    print("Net amount to be paid is", net_amount)

    # 5. A transport company charges the fare according to following table:

   
   
    distance = float(input("Enter the distance :"))
    if 1 <= distance <= 50:
        fear= distance*8
     
    elif 51 <= distance <=100:
        fear =  fare = (50 * 8) + ((distance - 50) * 10)
        
    elif distance >100:
        fear =  fare = (50 * 8) + (50 * 10) + ((distance - 100) * 12)
    else:
        print("invalid")
        fear=0

    print(f"The total fare is: Rs. ",fear)