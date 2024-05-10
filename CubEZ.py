import curses
import math
import time

def draw_3dline(stdscr, color, a, b):
    """Convert 3D coordinates to 2D and draw line."""
    ax, ay = int(a[0] + ORIGINX), int(a[1] + ORIGINY)
    bx, by = int(b[0] + ORIGINX), int(b[1] + ORIGINY)

    # Draw the line using ASCII characters
    delta_x = bx - ax
    delta_y = by - ay
    step = max(abs(delta_x), abs(delta_y))

    if step == 0:
        return

    for i in range(step + 1):
        x = ax + i * delta_x // step
        y = ay + i * delta_y // step
        if 0 <= y < stdscr.getmaxyx()[0] and 0 <= x < stdscr.getmaxyx()[1]:
            stdscr.addch(y, x, '|')

def draw_cube(stdscr, color, cube):
    """Draw 3D cube."""
    a, b, c, d, e, f, g, h = cube
    draw_3dline(stdscr, color, a, b)
    draw_3dline(stdscr, color, b, c)
    draw_3dline(stdscr, color, c, d)

    draw_3dline(stdscr, color, e, f)
    draw_3dline(stdscr, color, f, g)
    draw_3dline(stdscr, color, g, h)
    draw_3dline(stdscr, color, h, e)

    draw_3dline(stdscr, color, a, e)
    draw_3dline(stdscr, color, b, f)
    draw_3dline(stdscr, color, c, g)
    draw_3dline(stdscr, color, d, h)

def rotate_3dpoint(p, angle, axis):
    """Rotate a 3D point around a given axis."""
    cosang = math.cos(angle)
    sinang = math.sin(angle)
    x, y, z = p
    x_rot = (cosang + (1 - cosang) * axis[0] * axis[0]) * x
    x_rot += ((1 - cosang) * axis[0] * axis[1] - axis[2] * sinang) * y
    x_rot += ((1 - cosang) * axis[0] * axis[2] + axis[1] * sinang) * z
    y_rot = ((1 - cosang) * axis[0] * axis[1] + axis[2] * sinang) * x
    y_rot += (cosang + (1 - cosang) * axis[1] * axis[1]) * y
    y_rot += ((1 - cosang) * axis[1] * axis[2] - axis[0] * sinang) * z
    z_rot = ((1 - cosang) * axis[0] * axis[2] - axis[1] * sinang) * x
    z_rot += ((1 - cosang) * axis[1] * axis[2] + axis[0] * sinang) * y
    z_rot += (cosang + (1 - cosang) * axis[2] * axis[2]) * z
    return x_rot, y_rot, z_rot

def rotate_object(obj, angle, axis):
    """Rotate an object around a given axis."""
    for i in range(len(obj)):
        obj[i] = rotate_3dpoint(obj[i], angle, axis)

def main(stdscr):
    global ORIGINX, ORIGINY
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    # Move origin to the specified coordinates on the screen
    ORIGINX = 20
    ORIGINY = stdscr.getmaxyx()[0] // 2

    cube = [(-10, 10, 10), (10, 10, 10), (10, -10, 10), (-10, -10, 10),
            (-10, 10, -10), (10, 10, -10), (10, -10, -10), (-10, -10, -10)]

    rotation_speed = 0.1  # Adjust the rotation speed as needed

    while True:
        draw_cube(stdscr, 255, cube)
        stdscr.refresh()
        time.sleep(0.1)  # Adjust the sleep time for the desired frame rate
        stdscr.clear()
        rotate_object(cube, rotation_speed, (0, 1, 0))
        rotate_object(cube, rotation_speed * 0.1, (0, 0, 1))
        rotate_object(cube, rotation_speed * 0.1, (1, 0, 0))

if __name__ == "__main__":
    curses.wrapper(main)
