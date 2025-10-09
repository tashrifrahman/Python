"""
17. a) Write a Python program to sort a tuple of integers in ascending order. 
"""

my_tuple = tuple(map(int,input("Enter Tuple : ").split()))

print("Sort Tuple : ",sorted(my_tuple))


"""
b) Write a Python program to reverse a tuple without using any built-in functions. 
"""

def reverse_tuple(my_tuple):
      reversed_list = []
      for i in my_tuple:
            reversed_list.insert(0,i)
      return tuple(reversed_list)

my_tuple = tuple(map(int,input("\nEnter new Tuple for Reversing : ").split()))
print("Reversed Tuple : ",reverse_tuple(my_tuple))