sequences = {}
NUM_STEPS = 2000

with open("../../inputs/19-25/day_22.txt") as f:
    for line in f:
        num = int(line.strip())
        sequences[num] = num


def mix(val, secret):
    return val ^ secret


def prune(secret):
    return secret % 16777216


def calculate_next_secret(secret):
    secret = mix(secret * 64, secret)
    secret = prune(secret)

    secret = mix((secret // 32), secret)
    secret = prune(secret)

    secret = mix(secret * 2048, secret)
    secret = prune(secret)

    return secret


for _ in range(NUM_STEPS):
    for key in sequences.keys():
        sequences[key] = calculate_next_secret(sequences[key])

print(sum(sequences.values()))
