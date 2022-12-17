import turtle
# from turtle import *
import time

from triangle import Triangle


def main():
    st = time.time()

    iterations = 20000

    # turtle settings and instantiation
    turtle.delay(0)
    turtle.tracer(False)
    tur = turtle.Turtle(visible=False)
    tur.speed(0)
    tur.pen(pensize=.1)

    # Create the triangle, draw the corners, and the first dot
    base = draw_base(tur)
    point = base.get_starting_point()
    tur.goto(point)
    tur.dot()

    # Iterate n times drawing dots in between the current dot and
    # a randomly chosen corner of the triangle.
    for i in range(iterations):
        #  Acceleration schedule to show points being drawn more slowly in
        # the beginning and much more quickly (batches of 1000) towards the end
        if i < 300 and i % 2 == 0:
            turtle.update()
        elif i < 1000 and i % 10 == 0:
            turtle.update()
        elif i < 5000 and i % 100 == 0:
            turtle.update()
        else:
            if i % 1000 == 0:
                turtle.update()
        
        # Choose the corner, get the halfway point between the corner
        # and the current point, and then draw the new point
        corner = base.choose_random_corner()
        point = base.get_halfway_point(corner, point)
        tur.goto(point)
        tur.dot()


    et = time.time()
    elapsed_time = et - st
    print(f"Execution time: {elapsed_time} seconds")

    turtle.done()


def draw_base(tur: turtle.Turtle) -> Triangle:
    """
    Draws the triangle and returns the coordinates of each corner
    """
    EDGE_LENGTH = 500
    HALF_EDGE = EDGE_LENGTH / 2
    tur.penup()
    tur.goto(-HALF_EDGE, -(EDGE_LENGTH * 2 / 5))
    a = tur.position()
    tur.dot()

    tur.forward(500)
    b = tur.position()
    tur.dot()
    tur.left(120)

    tur.forward(500)
    c = tur.position()
    tur.dot()
    return Triangle(a, b, c)


if __name__ == '__main__':
    main()
