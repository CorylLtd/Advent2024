def read_input():
    with open('input.txt') as f:
        return f.read().strip()

def convert_to_filemap(data):
    fm = []
    file_id = 0
    is_space = False
    for c in data:
        count = int(c)
        for index in range(count):
            if is_space:
                fm.append(-1)
            else:
                fm.append(file_id)
        if is_space:
            is_space = False
        else:
            is_space = True
            file_id += 1
    return fm

def get_checksum(fm):
    checksum = 0
    for index in range(len(fm)):
        if fm[index] != -1:
            checksum += fm[index] * index
    return checksum

v = read_input()
filemap = convert_to_filemap(v)

last_entry = len(filemap) - 1
for i in range(0, len(filemap)):
    if filemap[i] == -1:
        while last_entry > i and filemap[last_entry] == -1:
            last_entry -= 1
        filemap[i] = filemap[last_entry]
        filemap[last_entry] = -1

print("Part 1 checksum", get_checksum(filemap))

# Part 2

def get_space_index(fm, space_size):
    for index in range(len(fm) - space_size + 1):
        if fm[index] == -1:
            found = True
            for j in range(1, space_size):
                if fm[index + j] != -1:
                    found = False

            if found:
                return index
    return -1

def get_file_size(fm, index):
    file_size = 0
    c = fm[index]
    while fm[index] == c and index >= 0:
        file_size += 1
        index -= 1
    return file_size

filemap = convert_to_filemap(v)

i = len(filemap)-1
while i >= 0:
    if filemap[i] != -1:
        size = get_file_size(filemap, i)
        space_index = get_space_index(filemap, size)
        if space_index != -1 and space_index < i:
            for j in range(size):
                filemap[space_index+j] = filemap[i-size+j + 1]
                filemap[i+j-size + 1] = -1
        i -= size
    else:
        i -= 1

print("Part 2 checksum", get_checksum(filemap))