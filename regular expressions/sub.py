import re
st="current rocking programming is .net"
res=re.sub(r".net","python",st)
print(res)