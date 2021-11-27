with open("data.txt" , "r") as f: ## r --- read
    print(f.readlines())


with open ("rahul.txt" , "w") as f: ## w ---- write
    f.write("hello rahul")

with open ("rahul.txt" , "a" ) as f: ## a ---- append
    f.write("I am waiting for job")




from prem import Person

P1 = Person("rahul" , "kumar" , 45000)
print(P1.full_name())

