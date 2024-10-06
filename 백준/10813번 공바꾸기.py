n, m = map(int, input().split())
li = []
for i in range(n):
    li.append(i+1)
for i in range(m):
    x, y = map(int, input().split())
    li[x-1], li[y-1] = li[y-1], li[x-1]
for i in li:
    print(i, end=' ')