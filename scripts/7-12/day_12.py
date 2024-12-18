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


def count_edges(region_points):
    edges = 4
    all_directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    region_points = list(region_points)
    region_points.sort(key=lambda tup: (tup[0], tup[1]))

    first = region_points[0]

    if (first[0], first[1] + 1) in region_points:
        edges -= 1
    if (first[0] + 1, first[1]) in region_points:
        edges -= 1

    for idx, point in enumerate(region_points):
        x, y = point
        if idx == 0:
            continue
        edges += 4

        left = top = right = bottom = False
        diag_top_left = diag_top_right = diag_bottom_left = False

        for dx, dy in all_directions:
            nx, ny = x + dx, y + dy

            if (nx, ny) in region_points:
                if (dx, dy) == (0, 1):
                    right = True
                    edges -= 1
                elif (dx, dy) == (1, 0):
                    bottom = True
                    edges -= 1
                elif (dx, dy) == (-1, 0):
                    top = True
                    edges -= 1
                elif (dx, dy) == (0, -1):
                    left = True
                    edges -= 1
                elif (dx, dy) == (-1, -1):
                    diag_top_left = True
                elif (dx, dy) == (-1, 1):
                    diag_top_right = True
                elif (dx, dy) == (1, -1):
                    diag_bottom_left = True

        if left and not top:
            if not diag_top_left:
                edges -= 1
        if left and not bottom:
            if not diag_bottom_left:
                edges -= 1
        if top and not left:
            if not diag_top_left:
                edges -= 1
        if top and not right:
            if not diag_top_right:
                edges -= 1

    return edges


def calculate_side_cost(regions):
    cost = 0

    for region in regions:
        cost += count_edges(region) * len(region)

    return cost


print(calculate_side_cost(regions))
