def print_map(tile_map, pos):
    tile_map[pos[0]][pos[1]] = "@"  # Mark the current position
    for row in tile_map:
        print(f'{"".join(row)}\n')
    tile_map[pos[0]][pos[1]] = "."  # Reset the position marker


def load_map_and_moves(file_path):
    tile_map = []
    moves = []
    pos = []

    with open(file_path) as f:
        mappy = True
        row = 0

        for line in f:
            if line == "\n":
                mappy = False
                continue

            if mappy:
                line = line.strip().replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")
                tile_map.append(line)
                if "@" in line:
                    pos = [row, line.index("@")]
            else:
                moves.append(line.strip())
            row += 1

        moves = "".join(moves)

    tile_map = [list(row) for row in tile_map]
    tile_map[pos[0]][pos[1]] = "."  # Replace starting point with a dot
    return tile_map, moves, pos


def find_boxes(box, direction, tile_map):
    positions = []

    for part in box:
        next_tile = tile_map[part[0] + direction][part[1]]
        if next_tile == "#":
            return -1
        elif next_tile in ["[", "]"]:
            if next_tile == "[":
                first = (part[0] + direction, part[1])
                second = (part[0] + direction, part[1] + 1)
            else:
                first = (part[0] + direction, part[1] - 1)
                second = (part[0] + direction, part[1])
            positions.append(first)
            positions.append(second)
            nested_boxes = find_boxes([first, second], direction, tile_map)
            if nested_boxes == -1:
                return -1
            positions.extend(nested_boxes)

    return positions


def process_moves(tile_map, moves, pos):
    for move in moves:
        next_pos = {
            "<": (pos[0], pos[1] - 1),
            "^": (pos[0] - 1, pos[1]),
            ">": (pos[0], pos[1] + 1),
            "v": (pos[0] + 1, pos[1]),
        }.get(move, pos)

        x, y = next_pos
        if tile_map[x][y] in ["[", "]"]:
            positions_to_move = [(x, y)]
            if tile_map[x][y] == "[":
                positions_to_move.append((x, y + 1))
            else:
                positions_to_move.append((x, y - 1))

            end = x, y
            valid = True

            match move:
                case "<":
                    while tile_map[end[0]][end[1] - 1] in ["[", "]"]:
                        if tile_map[end[0]][end[1] - 1] == "]":
                            positions_to_move.append((end[0], end[1] - 1))
                            positions_to_move.append((end[0], end[1] - 2))
                        end = (end[0], end[1] - 1)
                    if tile_map[end[0]][end[1] - 1] == "#":
                        valid = False
                case "^":
                    if tile_map[end[0]][end[1]] in ["[", "]"]:
                        if tile_map[end[0]][end[1]] == "]":
                            first = (end[0], end[1] - 1)
                            second = (end[0], end[1])
                        else:
                            first = (end[0], end[1])
                            second = (end[0], end[1] + 1)
                        nested_boxes = find_boxes([first, second], -1, tile_map)
                        if nested_boxes == -1:
                            valid = False
                        else:
                            positions_to_move.extend([first, second, *nested_boxes])
                    if tile_map[end[0]][end[1]] == "#":
                        valid = False
                case ">":
                    while tile_map[end[0]][end[1] + 1] in ["[", "]"]:
                        if tile_map[end[0]][end[1] + 1] == "[":
                            positions_to_move.append((end[0], end[1] + 1))
                            positions_to_move.append((end[0], end[1] + 2))
                        end = (end[0], end[1] + 1)
                    if tile_map[end[0]][end[1] + 1] == "#":
                        valid = False
                case "v":
                    if tile_map[end[0]][end[1]] in ["[", "]"]:
                        if tile_map[end[0]][end[1]] == "]":
                            first = (end[0], end[1] - 1)
                            second = (end[0], end[1])
                        else:
                            first = (end[0], end[1])
                            second = (end[0], end[1] + 1)
                        nested_boxes = find_boxes([first, second], 1, tile_map)
                        if nested_boxes == -1:
                            valid = False
                        else:
                            positions_to_move.extend([first, second, *nested_boxes])
                    if tile_map[end[0]][end[1]] == "#":
                        valid = False

            if valid:
                direction = {
                    "<": (0, -1),
                    "^": (-1, 0),
                    ">": (0, 1),
                    "v": (1, 0),
                }[move]
                positions_to_move = list(set(positions_to_move))
                positions_to_move.sort(key=lambda tup: (tup[0], tup[1]), reverse=(move in [">", "v"]))

                for position in positions_to_move:
                    dx, dy = direction
                    tile_map[position[0] + dx][position[1] + dy] = tile_map[position[0]][position[1]]
                    tile_map[position[0]][position[1]] = "."
                pos = [x, y]

        elif tile_map[x][y] != "#":
            pos = [x, y]

    return tile_map


def calculate_score(tile_map):
    return sum(idx * 100 + idx_c for idx, row in enumerate(tile_map) for idx_c, col in enumerate(row) if col == "[")


file_path = "../../inputs/13-18/day_15.txt"
tile_map, moves, pos = load_map_and_moves(file_path)
tile_map = process_moves(tile_map, moves, pos)
score = calculate_score(tile_map)
print(score)
