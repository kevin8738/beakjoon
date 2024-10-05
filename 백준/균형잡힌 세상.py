inputstr = input()
while inputstr != '.':
    
    save = []
    for j in inputstr:
        if not j in ['(',')','[',']']:
            continue
        if j == ')':
            if len(save) > 0:
                if save[-1]== '(':
                    save.pop()
                else:
                    break
            else:
                save.append(j)
                break
        elif j == '(':
            save.append(j)
        elif j == ']':
            if len(save) > 0:
                if save[-1]== '[':
                    save.pop()
                else:
                    break
            else:
                save.append(j)
                break
        elif j == '[':
            save.append(j)
    if len(save) == 0:
        print("yes")
    else:
        print("no")
        
    inputstr = input()