N, M, R = map(int, input().split())
li1, li2, pri = [], [], []
k = 1

for i in range(N):
    li1.append(i+1)
    pri.append(0)
    
for _ in range(M):
    li2.append(set())
    
for i in range(M):
    a, b = map(int, input().split())
    li2[a-1].add(b)
    li2[b-1].add(a)

def dfs():
    global k, pri
    pri[]