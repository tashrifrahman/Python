def first_last_same(numberList):
      print("Given List:",numberList)
      first_num = numberList[0]
      last_num = numberList[-1]

      if first_num == last_num:
            return True
      else:
            return False
      
number_x = [10,20,30,40,10]
print(first_last_same(number_x))
number_y = [75,65,35,75,30]
print(first_last_same(number_y))