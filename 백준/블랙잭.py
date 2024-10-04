n, m = map(int, input().split())
cardli = list(map(int, input().split()))
sumli = []
for x in range(n):
    for y in range(x+1, n):
        for z in range(y+1, n):
            sumli.append(cardli[x] + cardli[y] + cardli[z])
            
sumli = sorted(sumli)
for i in range(len(sumli)):
    if sumli[i]>m:
        print(sumli[i-1])
        break
    elif i+1 == len(sumli):
        print(sumli[-1])
        break