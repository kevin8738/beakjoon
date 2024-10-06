from collections import deque

n = int(input())
li = [[] for _ in range(n+1)]

for _ in range(n-1):
    i, j = map(int, input().split())
    li[i].append(j)
    li[j].append(i)

q = deque([1])
visited = [False] * (n + 1)
visited[1] = True
d = {}

while q:
    now = q.popleft()
    for neighbor in li[now]:
        if not visited[neighbor]:
            visited[neighbor] = True
            q.append(neighbor)
            d[neighbor] = now

for k in range(2, n+1):
    print(d[k])
