a, b = map(int, input().split())
c, d = map(int, input().split())

x = a*d + c*b
y = b*d

maxnum = max(x,y); minnum = min(x,y)
while (maxnum != 0) or minnum != 0:
    if maxnum > minnum:
        maxnum %= minnum
    else:
        minnum %= maxnum
    if minnum == 0 or maxnum == 0:
        break
    
if maxnum == 0 or minnum == 0:
    maxnum, minnum = max(maxnum, minnum), 1
    
print(int(x/maxnum * minnum), int(y/maxnum*minnum))