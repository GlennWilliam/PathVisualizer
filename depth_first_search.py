import pygame
import math

HEIGHT, WIDTH = 900, 900


def reconstructPath(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.makePath()
        draw()


def dfs(draw, grid, start, end):
    stack = [start]
    visited = set()
    came_from = {}

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = stack.pop()

        if current == end:
            reconstructPath(came_from, end, draw)
            return True

        if current not in visited:
            visited.add(current)
            current.makeVisiting()

            for neighbor in current.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    came_from[neighbor] = current

        draw()

        if current != start:
            current.makeVisited()

    return False
