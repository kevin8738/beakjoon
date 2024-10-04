word = input()
if len(word) == 1:
    print(1)
for i in range(len(word)//2):
    if not word[i] == word[(i+1)*(-1)]:
        print(0)
        break
    if i == len(word)//2-1:
        print(1)