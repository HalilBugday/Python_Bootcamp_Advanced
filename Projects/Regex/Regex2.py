import re

L="^aa[a-b]*aa$|^ab[a-b]*ba$|^ba[a-b]*ab$|^bb[a-b]*bb$"
w="baabaa"
result=re.match(L,w)
if(result):
    print("Matched!")
else:
    print("Wrong")
