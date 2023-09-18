with open('test_open_file.txt', 'r', encoding='utf-8') as f:
    # if multiple methods exe together, only the first method will be exec,
    # because it's been f.close() after iterate using `with`

    # ----------------------------------------
    # method 1
    # ----------------------------------------
    # require big memory, but easiest to use
    # lines = f.readlines()
    # for line in lines:
    #     print(f"readlines---> {line.strip()}")
    # print(lines)

    # ----------------------------------------
    # method 2
    # ----------------------------------------
    # Fewest memory consumption, and fast
    # line = f.readline()
    # while line:
    #     print(line.strip())
    #     line = f.readline()

    # I like this most
    for line in f:
        print(f"f ---> {line.strip()}")

    # ----------------------------------------
    # method 3
    # ----------------------------------------
    # perf, almost the same as read()
    # for line in iter(f):
    #     print(f"iter ---> {line.strip()}")

    # for line in iter(f.readline, ''):
    #     print(f"iter with readline ---> {line.strip()}")


    # ----------------------------------------
    # method 4
    # ----------------------------------------
    # Fastest , but useless...

    # lines = f.read()
    # print(lines)
    # for line in lines:
    #     print(f"---> {line}")

    # lines = f.read()
    # all_lines = lines.split("\n")
    # for line in all_lines:
    #     print(f"---> {line}")
