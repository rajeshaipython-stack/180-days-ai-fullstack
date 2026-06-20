# Day 3 Project - Text Analyzer

text = input("Enter a sentence: ")

# 1. Total characters (including spaces)
print("Characters:", len(text))

# 2. Number of words
words = text.split()
print("Words:", len(words))

# 3. Uppercase version
print("Uppercase:", text.upper())

# 4. Count vowels
count = 0
for char in text.lower():
    if char in "aeiou":
        count += 1
print("Vowels:", count)