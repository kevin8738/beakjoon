n, m, v = map(int, input().split())
li = [set() for i in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    li[i].add(j)
    li[j].add(i)
    
ans = []
for idx in range(1, n+1):
    li[idx] = sorted(li[idx])

def dfs(k, li, ans):
    que = [k]
    while que:
        state = que.pop()
        if not state in ans:
            ans.append(k)
            for i in li[state]:
                if not i in ans:
                    dfs(i,li,ans)
    return ans

def bfs(k, li):
    ans, que = [], [k]
    while que:
        state = que.pop(0)
        if not state in ans:
            ans.append(k)
        for i in li[state]:
            if not i in ans:
                ans.append(i)
                que.append(i)
    return ans
a = dfs(v, li, ans)
b = bfs(v, li)
for i in a:
    print(i, end=' ')
print('')
for i in b:
    print(i, end=' ')