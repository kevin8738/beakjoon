n = int(input())
data = list(map(int, input().split()))
m = int(input())
cnt = 0
dic = {i:(m-i) for i in data}
for i in dic.values():
    if i in dic.keys():
        cnt += 1
print(cnt//2)