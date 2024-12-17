with open("../../inputs/7-12/day_9.txt") as file:
    files = file.read().strip()

files = [num for num in files]

extended = []

counter = 0
cur_id = 0

for num in files:
    if counter == 0:
        for _ in range(int(num)):
            extended.append(cur_id)
        counter = 1
        cur_id += 1
    elif counter == 1:
        for _ in range(int(num)):
            extended.append('.')
        counter = 0


def part_one(num_list):
    last = len(num_list) - 1

    for i in range(last):
        if num_list.index(".") >= last - i:
            break
        if num_list[last - i] != '.':
            num_list[num_list.index(".")] = num_list[last - i]
            num_list[last - i] = '.'

    score = 0

    for idx, num in enumerate(num_list):
        if num == ".":
            continue
        score += idx * int(num)

    print(score)


def part_two(num_list):
    biggest = max([num for num in num_list if isinstance(num, int)])
    for i in range(biggest, 0, -1):
        id_count = num_list.count(i)
        id_start = num_list.index(i)

        dot_end, dot_start = 0, 0

        indices = [idx for idx, x in enumerate(num_list) if x == "."]
        dot_ranges = []
        cur_sequence = []

        for idx in indices:
            if len(cur_sequence) == 0 or cur_sequence[-1] == idx - 1:
                cur_sequence.append(idx)
            else:
                dot_ranges.append(cur_sequence)
                cur_sequence = [idx]

        if cur_sequence:
            dot_ranges.append(cur_sequence)

        for cur_range in dot_ranges:
            if cur_range[0] < id_start and len(cur_range) >= id_count:
                dot_start = cur_range[0]
                dot_end = cur_range[0] + id_count
                break

        if dot_end - dot_start >= id_count:
            num_list = ['.' if num == i else num for num in num_list]

            for idx in range(dot_start, dot_start + id_count):
                num_list[idx] = i

    score = 0

    for idx, num in enumerate(num_list):
        if num == ".":
            continue
        score += idx * int(num)

    print(score)


part_one(extended)
part_two(extended)
