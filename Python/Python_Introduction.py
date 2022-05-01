## Print Function : Use to print something on screen.
print("hello world")

# we can do any mathematical operations inside of print function
print(5 + 4) 
print(10 /5)

### String : collection of characters inside Double quotes or Single quotes
print('hello world')

## Escape sequences

#1. \" ---- Double quote
#2. \' ------ Single quote
#3. \\ ------- Backslash
#4. \n ------- New line
#5. \t -----   tab space
#6. \b -------  Backspace

print("Training \n Basket")
print("Training \t Basket")

## Comments : It is for user only


## Variables : It is like a container in which we can store anything
number = 7
name = "Rahul"

## Rules for variable

#1. we can not start our variable with any number like 0 1, 2 , 3....
#2. we can start it from any letter , _
#3. we can not use any special symbol in variable

## String Concatenation :

first_name = "Rahul"
last_name = "Singh"
Full_name = first_name + " " + last_name
print(Full_name)

## Note : We can multiply a string by a number but we can not add a number with a string


## User input :
name = input("please enter you name : ")
age = int(input("please enter your age"))

## Note : it will always take input from user in the form of strings

## String Formatting : we can easily write the code in easy way

print(f"hello {name} my age is {age}")

## Normally we use
print("Hello " + name + " "  + "your age is " + str(age))


### String Indexing :
#  -6  ---------- p ------------- 0
#  -5  ---------- y ------------- 1
#  -4  ---------- t ------------- 2
#  -3  ---------- h ------------- 3
#  -2  ---------- o ------------- 4
#  -1  ---------- n ------------- 5

name = "Prem kumar bharti"
print(name[2])
print(name[2:-1 : 2]) # start : end : step

## string Methods :
#1. lower() : it converts all alphabet in lower case
name = "Prem"
print(name.lower())

#2. upper() : it converts all alphabet in upper case letter
print(name.upper())

#3. title() : it converts first letter of word into capital letter
print(name.title())

#4. count() : it counts the same character in a word or string and it is case sensitive
print(name.count("P"))

#5. replace() : it is used to replace a word , character space with anything
print(name.replace("P" , "C"))

#6. find() : it is used to for finding the word , character in our string
print(name.find("r"))

## len() function : it counts the character of string
print(len(name))

## Note : Strings are immutable --- if you define the strings onces you can not change that defined string.

## Operators :
#1. Airthmatic  operator : 
# +	Addition	x + y	
# -	Subtraction	x - y	
# * 	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y

#2. Assignment operator : 
# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	
# **=	x **= 3	x = x ** 3	
# &=	x &= 3	x = x & 3	
# |=	x |= 3	x = x | 3	
# ^=	x ^= 3	x = x ^ 3	
# >>=	x >>= 3	x = x >> 3	
# <<=	x <<= 3	x = x << 3

#3. Comparison operator :
# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y

#4. Logical operators :
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)










































































