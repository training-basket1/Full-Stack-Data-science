## Function :
def hello():
    return "hello world"
print(hello())

def add_two(a , b):
    return a+b
a = int(input("enter first number : "))
b = int(input("enter second number : "))

total = add_two(a , b)
print(total)


## print vs return
#print -- it is used for printing the stuff on display
# return it is used to return value

def add(x , y , z):
    print(x+y+z)
add(5 , 30 , 5)

## find the greatest number out of three
def greatest(a , b , c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(greatest(30 , 20 , 5))

### function inside function
def prem():
    print("we can call any function inside of other function.")
    return hello()

print(prem())

## Default parameter : it is for the value given to parameter by default .
# if we dont overwrite this later it will be excuted

## variable scope
#1. Local variable
def function():
    x = 7
    return x
print(function())

#2. global variable
#we define global variable outside the function


## *args 
def add(*args):
    a = 0
    for i in args:
        a+=i
    return a
print(add(*(1,2,3,4,5,6)))


## **kwargs
user_info = {
          "name" : "aniket",
          "fav_games" : ["chess" , "uno" , "poker"]
    }
def user(**kwargs):
    for k , v in kwargs.items():
        print(f"{k} = {v}")
user(**user_info)


## Lambda expression
add = lambda a , b : a+b
print(add(10 , 10))

multiply = lambda a , b : a*b
print(multiply(2 , 3))

func = lambda string : True if len(string) >5 else False
print(func("prem"))



















