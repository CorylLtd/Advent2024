def parse_number(p):
    number = ''
    for i in range(len(p)):
        if p[i].isdigit():
            number += data[i]
        else:
            break
    return number

def parse_mul(p):
    if not p.startswith('mul('):
        return 0

    p = p[4:]
    number1 = parse_number(p)
    if len(number1) == 0:
        return 0
    p = p[len(number1):]
    if not p.startswith(','):
        return 0
    p = p[1:]
    number2 = parse_number(p)
    if len(number2) == 0:
        return 0
    p = p[len(number2):]
    if not p.startswith(')'):
        return 0

    return int(number1) * int(number2)

# load the input file
with open('input.txt') as f:
    data = f.read()

    # parse the data
    total = 0
    enabled = True
    for i in range(len(data)):
        toParse = data[i:]
        if toParse.startswith('do()'):
            enabled = True
        elif toParse.startswith('don\'t()'):
            enabled = False
        elif enabled:
            total += parse_mul(toParse)

    print('Sum', total)