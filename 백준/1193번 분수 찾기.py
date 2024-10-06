n = int(input())
a=0
for i in range(1, 4500):
    if a+i >= n:
        break
    a += i

k = n-a-1

if a+i == n:
    if n%2==0:
        print(f'{1}/{i}')
    else:
        print(f'{i}/{1}')
else:
    if i % 2==0:
        li = [1, i]
        for _ in range(k):
            li[0] += 1
            li[1] -= 1
    else:
        li = [i, 1]
        for _ in range(k):
            li[0] -= 1
            li[1] += 1

    print(f'{li[0]}/{li[1]}')