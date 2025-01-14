import heapq
import time

start_time = time.time()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W

track = []

with open("../../inputs/19-25/day_20.txt") as file:
    for line in file:
        track.append(line.strip())

track = [list(line) for line in track]

# find start and end positions
start = end = None
for y, row in enumerate(track):
    for x, cell in enumerate(row):
        if cell == 'S':
            start = (y, x)
        elif cell == 'E':
            end = (y, x)


def manhattan_distance(pos, goal):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])


# solve maze once with backtracking
def solve_maze(maze):
    # priority queue: (total_cost, current_cost, position, direction, path)
    pq = []
    heapq.heappush(pq, (0, 0, start, 1, []))

    visited = set()

    while pq:
        total_cost, current_cost, (y, x), direction, path = heapq.heappop(pq)

        if (y, x) == end:
            return path + [(y, x)]

        if (y, x, direction) in visited:
            continue
        visited.add((y, x, direction))

        for i, (dy, dx) in enumerate(directions):
            ny, nx = y + dy, x + dx

            if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] != '#':
                new_path = path + [(y, x)]
                heapq.heappush(pq,
                               (current_cost + 1 + manhattan_distance((ny, nx), end), current_cost + 1, (ny, nx), i,
                                new_path))

    return []


base_path = solve_maze(track)


# "cheating" means jumping to a different position on the base path.
# for each position, we need to scan if another one is reachable with our k
# if that's the case, jump and check how many picoseconds we saved

def find_shortcuts(path, k):
    saved_costs = {}

    for idx, point in enumerate(path):
        for idx_2, second_point in enumerate(path):
            if point == second_point:
                continue
            if idx > idx_2:
                continue
            distance = manhattan_distance(point, second_point)
            if distance <= k:
                cur_saved = (idx_2 - idx) - distance
                if cur_saved < 100:  # we don't care if it's less than 100 picoseconds saved
                    continue
                if cur_saved not in saved_costs:
                    saved_costs[cur_saved] = 1
                else:
                    saved_costs[cur_saved] += 1

    return saved_costs


# part 1
print(sum(find_shortcuts(base_path, 2).values()))
print(time.time() - start_time)


# part 2
start_time = time.time()
print(sum(find_shortcuts(base_path, 20).values()))
print(time.time() - start_time)
