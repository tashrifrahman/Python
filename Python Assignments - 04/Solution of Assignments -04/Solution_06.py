"""
6. Write a Python function called `is_leap_year` that takes a year as input and returns `True` if it is a 
leap year and `False` otherwise. Test the function with different years.
"""


def leaf_year(year):
      if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return True
      else:
            return False
      
year = int(input("Enter a Year : "))
print("Leap Year : ",leaf_year(year))