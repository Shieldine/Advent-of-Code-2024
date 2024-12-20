with open("../../inputs/13-18/day_16.txt") as f:
    maze = f.read()

maze = [list(row) for row in maze.splitlines()]

start = end = None
for y, row in enumerate(maze):
    for x, cell in enumerate(row):
        if cell == 'S':
            start = (y, x)
        elif cell == 'E':
            end = (y, x)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

lowest_cost = 93436
rows, cols = len(maze), len(maze[0])


def solve_with_dfs(maze, position, path, cost, prev_direction, visited):
    if cost > lowest_cost:
        return []
    x, y = position

    if x < 0 or x >= rows or y < 0 or y >= cols or maze[x][y] == '#' or position in visited:
        return []

    if maze[x][y] == 'E':
        return [(path + [position], cost)]

    visited.add(position)
    path.append(position)

    paths = []
    for i, (dx, dy) in enumerate(directions):
        new_position = (x + dx, y + dy)
        step_cost = 1
        turn_cost = 1000 if prev_direction is not None and prev_direction != i else 0
        paths += solve_with_dfs(maze, new_position, path, cost + step_cost + turn_cost, i, visited)

    path.pop()
    visited.remove(position)

    return paths


all_paths = solve_with_dfs(maze, start, [], 0, [], set())
min_cost = min([cost for _, cost in all_paths])

visited_locations = set()

for path, cost in all_paths:
    if cost == min_cost:
        visited_locations.update(path)

print(len(visited_locations))
