print("Hello World")



variable = "I am a global variable"

def my_function():
   
    variable = "I am a local variable"
    print("Inside the function:", variable)  

my_function()


print("Outside the function:", variable)  

string=str(input("Enter the String :"))
int=int(input("Enter the Int :"))
float=float(input("Enter the Float :"))
print(string)
print(int)
print(float)