n = int(input())

x=1
cnt=0

for i in range(1, n+1):
    x *= i

for i in range(0, len(str(x))):
    if x%10 == 0:
        cnt += 1
        x //= 10

print(cnt)  