from itertools import combinations_with_replacement

available_towels = []
desired_designs = []

with open("../../inputs/19-25/day_19.txt") as f:
    for idx, line in enumerate(f):
        if idx == 0:
            available_towels = line.strip().split(",")
            available_towels = [towel.strip() for towel in available_towels]

        elif idx == 1:
            continue

        else:
            desired_designs.append(line.strip())

count = 0


def can_form_string(target, substrings):
    if not target:
        return True
    for substring in substrings:
        if target.startswith(substring):
            if can_form_string(target[len(substring):], substrings):
                return True
    return False


for design in desired_designs:
    if can_form_string(design, available_towels):
        count += 1

print(count)
