## if statements :
age = int(input("enter your age"))
if age >18:
    print("you are above 18")

## Pass statements
if age > 56 :
    pass
## Note : if we don't have to write anything in the blocks then we will use pass

## if else statements
age = int(input("enter your age"))
if age >18:
    print("Adult")
else:
    print("Not adult")


## if elif  else statements
age = int(input("enter your age"))
if 0 <age < 3:
    print("ticket price is free")
elif 3<age<= 10:
    print("ticket price is 200")

elif 10 <age<=60:
    print("ticket price is 300")

else:
    print("ticket price is 150")

## Nested if- else statements
winning_number = 42
chance = 0
while True:
    number = int(input("enter any number between 1 and 100 : "))
    chance +=1
        
    if number == winning_number:
        print("you have won this game")
        
        print(f"you have guessed this number in {chance} chances ")
        break

    elif chance >=3:
        print("you loose")
        break
    
    else:       
        if number < 1 or number > 100:
            print("please choose number in the range 1 to 100")
        elif number > 42 and number < 100:
            print("the number you have entered is larger than winning number")
        else :
            print("the number you have entered is smaller than winning number")


## While loop :
i = 1
while i<=10:
    print("hello world")
    i+=1
    # it will print hello world ten times

## Infine loop:
    while True:
        print("hello world")


## For loop :
        for i in range(1 , 11):
            print("hello world")


## Break  : it is used to break the loop
for i in range(1,11):
    if i == 5:
        break
    print(i)

## continue:
for i in range(1 , 11):
    if i==5:
        continue
    print(i)





    





    
