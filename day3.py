'''def sum():
    a=int(input("num"))
    b=int(input("num"))  # type 1
    c=a+b
    print(c)
sum()



def sum(a,b):
    c=a+b
    print(c)
    
a=int(input("num"))     #TYPE 2
b=int(input("num"))
sum(a,b)




def sum(a,b):
    c=a+b
    return(c)
a=int(input("num"))
b=int(input("num"))  # type 3
res=sum(a,b)
print(res)

def pow(a,b):
    c=a**b
    print(c)
    
a=int(input("num"))
b=int(input("num"))

pow(a,b)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n= int(input("Enter a number: "))

res=factorial(n)
print(res)'''

def show():
    def display():
        print("display")
    display()
    print("show")
show()

            
