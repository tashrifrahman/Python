"""
2. Write a Python program to count the frequency of each character in a given string.
"""


string = input("Enter a String : ")
frequency = {}
for char in string:
      if char != " ":
            if char in frequency:
                  frequency[char] += 1
            else:
                  frequency[char] =1

print("Count the Frequency :",frequency)