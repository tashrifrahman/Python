def append_middle(str1,str2):
      print("Orginal String are :",str1,str2)
      mid = int(len(str1)/2)

      x = str1[:mid:]
      x = x + str2
      x = x + str1[mid:]
      print(x)
append_middle("Tashrif","TR")