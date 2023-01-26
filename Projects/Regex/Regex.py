import re

L="^[0-1][0-1]0[0]*$|^[0-1][0-1]0[0]*1$"
w="1100010001"
result=re.match(L,w)
if(result):
    print("String is member!")
else:
    print("String is non-member!")
    
