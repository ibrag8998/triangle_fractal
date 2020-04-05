# sorry for no docs I was just playing
import tkinter as tk
from random import randint
from time import sleep

from conf import *


class UI:

    def __init__(self):
        self.root = tk.Tk()
        self.canv = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
        self.canv.pack()
        self.root.bind('<Control-Key-w>', lambda *args: self.root.destroy())
        self.root.bind('<Return>', self.start)
        self.draw_dot = lambda radius, *coords: self.canv.create_oval(*(coords[0] - radius, coords[1] - radius, \
            coords[0] + radius, coords[1] + radius), fill=DOT_COLOR)  # coords is tuple with 2 elements: coords of dot centers
        self.maindots = []

    def randomize_start_dots(self):
        for _ in range(MAINDOTS_AMOUNT):
            coords = self.get_random_dot(MAINDOT_RADIUS)
            self.draw_dot(MAINDOT_RADIUS, *coords)
            self.maindots.append(coords)

    def draw_start_dots(self, dots):
        for x, y in dots:
            self.draw_dot(MAINDOT_RADIUS, x, y)
            self.maindots.append((x, y))

    def get_random_dot(self, radius):
        x = randint(radius, WIDTH - radius)
        y = randint(radius, HEIGHT - radius)
        return (x, y)

    def start(self, *args, n=10000):
        average = lambda *args: sum(args) / len(args)
        prev_dot = self.get_random_dot(DOT_RADIUS)
        self.draw_dot(DOT_RADIUS, *prev_dot)
        for _ in range(n):
            direction = self.maindots[randint(0, len(self.maindots)-1)]
            new_dot = (average(direction[0], prev_dot[0]), average(direction[1], prev_dot[1]))
            self.draw_dot(DOT_RADIUS, *new_dot)
            prev_dot = new_dot

    def mainloop(self):
        self.root.mainloop()


if USER_DOTS:
    dots = [tuple(map(int, input('Dot coords: ').split())) for _ in range(MAINDOTS_AMOUNT)]

ui = UI()

if USER_DOTS:
    ui.draw_start_dots(dots)
else:
    ui.randomize_start_dots()

ui.mainloop()
