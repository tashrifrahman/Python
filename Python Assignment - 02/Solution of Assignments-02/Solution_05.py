"""
 5. Write a Python program to count the frequency of each word in a paragraph. 
 """


paragraph = input("Enter a paragraph :")
words = paragraph.split()

frequency = {}

for char in words:
      char = char.lower()
      if char in frequency:
            frequency[char] += 1
      else:
            frequency[char] = 1
print("Count the frequency of each word :",frequency)