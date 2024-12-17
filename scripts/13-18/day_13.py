import re
import numpy as np

machines = []
tolerance = 1e-4

# Load the machine data
with open("../../inputs/13-18/day_13.txt") as file:
    i = 0
    a = []
    b = []
    prize = []

    for line in file:
        if i == 0:
            a = [int(re.findall(r"\d+", line)[0]), int(re.findall(r"\d+", line)[1])]
            i += 1
        elif i == 1:
            b = [int(re.findall(r"\d+", line)[0]), int(re.findall(r"\d+", line)[1])]
            i += 1
        elif i == 2:
            prize = [int(re.findall(r"\d+", line)[0]), int(re.findall(r"\d+", line)[1])]
            i += 1

            machines.append({
                "a": a,
                "b": b,
                "prize": prize
            })
        elif i == 3:
            i = 0

tokens = 0

# solved using CRAMER's RULE
for machine in machines:
    a, b = machine["a"], machine["b"]
    prize = machine["prize"]

    det_A = a[0] * b[1] - a[1] * b[0]

    if abs(det_A) < tolerance:
        continue

    det_A_x = prize[0] * b[1] - prize[1] * b[0]
    det_A_y = a[0] * prize[1] - a[1] * prize[0]

    x = det_A_x / det_A
    y = det_A_y / det_A

    if (abs(x - round(x)) < tolerance and abs(y - round(y)) < tolerance and
            0 <= x <= 100 and 0 <= y <= 100):
        tokens += 3 * x + y

print(int(tokens))

tokens = 0

for machine in machines:
    a, b = machine["a"], machine["b"]
    prize = [machine["prize"][0] + 10000000000000, machine["prize"][1] + 10000000000000]

    det_A = a[0] * b[1] - a[1] * b[0]

    if abs(det_A) < tolerance:
        continue

    det_A_x = prize[0] * b[1] - prize[1] * b[0]
    det_A_y = a[0] * prize[1] - a[1] * prize[0]

    x = det_A_x / det_A
    y = det_A_y / det_A

    if abs(x - round(x)) < tolerance and abs(y - round(y)) < tolerance:
        tokens += 3 * x + y

print(tokens)
