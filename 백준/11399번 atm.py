n = int(input())
N = list(map(int, input().split()))
N.sort(reverse=True)
cnt = 0
for i in range(n):
    cnt += (N[i]*(i+1))

print(cnt)