import sys
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
sum = 0 
for i in range(1, n+1):
    for j in range(n-i+1):
        sum += li[j]





'''len_li = []
k=1
for i in range(n):
    sum = li[i]
    while sum < m:
        if i+k < n:
            sum += li[i+k]
            k+=1
        else:
            break
    if sum >=15:
        len_li.append(k)
    k = 1
    
print(min(len_li))'''