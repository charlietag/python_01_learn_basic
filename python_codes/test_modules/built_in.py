# ------------ Built-in var ------------------
# https://www.geeksforgeeks.org/__name__-a-special-variable-in-python/
# https://docs.python.org/3/reference/import.html?highlight=__name__#import-related-module-attributes
# https://exampleprogramming.com/specialvars.html

def print_name():
    print(__name__)
    # test_modules.built_in

    print(__file__)
    # /home/pythonuser/work___space/python_01_learn_basic/python_codes/test_modules/built_in.py

    import __main__
    print(__main__.__file__)
    # /home/pythonuser/work___space/python_01_learn_basic/python_codes/test_test_modules.py

# ------------------------
# check __name__
# ------------------------
if __name__ == "__main__":
    print(__name__)
    # nothing, __name__ -> test_modules.built_in

    print(__file__)
    # nothing, __name__ -> test_modules.built_in
