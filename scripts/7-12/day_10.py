topo_map = []

with open("../../inputs/7-12/day_10.txt") as f:
    for line in f:
        cur_nums = []
        for num in line.strip():
            cur_nums.append(int(num))
        topo_map.append(cur_nums)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

start_points = []
visited_endpoints = set()

for idx, row in enumerate(topo_map):
    for idx_c, col in enumerate(row):
        if topo_map[idx][idx_c] == 0:
            start_points.append([idx, idx_c])


def walk(point, by_rating=False):
    if topo_map[point[0]][point[1]] == 9:
        if by_rating:
            return 1
        if (point[0], point[1]) not in visited_endpoints:
            visited_endpoints.add((point[0], point[1]))
            return 1
        else:
            return 0

    count = 0

    for direction in directions:
        new_point = (point[0] + direction[0], point[1] + direction[1])

        if not 0 <= new_point[0] < len(topo_map) or not 0 <= new_point[1] < len(topo_map[0]):
            continue

        if topo_map[new_point[0]][new_point[1]] == topo_map[point[0]][point[1]] + 1:
            count += walk(new_point, by_rating=by_rating)

    return count


scores = 0
scores_by_rating = 0

for point in start_points:
    visited_endpoints = set()
    scores += walk(point, False)
    scores_by_rating += walk(point, True)

print(scores)
print(scores_by_rating)
