import random
from turtle import *

class Triangle:
    def __init__(self, a: Vec2D, b: Vec2D, c: Vec2D) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.corner_map = {1: self.a, 2: self.b, 3: self.c}

    def __repr__(self) -> str:
        return f"a: {self.a}, b: {self.b}, c: {self.c}"

    def get_starting_point(self) -> Vec2D:
        corners = [self.a, self.b, self.c]
        valid_point = False
        while not valid_point:
            random_x = choose_random_value_between(
                min([corner[0] for corner in corners]), 
                max([corner[0] for corner in corners]),
            )
            random_y = choose_random_value_between(
                min([corner[1] for corner in corners]), 
                max([corner[1] for corner in corners]),
            )
            point = Vec2D(random_x, random_y)
            valid_point = self._is_within(point)
        return point

    def choose_random_corner(self) -> Vec2D:
        num = random.randrange(1, 4)
        return self.corner_map[num]

    def get_halfway_point(self, corner: Vec2D, point: Vec2D) -> Vec2D:
        vec = Vec2D(((corner[0] + point[0]) / 2), ((corner[1] + point[1]) /2))
        return vec

    def _is_within(self, point: Vec2D) -> bool:
        area_abc = self._area(self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1])
        area_pbc = self._area(point[0], point[1], self.b[0], self.b[1], self.c[0], self.c[1])
        area_apc = self._area(self.a[0], self.a[1], point[0], point[1], self.c[0], self.c[1])
        area_abp = self._area(self.a[0], self.a[1], self.b[0], self.b[1], point[0], point[1])

        if (area_abc == area_pbc + area_apc + area_abp):
            return True
        return False

    def _area(self, x1, y1, x2, y2, x3, y3) -> float:
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                    + x3 * (y1 - y2)) / 2.0)

def choose_random_value_between(start: float, end: float) -> float:
    return float(random.randrange(int(start), int(end) + 1))