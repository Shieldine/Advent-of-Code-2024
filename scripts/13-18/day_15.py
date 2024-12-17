tile_map = []
moves = []

pos = []


def print_map(tile_map):
    for row in tile_map:
        print(f'{"".join(row)}\n')


with open("../../inputs/13-18/day_15.txt") as f:
    mappy = True
    row = 0

    for line in f:
        if line == "\n":
            mappy = False
            continue

        if "@" in line:
            pos = [row, line.index("@")]

        if mappy:
            tile_map.append(line.strip())
        else:
            moves.append(line.strip())
        row += 1

    moves = "".join(moves)

tile_map = [list(row) for row in tile_map]

for idx, row in enumerate(tile_map):
    for idx_c, col in enumerate(row):
        if col == "@":
            tile_map[idx][idx_c] = "."

for move in moves:
    if move == "<":  # left
        next_pos = (pos[0], pos[1] - 1)
    elif move == "^":  # up
        next_pos = (pos[0] - 1, pos[1])
    elif move == ">":  # right
        next_pos = (pos[0], pos[1] + 1)
    elif move == "v":  # down
        next_pos = (pos[0] + 1, pos[1])
    else:
        continue

    x, y = next_pos

    if tile_map[x][y] == "O":
        end = x, y
        valid = True
        match move:
            case "<":
                while tile_map[end[0]][end[1] - 1] == "O":
                    end = end[0], end[1] - 1
                if tile_map[end[0]][end[1] - 1] == "#":
                    valid = False
                end = end[0], end[1] - 1
            case "^":
                while tile_map[end[0] - 1][end[1]] == "O":
                    end = end[0] - 1, end[1]
                if tile_map[end[0] - 1][end[1]] == "#":
                    valid = False
                end = end[0] - 1, end[1]
            case ">":
                while tile_map[end[0]][end[1] + 1] == "O":
                    end = end[0], end[1] + 1
                if tile_map[end[0]][end[1] + 1] == "#":
                    valid = False
                end = end[0], end[1] + 1
            case "v":
                while tile_map[end[0] + 1][end[1]] == "O":
                    end = end[0] + 1, end[1]
                if tile_map[end[0] + 1][end[1]] == "#":
                    valid = False
                end = end[0] + 1, end[1]

        if valid:
            tile_map[end[0]][end[1]] = "O"
            tile_map[x][y] = "."
            pos = [x, y]
    elif tile_map[x][y] != "#":
        pos = [x, y]

score = 0

for idx, row in enumerate(tile_map):
    for idx_c, col in enumerate(row):
        if col == "O":
            score += idx * 100 + idx_c

print(score)


