"""
In Python, variable names starting with underscores have special meaning, and the number of underscores at the beginning of a variable name affects its accessibility and visibility. Here's the difference between `_var_a` and `__var_b` in your example:

1. `_var_a`:
   - A single leading underscore (`_`) is a convention in Python to indicate that a variable is intended to be "protected," meaning it should not be accessed directly from outside the class or module. However, it is not enforced by the language itself, and the variable can still be accessed if desired.
   - `_var_a` is not private or hidden; it can be accessed and modified from outside the class if you have access to an instance of the `Person` class.

2. `__var_b`:
   - A double underscore (`__`) at the beginning of a variable name invokes name mangling in Python. Name mangling is a mechanism that adds a prefix to the variable name based on the class name to make it harder to accidentally override in subclasses.
   - In this example, `__var_b` is actually stored as `_Person__var_b` within the class. This means that it's not directly accessible from outside the class using its original name.
   - To access `__var_b` from outside the class, you would need to use the mangled name: `instance._Person__var_b`.

Here's an example to illustrate how these variables can be accessed:
<Codes shows below>

In practice, the use of a single leading underscore (`_var_a`) is a signal to other developers that the variable is intended for internal use and should not be accessed directly. However, it doesn't provide strict encapsulation or privacy. Double underscores (`__var_b`) provide stronger name mangling to prevent accidental access but are not completely private and can still be accessed if needed.
"""

class Person:
    def __init__(self):
        self._var_a = "a"
        self.__var_b = "b"

# Create an instance of the Person class
person = Person()

# Accessing _var_a (protected variable)
print(person._var_a)  # Outputs: "a"

# Accessing __var_b (name mangling)
# This will raise an AttributeError because the mangled name is used.
# print(person.__var_b)  # Raises an AttributeError

# Accessing __var_b using the mangled name
print(person._Person__var_b)  # Outputs: "b"

