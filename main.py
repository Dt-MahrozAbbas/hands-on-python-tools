# main.py

"""
🔧 Practical Snippets
This file contains practical and essential Python code snippets with detailed comments.
Ideal for learners, developers, and interview preparation.
"""

# ------------------------------------------
# 1. enumerate(): Get index + value from iterable
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# ------------------------------------------
# 2. list.extend(): Append elements of another iterable
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print("Extended List:", list1)

# ------------------------------------------
# 3. collections.Counter(): Count elements
from collections import Counter
words = ["apple", "banana", "apple", "orange", "banana", "banana"]
counter = Counter(words)
print("Word Frequencies:", counter)

# ------------------------------------------
# 4. Reverse a string using slicing
original = "Python"
reversed_str = original[::-1]
print("Reversed String:", reversed_str)

# string[:,-1] is invalid syntax for strings
# Instead, use string[-1] for last character
print("Last character of string:", original[-1])

# ------------------------------------------
# 5. zip(): Iterate multiple lists in parallel
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# ------------------------------------------
# 6. any() and all(): Check conditions
nums = [2, 4, 6, 8]
print("Any odd?", any(n % 2 != 0 for n in nums))
print("All even?", all(n % 2 == 0 for n in nums))

# ------------------------------------------
# 7. set(): Remove duplicates
items = ["apple", "banana", "apple", "orange"]
unique_items = set(items)
print("Unique items:", unique_items)

# ------------------------------------------
# 8. defaultdict: Set default value for missing keys
from collections import defaultdict
word_count = defaultdict(int)
for word in words:
    word_count[word] += 1
print("Word Count using defaultdict:", word_count)

# ------------------------------------------
# 9. Pythonic variable swap
a, b = 5, 10
a, b = b, a
print("Swapped:", a, b)

# ------------------------------------------
# 10. List comprehension
squares = [x**2 for x in range(5)]
print("Squares:", squares)

# ------------------------------------------
# 11. map(): Apply function to all items
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print("Doubled:", doubled)

# ------------------------------------------
# 12. filter(): Filter items by condition
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)

# ------------------------------------------
# 13. Reverse list in-place
data = [1, 2, 3, 4]
data.reverse()
print("Reversed list:", data)

# ------------------------------------------
# 14. Dictionary comprehension
squares_dict = {x: x * x for x in range(5)}
print("Square dictionary:", squares_dict)

# ------------------------------------------
# 15. sorted() with custom key (case-insensitive sort)
names = ["Alice", "bob", "Charlie"]
sorted_names = sorted(names, key=lambda x: x.lower())
print("Sorted Names:", sorted_names)
