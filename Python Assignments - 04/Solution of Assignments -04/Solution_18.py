"""
18. Given a tuple containing various elements, write a Python program to count the frequency of a 
specific element in the tuple.
"""


my_tuple = tuple(map(int,input("Enter Tuple : ").split()))
element = int(input("Enter element to count : "))

count = my_tuple.count(element)

print("Count the Frequency : ",count)