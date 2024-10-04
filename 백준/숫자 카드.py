n = int(input())
N = set(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

for i in M:
    if i in N:
        print(1)
        continue
    else:
        print(0)