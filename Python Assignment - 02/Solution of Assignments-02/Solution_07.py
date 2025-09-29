"""
7. Write a Python program to count the number of unique words in a sentence.
"""


sentence = input("Enter a Sentence :")

words = sentence.lower().split()

unique_words = set(words)

print("The number of unique words :",len(unique_words))