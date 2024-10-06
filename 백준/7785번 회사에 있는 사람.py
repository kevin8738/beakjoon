import sys
n = int(input())
entryLi = {}
for _ in range(n):
    name, state = sys.stdin.readline().split()
    if state == 'enter':
        entryLi[name] = 1
    else:
        del entryLi[name]

for i in sorted(entryLi.keys(), reverse=True):
    print(i)