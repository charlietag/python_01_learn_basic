# ------------ Built-in var ------------------
# https://www.geeksforgeeks.org/__name__-a-special-variable-in-python/
# https://docs.python.org/3/reference/import.html?highlight=__name__#import-related-module-attributes
# https://exampleprogramming.com/specialvars.html

def print_name():
    print(__name__)
    print(__file__)

    import __main__
    print(__main__.__file__)

if __name__ == "__main__":
    print(__name__)
    print(__file__)
