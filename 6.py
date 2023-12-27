# 6.Read a file and pass it to a function which checks for the given input string ( case
# insensitive check). If the given string is found, the function should return True.
# Create another function which will read the input file s
# and scan it to get the count of each word in it. After the process is completed print
# each word along with the number of times it occurred in the file.

def check_string_in_file(file_path, search_string):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()  
            return search_string.lower() in content
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return False

def count_word_occurrences(file_path):
    word_count = {}
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower().split()  
            for word in content:
                word = word.strip(".,!\?\"/'()[]{}")
                word_count[word] = word_count.get(word, 0) + 1 
        for word, count in word_count.items():
            print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")


file_path = 'file.txt'  
search_string = 'roshini' 
result = check_string_in_file(file_path, search_string)
print(f"'{search_string}' {'is' if result else 'is not'} present in the file.")
count_word_occurrences(file_path)
