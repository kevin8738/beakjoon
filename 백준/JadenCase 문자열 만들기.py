def solution(s):
    print(f'바뀌기 전 : {s}')
    s = list(s)
    for i in range(len(s)):
        if i == 0:
            if s[i] != ' ':
                if 96< ord(s[i])<123:
                    s[i] = chr(ord(s[i])-32)
                else:
                    continue
        elif s[i] == ' ':
            continue
        elif s[i-1] != ' ':
            if 64 < ord(s[i]) < 91:
                s[i] = chr(ord(s[i])+32)
            else:
                continue
        elif 96< ord(s[i])<123:
            s[i] = chr(ord(s[i])-32)
    
    s = ''.join(s)
    print(f'바뀐 후 : {s}')

if __name__ == "__main__":
    n = input()
    solution(n)