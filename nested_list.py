# 1. Extend nested list by adding the sublist

def nested_list():
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    sub_list = ["h", "i", "j"]

    list1[2][1][2].extend(sub_list)

    print(list1)

nested_list()

# 2. Convert two lists into a dictionary

def convert_two_list_to_dict():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    result = {}

    for i in range(len(keys)):
        result[keys[i]] = values[i]

    print(result)
convert_two_list_to_dict()

# 3. Delete a list of keys from a dictionary

def Delete_list_from_dict():
    sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
    keys = ["name", "salary"]

    for i in keys:
        if i in sample_dict:
            del sample_dict[i]

    print(sample_dict)
Delete_list_from_dict()
