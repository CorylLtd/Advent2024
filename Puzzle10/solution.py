def load_grid():
    with open('input.txt') as f:
        g = f.read().splitlines()
        # convert to a 2D array of integers
        return [[int(digit) for digit in row] for row in g]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'({self.x}, {self.y})'


def get_trailheads(grid):
    th = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                th.append(Point(j, i))
    return th


found_trailheads = []


def point_score(grid, pt: Point):
    total = 0
    value = grid[pt.y][pt.x]

    # found a top omitting alternative paths
    # if value == 9 and pt not in found_trailheads:
    #     found_trailheads.append(pt)
    #     return total + 1

    # for part 2 include alternative paths
    if value == 9:
        return total + 1

    # look north
    if pt.y > 0 and grid[pt.y - 1][pt.x] == value + 1:
        total += point_score(grid, Point(pt.x, pt.y - 1))

    # look east
    if pt.x < len(grid[0]) - 1 and grid[pt.y][pt.x + 1] == value + 1:
        total += point_score(grid, Point(pt.x + 1, pt.y))

    # look south
    if pt.y < len(grid) - 1 and grid[pt.y + 1][pt.x] == value + 1:
        total += point_score(grid, Point(pt.x, pt.y + 1))

    # look west
    if pt.x > 0 and grid[pt.y][pt.x - 1] == value + 1:
        total += point_score(grid, Point(pt.x - 1, pt.y))

    return total


grid_map = load_grid()
trailheads = get_trailheads(grid_map)
trailheads_count = len(trailheads)
map_score = 0
for t in trailheads:
    found_trailheads = []
    map_score += point_score(grid_map, t)
print('Score', map_score)
