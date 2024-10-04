x,y,z = map(int, input().split())

if max(x,y,z) >= (x+y+z-max(x,y,z)):
    print((x+y+z-max(x,y,z))*2-1)
else:
    print(x+y+z)