"""
16. Write a Python program and take input: password. 
    ● If length ≥ 8: 
          ○ If "AI" exists → "Strong Password" 
          ○ Else → "Weak Password" 
    ● Else → "Invalid Password" 
"""


password = input("Enter password :")
if len(password) >= 8:
      if "AI" in password:
            print("Strong Password")
      else:
            print("Weak Password")
else:
      print("Invalid Password")