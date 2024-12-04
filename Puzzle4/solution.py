
def load_grid():
    with open('input.txt') as f:
        return f.read().splitlines()

def rotate_grid(g):
    return [''.join([g[j][i] for j in range(len(g))]) for i in range(len(g[0]) - 1, -1, -1)]


def is_word_at_position(w, y, x, direction_x, direction_y):
    if direction_x == 0 and direction_y == 0:
        return False
    if x + direction_x * len(w) > len(grid[y]):
        return False
    if y + direction_y * len(w) > len(grid):
        return False

    for k in range(len(w)):
        if grid[y + (direction_y*k)][x + (direction_x * k)] != w[k]:
            return False
    return True

def is_x_mas_at_position(w, x, y):
    return w[y][x] == 'A' and w[y-1][x-1] == 'M' and w[y-1][x+1] == 'M' and w[y+1][x-1] == 'S' and w[y+1][x+1] == 'S'


# find all occurrences of the work 'XMAS' in the grid
count = 0
grid = load_grid()
word = 'XMAS'
for r in range(4):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if is_word_at_position(word, i, j, 1, 1):
                count += 1
            if is_word_at_position(word, i, j, 1, 0):
                count += 1
    grid = rotate_grid(grid)
print('Xmas Count', count)

xcount = 0
for r in range(4):
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            if is_x_mas_at_position(grid, j, i):
                xcount += 1
    grid = rotate_grid(grid)

print('X-mas Count', xcount)