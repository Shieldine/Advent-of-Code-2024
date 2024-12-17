stones = []

with open("../../inputs/7-12/day_11.txt") as file:
    stones = file.read().strip().split(" ")

stones = [int(stone) for stone in stones]

BLINKS = 75

for _ in range(BLINKS):
    new_list = []

    for stone in stones:
        if stone == 0:
            new_list.append(1)
        elif len(str(stone)) % 2 == 0:
            digits = list(str(stone))
            midpoint = len(digits) // 2
            new_list.append(int("".join(digits[:midpoint])))
            new_list.append(int("".join(digits[midpoint:])))
        else:
            new_list.append(stone*2024)

    stones = new_list

print(len(stones))
