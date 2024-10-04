'''from itertools import combinations as com
N, K = map(int, input().split())
dic,plu, li, W= {}, [], [], []
for i in range(N):
    w, v = map(int, input().split())
    dic[w]=v
    W.append(w)
for i in range(1,N+1):
    res = com(W,i)
    a = list(res)
    for j in range(len(a)):
        if sum(a[j]) <= K:
            li.append(list(a[j]))
res = 0
for i in range(len(li)):
    maxv, a = 0, 0
    for j in range(len(li[i])):
        a += dic[li[i][j]]
    if a > maxv:
        maxv = a
print(maxv)
'''
N, K = map(int, input().split())
W, V, li, ind, plu= [], [], [], [], []
for i in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
for i in range(N):
    new = W[i]
    for j in range(i+1, N):
        if new + W[j] <= K:
            new += W[j]
            plu.append(j)
    plu.append(i)
    li.append(new)
    ind.append(plu)
    plu = []
for i in range(len(li)):
    a = 0
    for j in range(len(ind[i])):
        a += V[ind[i][j]]
    plu.append(a)
print(max(plu))