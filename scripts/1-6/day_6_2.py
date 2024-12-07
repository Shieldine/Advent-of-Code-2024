import copy

lab = []

with open("../../inputs/1-6/day_6.txt") as f:
    for line in f:
        lab.append(line.strip())

start = []

for i, line in enumerate(lab):
    indices = [i for i, x in enumerate(line) if x == "^"]
    if len(indices) > 0:
        start = [i, indices[0]]
        break


def walk(lab_map, start_point):
    visited_positions = [[start_point, "up"]]
    distinct_positions = [start_point]
    rows, cols = len(lab_map), len(lab_map[0])
    point = start_point
    direction = "up"

    while True:
        if direction == "up":
            next_point = [point[0] - 1, point[1]]
        elif direction == "down":
            next_point = [point[0] + 1, point[1]]
        elif direction == "left":
            next_point = [point[0], point[1] - 1]
        elif direction == "right":
            next_point = [point[0], point[1] + 1]

        if next_point[0] < 0 or next_point[0] >= rows or next_point[1] < 0 or next_point[1] >= cols:
            break

        if lab_map[next_point[0]][next_point[1]] == "#":
            if direction == "up":
                direction = "right"
            elif direction == "right":
                direction = "down"
            elif direction == "down":
                direction = "left"
            elif direction == "left":
                direction = "up"
        else:
            point = next_point
            if point not in distinct_positions:
                distinct_positions.append(point)
            if [point, direction] not in visited_positions:
                visited_positions.append([point, direction])
            else:
                return False

    return distinct_positions


def search_possible_obstacles(lab_map, start_point):
    possible_obstacles = 0
    possible_positions = walk(lab_map, start_point)
    possible_positions.remove(start_point)

    for i, position in enumerate(possible_positions):
        print(i, " of ", len(possible_positions))
        row_idx = position[0]
        col_idx = position[1]

        cur_map = copy.deepcopy(lab_map)

        row_as_list = list(cur_map[row_idx])
        row_as_list[col_idx] = "#"
        cur_map[row_idx] = ''.join(row_as_list)

        if not walk(cur_map, start_point):
            possible_obstacles += 1

    return possible_obstacles


print(search_possible_obstacles(lab, start))
