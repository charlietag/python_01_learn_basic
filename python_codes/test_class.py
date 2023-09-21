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

        # variable no need to declare in __init__
        local_var_test = "test local method var"
        print(local_var_test)

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

class Post:
    # Initial
    def __init__(self):
        self.titles = []
    # new post
    def add_post(self, title):
        self.titles.append(title)
    # delete post
    def delete_post(self, title):
        self.titles.remove(title)


a = Post()
a.titles = [
    "asdfasdf"
]
a.add_post("cccc")
print(a.titles)
