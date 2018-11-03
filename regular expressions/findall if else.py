import re
st="this is mahesh"
word=("enter a word find")
res=re.findall("word",st)
if res==[]:
    print("no match found")
else:
    print("match found")
    print(res)

