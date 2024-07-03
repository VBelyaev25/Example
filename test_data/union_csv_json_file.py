from test_data import CSV_FILE_PATH
from test_data import JSON_FILE_PATH
import csv
import json


def parser_json_file():
    with open(JSON_FILE_PATH, 'r', encoding='utf8',) as jsonfile:
        return json.load(jsonfile)


def get_csv_data():
    csv_data = {
        "csv":[]
    }
    for data1, data2 in parser_csv_file().items():
        csv_data["csv"].append(data2)
    return csv_data["csv"]


def book_for_users():
    td = {
        "book":[]
    }

    user_dict = {
        "user":[]
    }
    my_list = []
    minor_dict ={}
    csv_file = get_csv_data()
    steps = get_len_csv_data()//len(parser_json_file())
    count = 0

    # print(steps)
    # print("len(parser_json_file()) = ", len(parser_json_file()))
    books = 0
    data = get_data_csv_file(csv_file)
    while books < len(parser_json_file()):
        while count < steps:
            count += 1
            for kkk in data:
                my_list[count].append(kkk.items())
                print((my_list))

        user_dict["user"].append(td)
        books += 1
        # print(my_list)

    # for count_book in range(len(parser_json_file())):
    #     user_dict["user"].append(td['book'][count_book])
        # for i in csv_file:
        #     for data in i:
        #         for kkk, vvv in data.items():
        #             # print(count)
        #             # print((kkk, vvv))
        #             # if kkk ==
        #             count += 1

        # print(user_dict)

def union_json_csv():
    json_file = parser_json_file()
    new_file = {
        "union":[]
    }
    for user in json_file:
        td = {}
        for kkk, vvv in user.items():
            if kkk == "name":
                td["name"] = vvv
            if kkk == "gender":
                td["gender"] = vvv
            if kkk == "address":
                td["address"] = vvv
            if kkk == "age":
                td["age"] = vvv
            td["books"]=[123]
            # print(td)
        new_file["union"].append(td)
    return new_file


def curr_step(len_json_file):
    return len(parser_csv_file()['book'])//int(len_json_file)


def parser_csv_file():

    book_dict = {
            "book":[]
        }
    with open(CSV_FILE_PATH) as csvfile:
        reader = csv.DictReader(csvfile)
        for iii in reader:
                book_dict['book'].append(iii)
        return book_dict


def get_len_csv_data():
    for i in get_csv_data():
        return len(i)


def get_data_csv_file(csv_file):
    for i in csv_file:
        for data in i:
            yield data




book_for_users()
# print(book_for_users())

# for i in union_json_csv()["union"]:
#     print(i)

# for i in get_data_csv_file(get_csv_data()):
#     print(i)











# psvc = Pcsv_file()
# psvc.get_csv_data()





# class Books:
#
#     def __init__(self, title, author, pages, genre):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.genre = genre
#
# books = {
#     "books":[]
# }
#
# for i in range(parser_csv_file().__sizeof__()):
#     books['books'].append(Books('qqq', 'f', '545s5478', 25).__dict__)
# print(type(parser_csv_file()))



def my_union_json_file(user):
    pass

# (my_union_json_file(parser_json_file()))
