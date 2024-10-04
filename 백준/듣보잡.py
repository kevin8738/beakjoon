n, m = map(int, input().split())
nSet, mSet = set(), set()
for _ in range(n):
    nSet.add(input())
    
for _ in range(m):
    mSet.add(input())
    
pluSet = nSet & mSet
print(len(pluSet))
for i in sorted(list(pluSet)):
    print(i)