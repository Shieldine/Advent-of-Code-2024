import heapq

WIDTH = 71
HEIGHT = 71

START = (0, 0)
END = (WIDTH - 1, HEIGHT - 1)

i = 2000


def solve_maze(maze, start, end):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W

    # manhattan distance heuristic
    def heuristic(pos, end):
        return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

    # priority queue: (total_cost, current_cost, position, direction)
    # direction is an index into `directions` (0=N, 1=E, 2=S, 3=W)
    pq = []
    heapq.heappush(pq, (0, 0, start, 1))

    visited = set()

    while pq:
        total_cost, current_cost, (y, x), direction = heapq.heappop(pq)

        if (y, x) == end:
            return total_cost

        if (y, x, direction) in visited:
            continue
        visited.add((y, x, direction))

        for i, (dy, dx) in enumerate(directions):
            ny, nx = y + dy, x + dx

            if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] != '#':
                move_cost = 1
                new_cost = current_cost + move_cost
                heapq.heappush(pq, (new_cost + heuristic((ny, nx), end), new_cost, (ny, nx), i))

    return -1


while True:
    grid = [['.' for x in range(HEIGHT)] for y in range(WIDTH)]

    with open("../../inputs/13-18/day_18.txt") as file:
        for idx, line in enumerate(file):
            if idx > i:
                break
            coords = line.strip().split(",")
            grid[int(coords[1])][int(coords[0])] = "#"

    steps = solve_maze(grid, START, END)
    if steps == -1:
        print("Blockage found")
        break

    i += 1

with open("../../inputs/13-18/day_18.txt") as file:
    for idx, line in enumerate(file):
        if idx == i:
            print(f"Coords: {line.strip()}")
        if idx > i:
            break
