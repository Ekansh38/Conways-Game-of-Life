import pygame
from pygame.math import Vector2

from button import Button
from grid import Grid

# Basic setup

pygame.init()

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
start_button = Button(
    button_pos,
    "START",
    button_size,
    "darkgreen",
    "black",
)

preivous_mouse_pressed = False
# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pressed = pygame.mouse.get_pressed()[0]
    screen.fill("white")
    grid.input()
    grid.draw_cells(screen)
    grid.draw_grid(screen)

    start_button.draw(screen)
    if start_button.check_click(preivous_mouse_pressed):
        if grid.start:
            grid.start = False
        else:
            grid.start = True

    grid.play()

    pygame.display.update()
    clock.tick(FPS)
    preivous_mouse_pressed = mouse_pressed
