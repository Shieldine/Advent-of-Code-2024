import re

a = 0
b = 0
c = 0

program = []

with open("../../inputs/13-18/day_17.txt") as file:
    for idx, line in enumerate(file):
        if idx == 0:
            a = int(re.findall(r"\d+", line)[0])
        elif idx == 1:
            b = int(re.findall(r"\d+", line)[0])
        elif idx == 2:
            c = int(re.findall(r"\d+", line)[0])
        elif idx == 3:
            continue
        elif idx == 4:
            program = line.replace("Program: ", "").strip().split(",")


def get_combo_operand(operand):
    match operand:
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c
        case 7:
            return None


program = [int(program) for program in program]

i = 0

out = ''

while i < len(program):
    opcode = program[i]
    operand = program[i + 1]

    match opcode:
        case 0:  # division
            a = int(a / (2 ** get_combo_operand(operand)))
        case 1:  # bitwise XOR
            b = b ^ operand
        case 2:  # bst
            b = get_combo_operand(operand) % 8
        case 3:  # jnz
            if a == 0:
                i += 2
                continue
            else:
                i = operand
                continue
        case 4:  # bxc
            b = b ^ c
        case 5:  # out
            out += str(get_combo_operand(operand) % 8) + ","
        case 6:  # bdv
            b = int(a / (2 ** get_combo_operand(operand)))
        case 7:  # cdv
            c = int(a / (2 ** get_combo_operand(operand)))

    i += 2

print(out[:-1])


