spamWords = ['buy now','subscribe this','click this']

comment = input("Enter your Comments : ")
spam = False

if('buy now' in comment):
      spam = True
if('subscribe this' in comment):
      spam = True
if('click this' in comment):
      spam = True

print("Spam is ", spam)