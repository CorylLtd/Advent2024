# rotate the grid 90 degrees clockwise
def rotate_grid(grid):
    return [''.join([grid[j][i] for j in range(len(grid))]) for i in range(len(grid[0])-1, -1, -1)]

def load_grid():
    with open('input.txt') as f:
        return f.read().splitlines()

def is_word_at_position(w, y, x, direction_x, direction_y):
    if direction_x == 0 and direction_y == 0:
        return False
    if x + direction_x * len(w) > len(grid[y]):
        return False
    if y + direction_y * len(w) > len(grid):
        return False
    if x + direction_x * len(w) < -1:
        return False
    if y + direction_y * len(w) < -1:
        return False

    for k in range(len(w)):
        if grid[y + (direction_y*k)][x + (direction_x * k)] != w[k]:
            return False
    return True

def is_x_mas_at_position(w, x, y):
    if x <= 0 or y <= 0 or y >= len(w)-1 or x >= len(w[y])-1:
        return False
    return w[y][x] == 'A' and w[y-1][x-1] == 'M' and w[y-1][x+1] == 'M' and w[y+1][x-1] == 'S' and w[y+1][x+1] == 'S'


# find all occurrences of the work 'XMAS' in the grid
count = 0
grid = load_grid()
row_count = len(grid)
column_count = len(grid[0])
word = 'XMAS'
for i in range(row_count):
    for j in range(column_count):
        if is_word_at_position(word, i, j, 1, 1):
            count += 1
        if is_word_at_position(word, i, j, -1, 0):
            count += 1
        if is_word_at_position(word, i, j, -1, -1):
            count += 1
        if is_word_at_position(word, i, j, 0, -1):
            count += 1
        if is_word_at_position(word, i, j, 1, -1):
            count += 1
        if is_word_at_position(word, i, j, 1, 0):
            count += 1
        if is_word_at_position(word, i, j, 0, 1):
            count += 1
        if is_word_at_position(word, i, j, -1, 1):
            count += 1
print('Xmas Count', count)

xcount = 0
for r in range(4):
    for i in range(row_count):
        for j in range(column_count):
            if is_x_mas_at_position(grid, j, i):
                xcount += 1
    grid = rotate_grid(grid)

print('X-mas Count', xcount)