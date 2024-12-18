from copy import deepcopy

tile_map = []
moves = []

pos = []


def print_map(tile_map):
    tile_map[pos[0]][pos[1]] = "@"  # print current position
    for row in tile_map:
        print(f'{"".join(row)}\n')


with open("../../inputs/13-18/day_15.txt") as f:
    mappy = True
    row = 0

    for line in f:
        if line == "\n":
            mappy = False
            continue

        if mappy:
            line = line.strip().replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", '@.')
            tile_map.append(line)
            if "@" in line:
                pos = [row, line.index("@")]
        else:
            moves.append(line.strip())
        row += 1

    moves = "".join(moves)

tile_map = [list(row) for row in tile_map]

# replace starting point with dot
tile_map[pos[0]][pos[1]] = "."

print_map(deepcopy(tile_map))


def find_boxes(box, direction):
    positions = []

    for part in box:
        if tile_map[part[0]][part[1] + direction] == "#":
            return -1
        if tile_map[part[0]][part[1] + direction] == "[" or tile_map[part[0]][part[1] + direction] == "]":
            first = (box[0], box[1] + direction)
            if tile_map[part[0]][part[1] + direction] == "[":
                second = (box[0] + 1, box[1] + direction)
            else:
                second = (box[0] - 1, box[1] + direction)
            positions.append(first)
            positions.append(second)

            positions.append(find_boxes([first, second], direction))

    return positions


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

    if tile_map[x][y] == "[" or tile_map[x][y] == "]":

        # to keep track of all affected boxes
        positions_to_move = [(x, y)]

        # second part of the box
        if tile_map[x][y] == "[":
            positions_to_move.append((x, y + 1))
        else:
            positions_to_move.append((x, y - 1))

        end = x, y
        valid = True
        match move:
            case "<":
                # all da boxes to da left
                while tile_map[end[0]][end[1] - 1] == "[" or tile_map[end[0]][end[1] - 1] == "]":
                    if tile_map[end[0]][end[1] - 1] == "]":
                        end = end[0], end[1] - 1
                        positions_to_move.append((end[0], end[1] - 1))
                        positions_to_move.append((end[0], end[1] - 2))
                    if tile_map[end[0]][end[1] - 1] == "[":
                        end = end[0], end[1] - 1
                if tile_map[end[0]][end[1] - 1] == "#":
                    valid = False
                end = end[0], end[1] - 1
            case "^":
                # all da boxes up
                if tile_map[end[0] - 1][end[1]] == "[" or tile_map[end[0] - 1][end[1]] == "]":
                    first = (end[0] - 1, end[1])
                    if tile_map[end[0] - 1][end[1]] == "[":
                        second = (end[0] - 1, end[1] + 1)
                    else:
                        second = (end[0] - 1, end[1] - 1)
                    boxes = find_boxes([first, second], -1)

                    if boxes == -1:
                        valid = False
                    else:
                        positions_to_move.append(first)
                        positions_to_move.append(second)
                        positions_to_move.append(boxes)
                if tile_map[end[0] - 1][end[1]] == "#":
                    valid = False
            case ">":
                # all da boxes to da right
                while tile_map[end[0]][end[1] + 1] == "[" or tile_map[end[0]][end[1] + 1] == "]":
                    if tile_map[end[0]][end[1] + 1] == "[":
                        end = end[0], end[1] + 1
                        positions_to_move.append((end[0], end[1] + 1))
                        positions_to_move.append((end[0], end[1] + 2))
                    if tile_map[end[0]][end[1] + 1] == "]":
                        end = end[0], end[1] + 1
                if tile_map[end[0]][end[1] + 1] == "#":
                    valid = False
                end = end[0], end[1] + 1
            case "v":
                # all da boxes down!
                if tile_map[end[0] + 1][end[1]] == "[" or tile_map[end[0] + 1][end[1]] == "]":
                    first = (end[0] + 1, end[1])
                    if tile_map[end[0] + 1][end[1]] == "[":
                        second = (end[0] + 1, end[1] + 1)
                    else:
                        second = (end[0] + 1, end[1] - 1)
                    boxes = find_boxes([first, second], 1)

                    if boxes == -1:
                        valid = False
                    else:
                        positions_to_move.append(first)
                        positions_to_move.append(second)
                        positions_to_move.append(boxes)
                end = end[0] + 1, end[1]

        if valid:
            pos = [x, y]
            direction = (0, 0)
            match move:
                case "<":
                    direction = (0, -1)
                    positions_to_move = sorted(positions_to_move, key=lambda tup: tup[1])
                case "^":
                    direction = (-1, 0)
                    positions_to_move = sorted(positions_to_move, key=lambda tup: tup[0])
                case ">":
                    direction = (0, 1)
                    positions_to_move = sorted(positions_to_move, key=lambda tup: tup[1])[::-1]
                case "v":
                    direction = (1, 0)
                    positions_to_move = sorted(positions_to_move, key=lambda tup: tup[0])[::-1]

            print(positions_to_move)

            for position in positions_to_move:
                tile_map[position[0] + direction[0]][position[1] + direction[1]] = tile_map[position[0]][position[1]]
                tile_map[position[0] + direction[0]][position[1]] = "."

    elif tile_map[x][y] != "#":
        pos = [x, y]

score = 0

for idx, row in enumerate(tile_map):
    for idx_c, col in enumerate(row):
        if col == "[":  # NEW: score is calculated by the left side of a box
            score += idx * 100 + idx_c

print(score)
