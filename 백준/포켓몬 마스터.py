n, m = map(int, input().split())
poke = {}
for i in range(n):
    pokemon = input()
    poke[pokemon] = i+1
    poke[str(i+1)] = pokemon
    
for _ in range(m):
    target = input()
    print(poke[target])