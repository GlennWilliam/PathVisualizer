import pygame
import heapq

HEIGHT, WIDTH = 900, 900


def reconstructPath(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.makePath()
        draw()


def dijkstra(draw, grid, start, end):
    count = 0
    heap = [(0, count, start)]
    came_from = {}
    cost_so_far = {node: float('inf') for row in grid for node in row}
    cost_so_far[start] = 0

    while heap:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = heapq.heappop(heap)[2]

        if current == end:
            reconstructPath(came_from, end, draw)
            return True

        for neighbor in current.neighbors:
            new_cost = cost_so_far[current] + 1
            if new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                count += 1
                heapq.heappush(heap, (new_cost, count, neighbor))
                came_from[neighbor] = current
                if neighbor != end:
                    neighbor.makeVisiting()

        draw()

        if current != start:
            current.makeVisited()

    return False
