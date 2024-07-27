import pygame
from pygame.math import Vector2

from cell import Cell


class Grid:
    def __init__(self):
        self.start = False
        self.rows = 20
        self.cols = 35
        self.cell_size = 50
        self.line_color = "black"
        self.generation = 0
        self.line_thickness = 2
        self.cells = []
        self.create_cells()

    def create_cells(self):
        for x in range(0, self.cols):
            for y in range(0, self.rows):
                cell = Cell(Vector2(x, y))
                self.cells.append(cell)

    def play(self):
        if self.start:
            new_cells = []

            for cell in self.cells:
                self.find_neighbors(cell)
                alive_neighbors = 0
                for neighbor in cell.neighbors:
                    if neighbor.alive:
                        alive_neighbors += 1

                if cell.alive:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_cell = Cell(cell.pos)
                        new_cell.kill()
                        new_cells.append(new_cell)
                    else:
                        new_cells.append(cell)

                if not cell.alive:
                    if alive_neighbors == 3:
                        new_cell = Cell(cell.pos)
                        new_cell.revive()
                        new_cells.append(new_cell)
                    else:
                        new_cells.append(cell)

            self.cells = new_cells
            self.generation += 1

    def find_neighbors(self, cell):
        cell.neighbors = []
        if 0 < cell.pos.x < self.cols and 0 < cell.pos.y < self.rows:
            directions = [
                Vector2(0, -1),
                Vector2(0, 1),
                Vector2(-1, 0),
                Vector2(1, 0),
                Vector2(-1, -1),
                Vector2(1, -1),
                Vector2(-1, 1),
                Vector2(1, 1),
            ]
            for direction in directions:
                neighbor_pos = cell.pos + direction
                for neighbor_cell in self.cells:
                    if neighbor_cell.pos == neighbor_pos:
                        cell.neighbors.append(neighbor_cell)
                        break

    def input(self):
        if not self.start:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pos = Vector2(
                mouse_pos[0] // self.cell_size, mouse_pos[1] // self.cell_size
            )
            for cell in self.cells:
                if cell.pos == mouse_pos:
                    if pygame.mouse.get_pressed()[0]:
                        cell.revive()
                    elif pygame.mouse.get_pressed()[2]:
                        cell.kill()

    def draw_grid(self, screen):
        for x in range(0, self.cols + 1):
            pygame.draw.line(
                screen,
                self.line_color,
                (x * self.cell_size, 0),
                (x * self.cell_size, self.rows * self.cell_size),
                self.line_thickness,
            )
            for y in range(0, self.rows + 1):
                pygame.draw.line(
                    screen,
                    self.line_color,
                    (0, y * self.cell_size),
                    (self.cols * self.cell_size, y * self.cell_size),
                    self.line_thickness,
                )

    def draw_cells(self, screen):
        for cell in self.cells:
            cell.draw(screen, self.cell_size)
