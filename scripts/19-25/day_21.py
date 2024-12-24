sequences = []

with open("../../inputs/19-25/day_21.txt") as f:
    for line in f:
        if line.strip() != "":
            sequences.append(line.strip())

sequences = [list(sequence) for sequence in sequences]

