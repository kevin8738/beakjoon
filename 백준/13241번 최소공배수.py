a,b = map(int, input().split())
maxnum = max(a,b); minnum = min(a,b)
while (maxnum != 0) or minnum != 0:
    if maxnum > minnum:
        maxnum %= minnum
    else:
        minnum %= maxnum
    if minnum == 0 or maxnum == 0:
        break
    
if maxnum == 0 or minnum == 0:
    maxnum, minnum = max(maxnum, minnum), 1

print(int(a*b/maxnum * minnum))