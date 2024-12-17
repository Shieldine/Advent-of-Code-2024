antenna_map = []

with open("../../inputs/7-12/day_8.txt") as f:
    for line in f:
        antenna_map.append(line.strip())

frequencies = {x for l in antenna_map for x in l}
frequencies.remove(".")

rows = len(antenna_map)
cols = len(antenna_map[0])

antinodes = set()

# foreach frequency
for freq in frequencies:
    # get all positions
    positions = []
    for idx, row in enumerate(antenna_map):
        for idx_c, col in enumerate(row):
            if antenna_map[idx][idx_c] == freq:
                positions.append((idx, idx_c))

    # get combinations of two antennas
    combinations = [(a, b) for idx, a in enumerate(positions) for b in positions[idx + 1:]]

    # for each combination
    for combination in combinations:
        # get direction
        direction = [combination[0][0] - combination[1][0], combination[0][1] - combination[1][1]]

        antinodes.add(combination[0])
        antinodes.add(combination[1])

        i = 1

        # keep going into one direction
        while True:
            node_1 = combination[0][0] + direction[0] * i, combination[0][1] + direction[1] * i
            if 0 <= node_1[0] < rows and 0 <= node_1[1] < cols:
                antinodes.add(node_1)
                i += 1
            else:
                break

        i = 1

        # keep going into the other direction
        while True:
            node_2 = combination[1][0] - direction[0] * i, combination[1][1] - direction[1] * i
            if 0 <= node_2[0] < rows and 0 <= node_2[1] < cols:
                antinodes.add(node_2)
                i += 1
            else:
                break

print(len(antinodes))
