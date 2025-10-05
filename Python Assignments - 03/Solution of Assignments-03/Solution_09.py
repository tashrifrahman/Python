"""
9. Write a Python program  inputs: data_source (public/private) and consent (yes/no) 
    ● If data_source == public → "Usable Data" 
    ● Else nested check: 
         ○ If consent == yes → "Usable Data" 
         ○ Else → "Ethical Issue" 
"""


data = input("Data Source(public/private) :").lower()
consent = input("COnsent(yes/no) :").lower()

if data == "public":
      print("Usable Data")
else:
      if consent == "yes":
            print("Usable Data")
      else:
            print("Ethical Issue")