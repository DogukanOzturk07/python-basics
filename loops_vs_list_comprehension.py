# loops_vs_list_comprehension.py
"""
Comparison between traditional for loops and Python list comprehensions.
Author: Dogukan Ozturk
Date: 2025-04-30
"""

# Squaring with classic for loop
numbers = [1, 2, 3, 4, 5, 6, 7]
squares = []

for num in numbers:
    squares.append(num ** 2)

print("Squares with loop:", squares)

# Same process as list comprehension
squares_comp = [num ** 2 for num in numbers]
print("Squares with list comprehension:", squares_comp)

# Cubing only even numbers
even_cubes = [n ** 3 for n in numbers if n % 2 == 0]
print("Even number cubes:", even_cubes)

# Same process as loop
even_cubes_loop = []
for n in numbers:
    if n % 2 == 0:
        even_cubes_loop.append(n ** 3)

print("Even number cubes with loop:", even_cubes_loop)

## Example with string list (length calculation)
words = ["Python", "GitHub", "Dogukan", "Ozturk"]
lengths = []

for word in words:
    lengths.append(len(word))
    
print("Lengths (loop):", lengths)

# Using List comprehension
lengths_comp = [len(word) for word in words]
print("Lengths (comprehension):", lengths_comp)

# Conditional substitution (with if-else)
nums= [-23,-5, -2, 0, 2, 17,108]
labels = ["positive" if n > 0 else "non-positive" for n in nums]
print("Number labels:", labels)

# Print each number in order with description
for i in range (len(nums)):
    print(f"{i + 1}. number ({nums[i]}) -> {labels[i]}")
# Double for loop (nested loop)
# Combinations that multiply 2 lists (classic method)
a = [2, 8]
b = [6, 20]
results = []

for x in a:
    for y in b:
        results.append(x * y)

print("Nested loop result:", results)

# Using list comprehension
nested_results = [x * y for x in a for y in b]
print("Nested comprehension result:", nested_results)
