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
rename_key()

# 5. Get the key of a minimum value from the following dictionary
def minimum_value():
    sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
    print(min(sample_dict))
minimum_value()

