"""
11. Given two lists of integers, write a Python program to create a new list that contains elements 
common to both lists. 
"""


def common_elements(list1, list2):
      common = []
      for i in list1:
            if i in list2 and i not in common:
                  common.append(i)
      return common

list1 = list(map(int,input("Enter List1 :").split()))
list2 = list(map(int,input("Enter List2 :").split()))

print("Commont Elements :",common_elements(list1,list2))