import sys
import random
import time

try:
    import bext
except ImportError:
    print("This program requires the bext module, which you")
    print("can install by following the instructions at")
    print("https://pypi.org/project/Bext/")
    sys.exit()

WIDTH, HEIGHT = bext.size()
WIDTH -= 1
NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.02
COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
UP_RIGHT = "ur"
UP_LEFT = "ul"
DOWN_RIGHT = "dr"
DOWN_LEFT = "dl"
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)
COLOR = "color"
X = "x"
Y = "y"
DIR = "direction"


def main():
    bext.clear()
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append(
            {
                COLOR: random.choice(COLORS),
                X: random.randint(1, WIDTH - 4),
                Y: random.randint(1, HEIGHT - 4),
                DIR: random.choice(DIRECTIONS),
            }
        )
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1

    cornerBounces = 0
    while True:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print("   ", end="")
            originalDirection = logo[DIR]
            # Check if logo bounces off the corners
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1
            # Check to see if logo bounces of the left edge
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT
            # Check to see if logo bounces of the right edge
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT
            # Check to see if logo bounces of the top edge
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT
            # Check to see if logo bounces of the bottom edge
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT
            # If logo changed direction change the color
            if logo[DIR] != originalDirection:
                logo[COLOR] = random.choice(COLORS)
            # Change coordinates based on direction
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        bext.goto(5, 0)
        bext.fg("white")
        print("Corner bounces: ", cornerBounces, end="")

        # Draw logos at new location
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print("DVD", end="")

        bext.goto(0, 0)
        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Bouncing DVD Logo")
        sys.exit()
