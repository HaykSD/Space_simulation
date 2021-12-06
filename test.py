# Created by Hayk_Sardaryan at 11/28/2021 / 15:35
planets = ['E','m','v']

for i, planet1 in enumerate(planets):
    for planet2 in planets[i + 1:]:
        print(planet1, planet2, planet2, planet1)
