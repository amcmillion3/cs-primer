import os
import random
import time

WIDTH, HEIGHT, ITERATIONS, DELAY  = 20, 20, 50, 0.01

OFFSETS = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
)

random.seed(42)

def alive(cells, x, y):
    neighbors = sum(cells[(y + dy) % HEIGHT][(x + dx) % WIDTH] for dx, dy in OFFSETS)
    return 2 <= neighbors <=3 if cells[y][x] else neighbors == 3

def next_state(cells):
    return [
        [alive(cells, x, y) for x in range(WIDTH)]
        for y in range(HEIGHT)
    ]

if __name__ == "__main__":
    cells = [[random.random() < 0.3 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for _ in range(ITERATIONS):
        os.system('clear')
        print('\n'.join(''.join('■' if x else '□' for x in row) for row in cells))
        cells = next_state(cells)
        time.sleep(DELAY)
