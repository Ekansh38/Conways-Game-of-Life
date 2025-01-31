import pygame
from pygame.math import Vector2

from button import Button
from grid import Grid

# Basic setup

pygame.init()
pygame.mixer.init()

grid = Grid()

BOTTOM_MARGIN = 100
SCREEN_SIZE = Vector2(
    grid.cols * grid.cell_size, (grid.rows * grid.cell_size) + BOTTOM_MARGIN
)
FPS = 60
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()
running = True

button_size = Vector2(100, 50)
button_pos = Vector2(
    ((grid.cols * grid.cell_size) // 2) - (button_size.x // 2),
    (grid.rows * grid.cell_size) + (BOTTOM_MARGIN // 2) - (button_size.y // 2),
)
button = Button(
    button_pos,
    "START",
    button_size,
    "darkgreen",
    "black",
)

can_pause = True
pause_timer = -1

# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    grid.input()
    grid.draw_cells(screen)
    grid.draw_grid(screen)

    button.draw(screen)
    if button.check_click() and can_pause:
        can_pause = False
        if grid.start:
            grid.start = False
            button.text = "START"
            button.color = "darkgreen"
        else:
            grid.start = True
            button.text = "STOP"
            button.color = "red"

    grid.play()

    if not can_pause:
        pause_timer += 1
        if pause_timer >= 8:
            can_pause = True
            pause_timer = -1

    pygame.display.update()
    clock.tick(FPS)
