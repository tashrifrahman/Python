"""
5. Write a Python program and take a message as input. 
    ● If "offer" or "free" is present, then print "Spam Message." 
    ● Else → "Not Spam"
"""


message = input("Enter a message :").lower()

if "offer" in message or "free" in message:
      print("Spam Message.")
else:
      print("Not Spam")