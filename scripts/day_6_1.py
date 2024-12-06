lab = []

with open("../inputs/day_6.txt") as f:
    for line in f:
        lab.append(line.strip())

start = []

for i, line in enumerate(lab):
    indices = [i for i, x in enumerate(line) if x == "^"]
    if len(indices) > 0:
        start = [i, indices[0]]
        break


def walk(lab_map, start_point):
    num = 1
    visited_positions = [start_point]
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
            if point not in visited_positions:
                visited_positions.append(point)
                num += 1

    return num


print(walk(lab, start))
