# Your are given a string s of length n consisting of 'o' and 'x', and intergers l and r.
# Determing whether al characters from the L-th to the R-th character of s are 'o'.
# If all characters are 'o', print "Yes", otherwise print "No".


n,l,r=map(int,input().split())
s=input()
count=0

for i in range(l-1, r):
      if (s[i]!='o'):
            count +=1 
            break
      
if count == 0:
      print("Yes")
else:
      print("No")


