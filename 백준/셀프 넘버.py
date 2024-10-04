made = set()
n = 1
while (n <= 100000):
    if n//10 == 0:
        made.add(n + n)
    elif n//100 == 0:
        made.add(n + (n%10) + (n//10) -1)
    elif n//1000 == 0:
        made.add(n + (n%10) + (n//10) + (n//100))
    elif n//10000 == 0:
        made.add(n + (n%10) + (n//10) + (n//100) + (n//1000)-2)
        
    n += 1
made.add(9995)
for i in range(10000):
    if (i+1) not in made:
        print(i+1, end=' ')