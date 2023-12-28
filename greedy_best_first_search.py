import pygame
import math
import heapq

HEIGHT, WIDTH = 900, 900


def reconstructPath(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.makePath()
        draw()


def greedyBestFirstSearch(draw, grid, start, end):
    count = 0
    heap = [(heuristic(end.getPosition(), start.getPosition()), count, start)]
    came_from = {}

    while heap:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = heapq.heappop(heap)[2]

        if current == end:
            reconstructPath(came_from, end, draw)
            return True

        for neighbor in current.neighbors:
            if neighbor not in came_from:
                count += 1
                heapq.heappush(heap, (heuristic(end.getPosition(), neighbor.getPosition()), count, neighbor))
                came_from[neighbor] = current
                if neighbor != end:
                    neighbor.makeVisiting()

        draw()

        if current != start:
            current.makeVisited()

    return False


def heuristic(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)
