# a = "abc"
a = 1
try:
    b = int(a)
    c = b * 2
    print(c)
except Exception as e:
    print(e)
else:
    print("go if no error")
finally:
    print("go no matter error exists, or not")
