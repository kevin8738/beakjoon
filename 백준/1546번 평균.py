n = int(input())
a = list(map(int, input().split()))

m = max(a)
x=0

for i in range(0, n):
    a[i] = a[i]/m*100
    x += a[i]

print(x/n)
