from collections import defaultdict

stones = []
with open("../../inputs/7-12/day_11.txt") as file:
    stones = file.read().strip().split(" ")

stones = [int(stone) for stone in stones]

BLINKS = 75

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


stone_counts = defaultdict(int)

for stone in stones:
    stone_counts[stone] += 1

for _ in range(BLINKS):
    new_counts = defaultdict(int)

    for stone, count in stone_counts.items():
        for new_stone in transform(stone):
            new_counts[new_stone] += count

    stone_counts = new_counts

total_stones = sum(stone_counts.values())
print(total_stones)
