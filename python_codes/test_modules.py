# class Post:
#     # 建構式
#     def __init__(self):
#         self.titles = []
#     # 新增文章
#     def add_post(self, title):
#         self.titles.append(title)
#     # 刪除文章
#     def delete_post(self, title):
#         self.titles.remove(title)
#
#
# a = Post()
# a.titles = [
#     "asdfasdf"
# ]
# a.add_post("cccc")
# print(a.titles)

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
