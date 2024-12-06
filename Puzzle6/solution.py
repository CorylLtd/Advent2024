directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def load_grid():
    with open('input.txt') as f:
        return f.read().splitlines()

def locate_guard(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '^':
                return i, j
    return None

grid = load_grid()

def count_steps_to_exit_room(obstacle_pos):
    guard_pos = locate_guard(grid)
    current_direction = 0
    previous_positions = [(guard_pos, current_direction)]
    in_room = True
    while in_room:
        new_pos = (guard_pos[0] + directions[current_direction][1], guard_pos[1] + directions[current_direction][0])
        if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(grid) or new_pos[1] >= len(grid[0]):
            in_room = False
        else:
            if grid[new_pos[0]][new_pos[1]] == '#' or new_pos == obstacle_pos:
                current_direction = (current_direction + 1) % 4
            else:
                guard_pos = new_pos
                if guard_pos not in list(map(lambda x: x[0], previous_positions)):
                    previous_positions.append((guard_pos, current_direction))
                # if we have been here before, we are in a loop
                elif (guard_pos, current_direction) in previous_positions:
                    return -1

    return len(previous_positions)

# add extra character to each possible position in the grid
loop_count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        print('Checking', i, j, 'loop count', loop_count)
        if grid[i][j] != '#' and count_steps_to_exit_room((i, j)) == -1:
            loop_count += 1
print('Loop count', loop_count)

