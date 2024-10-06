n, m = map(int, input().split())
bagu = [(i+1) for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    ugab = list(reversed(bagu[a-1:b]))
    bagu[a-1:b] = ugab
    
for i in bagu:
    print(i, end = ' ')