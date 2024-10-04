n = int(input())
li = list(map(int, input().split()))
soli = sorted(list(set(li)))
dic = {}
for i in range(len(soli)):
    dic[soli[i]] = i

for i in range(len(li)):
    li[i] = dic[li[i]]
            
for k in range(len(li)):
    if k != len(li):
        print(li[k], end=' ')
    else:
        print(li[k])