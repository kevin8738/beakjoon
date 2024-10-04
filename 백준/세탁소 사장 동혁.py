n = int(input())

for _ in range(n):
    k = int(input())
    a = k//25
    b = (k%25)//10
    c = ((k%25)%10)//5
    d = (((k%25)%10)%5)//1
    print(a, b, c, d)