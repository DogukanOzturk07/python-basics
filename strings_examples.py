# strings_examples.py
"""
Basic string operations in Python
Author: Dogukan Ozturk
Date: 2025-04-30
"""

# String definition
greeting = "Hello, GitHub!"
print(greeting)

# String Concatenation
name = "Dogukan"
surname ="Ozturk"
Mygreeting = greeting + " I am " + name + " " + surname
print(Mygreeting)

# Using f-string
age = 29
info = f"My name is {name} {surname} and I am {age} years old."
print(info)

# String methods
text = "python is awesome and so useful. There are good toolboxes"
print(text.upper())
print(text.title())
update_text = (text.replace("awesome", "powerful")).replace("useful","dynamic").replace("good","strong")
print(update_text)
# Search within string
if "python" in text:
    print("Yes, 'python' is in the text!")
else:
    print("No, python is not in the text!")

# Loop through the character array
for char in name + surname:
    print(char)
for char in name,surname:
    print(char)
