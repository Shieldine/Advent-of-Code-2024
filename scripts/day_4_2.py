lines = []

with open("../inputs/day_4.txt") as f:
    for line in f:
        lines.append(line.strip())


def is_star(text, line, start_char):
    rows, cols = len(text), len(text[0])

    if line-1 < 0 or line+1 >= rows:
        return False
    if start_char-1 < 0 or start_char+1 >= cols:
        return False

    diagonal = text[line - 1][start_char - 1] + text[line][start_char] + text[line + 1][start_char + 1]
    second_diagonal = text[line + 1][start_char - 1] + text[line][start_char] + text[line - 1][start_char + 1]
    if diagonal == "SAM" or diagonal == "MAS":
        if second_diagonal == "SAM" or second_diagonal == "MAS":
            return True

    return False


def count_occurrences(text):
    num = 0

    for i, line in enumerate(text):
        for c_i, character in enumerate(line):
            if character == "A" and is_star(text, i, c_i):
                num += 1

    return num


print(count_occurrences(lines))
