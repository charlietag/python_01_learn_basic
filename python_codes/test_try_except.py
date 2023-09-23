a = "abc"
# a = 1
try:
    b = int(a)
    c = b * 2
    print(c)
    # 2 --> if a = 1

except Exception as e:
    # if a = "abc"
    # print err msg: invalid literal for int() with base 10: 'abc'
    print(e)
else:
    # if a = 1
    print("go if no error")
finally:
    # if a = 1, or a = "abc"
    print("go no matter error exists, or not")
