n = int(input())
m = int(input())

li = []
for i in range(n,m+1):
    k = 2
    
    while k <= i:
        if k == i:
            li.append(i)
        if i % k == 0:
            break
        k += 1
        
if len(li) == 0:
    print(-1)
else:
    print(sum(li))
    print(min(li))