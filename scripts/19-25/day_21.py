import time

NUM_ROBOTS = 25
sequences = []

with open("../../inputs/19-25/day_21.txt") as f:
    for line in f:
        if line.strip() != "":
            sequences.append(line.strip())

sequences = [list(sequence) for sequence in sequences]


class KeypadBase:
    def __init__(self, keypad, position):
        self.keypad = keypad
        self.position = position
        self.key_positions = {}
        for idx, row in enumerate(self.keypad):
            for idx_c, col in enumerate(row):
                self.key_positions[col] = (idx, idx_c)

    def move_vertically(self, way, pos):
        dx = pos[0] - self.position[0]
        direction = -1, "^"

        if dx > 0:
            direction = 1, "v"

        for _ in range(abs(dx)):
            nx = self.position[0] + direction[0]

            way.append(direction[1])
            self.position = (nx, self.position[1])

    def move_sideways(self, way, pos):
        dy = pos[1] - self.position[1]
        direction = -1, "<"

        if dy > 0:
            direction = 1, ">"

        for _ in range(abs(dy)):
            ny = self.position[1] + direction[0]
            way.append(direction[1])
            self.position = (self.position[0], ny)


class NumericalKeypad(KeypadBase):
    def __init__(self):
        super().__init__(
            [
                ["7", "8", "9"],
                ["4", "5", "6"],
                ["1", "2", "3"],
                [None, "0", "A"]
            ],
            (3, 2)
        )

    def press_button(self, key):
        way = []
        pos = self.key_positions[key]

        up_down_first = False

        # check if we'd run into the None
        if self.position[0] == 3 and pos[0] < 3 and pos[1] == 0:
            way.append("^")
            up_down_first = True
            self.position = (self.position[0] - 1, self.position[1])

        # prioritise up and down over right
        if (pos[1] - self.position[1]) > 0 and not (self.position[0] < 3 and pos[0] == 3 and self.position[1] == 0):
            up_down_first = True

        if up_down_first:
            self.move_vertically(way, pos)
            self.move_sideways(way, pos)
        else:
            self.move_sideways(way, pos)
            self.move_vertically(way, pos)

        way.append("A")
        return way


class DirectionalKeypad(KeypadBase):
    def __init__(self):
        super().__init__(
            [
                [None, "^", "A"],
                ["<", "v", ">"]
            ],
            (0, 2)
        )

    def press_button(self, key):
        way = []
        pos = self.key_positions[key]

        up_down_first = False

        if self.position[0] == 0 and pos == (0, 1):
            up_down_first = True

        if (pos[1] - self.position[1]) > 0:
            up_down_first = True

        if up_down_first:
            self.move_vertically(way, pos)
            self.move_sideways(way, pos)
        else:
            self.move_sideways(way, pos)
            self.move_vertically(way, pos)

        way.append("A")
        return way


sequence_cache = {}  # position, key -> sequence, new_pos

temp_robot = DirectionalKeypad()

for i in range(2):
    for j in range(3):
        if (i, j) == (0, 0):
            continue

        for row in temp_robot.keypad:
            for key in row:
                temp_robot.position = (i, j)
                sequence_cache[((i, j), key)] = temp_robot.press_button(key), temp_robot.position

cost_cache = {}


def calculate_cost(key, robots, idx):
    cache_key = (robots[idx].position, key, idx)

    if cache_key in cost_cache:
        cost, final_pos = cost_cache[cache_key]
        robots[idx].position = final_pos
        return cost

    new_sequence = sequence_cache[(robots[idx].position, key)]

    if idx == 0:
        robots[idx].position = new_sequence[1]
        cost_cache[cache_key] = len(new_sequence[0]), robots[idx].position
        return len(new_sequence[0])

    cost = 0
    for cur_key in new_sequence[0]:
        robots[idx].position = new_sequence[1]
        cost += calculate_cost(cur_key, robots, idx - 1)

    cost_cache[cache_key] = cost, robots[idx].position
    return cost


def calculate(sequence_list, keypads):
    start_time = time.time()
    first_robot = NumericalKeypad()

    score = 0

    for sequence in sequence_list:
        cur_score = 0
        presses = []

        # calculate presses of numerical keyboard
        for key in sequence:
            presses.extend(first_robot.press_button(key))

        # calculate the rest
        for idx, key in enumerate(presses):
            cur_score += calculate_cost(key, keypads, len(keypads) - 1)
        score += cur_score * int("".join(sequence)[:-1])

    print(time.time() - start_time)
    return score


robot_2 = DirectionalKeypad()
robot_3 = DirectionalKeypad()

all_keypads = [robot_2, robot_3]

print(calculate(sequences, all_keypads))

# part two
all_keypads = []

for _ in range(NUM_ROBOTS):
    all_keypads.append(DirectionalKeypad())

print(calculate(sequences, all_keypads))
