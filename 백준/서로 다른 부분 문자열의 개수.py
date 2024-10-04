s = input()
sList = []
for i in range(len(s)):
    for j in range(len(s)-i):
        sList.append(s[j:j+i+1])
        
print(len(set(sList)))