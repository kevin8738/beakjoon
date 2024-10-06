h,w = map(int, input().split())
li = []
for i in range(h):
    li.append([])
    for j in range(w):
        li[i].append(0)
print(li)
n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    if d==0:
        for a in range(l):
            li[x-1][y-1] = 1
            y += 1
    elif d==1:
        for b in range(l):
            li[x-1][y-1] = 1
            x += 1
            
for i in range(0,h):
    for j in range(0,w):
        print(li[i][j], end = ' ')
    print()