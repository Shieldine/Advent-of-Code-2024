from itertools import product


def read_input():
    lines = []
    with open('../../inputs/7-12/day_7.txt') as f:
        for line in f:
            split = line.strip().split(":")
            result = split[0]
            parts = split[1].strip().split(" ")
            lines.append([int(result), [int(part) for part in parts]])

    return lines


def find_sum_of_valid_equations(equation_list, extended=False):
    num = 0
    for equation in equation_list:
        if extended:
            if try_extended_possibilities(equation):
                num += equation[0]
        else:
            if try_possibilities(equation):
                num += equation[0]
    return num


def try_extended_possibilities(equation):
    result = equation[0]
    numbers = equation[1]

    num_combinations = (len(numbers) - 1)
    combinations = list(product(['*', '+', '||'], repeat=num_combinations))

    for combination in combinations:
        res = numbers[0]
        for i in range(len(combination)):
            if combination[i] == "*":
                res = res * numbers[i + 1]
            elif combination[i] == "+":
                res = res + numbers[i + 1]
            elif combination[i] == "||":
                res = int(str(res) + str(numbers[i + 1]))
        if res == result:
            return True


def try_possibilities(equation):
    result = equation[0]
    numbers = equation[1]

    num_combinations = (len(numbers) - 1)
    combinations = list(product(['*', '+'], repeat=num_combinations))

    for combination in combinations:
        res = numbers[0]
        for i in range(len(combination)):
            if combination[i] == "*":
                res = res * numbers[i + 1]
            else:
                res = res + numbers[i + 1]
        if res == result:
            return True


equations = read_input()

print(find_sum_of_valid_equations(equations))
print(find_sum_of_valid_equations(equations, extended=True))
