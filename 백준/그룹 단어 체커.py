n = int(input())
cnt = n
for _ in range(n):
    string = input()
    closed = [string[0]]
    boolean = False
    x=0
    k = string[0]
    
    while True:
        while k == string[x]:
            x += 1
            if (x+1) > len(string):
                break
        if (x+1) > len(string):
            break
        closed.append(string[x])
        k = string[x]
            
    for i in closed:
        if closed.count(i)>1:
            boolean = True
            
    if boolean == True:
        cnt -= 1

print(cnt)