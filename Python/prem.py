class Person:
    def __init__(self , name , last_name , salary):
        self.name = name
        self.last_name = last_name
        self.salary = salary

    def full_name(self):
        return f"{self.name} {self.last_name}"

if __name__ == "__main__":
    print("hello  world")

