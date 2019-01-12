pikachu = []
pikachu.append("pikachu")
pikachu.append(50)  # strength
pikachu.append(800)  # health
pikachu.append(20)  # speed
pikachu.append(1)  # level

bulbasaur = []

bulbasaur.append("bulbasaur")
bulbasaur.append(67)
bulbasaur.append(56)
bulbasaur.append(56)
bulbasaur.append(56)

pokemons = []
pokemons.append(pikachu)
pokemons.append(bulbasaur)

for (n, s, h, sp, l) in pokemons:
    print("name", n)
    print("strength", s)
    print("health", h)
    print("speed", sp)
    print("level", l)
