n = int(input())
stri = input()
dic = {i: 0 for i in range(len(stri))}
odd = 2
for k in range(3):
    for i in range(0,len(stri),3):
        if i % 2 == 0:
            print(stri[i+k], end='')
        else:
            print(stri[i+odd+k], end='')
            odd -= 1
for i in range(0,len(stri),3):
    if i % 2 ==0:
        dic[i] = stri[i]
        dic[i+len(stri)//3] = stri[i+1]
        dic[i+2] = stri[i+2]
    else:
        dic[i] = stri[]