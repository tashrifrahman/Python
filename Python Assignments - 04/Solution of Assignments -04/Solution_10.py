"""
10.Write a Python program to reverse a given list without using any built-in functions.
"""


lst = list(map(int,input("Enter List : ").split()))
reversed_list = []

for i in lst:
      reversed_list.insert(0,i)
print("Reversed List : ",reversed_list)