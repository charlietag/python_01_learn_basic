import datetime

class Person:
    def __init__(self, birth):
        self.birth = birth
    @property
    def age(self):
        now = datetime.datetime.now()
        age = now.year - self.birth
        return age
#
p = Person(1984)
print(p.age)
# p.age = 3
print(p.age)

# now = datetime.datetime.now()
# aage = now.year - 1984
# print(aage)

