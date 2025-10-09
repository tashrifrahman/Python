"""
12. Given a list of integers, write a Python program to create a new list that contains the squares of 
the elements using list comprehension."""

def square_list(lst):
      return [i**2 for i in lst]


lst = list(map(int,input("Enter List :").split()))
print("Squares List : ",square_list(lst))

