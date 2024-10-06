n = int(input())
li = []
for i in range(n):
    appendLi = list(map(int, input().split()))
    li.append(appendLi)
    
soli = sorted(li)
for i in soli:
    print(i[0], i[1])
    