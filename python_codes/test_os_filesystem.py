# Ref. https://builtin.com/software-engineering-perspectives/python-pathlib
# Ref. https://betterprogramming.pub/should-you-be-using-pathlib-6f3a0fddec7e
# Ref. https://docs.python.org/3/library/pathlib.html#correspondence-to-tools-in-the-os-module

from pathlib import Path

this_home = Path.home()
print(this_home)

this_file = __file__
# this_file = "soft_link_file"
# this_file = "../python_codes"
print(this_file)

# -----------------------
# new Path Class
# -----------------------

# ------
p = Path(this_file)

# ------
this_file_basename = p.name
print(this_file_basename)

# ------
# This will resolve soft link absolute path (like os command readlink -m this_file)
this_file_realpath_file = p.resolve()
print(this_file_realpath_file)

# ------
this_file_realpath = Path(this_file_realpath_file).parent
# this_file_realpath = p.parent.absolute()
print(this_file_realpath)

# ------
this_file_realpath_ls = this_file_realpath.iterdir()
for file in this_file_realpath_ls:
    print(file)
# print(this_file_realpath_ls)

# ------
# mkdir -p a/b
mkdir_test_tree_folders = "a/b"
Path(mkdir_test_tree_folders).mkdir(parents=True, exist_ok=True)

# ------
# cd a/b
# import os
# os.chdir(mkdir_test_tree_folders)
# print(os.getcwd())

# ------
# rm -fr a
from shutil import rmtree
mkdir_test_tree_folders = "a"
rmtree(mkdir_test_tree_folders)
