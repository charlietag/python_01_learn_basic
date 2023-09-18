# Ref. https://builtin.com/software-engineering-perspectives/python-pathlib
# Ref. https://betterprogramming.pub/should-you-be-using-pathlib-6f3a0fddec7e
# Ref. https://docs.python.org/3/library/pathlib.html#correspondence-to-tools-in-the-os-module

from pathlib import Path

this_home = Path.home()
print(this_home)

this_file = __file__
print(this_file)

p = Path(this_file)

this_file_basename = p.name
print(this_file_basename)

# this_file_
