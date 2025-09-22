def leaf_year(year):
      if year % 4 == 0:
            if year % 100 == 0:
                  if year % 400 == 0:
                        return True
                  else:
                        return False
            else:
                  return True
      else:
            False
print(leaf_year(2020))
print(leaf_year(2025))