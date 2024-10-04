from collections import deque

n = int(input())
link = {}
for _ in range(n):
    k = list(input().split())
    link[k[0]] = [k[1], k[2]]
    
q = deque(['A'])

while q:
    now = q.popleft()
    print(now, end='')
    if link[now][0] != '.':
        q.appendleft(link[now][0])
    if link[now][1] != '.':
        q.append(link[now][1])
q.append('A')
print('')
while q:
    state = q.pop()
    if link[state][0] and link[state][0] != '.':
        q.append(link[state][0])
    else:
        q.append(state)
        break
        
while q:
    now = q.pop()
    print(now, end='')
    for k, v in link.items():
        if v in now:
            q.append(k)
    if link[q[-1]][1] and link[q[-1]][1] != '.':
        q.append(link[k][1])
        
def left(k, link):
    if link[k][0] and link[k][0] != '.':   
        return left(link[k][0], link)
    else:
        return None
    
def right(k, link):
    if link[k][1] and link[k][1] != '.':   
        return left(link[k][1], link)
    else:
        return None
    
def printInorder(node):
    if node is None:
        return

    printInorder(node.left)

    print(node.data, end=' ')

    printInorder(node.right)