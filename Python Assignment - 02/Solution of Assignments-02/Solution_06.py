"""
6. Write a Python program to remove common English stopwords (like "is," "the," "a," and "an") from a given string.
"""


stopwords = ["is","the","a","an","in","on","at","of","and","to"]

string = input("Enter a Sentence :")
words = string.split()
result = []

for char in words:
      if char.lower() not in stopwords:
            result.append(char)

print("After removing stopwords :"," ".join(result))