import re
st="this is python"
res=re.findall(r".",st)
print(res)
print("------------------------------")
import re
st= "i am learning python with naveen"
res=re.findall(r"\w",st)
print(res)
print("-----------------------------")
import re
st="i am learning python with naveen"
res=re.findall(r"\w*",st)
print(res)
print("------------------------")
import re
st="i am learning python with naveen"
res=re.findall(r"\w+",st)
print(res)
print("-----------------------------------")
import re
st="i am learning python with naveen"
res=re.findall(r"^\w*",st)
print(res)
print("----------------------")
import re
st="i am learning python with naveen"
res=re.findall(r"\w+$",st)
print(res)
print("-------------------------")
import re
st="i am learning python with naveen"
res=re.findall(r"\w\w",st)
print(res)
print("-------------------------")
import re
st="i am learning python with naveen"
res=re.findall(r"\b\w.",st)
print(res)
print("----------------------")
import re
st="rajeshanu414@gmail.com,rajeshanu414@yahoo.com,rajeshanu@co.in"
res=re.findall(r"@\w+",st)
print(res)
print("------------------------")
import re
st="rajeshanu414@gmail.com,rajeshanu414@yahoo.com,rajeshanu@co.in"
res=re.findall(r"@\w+.\w+",st)
print(res)
print("-------------------")
import re
st="rajeshanu414@gmail.com,rajeshanu414@yahoo.com,rajeshanu@co.in"
res=re.findall(r"@\w+.(\w+)",st)
print(res)
print("-----------------------------")
import re
st="hi 414 this is 007 from simha"
res=re.findall(r"\d",st)
print(res)
print("------------------------")
import re
st="hi 007 this is from sumanth"
res=re.findall(r"\w+",st)
print(res)
print("------------------")
import re
st="i am learning python with naveen"
res=re.findall(r"[aeiouAEIOU]\W+",st)
print(res)
print("-------------------------")
import re
user_name=input("name please")
res=re.match("^[A-Za-z]*$",user_name)
if res==None:
    print("invalid name")
else:
    print("Welcome india:",user_name)
print("---------------------")
import re
input=input("enter an input string:")
m=re.match('\d{5}\Z',input)
if m:
    print("True")
else:
    print("False")
