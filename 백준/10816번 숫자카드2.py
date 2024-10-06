from collections import deque

def find(key, list, cnt):
    if key > list[len(list)//2]:
        find(key, list[:len(list)//2-1], cnt)
        return cnt
    elif key < list[len(list)//2]:
        find(key, list[len(list)//2+1:],cnt)
        return cnt
    else:
        return cnt+1
    
m = int(input())
mL = list(map(int, input().split()))
n = int(input())
nL = deque(map(int, input().split()))
mL = sorted(mL)
print(mL)
while nL:
    cnt = 0
    key = nL.popleft()
    if key > mL[len(mL)//2]:
        find(key, mL[:len(mL)//2-1], cnt)
    elif key < mL[len(mL)//2]:
        find(key, mL[len(mL)//2+1:],cnt)
    print(cnt, end=" ")
