rules = {}

updates = []

with open("../../inputs/1-6/day_5.txt") as f:
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


def check_incorrect(update):
    for number in update:
        if number in rules.keys():
            cur_rule = rules[number]
            for rule in cur_rule:
                if rule in update and update.index(number) > update.index(rule):
                    return True
    return False


updates = [update for update in updates if check_incorrect(update)]


def fix_update(update):
    fixed = update.copy()
    index_map = {num: i for i, num in enumerate(fixed)}

    changed = True
    while changed:
        changed = False
        for number in fixed:
            if number in rules:
                cur_rules = rules[number]
                for rule in cur_rules:
                    if rule in index_map:
                        num_i = index_map[number]
                        rule_i = index_map[rule]
                        if num_i > rule_i:
                            fixed[num_i], fixed[rule_i] = fixed[rule_i], fixed[num_i]
                            index_map[fixed[num_i]] = num_i
                            index_map[fixed[rule_i]] = rule_i
                            changed = True

    return fixed


for update in updates:
    fixed = fix_update(update)
    num += int(fixed[len(fixed) // 2])

print(num)
