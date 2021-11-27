### Iterator --- filter , map , reduce , etc
### iterables -- list , string , tuples ,etc

num = list(range(1,21))

def is_even(a):
    return a%2==0
#print(is_even)

even = filter(is_even , num)

#for i in even:
    #print(i)


############################ Map , reduce , filter  ###########################
even1 = list(even)
for i in even1:
    print(i)
    
for i in even1:
    print(i)

odd = list(filter(lambda a : a%2!=0 , num))
print(odd)

### map

square = tuple(map(lambda a : a**2 , num))
print(square)

### reduce

import functools


def add(a , b):
    return a+b


a = functools.reduce(add , num )
print(a)

num = list(range(1 , 21))
multy = functools.reduce(lambda a , b : a*b , num)

######################### Closers ################################
def outer(name):
    def inner():
        print(f"this is inner function of {name}")
    return inner
abc = outer("prem")
abc()

def to_power(x):
    def cal_power(n):
        return n**x
    return cal_power
cube = to_power(3)
cube(5)


################## Decorators : Enhance the functionailty of other functions

def decorator_function(any_function):
    def wrapper_function(*args , **kwargs):
        print("this is  caculator function")
        return any_function(*args , **kwargs)
    return wrapper_function



@decorator_function
def calculator(a , b):
    add = a+b
    multy = a*b
    return add , multy

print(calculator(5 , 5 ))

from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    
    def wrapper_function():
        """ this is wrapper function """
        print("this is awesome function")
        return any_function()
    return wrapper_function


@decorator_function
def prem():
    """ this is prem function """
    return "this is prem"

print(prem())

print(prem.__doc__)


#wrap = decorator_function(prem)
#print(wrap.__doc__)
#print(wrap())



@decorator_function
def func():    
    return "hello world"

print(func())

@decorator_function
def prem():
    return "this is prem"
print(prem())


##################################### Generators ########################
# generators are iterators
#1. using function
def nums(n):
    for i in range(1 , n+1):
        yield(i)
nums(10)

#2. using tuple comprehention
square = (i**2 for i in range(1,11))
for i in square:
    print(i)


########### List vs generator ####################
import time
t1 = time.time()
g = (i**2 for i in range(1 , 1000000000000))
t2 = time.time()
total = t2-t1
print(total)


t1 = time.time()
l = [i**2 for i in range(1 , 100000)]
t2 = time.time()
total = t2-t1
print(total)










    







