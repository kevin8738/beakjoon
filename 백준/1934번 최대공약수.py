a,b = map(int, input().split())

maxnum = max(a,b); minnum = min(a,b)
while (maxnum % minnum != 0):
    if maxnum > minnum:
        maxnum %= minnum
    else:
        minnum %= maxnum
    if minnum == 0 or maxnum == 0:
        break
    
if minnum == 0:
    print(maxnum)
elif maxnum == 0:
    print(minnum)
else:
    print(maxnum * minnum)