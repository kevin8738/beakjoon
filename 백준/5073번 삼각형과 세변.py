while True:
    x,y,z = map(int, input().split())
    
    if x == 0 and y == 0 and z == 0:
        break
    
    if max(x,y,z) >= (x+y+z - max(x,y,z)):
        print("Invalid")
    elif x==y==z:
        print("Equilateral")
    elif x==y or y==z or z==x:
        print("Isosceles")
    else:
        print("Scalene")