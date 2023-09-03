class MyClass:
    x = 5

p1 = MyClass
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
    def my_func(self):
        print("Hi, my name is " + self.name)

p1 = Person("Charlie", 35)
print(p1.name)
print(p1.age)
print(p1)
p1.my_func()

p1.name = "Welly"
p1.age = 7
print(p1.name)
print(p1.age)
print(p1)
p1.my_func()

