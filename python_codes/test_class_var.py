# -----------------------------------------------
# Failed
# -----------------------------------------------
class Name:
    def __init__(self):
        self._name = "Charlie"
        return self._name

n = Name()
print(n) # TypeError: __init__() should return None, not 'str'

# -----------------------------------------------
# class access instance var
# -----------------------------------------------
class Name:
    def __init__(self):
        self._name = "Charlie"

n = Name()
print(n) # <__main__.Name object at 0x7f21ff6b3750>
print(n._name) # Charlie

# -----------------------------------------------
# class __str__
# -----------------------------------------------
class Name:
    def __init__(self):
        self._name = "Charlie"

    def __str__(self):
        return self._name

n = Name()
print(n) # Charlie
