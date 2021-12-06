# Created by Hayk_Sardaryan at 22.11.2021 / 14:23

# import platform
import colorsys
import pygame as pg
from space import Space, WIDTH, RES
from planet import Planet, G
from random import random



space = Space()

# Earth = Planet(name="Earth", coord=(WIDTH / 5, 500), v=(0.3, 0), mass=80, radius='calc by mass', is_indifferent=True,
#                color='#1F51FF')
# Mars = Planet(name="Mars", coord=(280, 280), v=(3.1, -0.02), mass=20, radius='calc by mass', is_indifferent=False,
#               color="#FF5733")

# Venus = Planet(name="Venus", coord=(1000, 700), v=(0.8, 0), mass=60, radius='calc by mass',  is_indifferent=True, color='yellow')


#
# Earth = Planet(name="Earth", coord=(WIDTH / 2, 300), v=(1, 0), mass=41.05, radius='calc by mass', is_indifferent=True, color='#1F51FF')
# Mars = Planet(name="Mars", coord=(742, 141), v=(1.32, -0.1), mass=30, radius='calc by mass', is_indifferent=False, color="#FF5733")
# Venus = Planet(name="Venus", coord=(1000, 700), v=(0.8, 0), mass=60, radius='calc by mass',  is_indifferent=True, color='yellow')

# Earth = Planet(name="Earth",coord=(100, 470), v=(0, 0), mass=70, radius='calc by mass', is_indifferent=False, color='blue')
# Mars = Planet(name="Mars",coord=(600, 470), v=(0,0), mass=40, radius='calc by mass', is_indifferent=False, color='red')
# Venus = Planet(name="Venus",coord=(1000, 700), v=(0, 0), mass=70, radius='calc by mass', is_indifferent=False, color='yellow')

# from random import randint
#
# Earth = Planet(name="Earth",coord=(100, 470), v=(randint(-10,10)/10, randint(-10,10)/10), mass=randint(5,80), radius='calc by mass',  is_indifferent=True, color='blue')
# Mars = Planet(name="Mars",coord=(600, 400), v=(randint(-10,10)/10, randint(-10,10)/10), mass=randint(5,80), radius='calc by mass', is_indifferent=False, color='red')
# Venus = Planet(name="Venus",coord=(1000, 700), v=(randint(-10,10)/10, randint(-10,10)/10), mass=randint(5,80), radius='calc by mass',  is_indifferent=True, color='yellow')

# orbital speed
# Earth = Planet(name="Earth", coord=(800, 500), v=(0.1, 0), mass=200, radius='calc by mass', is_indifferent=True,
#                color=(21, 120, 209))
# Mars = Planet(name="Mars", coord=(800, 150), v=((G * Earth.mass / 350) ** 0.5, 0), mass=20, radius='calc by mass',
#               is_indifferent=False, color=(193, 68, 14))



# Earth = Planet(name="Earth", coord=(800, 500), v=(0.1, 0), mass=100, radius='calc by mass', is_indifferent=True,
#                color=(21, 120, 209))
# Mars = Planet(name="Mars", coord=(1170, 330), v=(-0.58, 0.54), mass=20, radius='calc by mass',
#               is_indifferent=False, color=(193, 68, 14))
# Venus = Planet(name="Venus",coord=(1000, 700), v=(0, 0), mass=70, radius='calc by mass', is_indifferent=True, color='yellow')


# orbital speed
Earth = Planet(name="Earth", coord=(800, 500), v=(0, 0), mass=120, radius='calc by mass', is_indifferent=True,
               color=(21, 120, 209))

Mars = Planet(name="Mars", coord=(800, 150), v=((G * Earth.mass / 350) ** 0.5, 0), mass=50, radius='calc by mass',
              is_indifferent=False, color=(193, 68, 14))

# Mars = Planet(name="Mars", coord=(800, 150), v=(1.9, 0), mass=10, radius='calc by mass',
#               is_indifferent=False, color=(193, 68, 14))


Venus = Planet(name="Venus",coord=(1000, 700), v=(0, 0), mass=40, radius='calc by mass', is_indifferent=True, color='yellow')




space.planets = [
      Earth,
    Mars,
    # Venus,

# Planet(name="aaa",coord=(774, 244), v=(0, 0), mass=20, radius='calc by mass', is_indifferent=True, color='yellow'),
# Planet(name="aaa",coord=(719, 660), v=(0, 0), mass=20, radius='calc by mass', is_indifferent=True, color='yellow'),
# Planet(name="aaa",coord=(1457, 331), v=(0, 0), mass=20, radius='calc by mass', is_indifferent=True, color='yellow'),
# Planet(name="aaa",coord=(1705, 110), v=(0, 0), mass=20, radius='calc by mass', is_indifferent=True, color='yellow'),
# Planet(name="aaa",coord=(1264, 608), v=(0, 0), mass=20, radius='calc by mass', is_indifferent=True, color='yellow'),
# Planet(name="aaa",coord=(228, 651), v=(0, 0), mass=20, radius='calc by mass', is_indifferent=True, color='yellow'),
# Planet(name="aaa",coord=(258, 716), v=(0, 0), mass=20, radius='calc by mass', is_indifferent=True, color='yellow'),


]


class App:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        ## self.alpha_surface = pg.Surface(RES)
        self.clock = pg.time.Clock()

        self.button_still_down = False
        self.fix_coord_once = True
        self.mouse_down_pos = (0, 0)
        self.mouse_current_pos = (0, 0)
        self.mouse_last_coord = (0, 0)

        # mous_planet
        self.random_color = self.random_lightness_color()
        self.mass = 20

    # @staticmethod
    # def hls_RGB(h, l, s):
    #     return tuple(round(i * 255) for i in colorsys.hls_to_rgb(h, l, s))

    @staticmethod
    def random_lightness_color():
        return tuple(round(i * 255) for i in colorsys.hls_to_rgb(random(), 0.6, 0.88))

    def show_FPS(self, size=15):
        font = pg.font.Font(None, size)
        text = font.render(f"{int(self.clock.get_fps())} FPS",
                           True, "green", "black")
        textRect = text.get_rect()
        textRect.topright = self.screen.get_rect().topright
        self.screen.blit(text, textRect)

    def create_planet_by_mouse(self, event):
        # left button down and motion
        if event.type == pg.MOUSEMOTION and event.buttons[0]:
            self.button_still_down = True
            if self.fix_coord_once:
                self.mouse_down_pos = pg.Vector2(
                    event.pos)  # when button pressed save coordinat (only once ) and dont change
                self.fix_coord_once = False
            self.mouse_current_pos = pg.Vector2(event.pos)
            self.mouse_vec = self.mouse_current_pos - self.mouse_down_pos
            # mouse_rel=event.rel

        # left button up
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 and self.button_still_down:
                self.button_still_down = False  # for dra vector
                self.fix_coord_once = True  # for dra vector

                space.create_planet(pos=self.mouse_down_pos, v=self.mouse_vec, mass=self.mass, color=self.random_color)
                self.random_color = self.random_lightness_color()

        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 3:
                space.create_planet(pos=event.pos, v=(0.0), mass=self.mass, color=self.random_color,
                                    is_indifferent=True)
                self.random_color = self.random_lightness_color()

    def draw_planet_in_mouse_position(self):
        pg.draw.circle(self.screen, self.random_color, pg.mouse.get_pos(), self.mass / 4)

    def change_created_planet_mass_by_wheel(self, event, mul=1):
        if event.type == pg.MOUSEWHEEL:
            if self.mass > 11:
                self.mass += event.y * mul
            else:
                self.mass = 12

    def draw_vector_by_click(self):
        if self.button_still_down:
            pg.draw.line(self.screen, 'green', self.mouse_down_pos, self.mouse_current_pos, 2)
        else:
            pg.draw.line(self.screen, 'gray', self.mouse_down_pos, self.mouse_current_pos, 3)

    def run(self):
        bg = pg.image.load("bg.jpg")

        while True:
            self.screen.blit(bg, (0, 0))
            ## self.screen.blit(self.alpha_surface, (0, 0))
            self.clock.tick(60)
            self.show_FPS(size=25)

            for event in pg.event.get():
                if event.type == pg.QUIT: exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        Mars.v.x += 0.3
                    if event.key == pg.K_DOWN:
                        Mars.v.x -= 0.3

                self.change_created_planet_mass_by_wheel(event, mul=3)
                self.create_planet_by_mouse(event)

            # pg.display.set_caption(
            #     f"Pygame App_name   •   Python {platform.python_version()}  Pygame {pg.version.ver}  SDL {'.'.join([str(v) for v in pg.get_sdl_version()])}, FPS={str(self.clock.get_fps())}")

            # drawing

            space.draw_planets(self.screen, draw_trajectory=True)
            # space.draw_v_vectors(self.screen)
            space.delete_planet_if_not_on_screen(out_size=300)
            space.move_planets_to_each_other()

            self.draw_planet_in_mouse_position()
            self.draw_vector_by_click()
            Mars.show_info_towards(self.screen, towards=Earth, font_size=30)
            Mars.show_info(self.screen, font_size=25)
            pg.display.update()


if __name__ == '__main__':
    app = App()
    app.run()





