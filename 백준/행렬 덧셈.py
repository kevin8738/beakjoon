n, m = map(int, input().split())

a, b, ans = [], [], []

for i in range(n):
    ans.append([])
    for j in range(m):
        ans[i].append(0)

for i in range(n):
    inli = list(map(int, input().split()))
    a.append(inli)
    
for i in range(n):
    inli = list(map(int, input().split()))
    b.append(inli)
        
for i in range(n):
    for j in range(m):
        ans[i][j] = a[i][j] + b[i][j]
        print(ans[i][j], end=' ')
    print('')