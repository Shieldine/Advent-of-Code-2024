rules = {}

updates = []

with open("../inputs/day_5.txt") as f:
    for line in f:
        if "|" in line:
            first, second = line.strip().split("|")
            if first not in rules.keys():
                rules[first] = [second]
            else:
                new_rules = rules[first].copy()
                new_rules.append(second)
                rules[first] = new_rules
        else:
            if line.strip() == "":
                continue
            updates.append(line.strip().split(","))

num = 0


def check_update(update):
    for number in update:
        if number in rules.keys():
            cur_rule = rules[number]
            for rule in cur_rule:
                if rule in update and update.index(number) > update.index(rule):
                    return 0
    return update[len(update) // 2]


for update in updates:
    num += int(check_update(update))

print(num)
