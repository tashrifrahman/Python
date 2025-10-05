"""
6. Write a Python program and give input: 
   ● Age 
   ● Number of published papers 
      rules: 
   ● If age ≥ 18: 
         ○ If papers ≥ 2 → "Eligible for Talk" 
         ○ Else → "Eligible for Attendee only" 
   ● Else → "Not Eligible"
"""


age = int(input("Enter Age :"))
papers = int(input("Number of published papers :"))

if age >= 18:
      if papers >= 2:
            print("Eligible for Talk.")
      else:
            print("Eligible for Attendee only.")
else:
      print("Not Eligible")
