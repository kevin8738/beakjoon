n, m = map(int, input().split())
nList = []
for i in range(n):
    k = input()
    nList.append(k)
cnt = 0
for _ in range(m):
    check = input()
    if check in nList:
        cnt += 1
            
print(cnt)