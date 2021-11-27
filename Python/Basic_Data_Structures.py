## List
#it is a data structure
# collection of items
# you can store anything in list

numbers = [1,2,3,4,5,6]
print(numbers)

num = list(range(1,11)) ### start : end : step
print(num)

##Note :  we can access all the data from list

numbers = ["shivam" , 23 , 56.5 , [1,2,3,4]]
print(numbers)
print(type(numbers))
print(numbers[0][3])
print(numbers[3][2])

## looping in list
char = ["a" , "b" , "c" , "d" , "e"]
for i in char:
    print("shivam")


########################## List Methods #############################################
# 1. Append
names = ["prem" , "aniket" , "shivam" , "shalu" , "kajal"]
names.append("rahul")
print(names)

#2. insert
number = [1,2,3,4,5]
#number.insert(3, 78)
#print(number)


################# delete data from list ##############33

#1. pop
number.pop(2)
print(number)

#2. remove

name = ["prem" ,"rahul" , "mohit"]
name.remove("rahul")
print(name)

## sort
num = [5 , 4 , 1 , 2 , 67]
num.sort()
print(num)

##copy

a = [1,2,3,4,5]
b = a.copy()
b.pop()
print(b)

### even odd
num1 = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []
for i in num1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)

############################# Dictionary  ########################################
user_info = {
       "name" : "aniket",
       "age" : 25,
       "fav_movies" : ["gadar" , "end_game" , "agneepat" , "avengers"],
       "fav_sports" : ["cricket" , "basketball" , "hockey"]
    }

print(user_info["fav_movies"][2])
user_info["fav_movies"].pop()
for i in user_info.keys():
    print(i)

for i in user_info.values():
    print(i)

for k , v in user_info.items():
    print(f"{k} : {v}")

## add data into dictionary
user_info["games"] = ["card", "asphlt" , "bgmi" , "candycrush"]
print(user_info)


##update method
more_info = {
            "mobile" : "samsunf",
            "device" : "laptop" 
    }
user_info.update(more_info)
print(user_info)

## we can also use clear and copy method in dictionary

## sets
## unordered collection of unique items

s = {1 ,2, 3, 4, 4, 4, 5}
print(s)

# add()
s.add(6)

# remove()
s.remove(4)

# clear
s.clear()

## Note : we can not store dictionary and list in sets.

## Tuple :
# tuple can store any data type
# Most important tuples are immutable, Once tuple is updated you cant change it.
# no append , npo insert , no pop , no remove
# tuples are faster than list

num = (1,)
print(num)

number = (1,2,3,4,5,6,7)
print(number)

mixed = ("rahul" , "prem" , [1,2,3,4])
mixed[2].pop()

## Note : we can edit list that is present inside the tuple


## List Comprehention : with the help of list comprehention we can create list in one line
#################################3Comprehention############################
""" without list comprehention """
num = []
for i in range(1,21):
    if i%2==0:
        num.append(i**2)
    else:
        num.append(i**3)
    
    
    
number = [i for i in range(1,21)]    #append, for loop

number = [i for i in range(1,21) if i%2==0] ## append for loop condition


""" with list Comprehention """
number = [i**2 if i%2==0 else i**3 for i in range(1,21) ] # append codition for loop
print(number)
print(num)

## Find hcf of two numbers
""" without list comprehention """
a = int(input("enter first number : "))
b = int(input("enter second number : "))
for i in range(1 , min(a,b)+1):
    if a%i==0 and b%i==0:
        hcf = i
print(hcf)

""" with list Comprehention """
hcf = [i for i in range(1 , min(a , b)+1) if a%i==0 and b%i==0]
print(hcf[-1])


## dictionary comprehention

even = {i : "even" if i%2==0  else "odd" for i in range(1 , 11) }
print(even)














































