"""n = int(input())
all = 0
for i in range(1, n+1):
    i = str(i)
    fori = i[:((len(i))//2)]
    backi = i[((len(i))//2):]
    if len(i) % 2 == 0:
        back = backi[::-1]
        if fori == back:
            all += 1
    else:
        backi = backi[1:]
        back = backi[::-1]
        if fori == back:
            all += 1

print(all)"""

"""from collections import deque

n = int(input())
all = 0
for i in range(1, n+1):
    i = list(str(i))
    fori = deque(i[:((len(i))//2)])
    backi = deque(i[((len(i))//2):])
    cnt = 0
    lenF = len(fori)
    for j in range(len(fori)):
        a = fori.popleft()
        b = backi.pop()
        if a == b:
            cnt += 1
            if lenF == cnt:
                all += 1
        else:
            break
    
if len(str(n)) == 1:
    all += n
else:
    all += 9

print(all)"""

def count(k):
    value = {1:9, 2:9, 3:9*10, 4:9*10, 5:9*10*10, 6:9*10*10, 7:9*10*10*10, 8:9*10*10*10, 9:9*10*10*10*10}
    cnt = 0
    for i in range(1,k):
        cnt += value[i]
    return cnt

def rhq(li, f):
    if len(li) == 0:
        return f
    if len(li) == 1:
        f *= int(li[0])+1
        return f
    if int(li[0]) <= int(li[-1]):
        f *= int(li[0])
    else:
        f *= int(li[-1])+1
    del li[0], li[-1]
    return rhq(li, f)

n = int(input())
a = len(str(n))
all = count(a)
cnt = 1
lin = list(str(n))
cnt = rhq(lin, cnt)
if cnt == 1:
    print(all)
else:
    print(all+cnt)

"""fori = i[:((len(i))//2)]
    backi = i[((len(i))//2):]
    if len(i) % 2 == 0:
        back = backi[::-1]
        if fori == back:
            all += 1
    else:
        backi = backi[1:]
        back = backi[::-1]
        if fori == back:
            all += 1"""