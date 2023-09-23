# -----------------------------------------------------
# Try comment
# -----------------------------------------------------
# Try comment
# This is recursive function
"""Try comment
This is recursive function
"""

# -----------------------------------------------------
# Test recursive function
# -----------------------------------------------------
def recursive_list(the_lists):
    for the_list in the_lists:
        if isinstance(the_list, list):
            recursive_list(the_list)
        else:
            show_msg = "Hi, " + str(the_list)
            print(show_msg)



# -----------------------------------------------------
# Main
# -----------------------------------------------------
if __name__ == "__main__":

    all_lists = [
        "Brat",
        "Anne",
        [
            "Guru",
            1988,
            [
                "Apple",
                "Samsung"
            ],
        ],
    ]

    recursive_list(all_lists)

    # Hi, Brat
    # Hi, Anne
    # Hi, Guru
    # Hi, 1988
    # Hi, Apple
    # Hi, Samsung
