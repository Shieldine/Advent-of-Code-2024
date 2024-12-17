stones = []
with open("../../inputs/7-12/day_11.txt") as file:
    stones = file.read().strip().split(" ")

stones = [int(stone) for stone in stones]

BLINKS = 25

memo_cache = {}


def transform(stone):
    if stone in memo_cache:
        return memo_cache[stone]

    if stone == 0:
        result = [1]
    elif len(str(stone)) % 2 == 0:
        digits = list(str(stone))
        midpoint = len(digits) // 2
        result = [int("".join(digits[:midpoint])), int("".join(digits[midpoint:]))]
    else:
        result = [stone * 2024]

    memo_cache[stone] = result
    return result


for _ in range(BLINKS):
    new_list = []

    for stone in stones:
        new_list.extend(transform(stone))

    stones = new_list

print(len(stones))
