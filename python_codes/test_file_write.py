# Ref. https://www.geeksforgeeks.org/writing-to-file-in-python/

# Ref. https://mkyong.com/python/python-difference-between-r-w-and-a-in-open/
# difference: r, r+, w, w+

# This will empty file first before starting to write file
with open("test_file_write.txt", "w", encoding="utf-8") as f:
    f.write("testAA\n")
    f.write("testAA\n")
    print("testB", file = f)
    print("testB", file = f)
