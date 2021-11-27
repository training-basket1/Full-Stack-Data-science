
#######################################  Multithreading  #########################################

""" Without Multithreading """
import time
def square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print("square:",n*n)

def cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("cube:",n**3)

num = list(range(1,11))
t1=time.time()
square(num)
cube(num)
t2 = time.time()
t = t2-t1
print(f"i am done in {t} seconds")
print("i m done with all of my work now")


##################################################################################################

""" With Multithreading """
import time
import threading

def square(numbers):
    print("calculate square of numbers")
    time.sleep(2)
    for i in numbers :
        print(f" square : {i**2}")


def cube(numbers):
    print("calculate cube of numbers")
    time.sleep(2)
    for i in numbers :
        print(f" cube :  {i**3}")

num = list(range(1,11))

t1 = time.time()

A1 = threading.Thread(target= square , args= (num , ))

A2 = threading.Thread(target= cube , args= (num , ))


A1.start()
A2.start()

A1.join()
A2.join()

t2 = time.time()

t = t2 -t1

print(f"i am done in {t} seconds")
print("i m done with all of my work now")


########################################  Multiprocessing ######################################

""" With Multiprocessing """

import time
import multiprocessing

def square(num):
    for i in num:
        print("square" , i**2)

def cube(num):
    for i in num:
        print("cube" , i**3)


if __name__ == "__main__":

    num = [1,2,3,4,5,6,7,8,9,10]
    t1 = time.time()
    time.sleep(10)
    P1 = multiprocessing.Process(target= square , args = (num , ))
    P2 = multiprocessing.Process(target= cube , args = (num , ))
    
    time.sleep(10)
    P1.start()
    P2.start()
    

    P1.join()
    P2.join()
    
    t2 = time.time()

    t = t2 - t1
    print(f"this program is ended in {t} seconds")



















