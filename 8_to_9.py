# 8. Explore lambda functions in python.
# Explore the use cases of ‘for loops’ and lambda functions
# Write a program using lambda with map, filter, reduce functions.
from functools import reduce
def lambda_function():
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    doubled_numbers = list(map(lambda x: x * 2, num))
    print("Doubled numbers: ", doubled_numbers)

    even_numbers = list(filter(lambda x: x % 2 == 0, num))
    print("Even numbers: ", even_numbers)

    sum = reduce(lambda x, y: x + y, num)
    print("sum: ", sum)
lambda_function()

# 9. Explore the difference between sorted and sort functions.
# Write example programs using sort and sorted function and interpret.
# Using sorted()
numbers = [3, 1, 4, 2]
sorted_numbers = sorted(numbers)  
print(numbers)  
print(sorted_numbers)  
# Using sort()
numbers.sort()
print(numbers) 
words = ["apple", "banana", "orange", "grape", "kiwi"]

# Using sorted() function
sorted_words = sorted(words)
print("Original Words:", words)
print("Sorted Words by Length:", sorted_words)
words.sort()
print(words)