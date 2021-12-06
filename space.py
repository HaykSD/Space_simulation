# Created by Hayk_Sardaryan at 11/27/2021 / 18:55
from planet import Planet
from utils import get_screen_size


RES = WIDTH, HEIGHT = get_screen_size(minus=160)


class Space:
    def __init__(self):
        self.planets = []
        self.planet_number=0


    def create_planet(self, pos, v, mass, color, is_indifferent=False):
        print(pos)
        print(v / 50)
        Xplanet = Planet(name=f"planet{self.planet_number}", coord=pos, v=v / 50, mass=mass, radius='calc by mass',
                         is_indifferent=is_indifferent,
                         color=color)
        self.planets.append(Xplanet)
        self.planet_number+=1

    def draw_planets(self, screen, draw_trajectory=False):
        for planet in self.planets:
            if draw_trajectory:
                planet.draw_trajectory(screen)
            planet.draw(screen)


    def draw_v_vectors(self, screen, others=None):
        if others is None:
            others = self.planets
        for planet in others:
            planet.draw_v_vectors(screen, others)

    def move_planets_to_each_other(self):
        for i, planet1 in enumerate(self.planets):
            if not planet1.is_indifferent:
                planet1.move()

            for planet2 in self.planets[i + 1:]:
                # print(planet1,planet2,'select')
                if not planet1.is_indifferent:
                    planet1.set_velocity(planet2)
                    # print("    ",planet1,'move to',planet2,)
                if not planet2.is_indifferent:
                    planet2.set_velocity(planet1)
                    # print("    ",planet2,'move to', planet1)




    def delete_planet_if_not_on_screen(self, out_size=300):
        for planet in self.planets:
            if planet.coord.x > WIDTH + out_size or planet.coord.x < -out_size or \
                    planet.coord.y > out_size + HEIGHT or planet.coord.y < -out_size:
                self.planets.remove(planet)
