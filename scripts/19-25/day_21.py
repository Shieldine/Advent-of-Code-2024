sequences = []

with open("../../inputs/19-25/day_21.txt") as f:
    for line in f:
        if line.strip() != "":
            sequences.append(line.strip())

sequences = [list(sequence) for sequence in sequences]


class NumericalKeypad:
    def __init__(self):
        self.keypad = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            [None, "0", "A"]
        ]
        self.position = (3, 2)

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

        if up_down_first:
            # up/down
            dx = pos[0] - self.position[0]
            direction = -1, "^"

            if dx > 0:
                direction = 1, "v"

            for i in range(abs(dx)):
                nx = self.position[0] + direction[0]

                way.append(direction[1])
                self.position = (nx, self.position[1])

            # left/right
            dy = pos[1] - self.position[1]
            direction = -1, "<"

            if dy > 0:
                direction = 1, ">"

            for i in range(abs(dy)):
                ny = self.position[1] + direction[0]

                way.append(direction[1])
                self.position = (self.position[0], ny)
        else:
            # left/right
            dy = pos[1] - self.position[1]
            direction = -1, "<"

            if dy > 0:
                direction = 1, ">"

            for i in range(abs(dy)):
                ny = self.position[1] + direction[0]

                way.append(direction[1])
                self.position = (self.position[0], ny)
            # up/down
            dx = pos[0] - self.position[0]
            direction = -1, "^"

            if dx > 0:
                direction = 1, "v"

            for i in range(abs(dx)):
                nx = self.position[0] + direction[0]

                way.append(direction[1])
                self.position = (nx, self.position[1])

        way.append("A")
        return way


class DirectionalKeypad:
    def __init__(self):
        self.keypad = [
            [None, "^", "A"],
            ["<", "v", ">"]
        ]

        self.position = (0, 2)

    def press_button(self, key):
        way = []
        pos = None

        for idx, row in enumerate(self.keypad):
            for idx_c, col in enumerate(row):
                if col == key:
                    pos = (idx, idx_c)

        # check if we'd run into None
        if self.position[0] == 0 and pos == (1, 0):
            way.append("v")
            self.position = (self.position[0] + 1, self.position[1])

        # decide if we should go left/right or up/down first
        up_down_first = True

        if self.position[1] == 2 and pos[1] == 2 or self.position[1] == 0 and pos[1] == 0:
            up_down_first = False

        if up_down_first:
            # up/down
            dx = pos[0] - self.position[0]
            direction = -1, "^"

            if dx > 0:
                direction = 1, "v"

            for i in range(abs(dx)):
                nx = self.position[0] + direction[0]

                way.append(direction[1])
                self.position = (nx, self.position[1])

            # left-right
            dy = pos[1] - self.position[1]
            direction = -1, "<"

            if dy > 0:
                direction = 1, ">"

            for i in range(abs(dy)):
                ny = self.position[1] + direction[0]
                way.append(direction[1])
                self.position = (self.position[0], ny)
        else:
            # left-right
            dy = pos[1] - self.position[1]
            direction = -1, "<"

            if dy > 0:
                direction = 1, ">"

            for i in range(abs(dy)):
                ny = self.position[1] + direction[0]
                way.append(direction[1])
                self.position = (self.position[0], ny)

            # up/down
            dx = pos[0] - self.position[0]
            direction = -1, "^"

            if dx > 0:
                direction = 1, "v"

            for i in range(abs(dx)):
                nx = self.position[0] + direction[0]

                way.append(direction[1])
                self.position = (nx, self.position[1])


        way.append("A")
        return way


robot_1 = NumericalKeypad()
robot_2 = DirectionalKeypad()
robot_3 = DirectionalKeypad()

all_keypads = [robot_1, robot_2, robot_3]
presses = []
all_presses = {}

for sequence in sequences:
    presses = sequence

    for idx, keypad in enumerate(all_keypads):
        new_presses = []

        for key in presses:
            new_presses.extend(keypad.press_button(key))

        presses = new_presses
    all_presses["".join(sequence)] = presses.copy()

score = 0

for key, val in all_presses.items():
    print(key, len(val), "".join(val))
    score += len(val) * int(key[:-1])

print(score)
