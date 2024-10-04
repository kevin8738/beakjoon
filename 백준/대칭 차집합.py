n, m = map(int, input().split())
nSet = set(list(map(int, input().split())))
mSet = set(list(map(int, input().split())))

print(len(nSet-mSet) + len(mSet-nSet))