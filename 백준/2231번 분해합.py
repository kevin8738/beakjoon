n = int(input())

for i in range(n):
    stri = str(i)
    sumi = 0
    for j in range(len(stri)):
        sumi += int(stri[j])
    if i + sumi == n:
        print(i)
        break
    elif i+1 == n:
        print(0)