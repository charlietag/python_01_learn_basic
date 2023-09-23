# -----------------------------------------------------
# Test - Basic class (special use --- pass)
# -----------------------------------------------------
class Special:
    def __init__(self):
        # Cannot be empty, so add continue method - pass
        pass

s = Special()
s.name = "Anne"
print(s.name)
# Anne

# amazing... no need , getter and setter
# no even need to setup class variable or instance variable first


# -----------------------------------------------------
# Test 1 - Basic class
# -----------------------------------------------------
class MyClass:
    # class variable
    x = 5

# attributes x becomes instance variable in namespace (c1)
# --- bad ---
# c1 = MyClass
# --- good ---
c1 = MyClass()

print(c1.x)
# 5

c1.x = "X 2"
print(c1.x)
# X 2

c2 = MyClass()
print(c2.x)
# 5

# attributes try_name becomes instance variable in namespace (c1)
c1.try_name = "try Name"
print(c1.try_name)
# try Name

print()
print("-------------------------")
print()

# -----------------------------------------------------
# Test 2 - class with __init__ and method
# -----------------------------------------------------
class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # python class built-in method
    def __str__(self):
        return f"{self._name}({self._age})"

    def my_func(self):
        print("Hi, my name is " + self._name)

        # variable no need to declare in __init__
        local_var_test = "- test local method var -"
        print(local_var_test)

c1 = Person("Brad", 35)

print(c1._name)
# Brad

print(c1._age)
# 35

# This will call __str__
print(c1)
# Brad(35)

c1.my_func()
# Hi, my name is Brad
# - test local method var -

print("\n-------------------------\n")

c1.name = "Anne"
c1.age = 7
print(c1.name)
# Anne
print(c1.age)
# 7

# This will call __str__
print(c1)
# Brad(35)

c1.my_func()
# Hi, my name is Brad
# - test local method var -

print("\n-------------------------\n")

# -----------------------------------------------------
# Test 3 - class with __init__ and method + call self.method in class
# -----------------------------------------------------
class Post:
    name = "ccc"

    # Initial
    def __init__(self):
        self._titles = []
        self.call_another_method()

    # new post
    def add_post(self, title):
        self._titles.append(title)

    # delete post
    def delete_post(self, title):
        self._titles.remove(title)

    def call_another_method(self):
        print("- this line is called from __init__ -")


a = Post()
# - this line is called from __init__ -

a._titles = [
    "asdfasdf"
]
a.add_post("cccc")
print(a._titles)
# ['asdfasdf', 'cccc']
