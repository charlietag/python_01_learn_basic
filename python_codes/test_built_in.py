# ------------------------------------------------
# Try built-in
# ------------------------------------------------
my_list = []

# ---------- range() ----------
for i in range(10):
    my_list.append(i)
    print(i)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

print(my_list)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ---------- len() ----------
print(len(my_list))
# 10

# ---------- min() ----------
print(min(my_list))
# 0

# ---------- max() ----------
print(max(my_list))
# 9


# ------------------------------------------------
# Try built-in: list.sort(), and sorted(list)
# ------------------------------------------------
# Ref. https://docs.python.org/3/howto/sorting.html

second_list = [6, 3,1, 2, 99, 88, 9, 8]

print(second_list)
# [6, 3, 1, 2, 99, 88, 9, 8]

print(sorted(second_list))
# [1, 2, 3, 6, 8, 9, 88, 99]

print(second_list)
# [6, 3, 1, 2, 99, 88, 9, 8]

second_list.sort()
print(second_list)
# [1, 2, 3, 6, 8, 9, 88, 99]


# ------------------------------------------------
# Try built-in: strip()
# ------------------------------------------------
my_string = "     --- test string ---"
print(my_string)
#      --- test string ---

print(my_string.strip())
# --- test string ---



# ------------------------------------------------
# Try built-in: datetime
# ------------------------------------------------
import datetime
now = datetime.datetime.now()
aage = now.year - 1984
print(aage)
# 39


