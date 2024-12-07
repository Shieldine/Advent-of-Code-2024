def read_input():
    reports = []

    with open('../../inputs/1-6/day_2.txt') as f:
        for line in f:
            numbers = line.split(" ")

            reports.append([int(number) for number in numbers])

    return reports


def check_reports(reports):
    num = 0

    for report in reports:
        if check_report(report):
            num += 1

    return num


def check_report(report):
    last = None
    decrease = report[0] > report[1]

    for number in report:
        if last is None:
            last = number
            continue

        if decrease and number > last:
            return False
        if not decrease and number < last:
            return False

        if 1 <= abs(number - last) <= 3:
            last = number
            continue
        else:
            return False

    return True


def check_dampened(reports):
    num = 0

    for report in reports:
        if check_report(report):
            num += 1
            continue
        else:
            for i, number in enumerate(report):
                temp = report.copy()
                temp = [element for index, element in enumerate(temp) if index != i]
                if check_report(temp):
                    num += 1
                    break

    return num


r = read_input()

print(check_reports(r))
print(check_dampened(r))
