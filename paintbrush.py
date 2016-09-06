# -*- coding: utf-8 -*-

# Author: Ricardo Dani (https://github.com/ricardodani)


'''
Paintbrush
Create simple paintbrush. In the array screen of dimensions NxM, every color is denoted by single integer. Create function:
fill(screen, x, y, color)
Which fills the screen with color on x, y. Upper left corner is (0, 0).

Filling adheres to the following rules:
1. Neighboring squares are those who share an edge.
2. If the color of two neighboring squares is same before the fill, then the color spills through both of them if it is spilled on any one of the two.
3. Color can’t spill from one square to another if their color is not the same.
4. Color does not spill out of the plane.

Example:

Before fill
0 4 0 0 0 2 0 0 0 0 0 0 1
0 4 0 0 0 2 0 0 0 0 0 0 1
0 4 0 0 0 2 0 0 0 0 0 0 1
0 4 0 0 0 2 7 7 7 7 7 7 1
0 4 0 0 0 2 0 0 0 0 0 0 1
0 4 0 0 0 3 0 0 0 0 0 0 1
0 0 3 3 3 0 0 0 0 0 0 0 1
0 0 0 0 8 0 0 0 0 0 0 0 1

After fill(screen, 2, 1, 5)
0 4 5 5 5 2 0 0 0 0 0 0 1
0 4 5 5 5 2 0 0 0 0 0 0 1
0 4 5 5 5 2 0 0 0 0 0 0 1
0 4 5 5 5 2 7 7 7 7 7 7 1
0 4 5 5 5 2 0 0 0 0 0 0 1
0 4 5 5 5 3 0 0 0 0 0 0 1
0 0 3 3 3 0 0 0 0 0 0 0 1
0 0 0 0 8 0 0 0 0 0 0 0 1

'''

def fill(screen, x, y, color):
    # x = 2
    # y = 1
    old_color = str(screen[y][x])
    screen[y][x] = str(color)
    # upper
    neighbors = (
        (x, y - 1), # upper
        (x + 1, y), # right
        (x, y + 1), # bottom
        (x - 1, y)  # left
    )
    neighbors = filter(lambda x: x[0] >= 0 and x[1] >= 0, neighbors)
    for x_, y_ in neighbors:
        try:
            neighbor = screen[y_][x_]
        except:
            pass
        else:
            if neighbor == old_color:
                fill(screen, x_, y_, color)

def get_example_screen():
    screen = [
        '0 4 0 0 0 2 0 0 0 0 0 0 1'.split(' '),
        '0 4 0 0 0 2 0 0 0 0 0 0 1'.split(' '),
        '0 4 0 0 0 2 0 0 0 0 0 0 1'.split(' '),
        '0 4 0 0 0 2 7 7 7 7 7 7 1'.split(' '),
        '0 4 0 0 0 2 0 0 0 0 0 0 1'.split(' '),
        '0 4 0 0 0 3 0 0 0 0 0 0 1'.split(' '),
        '0 0 3 3 3 0 0 0 0 0 0 0 1'.split(' '),
        '0 0 0 0 8 0 0 0 0 0 0 0 1'.split(' '),
    ]
    return screen

def print_screen(screen):
    for line in screen:
        print ' '.join(line)
    print '*'*50

screen = get_example_screen()

print_screen(screen)
fill(screen, 2, 1, 5)
print_screen(screen)
