n = int(input())
N = list(map(int, input().split()))
K = []
N.reverse()

for i in range(len(N)-1):
    x = i+1
    if len(K) == 0:
        for _ in range(len(N)):
            if N[-1] == x:
                N.pop()
                break
            K.append(N.pop())
    elif x in N:
        for _ in range(len(N)):
            if K[-1] == x or N[-1] == x:
                N.pop()
                break
            K.append(N.pop())
    elif K[-1] == x:
        K.pop()

if K == [n]:
    print("Nice")
elif N == [n]:
    print("Nice")
else:
    print("Sad")