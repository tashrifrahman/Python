m1 = int(input("Subject1 : "))
m2 = int(input("Subject2 : "))
m3 = int(input("Subject3 : "))

overAll = (m1+m2+m3)/3

if(overAll >= 40):
      if(m1>=33 and m2>=33 and m3>=33):
            print("Pass")
      else:
            print("Fail(Due to one of the subject)")
else:
      print("Fail(Due to overall mark under 40% )")