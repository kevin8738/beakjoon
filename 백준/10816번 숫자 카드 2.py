n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))
ndic = {}
for i in nlist:
    if i not in ndic:
        ndic[i] = 0
for i in mlist:
    if i not in ndic:
        ndic[i] = 0
for i in nlist:
    ndic[i] += 1
    
for i in range(m):
    print(ndic[mlist[i]], end=' ')