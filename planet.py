# Created by Hayk_Sardaryan at 11/27/2021 / 13:41
import pygame as pg
from itertools import cycle

G = 21


class Planet:
    def __init__(self, name, coord: tuple, v: tuple, mass, radius, is_indifferent, color="black"):
        self.name = name
        self.v = pg.math.Vector2(v)
        self.coord = pg.math.Vector2(coord)
        self.a_center = 0
        self.trajectory_list = []
        self.cycle_TF = cycle([True] + [False] * 2)
        self.mass = mass
        self.radius = mass / 4
        # self.radius = radius
        self.color = pg.Color(color)
        self.is_indifferent = is_indifferent

    def draw(self, screen):
        pg.draw.circle(surface=screen, radius=self.radius, color=self.color, center=self.coord)
        # pg.draw.circle(surface=screen, radius=self.radius+3, color=self.color*pg.Color(2,2,2), center=self.coord,width=2)

    def draw_trajectory(self, screen):
        # if self.coord not in self.trajectory_list and next(self.cycle_TF):
        if self.coord not in self.trajectory_list and self.v.x + self.v.y < 15:
            self.trajectory_list.append((self.coord.x, self.coord.y))
        elif self.v.x + self.v.y > 15:
            self.trajectory_list.append((self.coord.x, self.coord.y))

        for i, start in enumerate(self.trajectory_list[:-1]):
            pg.draw.line(screen, self.color, start, self.trajectory_list[i + 1], 2)

    def draw_v_vectors(self, screen, others):
        if self.a_center==0: self.a_center=10e-10

        k = 0.01 / self.a_center
        for planet in others:
            pg.draw.line(screen, 'yellow', self.coord, ((k * self.coord + planet.coord) / (k + 1)))

        # vxy
        pg.draw.line(screen, 'springgreen', self.coord, (self.coord + (100 * self.v.x, 0)))
        pg.draw.line(screen, 'orange     ', self.coord, (self.coord + (0, 100 * self.v.y)))

        # x+y
        pg.draw.line(screen, 'white', self.coord, (self.coord + self.v * 100))

    def move(self, v: tuple = None):
        if self.v and not v:
            self.coord += self.v
        if v:
            self.coord += v

    def set_velocity(self, to):
        other = to
        cosx = (other.coord.x - self.coord.x) / (self.coord.distance_to(other.coord))
        siny = (other.coord.y - self.coord.y) / (self.coord.distance_to(other.coord))
        self.a_center = G * other.mass / (self.coord.distance_squared_to(other.coord))
        self.v += (self.a_center * cosx, self.a_center * siny)

    def show_info_towards(self, screen, towards=None, font_size=20, ):
        other = towards
        font = pg.font.Font(None, font_size)
        text = font.render(f'a_center = {self.a_center:.5f} '
                           f'V = {self.v.x + self.v.y:.2f} '
                           f'Vxy = {self.v.x:.2f}, {self.v.y:.2f} '
                           f'd={self.coord.distance_to(other.coord):.2f}'
                           , True,
                           "green", "black")

        textRect = text.get_rect()
        text.get_rect().topleft = screen.get_rect().topleft
        self.info_towards_rect = text.get_rect()
        screen.blit(text, textRect)

    def show_info(self, screen, font_size=12, ):
        font = pg.font.Font(None, font_size)
        text = font.render(f'a_center = {self.a_center:.5f} '
                           f'V_x+y = {self.v.x + self.v.y:.3f} ', True, self.color, "black")
        textRect = text.get_rect()
        textRect.topleft = self.info_towards_rect.bottomleft
        screen.blit(text, textRect)

    def __str__(self):
        return self.name
