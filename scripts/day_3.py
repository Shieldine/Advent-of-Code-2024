import re

with open("../inputs/day_3.txt") as f:
    lines = f.readlines()

lines = "".join(lines)

dos = [m.end(0) for m in re.finditer(r"do\(\)", lines)]
donts = [m.end(0) for m in re.finditer(r"don't\(\)", lines)]

indexes = [m.start(0) for m in re.finditer(r"mul\(\d+,\d+\)", lines)]

results = re.findall(r"mul\(\d+,\d+\)", lines)


def add_multiply(input_list):
    number = 0

    for result in input_list:
        result = result.replace("mul(", "")
        result = result.replace(")", "")

        numbers = result.split(",")

        number += int(numbers[0]) * int(numbers[1])

    return number


valid = []

for i, index in enumerate(indexes):
    dos_before = [n for n in dos if n <= index]
    donts_before = [n for n in donts if n <= index]

    if len(donts_before) == 0:
        valid.append(results[i])
        continue

    if len(dos_before) == 0:
        continue

    if dos_before[len(dos_before) - 1] > donts_before[len(donts_before) - 1]:
        valid.append(results[i])

print(add_multiply(results))
print(add_multiply(valid))
