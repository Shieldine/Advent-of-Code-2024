def read_input():
    left = []
    right = []

    with open("../../inputs/1-6/day_1.txt", "r") as f:
        for line in f:
            one, two = line.split("   ")
            left.append(int(one.strip()))
            right.append(int(two.strip()))

    return sorted(left), sorted(right)


def calculate_distances(left, right):
    distances = 0

    for one, two in zip(left, right):
        distances += abs(one - two)

    return distances


def calculate_score(left, right):
    score = 0

    for number in left:
        score += number * right.count(number)

    return score


l, r = read_input()
print(calculate_distances(l, r))
print(calculate_score(l, r))
