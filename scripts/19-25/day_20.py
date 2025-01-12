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


# manhattan distance heuristic
def heuristic(pos, end):
    return abs(pos[0] - end[0]) + abs(pos[1] - end[1])


def solve_maze(maze):
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
                heapq.heappush(pq, (current_cost + heuristic((ny, nx), end), current_cost + 1, (ny, nx), i))

    return -1


blockage_indices = []

for idx, row in enumerate(track):
    for idx_c, col in enumerate(row):
        if 0 < idx < len(track) - 1 and 0 < idx_c < len(track[0]) - 1:
            if track[idx][idx_c] == '#':
                blockage_indices.append((idx, idx_c))

base_cost = solve_maze(track)

track_nums = {}

for idx, block in enumerate(blockage_indices):
    # don't try blocks that are far away from the points
    if heuristic(block, start) + heuristic(block, end) > base_cost:
        continue

    direction_count = 0
    for direction in directions:
        dx, dy = block[0] + direction[0], block[1] + direction[1]
        if track[dx][dy] == '#':
            direction_count += 1

    if direction_count == 4:
        continue

    # modify in-place instead of copying to... well, avoid copying
    track[block[0]][block[1]] = "."
    cur_cost = solve_maze(track)
    track[block[0]][block[1]] = "#"

    difference = base_cost - cur_cost

    if difference > 0:
        if difference not in track_nums.keys():
            track_nums[difference] = 1
        else:
            track_nums[difference] = track_nums[difference] + 1

count = 0

for key, value in track_nums.items():
    if key >= 100:
        count += value

print(count)
print(time.time() - start_time)
