"""
8. Write a Python program with the following inputs: number of samples and percentage of 
missing values. 
     ● If samples ≥ 1000: 
           ○ If missing ≤ 10% → "Good Dataset" 
           ○ Else → "Needs Cleaning" 
     ● Else → "Insufficient Data"
"""


samples = int(input("Number of Samples :"))
percentage = float(input("Percentage of Missing Values :"))

if samples >= 1000:
      if percentage <= 10:
            print("Good Dataset")
      else:
            print("Needs Cleaning")
else:
      print("Insufficients Data")