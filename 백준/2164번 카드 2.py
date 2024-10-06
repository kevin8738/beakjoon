from collections import deque

n = int(input())

dq = deque()

for i in range(n):
    dq.appendleft(i+1)

while len(dq) > 1:
    dq.pop()
    dq.appendleft(dq[-1])
    dq.pop()        
    
print(dq.pop())

'''

n = int(input())

k = []

for i in range(n):
    k.append(i+1)

k.reverse()

for _ in range(n):
    k.remove(k[-1])
    k.insert(0, k[-1])
    k.remove(k[-1])
    if len(k) == 1:
        print(k[0])
        break
'''