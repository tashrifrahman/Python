"""
3.Write a Python program to count how many vowels and consonants are present in a sentence.
"""


sentence = input("Enter a Sentence : ")
sentence = sentence.lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in sentence:
      if char.isalpha():
            if char in vowels:
                  vowel_count += 1
            else:
                  consonant_count += 1

print("Vowels :",vowel_count)
print("Consonants :",consonant_count)