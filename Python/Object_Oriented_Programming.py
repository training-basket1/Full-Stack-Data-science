class Person:
    def __init__(self , name , last_name , age , salary ):
        self.name = name ## instance variable
        self.age = age
        self.salary = salary
        self.last_name = last_name

    def full_info(self): ## methods
        return f"my name is {self.name} and my age is {self.age}"

P1 = Person("rahul" , "singh" , 34 , 45000)
P2 = Person("shivam" , "bharti" , 43 , 55000)

print(P1.full_info())
        

class Laptop:
    def __init__(self , brand_name , model , price):
        self.brand_name = brand_name
        self.model = model
        self.price = price

    def discount(self , num):
        return self.price - (num / 100) * self.price



L1 = Laptop("Hp" , "abc123" , 34000)
L2 = Laptop("Asus" , "mvgf" , 56000)

print(L1.discount(12))



class Height():

    def converter(self ,num):
        return 2.54 * 12* num


H1 = Height()
print(H1.converter(6.2))


class Circle:
    pi = 3.14## class variable
    def __init__(self , radius ):
        self.radius = radius
        

    def circumference(self):
        return 2*Circle.pi *self.radius




C1 = Circle(5 )
C2 = Circle(4 )
print(C1.circumference())


## Inheritance
class Phone:
    def __init__(self , brand , model , price):
        self.brand = brand
        self.model = model
        self.price = price

    def full_name(self):
        return f"{self.brand} {self.model} {self.price}"



class Smartphone(Phone):
    def __init__(self , brand , model , price , ram , internal_memory , battery):
        super().__init__(brand , model , price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.battery = battery

    def specification(self):
        return f"brand : {self.brand} model : {self.model} ram : {self.ram} internal_memory : {self.internal_memory} price : {self.price}"
        
        

Phone1 = Phone("Realme" , "Narzo" , 13000)
Phone2 = Phone("LG" , "g7plus" , 50000)
s1 = Smartphone("Redmi" , "9power" , 11000 , "4GB" , "64GB" , "6000MZ")
print(s1.specification())


## Multilevel Inheritance

class Phone:
    def __init__(self , brand , model , price):
        self.brand = brand
        self.model = model
        self.price = price

    def full_name(self):
        return f"{self.brand} {self.model} {self.price}"



class Smartphone(Phone):
    def __init__(self , brand , model , price , ram , internal_memory , battery):
        super().__init__(brand , model , price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.battery = battery

    def specification(self):
        return f"brand : {self.brand} model : {self.model} ram : {self.ram} internal_memory : {self.internal_memory} price : {self.price}"


class Super_smartphone(Smartphone):
    count = 0
    def __init__(self , brand , model , price , ram , internal_memory , battery,front_camera):
        Super_smartphone.count = Super_smartphone.count+1
        super().__init__(brand , model , price , ram , internal_memory , battery) 
        self.front_camera = front_camera

    def product_info(self):
        return f"{self.brand} {self.front_camera}"

    def instance_count(self):
        return f"i have created {Super_smartphone.count} instances"

    def __add__(self , other): ## dunder methods/ special methods
        return self.price + other.price
        


S1 = Super_smartphone("samsung" , "abc123" , 43900 , "5GB" , "234GB" , "6000MH" , "15MP")
S2 = Super_smartphone("samsung" , "ab" , 70000 , "5GB" , "256GB" , "5000MH" , "15MP")

print(S1.instance_count())
print(S1 + S2)


class A:

    def method_A(self):
        return "this is method A"

    def hello(self):
        return "this is hello method"



class B:
    def method_B(self):
        return "this is method B"

    def hello(self):
        return "this is hello function"

class C(A , B):
    pass

C1 = C()

print(C1.hello())

#print(help(C))


from prem import Person

P1 = Person("rishab" , "sagar" , 345678)

print(P1.full_name())

print(s1.brand)
