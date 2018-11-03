import re
st="this is sathya"
word=input("enter a word search:")
str=re.search(r"sathya",st)
print(str)
print(str.group(0))