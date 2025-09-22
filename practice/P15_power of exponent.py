def exponent(base,exp):
      num = exp
      result = 1
      while num>0:
            result = result * base
            num = num - 1
      print(result)
exponent(5,4)