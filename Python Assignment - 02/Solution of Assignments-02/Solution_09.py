"""
9. Write a Python program to find the most frequent word in a sentence or paragraph.
"""


sentence = input("Enter a Sentence :")
words = sentence.lower().split()

frequency = {}

for char in words:
      if char in frequency:
            frequency[char] += 1
      else:
            frequency[char] = 1

print("Most frequency word :",max(frequency,key=frequency.get))