# -----------------------------------------------------
# Test function
# -----------------------------------------------------
def print_help():
    print("----------------------")
    print("help function")
    print("----------------------")

def list_name():
    print("----------------------")
    for name in names:
        show_name = "Welcome, " + str(name)
        print(show_name)
    print("----------------------")


# -----------------------------------------------------
# List
# -----------------------------------------------------
# this is just like array
names = [
    "Bratte",
    "Tom",
]

print(len(names))
# 2

print(names[0])
# Bratte

print(names)
# ['Bratte', 'Tom']

names.append("Ohoh")
print(names)
# ['Bratte', 'Tom', 'Ohoh']

# This will remove last one elememt "ohoh"
names.pop()
print(names)
# ['Bratte', 'Tom']

names.extend(["Gracy", "Anne"])
print(names)
# ['Bratte', 'Tom', 'Gracy', 'Anne']

names.remove("Bratte")
print(names)
# ['Tom', 'Gracy', 'Anne']

names.insert(0, "Bratte")
names.insert(1, 1984)
print(names)
# ['Bratte', 1984, 'Tom', 'Gracy', 'Anne']

# -----------------------------------------------------
# Test
# -----------------------------------------------------
print_help()
# ----------------------
# help function
# ----------------------


list_name()
# ----------------------
# Welcome, Bratte
# Welcome, 1984
# Welcome, Tom
# Welcome, Gracy
# Welcome, Anne
# ----------------------

