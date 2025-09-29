"""
10. Write a Python program to convert a sentence into title case format (each word's first letter capitalized).
"""



sentence = input("Enter a Sentence :")

title_formate = sentence.title()

print("Title Formate : ",title_formate)




"""
Without using title() method
"""


sentence = input("Enter a Sentence :")
words = sentence.split()
title_formate = []

for char in words:
      title_formate.append(char[0].upper() + char[1:].lower())

print("Title Case Formate :"," ".join(title_formate))
