# Day 3 - Strings practice

word = "DEVELOPER"
print(word[0])      # first letter
print(word[-2])     # second from end
print(word[0:4])    # slice
print(word[::-1])   # reversed

 #string methods (add these to the same file)
text = "  AI Full Stack Developer  "

print(text.strip())          # removes spaces at both ends
print(text.lower())          # all lowercase
print(text.upper())          # all uppercase
print(text.replace("AI", "ML"))  # swap a word

words = text.strip().split()  # split into a LIST of words
print(words)                  # ['AI', 'Full', 'Stack', 'Developer']
print(len(words))             # 4  → word count!

joined = "-".join(words)      # glue list back into a string
print(joined)                 # AI-Full-Stack-Developer