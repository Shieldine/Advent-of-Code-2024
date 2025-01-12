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

    def move_vertically(self, way, pos):
        dx = pos[0] - self.position[0]
        direction = -1, "^"

        if dx > 0:
            direction = 1, "v"

        for i in range(abs(dx)):
            nx = self.position[0] + direction[0]

            way.append(direction[1])
            self.position = (nx, self.position[1])

    def move_sideways(self, way, pos):
        dy = pos[1] - self.position[1]
        direction = -1, "<"

        if dy > 0:
            direction = 1, ">"

        for i in range(abs(dy)):
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
        pos = None

        for idx, row in enumerate(self.keypad):
            for idx_c, col in enumerate(row):
                if col == key:
                    pos = (idx, idx_c)

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
        pos = None

        for idx, row in enumerate(self.keypad):
            for idx_c, col in enumerate(row):
                if col == key:
                    pos = (idx, idx_c)

        up_down_first = False

        # that's if we'd run into the None
        if self.position[0] == 0 and pos == (0, 1):
            up_down_first = True

        # here we prioritise up and down over right
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


def calculate(sequence_list, keypads):
    score = 0

    for sequence in sequence_list:
        presses = sequence

        for cur_keypad in keypads:
            new_presses = []

            for cur_key in presses:
                new_presses.extend(cur_keypad.press_button(cur_key))

            presses = new_presses
        score += len(presses) * int("".join(sequence)[:-1])

    return score


robot_1 = NumericalKeypad()
robot_2 = DirectionalKeypad()
robot_3 = DirectionalKeypad()

all_keypads = [robot_1, robot_2, robot_3]

print(calculate(sequences, all_keypads))


# part two
all_keypads = [NumericalKeypad()]

for i in range(NUM_ROBOTS):
    all_keypads.append(DirectionalKeypad())

print(calculate(sequences, all_keypads))
