word = "XMAS"

lines = []

with open("../inputs/day_4.txt") as f:
    for row in f:
        lines.append(row.strip())


def check_diagonal(text, line, start_char):
    num = 0
    rows, cols = len(text), len(text[0])

    # up right
    if line + 3 < rows and start_char + 3 < cols:
        if all(text[line + i][start_char + i] == word[i] for i in range(4)):
            num += 1

    # down right
    if line - 3 >= 0 and start_char + 3 < cols:
        if all(text[line - i][start_char + i] == word[i] for i in range(4)):
            num += 1

    # up left
    if line + 3 < rows and start_char - 3 >= 0:
        if all(text[line + i][start_char - i] == word[i] for i in range(4)):
            num += 1

    # down left
    if line - 3 >= 0 and start_char - 3 >= 0:
        if all(text[line - i][start_char - i] == word[i] for i in range(4)):
            num += 1

    return num


def check_horizontal(text, line, start_char):
    num = 0

    # right
    if text[line][start_char:start_char + 4] == word:
        num += 1
    # left
    if text[line][start_char - 3:start_char + 1] == word[::-1]:
        num += 1
    return num


def check_vertical(text, line, start_char):
    num = 0
    rows = len(text)
    # up
    if line + 3 < rows:
        if all(text[line + i][start_char] == word[i] for i in range(4)):
            num += 1
    # down
    if line - 3 >= 0:
        if all(text[line - i][start_char] == word[i] for i in range(4)):
            num += 1
    return num


def count_occurrences(text):
    num = 0

    for i, line in enumerate(text):
        for c_i, character in enumerate(line):
            if character == word[0]:
                num += check_horizontal(text, i, c_i) + check_vertical(text, i, c_i) + check_diagonal(text, i, c_i)

    return num


print(count_occurrences(lines))
