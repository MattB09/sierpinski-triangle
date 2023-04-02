import random
from turtle import *

class Triangle:
    def __init__(self, c1: Vec2D, c2: Vec2D, c3: Vec2D) -> None:
        """
        Triangle constructor that takes three vectors to represent the corners.
        """
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def __repr__(self) -> str:
        return f"c1: {self.c1}, c2: {self.c2}, c3: {self.c3}"

    def get_starting_point(self) -> Vec2D:
        """
        Generate a starting point randomly within the triangle
        """
        corners = [self.c1, self.c2, self.c3]
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
        """
        Chooses a corner of the triangle randomly
        """
        num = random.randrange(1, 4)
        return getattr(self, f"c{num}")

    def get_halfway_point(self, corner: Vec2D, point: Vec2D) -> Vec2D:
        """
        Calculate the halfway point between the corner and the point
        """
        vec = Vec2D(((corner[0] + point[0]) / 2), ((corner[1] + point[1]) /2))
        return vec

    def _is_within(self, point: Vec2D) -> bool:
        """
        If the area of the triangle is equal to the sum of the areas of the combinations 
        of triangles created by the point and the corners, the point is within the 
        triangle
        """
        area_123 = self._area(self.c1, self.c2, self.c3)
        area_p23 = self._area(point, self.c2, self.c3)
        area_1p3 = self._area(self.c1, point, self.c3)
        area_12p = self._area(self.c1, self.c2, point)

        if (area_123 == area_p23 + area_1p3 + area_12p):
            return True
        return False

    def _area(self, c1: Vec2D, c2: Vec2D, c3: Vec2D) -> float:
        """
        Calculates the area of a triangle given the coordinates of each corner.
        """
        return abs((c1[0] * (c2[1] - c3[1]) + c2[0] * (c3[1] - c1[1])
                    + c3[0] * (c1[1] - c2[1])) / 2.0)

def choose_random_value_between(start: float, end: float) -> float:
    return float(random.randrange(int(start), int(end) + 1))