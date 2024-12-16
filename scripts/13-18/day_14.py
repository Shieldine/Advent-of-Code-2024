from math import floor

robots = []

vis = open("../../files/day_14_vis.txt", "w")

with open("../../inputs/13-18/day_14.txt") as f:
    for line in f:
        position, velocity = line.strip().split(" ")
        position = position.replace("p=", "")
        velocity = velocity.replace("v=", "")

        robots.append({
            "position": [int(p) for p in position.strip().split(",")],
            "velocity": [int(v) for v in velocity.strip().split(",")]
        })

SIZE = [101, 103]
DURATION = 10000


def print_arrangements(seconds):
    tilemap = [[" " for _ in range(SIZE[0])] for _ in range(SIZE[1])]
    for r in robots:
        tilemap[r["position"][1]][r["position"][0]] = "X"

    vis.write(f"{seconds}\n")

    for row in tilemap:
        vis.write(f"{''.join(row)}\n")

    vis.write("\n")


def find_lots_of_x(seconds):
    tilemap = [[" " for _ in range(SIZE[1])] for _ in range(SIZE[0])]

    for r in robots:
        tilemap[r["position"][0]][r["position"][1]] = "X"

    for idx, row in enumerate(tilemap):
        if "X" * 10 in "".join(row):
            print(f"row: {idx} at {seconds} seconds")
            print_arrangements(seconds)
            return

    for col_idx in range(len(tilemap[0])):
        column = [tilemap[row_idx][col_idx] for row_idx in range(len(tilemap))]
        if "X" * 10 in "".join(column):
            print(f"col: {col_idx} at {seconds} seconds")


moves = 1

for _ in range(DURATION):
    for robot in robots:
        new_position = [
            (robot["position"][0] + robot["velocity"][0]) % SIZE[0],
            (robot["position"][1] + robot["velocity"][1]) % SIZE[1]
        ]

        new_position[0] = new_position[0] if new_position[0] >= 0 else new_position[0] + SIZE[0]
        new_position[1] = new_position[1] if new_position[1] >= 0 else new_position[1] + SIZE[1]

        robot["position"] = new_position

    find_lots_of_x(moves)
    moves += 1

up_left = 0
up_right = 0
down_left = 0
down_right = 0

for robot in robots:
    if robot["position"][0] == floor(SIZE[0] / 2) or robot["position"][1] == floor(SIZE[1] / 2):
        continue

    if robot["position"][0] > SIZE[0] / 2:
        if robot["position"][1] > SIZE[1] / 2:
            down_right += 1
        else:
            up_right += 1
    else:
        if robot["position"][1] > SIZE[1] / 2:
            down_left += 1
        else:
            up_left += 1

result = up_left * up_right * down_left * down_right
print(result)

vis.close()
