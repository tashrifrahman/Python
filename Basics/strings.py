#You can use  single or double quotes:
a = """Lorem ipsum dolor sit amet,
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
ut labore et dolore magna aliqua.'''
print(a)

#String are Arrays
a = "Hello, World"
print(a[4])

#Looping Through a String
for x in "banana":
    print(x)

#Check String(we can use the keyword in to determine if a specified phrase or character is present in a string)
txt = "The best things in life are free"
print("free" in txt)   

#Chech if
txt = "The best things in life are free"
if "food" in txt:
    print("Yes")
else:
    print("No")

#Slicing Strings
b = "Hello, World"
print(b[2:5])

#Upeer Case and Lower Case
a = "Hello, World"
print(a.upper())
print(a.lower())

#Remove Whitespace
a = " Hello, World "
print(a.strip())

#Replace String
a = "Hello, World"
print(a.replace("H","j"))

#Format String or F-String
price = 50
txt = f"The price is {price} taka"
print(txt)