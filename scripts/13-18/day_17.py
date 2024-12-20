import re

a = b = c = 0
program = []

with open("../../inputs/13-18/day_17.txt") as file:
    for idx, line in enumerate(file):
        if idx == 0:
            a = int(re.findall(r"\d+", line)[0])
        elif idx == 1:
            b = int(re.findall(r"\d+", line)[0])
        elif idx == 2:
            c = int(re.findall(r"\d+", line)[0])
        elif idx == 4:
            program = [int(n) for n in line.replace("Program: ", "").strip().split(",")]


def get_operand_value(operand, a, b, c):
    match operand:
        case 0:
            return 0
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
        case _:
            return None


def execute_program(a, b, c, program):
    i = 0
    result = ''
    while i < len(program):
        opcode = program[i]
        operand = program[i + 1]
        match opcode:
            case 0:
                a = int(a / (2 ** get_operand_value(operand, a, b, c)))
            case 1:
                b = b ^ operand
            case 2:
                b = get_operand_value(operand, a, b, c) % 8
            case 3:
                if a == 0:
                    i += 2
                    continue
                else:
                    i = operand
                    continue
            case 4:
                b = b ^ c
            case 5:
                result += str(get_operand_value(operand, a, b, c) % 8) + ","
            case 6:
                b = int(a / (2 ** get_operand_value(operand, a, b, c)))
            case 7:
                c = int(a / (2 ** get_operand_value(operand, a, b, c)))
        i += 2
    return result[:-1]


print(execute_program(a, b, c, program))

# brute force ain't gonna work
# correct_a = 1
#
# while True:
#     output = execute_program(correct_a, b, c, program)
#
#     split = output.split(",")
#     split = [int(n) for n in split]
#
#     if split == program:
#         break
#
#     correct_a += 1
#
# print(correct_a)


candidates = [0]

for idx in range(1, len(program) + 1):
    next_candidates = []

    for val in candidates:
        for i in range(8):
            target = (val * 8) + i
            cur_execution = execute_program(target, 0, 0, program).split(",")
            cur_execution = [int(num) for num in cur_execution]

            if cur_execution == program[len(program) - idx:len(program)]:
                next_candidates.append(target)

    candidates = next_candidates

test_program = execute_program(min(candidates), b, c, program).split(",")
test_program = [int(num) for num in test_program]

print(min(candidates))
