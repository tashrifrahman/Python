def count(str):
      char_count = 0
      digit_count = 0
      symbol_count = 0
      for char in str:
            if char.isalpha():
                  char_count += 1
            elif char.isdigit():
                  digit_count += 1
            else:
                  symbol_count += 1
      print("Letter = ",char_count,"\nDigits = ",digit_count,"\nSymbol = ",symbol_count)

str = input("Enter String:")
count(str)