n = int(input())
li = []
for i in range(n):
    x,y = input().split()
    li.append([int(x),i,y])
    
soli = sorted(li)
for i in soli:
    print(i[0], i[2])