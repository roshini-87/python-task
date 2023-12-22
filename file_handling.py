def string_check(file_content, target_string):
    """Check if the target string is present in the file content (case-insensitive)."""
    return target_string.lower() in file_content.lower()

def word_count(file_content):
    """Count the occurrences of each word in the file content."""
    word_count_dict = {}
    words = file_content.split()

    for word in words:
        # Remove punctuation and convert to lowercase for case-insensitive counting
        word = word.strip('.,!?()[]{}:;"\'').lower()

        if word:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1

    return word_count_dict

# def write_file():
#     # write file 
#     with open("file.txt", "w") as file:
#         L = ["This is roshini \n", "This is Python \n", "This is textfile\n"]
#         file.write("Hello There \n")
#         file.writelines(L)


def read_file():
    # read file
    with open("file.txt", "r") as file:
        file_content = file.read()
        print("Output of the Read function is ")
        print(file_content)

        target_string = 'maha'  # Replace with the string to check
        found_string = string_check(file_content, target_string)
        print(f"String '{target_string}' found in the file: {found_string}")

        word_counts = word_count(file_content)

        # Print word counts
        print("\nWord counts in the file:")
        for word, count in word_counts.items():
            print(f"{word}: {count}")

# write_file()
read_file()
