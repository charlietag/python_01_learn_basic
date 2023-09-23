import datetime

# ---------------------------------------
# test class
# ---------------------------------------
class Person:

    def __init__(self, birth):
        self._birth = birth
        now = datetime.datetime.now()
        self._age = now.year - self._birth

    def my_age(self):
        return self._age

    # -----------------------
    # getter, setter are not quite useful in Python
    # in Python, it is easy to set class variable
    # -----------------------

    # --- getter ---
    # easily define a method (ex. age()) to display var (ex. age)
    # in ruby:
    # attr_reader :age
    @property
    def age(self):
        return self._age

    # --- setter ---
    # easily define a method (ex. age()) to setup var (ex. age)
    # in ruby:
    # attr_writer :age
    @age.setter
    def age(self, new_age):
        self._age = new_age

# ---------------------------------------
# main
# ---------------------------------------

if __name__ == "__main__":
    p = Person(1984)

    # call method without getter - require parenthesis p.my_age()
    print(p.my_age())
    # 39

    # call getter - no need parenthesis p.age
    print(p.age)
    # 39

    p.age = 88
    print(p.age)
    # 88

