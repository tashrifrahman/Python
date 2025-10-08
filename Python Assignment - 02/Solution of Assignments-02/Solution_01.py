"""
1. Write a Python program to count the total number of words in a given sentence.
"""


sentence = input("Enter a sentence: ")
words_count = len(sentence.split())
print("Total number of words: ", words_count)