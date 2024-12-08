def load_grid():
    with open('input.txt') as f:
        return f.read().splitlines()

def get_distinct_letters(grid):
    l = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "." and grid[i][j] not in l:
                l.append(grid[i][j])
    return l

def get_letter_positions(grid, letter):
    positions = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == letter:
                positions.append((j, i))
    return positions

def on_grid(grid, x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def get_antinodes(grid, positions):
    antinodes = []
    for i in range(len(positions) - 1):
        for j in range(i + 1, len(positions)):
            (xdiff, ydiff) = (positions[j][0] - positions[i][0], positions[j][1] - positions[i][1])
            (node1_x, node1_y) = (positions[i][0] - xdiff, positions[i][1] - ydiff)
            (node2_x, node2_y) = (positions[j][0] + xdiff, positions[j][1] + ydiff)
            if on_grid(grid, node1_x, node1_y):
                antinodes.append((node1_x, node1_y))
            if on_grid(grid, node2_x, node2_y):
                antinodes.append((node2_x, node2_y))
    return antinodes

def get_resonant_antinodes(grid, positions):
    antinodes = positions.copy()
    for i in range(len(positions) - 1):
        for j in range(i + 1, len(positions)):
            (xdiff, ydiff) = (positions[j][0] - positions[i][0], positions[j][1] - positions[i][1])
            (node1_x, node1_y) = (positions[i][0] - xdiff, positions[i][1] - ydiff)
            (node2_x, node2_y) = (positions[j][0] + xdiff, positions[j][1] + ydiff)
            while on_grid(grid, node1_x, node1_y):
                antinodes.append((node1_x, node1_y))
                (node1_x, node1_y) = (node1_x - xdiff, node1_y - ydiff)
            while on_grid(grid, node2_x, node2_y):
                antinodes.append((node2_x, node2_y))
                (node2_x, node2_y) = (node2_x + xdiff, node2_y + ydiff)
    return antinodes

main_grid = load_grid()
letters = get_distinct_letters(main_grid)
grid_antinodes = []
for letter in letters:
    positions = get_letter_positions(main_grid, letter)
    letter_antinodes = get_resonant_antinodes(main_grid, positions)
    grid_antinodes = (grid_antinodes +
                      [antinode for antinode in letter_antinodes
                       if antinode not in grid_antinodes])

print('Grid antinodes', len(grid_antinodes))





