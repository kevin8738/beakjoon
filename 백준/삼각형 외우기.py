li = []
for _ in range(3):
    x = int(input())
    li.append(x)
    
if li.count(60) == 3:
    print("Equilateral")
elif sum(li) == 180 and ((li.count(li[0]) == 2) or (li.count(li[1]) == 2) or (li.count(li[2]) == 2)):
    print("Isosceles")
elif sum(li) == 180 and ((li.count(li[0]) == 1) and (li.count(li[1]) == 1) and (li.count(li[2]) == 1)):
    print("Scalene")
else:
    print("Error")