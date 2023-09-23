# -------------------------------------------------------------------
# Sample 1
# -------------------------------------------------------------------
# from test_modules.recursive import recursive_list
from test_modules.recursive import recursive_list as r
# import test_modules.recursive
# import test_modules.recursive as r

all_lists = [
    "Charlie",
    "Welly",
    [
        "Guru",
        1988,
        [
            "Apple",
            "Samsung"
        ],
    ],
]

# recursive_list(all_lists)
r(all_lists)
# test_modules.recursive.recursive_list(all_lists)
# r.recursive_list(all_lists)


# error
# import recursive_list

# -------------------------------------------------------------------
# Sample 2 - leverage test_modules/__init__.py
# -------------------------------------------------------------------
# print("-----------------------------------------")
# import sys
# print(sys.version)




print("-----------------------------------------")
# import test_modules.built_in
# test_modules.built_in.print_name()

# works with test_modules/__init__.py
# import test_modules
# test_modules.built_in.print_name()

import test_modules
test_modules.print_name()

# --- This will fail ---
# test_modules/__init__.py: from test_modules import built_in
# import test_modules
# built_in.print_name()
# --- This will fail ---

# print("-----------------------------------------")
# from test_modules import built_in
# built_in.print_name()

# from test_modules.built_in import print_name as b
# b()


print("-----------------------------------------")
print(__name__)
# __main__

print(__file__)
# /home/pythonuser/work___space/python_01_learn_basic/python_codes/test_modules.py
