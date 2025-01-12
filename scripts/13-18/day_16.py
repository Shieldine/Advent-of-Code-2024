with open("../../inputs/13-18/day_16.txt") as f:
    maze = f.read()

maze = [list(row) for row in maze.splitlines()]


def print_maze(maze, path=None):
    if path is not None:
        for y, x in path:
            maze[y][x] = '+'

    for row in maze:
        print(''.join(row))


start = end = None
for y, row in enumerate(maze):
    for x, cell in enumerate(row):
        if cell == 'S':
            start = (y, x)
        elif cell == 'E':
            end = (y, x)

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # E, S, W, N


def find_ways(grid):
    queue = [(start, [start], 0, 0)]  # start, history, cost, direction (start facing east)
    paths = []
    visited = {}  # holds visited positions including the direction and cost, as in: ((y, x), direction): cost

    while queue:
        (y, x), cur_history, cur_cost, cur_direction = queue.pop(0)

        if (y, x) == end:
            paths.append((cur_history, cur_cost))
            continue

        if ((y, x), cur_direction) in visited and visited[((y, x), cur_direction)] < cur_cost:  # last one checks if
            # we found a possibly shorter path even if we've visited this position before
            continue

        visited[((y, x), cur_direction)] = cur_cost

        for direction, (dy, dx) in enumerate(directions):
            new_y, new_x = y + dy, x + dx

            # don't keep going if we've hit a border or if we've been here before (prevent loops)
            if grid[new_y][new_x] == '#' or (new_y, new_x) in cur_history:
                continue

            if cur_direction == direction:
                # note: we use the 'cur_history + [(new_y, new_x)]' syntax to explicitly construct a new list
                # python lists are passed by reference, so if we just did .append and then passed, we'd work with
                # one list in all iterations
                queue.append(((new_y, new_x), cur_history + [(new_y, new_x)], cur_cost + 1, direction))  # move forward
            else:
                queue.append(((y, x), cur_history, cur_cost + 1000, direction))  # turn

    return paths


all_paths = find_ways(maze)
min_cost = min([cost for _, cost in all_paths])
shortest_paths = [path for path, cost in all_paths if cost == min_cost]

tiles = set()

for path in shortest_paths:
    tiles.update(path)

print(min_cost)
print(len(tiles))
