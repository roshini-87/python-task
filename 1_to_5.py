# 1. Extend nested list by adding the sublist

def nested_list():
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    sub_list = ["h", "i", "j"]

    list1[2][1][2].extend(sub_list)

    print(list1)

# 2. Convert two lists into a dictionary

def convert_two_list_to_dict():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    result = {}

    for i in range(len(keys)):
        result[keys[i]] = values[i]

    print(result)


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

# 4. Rename key of a dictionary
def rename_key():
    sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"}
    sample_dict['location'] = sample_dict['city']
    del sample_dict['city']
    print(sample_dict)


# 5. Get the key of a minimum value from the following dictionary
def minimum_value():
    sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}

    print(min(sample_dict))

nested_list()
convert_two_list_to_dict()
Delete_list_from_dict()
rename_key()
minimum_value()