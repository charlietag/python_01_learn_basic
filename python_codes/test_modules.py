# -------------------------------------------------------------------
# Sample 1
# -------------------------------------------------------------------
# from modules.recursive import recursive_list
from modules.recursive import recursive_list as r
# import modules.recursive
# import modules.recursive as r

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
# modules.recursive.recursive_list(all_lists)
# r.recursive_list(all_lists)


# error
# import recursive_list

# -------------------------------------------------------------------
# Sample 2 - leverage modules/__init__.py
# -------------------------------------------------------------------
# print("-----------------------------------------")
# import sys
# print(sys.version)




print("-----------------------------------------")
# import modules.built_in
# modules.built_in.print_name()

# works with modules/__init__.py
# import modules
# modules.built_in.print_name()

import modules as ml
ml.built_in.print_name()

# --- This will fail ---
# modules/__init__.py: from modules import built_in
# import modules
# built_in.print_name()
# --- This will fail ---

# print("-----------------------------------------")
# from modules import built_in
# built_in.print_name()

# from modules.built_in import print_name as b
# b()


# print("-----------------------------------------")
# print(__name__)
#
# print(__file__)

