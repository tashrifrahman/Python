"""
14. Given a list of nested lists, write a Python program to concatenate all the sublists into a single flat 
list.
"""


def flatten_list(lst):
      flat_list = []
      for sublist in lst:
            for i in sublist:
                  flat_list.append(i)
      return flat_list


n = int(input("Number of Sublists : "))
lst = []

for i in range(n):
      sublist = list(map(int,input(f"Enter number of sublist {i+1}: ").split()))
      lst.append(sublist)

result = flatten_list(lst)

print("Orginal Nested List : ",lst)
print("\nFlat List : ",result)
