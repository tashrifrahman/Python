"""
2. Write a Python function called `is_palindrome` that takes a string as input and returns `True` if it is 
a palindrome and `False` otherwise. Test the function with different words.
"""


def is_palindrome(str):
      str = str.lower().replace(" ","")
      return str == str[::-1]

str = input("Enter string : ")
print("Palindrome : ",is_palindrome(str))