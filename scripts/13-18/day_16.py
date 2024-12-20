import heapq


def solve_maze(maze):
    maze = [list(row) for row in maze.splitlines()]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W

    # find start and end positions
    start = end = None
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (y, x)
            elif cell == 'E':
                end = (y, x)

    # manhattan distance heuristic
    def heuristic(pos, end):
        return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

    # Priority queue: (total_cost, current_cost, position, direction, path)
    pq = []
    heapq.heappush(pq, (0, 0, start, 1, []))

    visited = set()

    while pq:
        total_cost, current_cost, (y, x), direction, path = heapq.heappop(pq)

        if (y, x) == end:
            full_path = path + [(y, x)]
            for (py, px) in full_path:
                if maze[py][px] != 'S' and maze[py][px] != 'E':
                    maze[py][px] = '+'
            return total_cost, full_path, maze

        if (y, x, direction) in visited:
            continue
        visited.add((y, x, direction))

        for i, (dy, dx) in enumerate(directions):
            ny, nx = y + dy, x + dx

            if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] != '#':
                move_cost = 1
                turn_cost = 1000 if i != direction else 0
                new_cost = current_cost + move_cost + turn_cost
                new_path = path + [(y, x)]  # Add current position to path
                heapq.heappush(pq, (new_cost + heuristic((ny, nx), end), new_cost, (ny, nx), i, new_path))

    return -1, [], maze


def print_maze(maze):
    for row in maze:
        print(''.join(row))


with open("../../inputs/13-18/day_16.txt") as f:
    maze = f.read()

cost, path, maze_with_path = solve_maze(maze)
print(f"Cost to reach the end: {cost}")
print("\nMaze with path:")
print_maze(maze_with_path)
