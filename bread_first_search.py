import pygame
from queue import Queue

HEIGHT, WIDTH = 900, 900


def reconstructPath(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.makePath()
        draw()


def bfs(draw, grid, start, end):
    queue = Queue()
    queue.put(start)
    visited = set()
    came_from = {}

    while not queue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = queue.get()

        if current == end:
            reconstructPath(came_from, end, draw)
            return True

        if current not in visited:
            visited.add(current)
            current.makeVisiting()

            for neighbor in current.neighbors:
                if neighbor not in visited:
                    queue.put(neighbor)
                    came_from[neighbor] = current

        draw()

        if current != start:
            current.makeVisited()

    return False
