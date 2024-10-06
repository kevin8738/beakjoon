n, m = map(int, input().split())
a = list(map(int, input().split()))
M = []
sum = []
k = 0
for x in range(0, len(a)):
    k += a[x]
    M.append(k)

for x in range(0, m):
    i, j = map(int, input().split())
    if i == 1: 
        sum.append(M[j-1])
    else:
        sum.append(M[j-1] - M[i-2])

for x in sum:
    print(x)