# dir(var) - display what functions, methods exists in var


def show_msg():
    # print("msg")
    return "--msg--"

a = show_msg()
print(dir(a))
print(dir("str"))
for i in range(10):
    print(i)
import sys
print(dir(sys))
