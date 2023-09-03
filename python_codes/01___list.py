# this is just like array
names = [
    "Charlie",
    "Welly",
]

print(len(names))
print(names[0])
print(names)

names.append("Ohoh")
print(names)

# This will remove last one elememt "ohoh"
names.pop()
print(names)

names.extend(["newGuy", "badGuy"])
print(names)

names.remove("Charlie")
print(names)

names.insert(0, "Charlie")
names.insert(1, 1984)
print(names)

def print_help():
    print("help function")

print_help()


def list_name():
    for name in names:
        show_name = "Welcome, " + str(name)
        print(show_name)

list_name()
