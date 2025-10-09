"""
20. Write a Python program that takes an element as input and checks if it exists in a given tuple.
"""


def check_tuple(t,element):
      for item in t:
            if item == element:
                  return True
      return False


t = tuple(input("Enter Tuple : ").split())
element = input("Element to check : ")

print("Exists in given tuple : ",check_tuple(t,element))