"""
12. Write a Python program and Create a chatbot that takes user input. 
    It should keep responding "Bot: I am learning..." until the user types "exit." 
"""


while True:
      user = input("User :")

      if user.lower() == "exit":
            break
      else:
            print("Bot: I am learning...")
      
