garden_map = []

with open("../../inputs/7-12/day_12.txt") as f:
    for line in f:
        garden_map.append(line.strip())

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

regions = []
cur_plot = garden_map[0][0]
x, y = 0, 0
visited = set()


def discover_area(point, area):
    x, y = point
    if point in visited:
        return set()

    visited.add(point)
    cur_area = {point}

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(garden_map) and 0 <= ny < len(garden_map[0]):
            if garden_map[nx][ny] == area and (nx, ny) not in visited:
                cur_area.update(discover_area((nx, ny), area))

    return cur_area


for idx, row in enumerate(garden_map):
    for idx_r, col in enumerate(row):
        discovered = discover_area((idx, idx_r), garden_map[idx][idx_r])
        if discovered != set():
            regions.append(discovered)


def calculate_perimeter_cost(regions, garden_map):
    cost = 0

    for region in regions:
        perimeter = 0
        for x, y in region:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < len(garden_map) and 0 <= ny < len(garden_map[0])) or (nx, ny) not in region:
                    perimeter += 1

        cost += perimeter * len(region)

    return cost


print(calculate_perimeter_cost(regions, garden_map))


def calculate_side_cost(regions, garden_map):
    cost = 0

    for region in regions:
        pass

    return cost


print(calculate_side_cost(regions, garden_map))
