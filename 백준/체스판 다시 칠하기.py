n, m = map(int, input().split())
borad = []
borad_case1 = [["WBWBWBWB"], 
               ["BWBWBWBW"],
               ["WBWBWBWB"], 
               ["BWBWBWBW"],
               ["WBWBWBWB"], 
               ["BWBWBWBW"],
               ["WBWBWBWB"], 
               ["BWBWBWBW"]]

borad_case2 = [["BWBWBWBW"],
               ["WBWBWBWB"],
               ["BWBWBWBW"],
               ["WBWBWBWB"],
               ["BWBWBWBW"],
               ["WBWBWBWB"],
               ["BWBWBWBW"],
               ["WBWBWBWB"]]

for i in range(n):
    x = list(input().split())
    borad.append(x)

cntli = []
for i in range(m-7):
    for j in range(n-7):
        new_borad = []
        for k in range(8):
            new_borad.append(borad[j+k][0][i:i+8])
        
        cnt = 0
        
        if new_borad != borad_case1:
            for x in range(8):
                for y in range(8):
                    if new_borad[x][y] != borad_case1[x][0][y]:
                        cnt += 1
            cntli.append(cnt)
    
        cnt = 0
        
        if new_borad != borad_case2:
            for x in range(8):
                for y in range(8):
                    if new_borad[x][y] != borad_case2[x][0][y]:
                        cnt += 1
            cntli.append(cnt)
                    
print(min(cntli))
