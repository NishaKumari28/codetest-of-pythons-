
'''# oops me 2 number ko add kre?

class add():
    def sum(self,a,b):
        print("sum of two number",(a+b))
ad=add()
ad.sum(4,6)

# oops me 2 number ko substract kre?

class sub():
    def subs(self,a,b):
        print("subtraction of two number",(a-b))
subst=sub()
subst.subs(46,6)

# oops me 2 number ko guna  kre?


class mul():
    def mult(self,a,b):
        print("multiplication of two number",(a*b))
ab=mul()
ab.mult(6,6)


# oops me 2 number ko bhag kre?

class div():
    def divs(self,a,b):
        print("sum of two number",(a/b))
dv=div()
dv.divs(12,6)

# oops me 3 number ko guna  kre?

class mul():
    def mult(self,a,b,c):
        print("multiplication of two number",(a*b*c))
ab=mul()
ab.mult(6,6,2)

#multilevel inheritance me animal ke upar kch batao ?

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("{self.name} is eating.")



class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def walk(self):
        print(f"{self.name} is walking.")

class Dog(Mammal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} is barking.")

my_dog = Dog("tuffy", 3, "hssh wala dog")


my_dog.eat()    
my_dog.walk()    
my_dog.bark()    

print(my_dog.name)  
print(my_dog.age)   
print(my_dog.breed)  



class add(sub):
    def sum(self,a,b):
        return a+b
class sub(add):
    def sub(self,a,b):
        return a-b 
       
a1=add()
print(a1.sum(20,30))
print(a1.sub(20,30))

a12=sub()
print(a12.sum(120,30))
print(a12.sub(120,30))'''



class add():
    def sum(self,a,b):
        return a+b
class subs(add):
    def sub(self,a,b):
        return a-b 
       
a1=add()
print(a1.sum(20,30))
'''print(a1.sub(20,30))'''

a12=subs()
print(a12.sum(120,30))
print(a12.sub(120,30))










