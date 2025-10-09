"""
4. Write a Python function called `list_sum` that takes a list of integers as input and returns the sum 
of all elements in the list. Test the function with different lists. 
"""


def list_sum(lst):
      total = 0
      for i in lst:
            total += i
      return total

lst = list(map(int,input("Enter List : ").split()))
print("List Sum :",list_sum(lst))
