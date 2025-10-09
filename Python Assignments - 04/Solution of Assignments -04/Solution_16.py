"""
16.  a) Given a tuple with three elements (x, y, z), write a Python program to unpack the tuple 
and assign the values to three variables.
"""

my_tuple = tuple(map(int,input("Enter Tuple : ").split()))
x,y,z = my_tuple
print(f"Unpacked Tuple : x={x}, y={y}, z={z}")



"""
b) Write a Python program to pack three variables into a single tuple and print the tuple. 
"""

a,b,c = map(int,input("\n\nEnter three variables : ").split())
packed_tuple = (a,b,c)
print("Packed Tuple : ",packed_tuple)
