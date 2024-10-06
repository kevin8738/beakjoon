n = int(input())
li = []

for i in range(n):
    x,y = map(int, input().split())
    li.append([y, x])
    
soli =sorted(li)
for i in soli:
    print(i[1], i[0])