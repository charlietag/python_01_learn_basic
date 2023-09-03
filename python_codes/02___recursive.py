"""Try comment
This is recursive function
"""

# Try comment
# This is recursive function

def recursive_list(the_lists):
    for the_list in the_lists:
        if isinstance(the_list, list):
            recursive_list(the_list)
        else:
            show_msg = "Hi, " + str(the_list)
            print(show_msg)



# all_lists = [
#     "Charlie",
#     "Welly",
#     [
#         "Guru",
#         1988,
#         [
#             "Apple",
#             "Samsung"
#         ],
#     ],
# ]
#
# recursive_list(all_lists)
