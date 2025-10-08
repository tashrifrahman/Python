import string
str1 = input("Enter String: ")

replace_char = '#'

for i in string.punctuation:
      str1 = str1.replace(i,replace_char)
print(str1)