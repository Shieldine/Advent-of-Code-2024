locks = []
keys = []

SIZE = 5


def convert_schema(schema):
    schema = [list(part) for part in schema]
    numbers = [-1 for _ in range(len(schema[1]))]

    for row in range(len(schema)):
        for col in range(len(schema[0])):
            if schema[row][col] == '#':
                numbers[col] += 1

    return numbers


with open("../../inputs/19-25/day_25.txt") as file:
    middle = False
    lock = False

    schema = []

    for line in file:
        if line.strip() == "":
            if lock:
                locks.append(convert_schema(schema))
            else:
                keys.append(convert_schema(schema))
            middle = False
            schema = []
            continue
        if not middle and "#" in line:
            middle = True
            lock = True
        elif not middle and "." in line:
            middle = True
            lock = False

        schema.append(line.strip())

    if lock:
        locks.append(convert_schema(schema))
    else:
        keys.append(convert_schema(schema))


fitting = 0

for lock in locks:
    for key in keys:
        all_fit = True
        for num_1, num_2 in zip(lock, key):
            if num_1 + num_2 > SIZE:
                all_fit = False
        if all_fit:
            fitting += 1

print(fitting)
