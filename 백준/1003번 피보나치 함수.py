'''
def fibo0(x):
    cnt0 = 0
    if x == 0:
        cnt0 += 1
    elif x == 1:
        cnt0 == 0
    else:
        cnt0 = fibo1(x-1)
    
    return cnt0

def fibo1(x):
    cnt1 =  0
    if x == 0:
        cnt1 == 0
    elif x == 1:
        cnt1 += 1
    else:
        fibo1(x-1) + fibo1(x-2)
    
    return cnt1

n = int(input())

for i in range(n):
    k = int(input())
    print(fibo0(k), fibo1(k))'''

def fibo(x):
    cnt = 0
    if x == 0:
        cnt == 0
    elif x == 1:
        cnt += 1
    else:
        fibo(x-1) + fibo(x-2)
    
    return cnt

n = int(input())

for i in range(n):
    k = int(input())
    if k == 0:
        print(1, 0)
    if k == 1:
        print(0, 1)
    else:
        print(fibo(k-1),fibo(k-1)+fibo(k-2))
