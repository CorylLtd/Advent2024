order_rules = []
pages = []

def is_valid_order(p):
    for h in range(0, len(p)-1):
        for s in range(h+1, len(p)):
            if (p[h], p[s]) not in order_rules:
                return False
    return True

def fix_order(p):
    while not is_valid_order(p):
        for h in range(0, len(p)-1):
            if (p[h], p[h+1]) not in order_rules:
                p[h], p[h+1] = p[h+1], p[h]
    return p

with open('input.txt') as f:
    for line in f:
        if '|' in line:
            rule = line.split('|')
            order_rules.append((int(rule[0].strip()), int(rule[1].strip())))
        elif len(line) > 1:
            data = line.split(',')
            pages.append([int(x) for x in data])

    valid_total = 0
    invalid_total = 0
    for page in pages:
        if is_valid_order(page):
            valid_total += page[len(page) // 2]
        else:
            page = fix_order(page)
            invalid_total += page[len(page)//2]

    print("valid total", valid_total)
    print("invalid total", invalid_total)


