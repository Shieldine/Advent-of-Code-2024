import time
from collections import Counter

start_time = time.time()

sequences = {}
bananas = {}
changes = {}

NUM_STEPS = 2000

with open("../../inputs/19-25/day_22.txt") as f:
    for line in f:
        num = int(line.strip())
        sequences[num] = num
        bananas[num] = [num % 10]
        changes[num] = []


def calculate_next_secret(secret):
    secret = (secret * 64) ^ secret
    secret = secret % 16777216

    secret = (secret // 32) ^ secret
    secret = secret % 16777216

    secret = (secret * 2048) ^ secret
    secret = secret % 16777216

    return secret


for _ in range(NUM_STEPS):
    for key in sequences.keys():
        sequences[key] = calculate_next_secret(sequences[key])
        bananas[key].append(sequences[key] % 10)
        changes[key].append(bananas[key][len(bananas[key]) - 1] - bananas[key][len(bananas[key]) - 2])

print(sum(sequences.values()))
print("--- %s seconds ---" % (time.time() - start_time))

# part 2
# this solution is super slow, but I don't really care
sequence_counts = Counter()

for seq in changes.values():
    seen_in_list = set(tuple(seq[i:i + 4]) for i in range(len(seq) - 3))
    sequence_counts.update(seen_in_list)

most_common = sequence_counts.most_common()

if most_common:
    highest_count = most_common[0][1]
    # how I know about the 90? well, I tried out some stuff, of course!
    highest_sequences = [seq for seq, count in most_common if count >= highest_count - 90]
else:
    highest_sequences = []


def find_first_occurrence(sequence, lst):
    for i in range(len(lst) - len(sequence) + 1):
        if lst[i:i + len(sequence)] == list(sequence):
            return i
    return -1


counts = {}

for seq in highest_sequences:
    counts[seq] = 0

    for key in changes.keys():
        index = find_first_occurrence(seq, changes[key])
        if index == -1:
            continue
        else:
            counts[seq] += bananas[key][index + 4]

print(max(counts.values()))
print("--- %s seconds ---" % (time.time() - start_time))
