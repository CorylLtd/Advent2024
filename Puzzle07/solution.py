def int_to_base3(n):
    if n == 0:
        return "0"

    digits = []
    is_negative = n < 0
    n = abs(n)

    while n:
        digits.append(str(n % 3))
        n //= 3

    if is_negative:
        return "-" + "".join(reversed(digits))
    else:
        return "".join(reversed(digits))

with open('input.txt') as f:
    total = 0
    for line in f:
        parameters = line.split(':')
        answer = int(parameters[0])
        numbers = [int(x.strip()) for x in parameters[1].split(' ') if x.strip().isdigit()]
        for i in range(3**(len(numbers)-1)):
            line_total = 0
            operator_combinations = int_to_base3(i).zfill(len(numbers)-1)
            for j in range(0, len(numbers)):
                if line_total == 0:
                    line_total = numbers[j]
                else:
                    if operator_combinations[j-1] == '0':
                        line_total += numbers[j]
                    elif operator_combinations[j-1] == '1':
                        line_total *= numbers[j]
                    else:
                        line_total = int(str(line_total) + str(numbers[j]))

            if line_total == answer:
                total += answer
                break

print('Total', total)