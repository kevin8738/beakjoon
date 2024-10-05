n = int(input())

for i in range(n):
    save = []
    str = input()
    for j in str:
        if j == ')':
            if len(save) > 0:
                if save[-1]== '(':
                    save.pop()
            else:
                save.append(j)
                break
        elif j == '(':
            save.append(j)
    if len(save) == 0:
        print("YES")
    else:
        print("NO")