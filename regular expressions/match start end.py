import re
st="sanju is from sathya his learning python"
word=input("enter a word to match:")
str=re.match(r"sanju",st)
str=re.match(word,st)
print(str.start())
print(str.end())
