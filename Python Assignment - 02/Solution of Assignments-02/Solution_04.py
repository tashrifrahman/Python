"""
4. Write a Python program to check if a word or sentence is a palindrome, ignoring punctuation and spaces.
"""


sentence = input("Enter a Word or Sentence :")

string = ""
for char in sentence:
      if char.isalnum():
            string += char.lower()

if string == string[::-1]:
      print("Palindrome")
else:
      print("Not a Palindrome")